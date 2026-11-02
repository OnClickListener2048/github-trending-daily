#!/usr/bin/env python3
"""抓取 GitHub Trending 页面（GitHub 没有官方的 trending API，直接解析 HTML）。"""
from __future__ import annotations

import re
import time

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

_NUMBER_RE = re.compile(r"[\d,]+")


def _parse_number(text: str) -> int:
    """从 '1,234' / '123 stars today' 这类文本中提取整数。"""
    match = _NUMBER_RE.search(text or "")
    return int(match.group().replace(",", "")) if match else 0


def _repo_href(article: BeautifulSoup) -> str | None:
    """取仓库链接（跳过 Sponsor 按钮等无关链接）。"""
    for link in article.select("h2 a"):
        href = link.get("href", "")
        if href.startswith("/") and not href.startswith("/sponsors"):
            return href
    return None


def fetch_trending(language: str | None = None, since: str = "daily") -> list[dict]:
    """抓取某个语言（None 表示全语言）的 trending 列表。"""
    url = "https://github.com/trending"
    if language:
        url += f"/{language}"
    url += f"?since={since}"

    last_error: Exception | None = None
    for attempt in range(4):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            if resp.status_code == 429:
                raise RuntimeError("rate limited (429)")
            resp.raise_for_status()
            break
        except Exception as exc:  # 网络抖动 / 429 时指数退避重试
            last_error = exc
            time.sleep(2 ** attempt * 5)
    else:
        raise RuntimeError(f"抓取失败 {url}: {last_error}")

    soup = BeautifulSoup(resp.text, "html.parser")
    repos: list[dict] = []
    for article in soup.select("article.Box-row"):
        href = _repo_href(article)
        if not href:
            continue
        description = article.select_one("p")
        language_el = article.select_one('span[itemprop="programmingLanguage"]')
        stars_el = article.select_one('a[href$="/stargazers"]')
        forks_el = article.select_one('a[href$="/forks"]')
        today_el = article.select_one("span.d-inline-block.float-sm-right")
        repos.append(
            {
                "full_name": href.strip("/"),
                "url": f"https://github.com{href}",
                "description": description.get_text(strip=True) if description else "",
                "language": language_el.get_text(strip=True) if language_el else "",
                "stars": _parse_number(stars_el.get_text() if stars_el else ""),
                "forks": _parse_number(forks_el.get_text() if forks_el else ""),
                "stars_today": _parse_number(today_el.get_text() if today_el else ""),
            }
        )
    return repos


if __name__ == "__main__":
    import json

    print(json.dumps(fetch_trending(), ensure_ascii=False, indent=2))
