#!/usr/bin/env python3
"""发布日报：更新 README、创建 Issue、@ 提及所有 stargazer（分批评论）。"""
from __future__ import annotations

import json
import os
import re
import time

import requests

API_BASE = "https://api.github.com"

README_START = "<!-- TRENDING:START -->"
README_END = "<!-- TRENDING:END -->"


def _session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )
    return session


def update_readme(report: str) -> None:
    """把 README 中两个标记之间的内容替换为最新日报。"""
    with open("README.md", encoding="utf-8") as fh:
        text = fh.read()
    pattern = re.compile(re.escape(README_START) + r".*?" + re.escape(README_END), re.S)
    if not pattern.search(text):
        raise RuntimeError("README.md 中找不到 TRENDING 标记，请勿删除标记注释")
    new_text = pattern.sub(f"{README_START}\n\n{report}\n{README_END}", text)
    with open("README.md", "w", encoding="utf-8") as fh:
        fh.write(new_text)


def ensure_label(session: requests.Session, owner: str, repo: str) -> None:
    resp = session.post(
        f"{API_BASE}/repos/{owner}/{repo}/labels",
        json={"name": "daily-trending", "color": "FBC02D"},
    )
    if resp.status_code == 422:  # 标签已存在
        return
    resp.raise_for_status()


def find_issue(session: requests.Session, owner: str, repo: str, title: str) -> dict | None:
    resp = session.get(
        f"{API_BASE}/repos/{owner}/{repo}/issues",
        params={"labels": "daily-trending", "state": "all", "per_page": 100},
    )
    resp.raise_for_status()
    for issue in resp.json():
        if issue["title"] == title:
            return issue
    return None


def list_stargazers(session: requests.Session, owner: str, repo: str) -> list[str]:
    users: list[str] = []
    for page in range(1, 31):  # 最多 3000 人，足够日常规模
        resp = session.get(
            f"{API_BASE}/repos/{owner}/{repo}/stargazers",
            params={"per_page": 100, "page": page},
        )
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        users.extend(user["login"] for user in batch)
    return users


def load_opt_out(path: str) -> set[str]:
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        return set(data.get("usernames", []))
    except (OSError, ValueError):
        return set()


def post_mentions(
    session: requests.Session,
    owner: str,
    repo: str,
    issue_number: int,
    report: str,
    users: list[str],
    chunk_size: int,
    pages_url: str = "",
) -> int:
    """分批评论 @ 用户；每批评论正文带上完整榜单，保证邮件里能看到内容。"""
    issue_url = f"https://github.com/{owner}/{repo}/issues/{issue_number}"
    pages_line = f"🎨 精美 HTML 报告：{pages_url}\n" if pages_url else ""
    count = 0
    for i in range(0, len(users), chunk_size):
        chunk = users[i : i + chunk_size]
        body = (
            f"📬 今日 Trending 已送达：{' '.join('@' + user for user in chunk)}\n\n"
            f"{report}\n\n"
            f"---\n"
            f"不想再收？取消 Star，或把你的用户名加进 `data/opt_out.json` 提个 PR，"
            f"或在 GitHub 通知设置里关闭提及通知。\n"
            f"完整榜单：{issue_url}\n"
            f"{pages_line}"
        )
        session.post(
            f"{API_BASE}/repos/{owner}/{repo}/issues/{issue_number}/comments",
            json={"body": body},
        ).raise_for_status()
        count += 1
        time.sleep(1)  # 放慢节奏，避免触发 secondary rate limit
    return count


def publish(report: str, date_str: str, cfg: dict) -> None:
    session = _session()
    owner, repo = os.environ["GITHUB_REPOSITORY"].split("/")
    title = f"🔥 GitHub 每日 Trending · {date_str}"

    update_readme(report)
    ensure_label(session, owner, repo)

    existing = find_issue(session, owner, repo, title)
    if existing:
        # 同一天重复运行（如手动重跑）：只更新内容，不再 @，避免重复打扰
        session.patch(
            f"{API_BASE}/repos/{owner}/{repo}/issues/{existing['number']}",
            json={"body": report},
        ).raise_for_status()
        print(f"⚠️ 今天的 Issue 已存在（#{existing['number']}），已更新内容、跳过 @ 提醒")
        return

    resp = session.post(
        f"{API_BASE}/repos/{owner}/{repo}/issues",
        json={"title": title, "body": report, "labels": ["daily-trending"]},
    )
    resp.raise_for_status()
    issue_number = resp.json()["number"]
    print(f"✅ 已创建 Issue #{issue_number}：{title}")

    mentions = cfg.get("mentions", {})
    if not mentions.get("enabled", True):
        return
    users = list_stargazers(session, owner, repo)
    opt_out = load_opt_out(mentions.get("opt_out_file", "data/opt_out.json"))
    users = [user for user in users if user not in opt_out]
    if not users:
        print("还没有 stargazer，跳过 @ 提醒")
        return
    comment_count = post_mentions(
        session,
        owner,
        repo,
        issue_number,
        report,
        users,
        int(mentions.get("chunk_size", 10)),
        cfg.get("pages_url", ""),
    )
    print(f"✅ 已通过 {comment_count} 条评论 @ 提及 {len(users)} 位 stargazer（邮件已触发）")
