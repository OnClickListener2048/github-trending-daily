#!/usr/bin/env python3
"""独立创业 / 一人公司渠道抓取：Show HN、Product Hunt、V2EX 分享创造。

所有渠道返回统一结构：
{"id": "hn:123" | "ph:123" | "v2ex:123", "title": str, "url": str,
 "tagline": str, "points": int, "comments": int}
"""
from __future__ import annotations

import html as html_lib
import re
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

import requests

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
)

POST_SUMMARY_SYSTEM_PROMPT = (
    "你是面向开发者的中文技术编辑，擅长把社区热帖和新产品介绍翻译并浓缩成一句中文。"
    "要求：20~45 字，保留产品名和关键信息，必须输出中文（标题是英文时要翻译），只输出这一句话。"
)

_SOURCE_LABEL = {
    "show_hn": "Hacker News 的 Show HN 新品发布帖",
    "product_hunt": "Product Hunt 上今天新发布的产品",
    "v2ex": "V2EX「分享创造」节点里中文独立开发者的作品帖",
}


def _get(url: str, params: dict | None = None, timeout: int = 20) -> requests.Response:
    return requests.get(
        url,
        params=params,
        headers={"User-Agent": UA, "Accept": "*/*"},
        timeout=timeout,
    )


def fetch_show_hn(cfg: dict) -> list[dict]:
    """HN Algolia：最近的 Show HN 帖，按分数取前 N 条（N = count * 2，留冷却缓冲）。"""
    count = int(cfg.get("count", 3)) * 2
    min_points = int(cfg.get("min_points", 20))
    data = _get(
        "https://hn.algolia.com/api/v1/search_by_date",
        {"tags": "show_hn", "hitsPerPage": 30, "numericFilters": f"points>{min_points}"},
    ).json()
    hits = [h for h in data.get("hits", []) if h.get("title")]
    hits.sort(key=lambda h: h.get("points") or 0, reverse=True)
    return [
        {
            "id": f"hn:{h['objectID']}",
            "title": h["title"].replace("Show HN:", "").strip() or h["title"],
            "url": f"https://news.ycombinator.com/item?id={h['objectID']}",
            "tagline": "",
            "points": h.get("points") or 0,
            "comments": h.get("num_comments") or 0,
        }
        for h in hits[:count]
    ]


def fetch_product_hunt(cfg: dict) -> list[dict]:
    """Product Hunt 官方 Atom feed（/feed）：按发布时间取前 N 条，含一句话介绍。"""
    count = int(cfg.get("count", 5)) * 2
    resp = _get("https://www.producthunt.com/feed")
    resp.raise_for_status()
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(resp.content)
    items: list[dict] = []
    for entry in root.findall("a:entry", ns):
        title_el = entry.find("a:title", ns)
        link_el = entry.find("a:link", ns)
        id_el = entry.find("a:id", ns)
        content_el = entry.find("a:content", ns)
        tagline = ""
        if content_el is not None and content_el.text:
            # content 里是转义后的 HTML，形如 <p>一句话介绍</p>
            text = html_lib.unescape(content_el.text)
            match = re.search(r"<p>\s*(.*?)\s*</p>", text, re.S)
            if match:
                tagline = re.sub(r"<[^>]+>", "", match.group(1)).strip()
        raw_id = (id_el.text or "").strip().rsplit("/", 1)[-1]
        items.append(
            {
                "id": f"ph:{raw_id}",
                "title": (title_el.text or "").strip(),
                "url": link_el.get("href", "") if link_el is not None else "",
                "tagline": tagline,
                "points": 0,
                "comments": 0,
            }
        )
    return items[:count]


def fetch_v2ex_create(cfg: dict) -> list[dict]:
    """V2EX「分享创造」节点：最近的独立开发者作品帖。"""
    count = int(cfg.get("count", 5)) * 2
    data = _get(
        "https://www.v2ex.com/api/topics/show.json", {"node_name": "create"}
    ).json()
    return [
        {
            "id": f"v2ex:{t['id']}",
            "title": t["title"],
            "url": f"https://www.v2ex.com/t/{t['id']}",
            "tagline": "",
            "points": 0,
            "comments": t.get("replies", 0),
        }
        for t in data[:count]
    ]


CHANNELS: dict[str, dict] = {
    "show_hn": {
        "title": "🚀 Show HN 今日新品",
        "fetch": fetch_show_hn,
    },
    "product_hunt": {
        "title": "🧡 Product Hunt 今日榜",
        "fetch": fetch_product_hunt,
    },
    "v2ex": {
        "title": "🇨🇳 中文独立开发 · V2EX 分享创造",
        "fetch": fetch_v2ex_create,
    },
}


def post_fallback(item: dict) -> str:
    """AI 不可用时的兜底摘要。"""
    text = item.get("tagline") or item["title"]
    return text[:60] + ("…" if len(text) > 60 else "")


