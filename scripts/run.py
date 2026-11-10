#!/usr/bin/env python3
"""编排入口：抓取 → 补充 README/topics → 逐个深度分析 → 生成日报和 HTML → 发布。"""
from __future__ import annotations

import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone

import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from trending import fetch_trending  # noqa: E402
from report import analyze_all, render_html, render_report  # noqa: E402
import publish  # noqa: E402

ROOT = os.path.dirname(SCRIPT_DIR)


def load_config() -> dict:
    with open(os.path.join(ROOT, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def load_cache(path: str) -> dict:
    """读取仓库缓存（data/repos.json）；不存在或损坏时返回空字典。"""
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def save_cache(path: str, cache: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(cache, fh, ensure_ascii=False, indent=2, sort_keys=True)
        fh.write("\n")


def update_streaks(repos: list[dict], cache: dict, date_str: str) -> None:
    """更新每个仓库的首次出现日期、最近出现日期和连续在榜天数。"""
    yesterday = (
        datetime.strptime(date_str, "%Y-%m-%d") - timedelta(days=1)
    ).strftime("%Y-%m-%d")
    for repo in repos:
        entry = cache.setdefault(repo["full_name"], {})
        if entry.get("last_seen") == date_str:  # 同一天重复运行，保持幂等
            continue
        if entry.get("last_seen") == yesterday:
            entry["streak_days"] = int(entry.get("streak_days", 0)) + 1
        else:
            entry["streak_days"] = 1
        entry.setdefault("first_seen", date_str)
        entry["last_seen"] = date_str


def enrich_repos(
    repos: list[dict], cached_names: set[str] | frozenset[str] = frozenset()
) -> None:
    """从 GitHub API 补充 topics / homepage / README 原文（仅在有 token 时）。

    cached_names 中的仓库已有 AI 介绍缓存，跳过 README 抓取。
    """
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        return
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    def work(repo: dict) -> None:
        try:
            resp = requests.get(
                f"https://api.github.com/repos/{repo['full_name']}",
                headers=headers,
                timeout=15,
            )
            if resp.status_code == 200:
                data = resp.json()
                repo["topics"] = data.get("topics", [])
                repo["homepage"] = data.get("homepage") or ""
            if repo["full_name"] in cached_names:
                return
            readme_resp = requests.get(
                f"https://api.github.com/repos/{repo['full_name']}/readme",
                headers={**headers, "Accept": "application/vnd.github.raw"},
                timeout=15,
            )
            if readme_resp.status_code == 200:
                repo["readme"] = readme_resp.text[:8000]
        except Exception:  # 单个仓库失败不影响整体
            return

    with ThreadPoolExecutor(max_workers=6) as pool:
        list(pool.map(work, repos))


def main() -> None:
    cfg = load_config()

    repos = []
    for language in cfg.get("languages") or [None]:
        repos.extend(fetch_trending(language, cfg.get("since", "daily")))
        if len(repos) >= cfg.get("limit", 25):
            repos = repos[: cfg["limit"]]
            break
    repos = repos[: cfg.get("limit", 25)]
    if not repos:
        sys.exit("❌ 没有抓到任何仓库（GitHub 可能临时反爬），本次跳过，明天自动重试")

    date_str = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")

    cache_path = os.path.join(ROOT, "data", "repos.json")
    cache = load_cache(cache_path)
    update_streaks(repos, cache, date_str)
    cached_names = {name for name, entry in cache.items() if entry.get("summary")}
    reused = sum(1 for repo in repos if repo["full_name"] in cached_names)

    enrich_repos(repos, cached_names)

    ai_cfg = cfg.get("ai", {})
    use_ai = bool(
        ai_cfg.get("enabled", True)
        and os.environ.get(ai_cfg.get("api_key_env", "DEEPSEEK_API_KEY"))
    )
    details = analyze_all(repos, ai_cfg, cache=cache, date_str=date_str, use_ai=use_ai)
    for repo, detail in zip(repos, details):
        repo["summary"] = detail["summary"]
        repo["intro"] = detail.get("intro", "")
        repo["features"] = detail.get("features", [])
        repo["audience"] = detail.get("audience", "")
    save_cache(cache_path, cache)
    if use_ai:
        print(f"📦 复用缓存 {reused} 个仓库介绍，AI 新分析 {len(repos) - reused} 个")
    else:
        print(f"📦 复用缓存 {reused} 个仓库介绍（AI 未启用，其余走兜底）")

    # 连续在榜达到上限的仓库不再占详细介绍位，由榜单后面的仓库顺延补位
    top_n = int(cfg.get("top_n", 10))
    max_streak = int(cfg.get("top_n_max_streak_days", 3))
    featured = [
        repo
        for repo in repos
        if int(cache.get(repo["full_name"], {}).get("streak_days", 0)) < max_streak
    ][:top_n]
    if not featured:  # 极端情况：全部连续在榜很久，保证日报仍有内容
        featured = repos[:top_n]
    print(f"📌 今日精选 {len(featured)} 个（连续在榜 ≥{max_streak} 天的已跳过）")

    report = render_report(
        repos,
        date_str,
        cfg.get("pages_url", ""),
        top_n=top_n,
        featured=featured,
    )
    html_page = render_html(
        repos,
        date_str,
        cfg.get("pages_url", ""),
        cfg.get("repo_url", ""),
        top_n=top_n,
        featured=featured,
    )

    daily_dir = os.path.join(ROOT, "data", "daily")
    os.makedirs(daily_dir, exist_ok=True)
    with open(os.path.join(daily_dir, f"{date_str}.md"), "w", encoding="utf-8") as fh:
        fh.write(report)
    print(f"✅ 日报已生成：data/daily/{date_str}.md（{len(repos)} 个仓库）")

    docs_dir = os.path.join(ROOT, "docs")
    os.makedirs(docs_dir, exist_ok=True)
    with open(os.path.join(docs_dir, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(html_page)
    print("✅ HTML 报告已生成：docs/index.html")

    if os.environ.get("GITHUB_ACTIONS") == "true":
        publish.publish(report, date_str, cfg)


if __name__ == "__main__":
    main()
