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
from report import analyze_all, fallback_details, render_html, render_report  # noqa: E402
import publish  # noqa: E402

ROOT = os.path.dirname(SCRIPT_DIR)


def load_config() -> dict:
    with open(os.path.join(ROOT, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def enrich_repos(repos: list[dict]) -> None:
    """从 GitHub API 补充 topics / homepage / README 原文（仅在有 token 时）。"""
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

    enrich_repos(repos)

    date_str = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")

    ai_cfg = cfg.get("ai", {})
    if ai_cfg.get("enabled", True) and os.environ.get(
        ai_cfg.get("api_key_env", "DEEPSEEK_API_KEY")
    ):
        details = analyze_all(repos, ai_cfg)
    else:
        details = [fallback_details(r) for r in repos]
    for repo, detail in zip(repos, details):
        repo["summary"] = detail["summary"]
        repo["intro"] = detail.get("intro", "")
        repo["features"] = detail.get("features", [])
        repo["audience"] = detail.get("audience", "")

    report = render_report(repos, date_str, cfg.get("pages_url", ""))
    html_page = render_html(
        repos, date_str, cfg.get("pages_url", ""), cfg.get("repo_url", "")
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