def _post_user_prompt(item: dict, source: str) -> str:
    lines = [f"来源：{_SOURCE_LABEL[source]}", f"标题：{item['title']}"]
    if item.get("tagline"):
        lines.append(f"官方一句话介绍：{item['tagline']}")
    if item.get("points"):
        lines.append(f"热度：{item['points']} 分，{item.get('comments', 0)} 条评论")
    lines.append("")
    lines.append("请用一句中文（20~45 字）概括这个作品/帖子，保留产品名和关键信息。只输出这一句话。")
    return "\n".join(lines)


def _summarize_one(item: dict, source: str, cfg: dict) -> str:
    api_key_env = cfg.get("api_key_env", "DEEPSEEK_API_KEY")
    import os

    api_key = os.environ.get(api_key_env)
    if not api_key:
        raise ValueError(f"未配置环境变量 {api_key_env}")
    model = cfg.get("model", "deepseek-flash")
    user_prompt = _post_user_prompt(item, source)
    if cfg.get("provider", "deepseek") == "anthropic":
        import anthropic

        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model=model,
            max_tokens=200,
            system=POST_SUMMARY_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        text = "".join(block.text for block in response.content if block.type == "text")
    else:
        resp = requests.post(
            f"{cfg.get('base_url', 'https://api.deepseek.com/v1').rstrip('/')}/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": model,
                "temperature": 0.3,
                "max_tokens": 200,
                "messages": [
                    {"role": "system", "content": POST_SUMMARY_SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
            },
            timeout=120,
        )
        resp.raise_for_status()
        text = resp.json()["choices"][0]["message"]["content"]
    return text.strip()


def summarize_posts(
    items: list[dict], source: str, cfg: dict, cache: dict, date_str: str, use_ai: bool
) -> None:
    """并行为帖子生成一句话中文摘要；优先复用缓存（同一天重跑幂等）。"""

    def work(item: dict) -> None:
        entry = cache.get(item["id"]) or {}
        if entry.get("summary"):
            item["summary"] = entry["summary"]
            return
        item["summary"] = post_fallback(item)
        if not use_ai:
            return
        try:
            summary = _summarize_one(item, source, cfg)
        except Exception as exc:  # 单个失败不影响整体
            print(f"⚠️ {item['id']} 摘要生成失败，用原标题兜底：{exc}")
            return
        if not summary:
            print(f"⚠️ {item['id']} 摘要为空，保持兜底，不写缓存")
            return
        # AI 原样回显标题/官方简介的不算有效摘要，不缓存（保持兜底，冷却后重试）
        if summary == item["title"] or (item.get("tagline") and summary == item["tagline"]):
            print(f"⚠️ {item['id']} AI 原样回显，保持兜底，不写缓存")
            return
        entry["summary"] = summary
        entry["analyzed_at"] = date_str
        cache[item["id"]] = entry
        item["summary"] = summary

    workers = int(cfg.get("workers", 5))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(work, items))


def build_post_sections(
    posts_cfg: dict,
    ai_cfg: dict,
    cache: dict,
    date_str: str,
    cooldown_days: int,
    use_ai: bool,
) -> list[dict]:
    """抓取各渠道并按冷却期过滤，返回今日要展示的栏目列表。

    栏目结构：{"key": str, "title": str, "items": [{"title", "url", "summary", "meta"}]}
    单个渠道失败只跳过该栏目，不影响整体。
    """
    cutoff = (
        datetime.strptime(date_str, "%Y-%m-%d") - timedelta(days=cooldown_days)
    ).strftime("%Y-%m-%d")
    sections: list[dict] = []
    for key, spec in CHANNELS.items():
        channel_cfg = posts_cfg.get(key) or {}
        if not channel_cfg.get("enabled", True):
            continue
        count = int(channel_cfg.get("count", 3 if key == "show_hn" else 5))
        try:
            items = spec["fetch"](channel_cfg)
        except Exception as exc:
            print(f"⚠️ {spec['title']} 抓取失败，本栏目跳过：{exc}")
            continue
        fresh: list[dict] = []
        for item in items:
            last_seen = cache.get(item["id"], {}).get("last_seen", "")
            # 冷却期内展示过的跳过；当天已展示的允许同日重跑复用（幂等）
            if last_seen and last_seen >= cutoff and last_seen != date_str:
                continue
            fresh.append(item)
            if len(fresh) >= count:
                break
        if not fresh:
            print(f"⚠️ {spec['title']} 没有冷却期外的新内容，本栏目跳过")
            continue

        summarize_posts(fresh, key, ai_cfg, cache, date_str, use_ai)
        for item in fresh:
            entry = cache.setdefault(item["id"], {})
            entry.setdefault("first_seen", date_str)
            entry["last_seen"] = date_str
        for item in fresh:
            if key == "show_hn" and item.get("points"):
                item["meta"] = f"⬆️ {item['points']} · 💬 {item['comments']}"
            elif key == "product_hunt":
                item["meta"] = "Product Hunt"
            elif key == "v2ex":
                item["meta"] = f"💬 {item['comments']} 回复"
            else:
                item["meta"] = ""
        sections.append({"key": key, "title": spec["title"], "items": fresh})
    return sections
