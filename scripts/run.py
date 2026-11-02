#!/usr/bin/env python3
"""编排入口：抓取 → 生成日报（可选 AI 简介）→ 发布。"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timedelta, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from trending import fetch_trending  # noqa: E402
from report import generate_intros, render_report  # noqa: E402
import publish  # noqa: E402

ROOT = os.path.dirname(SCRIPT_DIR)


def load_config() -> dict:
    with open(os.path.join(ROOT, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


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

    intros = None
    ai_cfg = cfg.get("ai", {})
    if ai_cfg.get("enabled", True) and os.environ.get(
        ai_cfg.get("api_key_env", "DEEPSEEK_API_KEY")
    ):
        try:
            intros = generate_intros(repos, ai_cfg)
        except Exception as exc:  # AI 失败不影响推送，回退到原始描述
            print(f"⚠️ AI 简介生成失败，已回退到仓库原始描述：{exc}")

    report = render_report(repos, date_str, intros)

    daily_dir = os.path.join(ROOT, "data", "daily")
    os.makedirs(daily_dir, exist_ok=True)
    with open(os.path.join(daily_dir, f"{date_str}.md"), "w", encoding="utf-8") as fh:
        fh.write(report)
    print(f"✅ 日报已生成：data/daily/{date_str}.md（{len(repos)} 个仓库）")

    if os.environ.get("GITHUB_ACTIONS") == "true":
        publish.publish(report, date_str, cfg)


if __name__ == "__main__":
    main()
