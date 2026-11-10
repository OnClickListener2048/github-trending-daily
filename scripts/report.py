#!/usr/bin/env python3
"""把 Trending 数据渲染成 Markdown 日报和 HTML 报告；逐个仓库调用 LLM 生成详细介绍。

每个仓库单独调用一次 LLM，输入为仓库元数据 + README 原文（截断），输出：
{"summary": "一句话定位", "intro": "详细介绍", "features": ["核心功能"],
 "audience": "适合谁"}

要求是「介绍」而非技术分析：不写底层实现细节，不做数据归因。

支持两种 provider（config.json 的 ai.provider 切换）：
- deepseek（默认）及任何 OpenAI 兼容接口：直接 HTTP 调用，base_url 可配
- anthropic：官方 SDK，需 ANTHROPIC_API_KEY
"""
from __future__ import annotations

import html
import json
import os
import re
from concurrent.futures import ThreadPoolExecutor

import anthropic
import requests

INTRODUCTION_SYSTEM_PROMPT = (
    "你是 GitHub 开源项目的技术编辑。根据 README 内容，为仓库写一份面向开发者的详细项目介绍。"
    "风格要求：像朋友介绍一个好项目一样，讲清楚它是什么、解决什么问题、有哪些核心功能、适合谁。"
    "必须基于 README 的实际内容，写得具体、有信息量；禁止空话套话。"
    "不要罗列底层技术实现细节（除非是项目的关键卖点），不要做 star 数据归因分析。"
    "只输出一个 JSON 对象，不要输出任何其他文字。"
)

# AI 生成的介绍里可能原样照抄 README 中的 "@xxx" 示例（如 "@e1 这样的 ref"），
# 发到 Issue / 评论后 GitHub 会把它当成对真实账号/组织的提及并发送通知。
# 在 @ 后插入零宽空格，显示效果不变，但不再被解析为 mention。
# 负向后顾排除邮箱地址（a@b.com 的 @ 前面是单词字符），避免把邮箱拆坏。
_MENTION_RE = re.compile(r"(?<![A-Za-z0-9._%+-])@(?=[A-Za-z0-9])")


def escape_mentions(text: str) -> str:
    return _MENTION_RE.sub("@\u200b", text or "")


# GitHub 常见语言色（用于 HTML 报告的语言标签圆点）
LANGUAGE_COLORS = {
    "Python": "#3572A5", "JavaScript": "#f1e05a", "TypeScript": "#3178c6",
    "Go": "#00ADD8", "Rust": "#dea584", "C++": "#f34b7d", "C": "#555555",
    "C#": "#178600", "Java": "#b07219", "Shell": "#89e051", "HTML": "#e34c26",
    "CSS": "#563d7c", "Ruby": "#701516", "Swift": "#F05138", "Kotlin": "#A97BFF",
    "PHP": "#4F5D95", "Vue": "#41b883", "Dart": "#00B4AB", "Zig": "#ec915c",
    "Lua": "#000080", "Jupyter Notebook": "#DA5B0B", "MDX": "#fcb32c",
}


def _introduction_user_prompt(repo: dict, readme: str) -> str:
    return (
        f"仓库：{repo['full_name']}\n"
        f"语言：{repo['language'] or '未知'}\n"
        f"总 Star：{repo['stars']:,}，Fork：{repo['forks']:,}\n"
        f"官方描述：{repo['description'][:300] or '（无）'}\n"
        f"README 内容（截断）：\n{readme or '（未获取到）'}\n\n"
        '输出 JSON：{"summary": "一句话定位，20~40字", '
        '"intro": "详细介绍：它是什么、解决什么问题、怎么用，100~200字", '
        '"features": ["核心功能1", "核心功能2", "核心功能3", "核心功能4", "核心功能5", "核心功能6"], '
        '"audience": "适合谁使用，20~40字（不确定就输出空字符串）"}\n'
        "注意：必须是合法 JSON，字符串内如出现双引号要转义为 \\\"。"
    )


def _anthropic_chat(user_prompt: str, api_key: str, model: str) -> str:
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=model,
        max_tokens=2000,
        system=INTRODUCTION_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return "".join(block.text for block in response.content if block.type == "text")


def _openai_compatible_chat(user_prompt: str, api_key: str, model: str, base_url: str) -> str:
    """DeepSeek 等 OpenAI 兼容接口。"""
    resp = requests.post(
        f"{base_url.rstrip('/')}/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": model,
            "temperature": 0.3,
            "max_tokens": 2000,
            "messages": [
                {"role": "system", "content": INTRODUCTION_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
        },
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def fallback_details(repo: dict) -> dict:
    """AI 不可用时的兜底内容。"""
    return {
        "summary": repo["description"][:50] or "（暂无介绍）",
        "intro": repo["description"] or "",
        "features": [],
        "audience": "",
    }


def _parse_details(text: str, repo: dict) -> dict:
    """解析 AI 返回的 JSON 对象；失败抛 ValueError。"""
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end <= start:
        raise ValueError(f"AI 返回中找不到 JSON 对象: {text[:200]}")
    data = json.loads(text[start : end + 1])
    if not isinstance(data, dict):
        raise ValueError("AI 返回的不是 JSON 对象")

    result = {
        "summary": str(data.get("summary") or "").strip() or fallback_details(repo)["summary"],
        "intro": str(data.get("intro") or "").strip() or repo["description"],
        "audience": str(data.get("audience") or "").strip(),
    }
    features = data.get("features")
    result["features"] = (
        [str(f).strip() for f in features if str(f).strip()][:6]
        if isinstance(features, list)
        else []
    )
    return result


def analyze_repo(repo: dict, cfg: dict) -> dict:
    """对单个仓库生成一次独立的详细介绍；解析失败自动重试一次。"""
    api_key = os.environ.get(cfg.get("api_key_env", "DEEPSEEK_API_KEY"))
    if not api_key:
        raise ValueError(f"未配置环境变量 {cfg.get('api_key_env', 'DEEPSEEK_API_KEY')}")
    model = cfg.get("model", "deepseek-flash")
    readme = (repo.get("readme") or "")[: int(cfg.get("readme_chars", 6000))]
    user_prompt = _introduction_user_prompt(repo, readme)

    last_error: Exception | None = None
    for attempt in range(2):
        try:
            if cfg.get("provider", "deepseek") == "anthropic":
                text = _anthropic_chat(user_prompt, api_key, model)
            else:
                text = _openai_compatible_chat(
                    user_prompt,
                    api_key,
                    model,
                    cfg.get("base_url", "https://api.deepseek.com/v1"),
                )
            return _parse_details(text, repo)
        except (ValueError, json.JSONDecodeError, requests.RequestException) as exc:
            last_error = exc
            # 第二次尝试时提醒模型输出合法 JSON
            user_prompt += "\n\n注意：你上一次的输出不是合法 JSON（字符串内的双引号必须转义为 \\\"）。请重新输出一次。"
    raise ValueError(f"两次尝试均失败：{last_error}")


def analyze_all(
    repos: list[dict],
    cfg: dict,
    cache: dict | None = None,
    date_str: str = "",
    use_ai: bool = True,
) -> list[dict]:
    """并发生成详细介绍；优先复用 cache 中已分析过的结果。

    cache 以 full_name 为键，分析成功后原地写回（含 analyzed_at、first_seen
    等字段）。use_ai=False（关闭 AI 或没配 Key）时缓存命中仍复用，否则兜底。
    """
    cache = cache if cache is not None else {}
    results: list[dict] = [fallback_details(r) for r in repos]

    def work(index: int) -> tuple[int, dict]:
        repo = repos[index]
        entry = cache.get(repo["full_name"]) or {}
        if entry.get("summary"):
            return index, {
                "summary": entry["summary"],
                "intro": entry.get("intro", ""),
                "features": entry.get("features", []),
                "audience": entry.get("audience", ""),
            }
        if not use_ai:
            return index, fallback_details(repo)
        try:
            detail = analyze_repo(repo, cfg)
        except Exception as exc:  # 单个仓库失败回退，不写缓存，下次重试
            print(f"⚠️ {repo['full_name']} 介绍生成失败，已回退：{exc}")
            return index, fallback_details(repo)
        entry.update(detail)
        entry["analyzed_at"] = date_str
        cache[repo["full_name"]] = entry
        return index, detail

    workers = int(cfg.get("workers", 5))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for index, detail in pool.map(work, range(len(repos))):
            results[index] = detail
    return results


def render_report(
    repos: list[dict],
    date_str: str,
    pages_url: str = "",
    top_n: int = 10,
    featured: list[dict] | None = None,
) -> str:
    """渲染 Markdown 日报（Issue 正文 / README 区块 / @提及邮件内容）。

    featured 是进入详细介绍的仓库列表（默认前 top_n 个）。连续在榜较久的
    仓库会被跳过并由后面的仓库顺延补位，因此编号沿用完整榜单里的原始名次，
    可能出现不连续。
    """
    top = list(featured) if featured is not None else repos[:top_n]
    rank_of = {r["full_name"]: i for i, r in enumerate(repos, 1)}

    lines = [
        f"# 🔥 GitHub 每日 Trending · {date_str}",
        "",
        f"> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 {len(repos)} 个仓库",
    ]
    if pages_url:
        lines.append(f"> 🎨 [打开精美 HTML 报告]({pages_url})（推荐浏览器查看）")
    lines += ["", "## 🏆 今日精选（详细介绍）", ""]

    for r in top:
        i = rank_of.get(r["full_name"], 0)
        lines.append(
            f"### {i}. [{r['full_name']}]({r['url']}) — ⭐ {r['stars']:,}（今日 +{r['stars_today']:,}）"
        )
        lines.append("")
        lines.append(f"> {r['summary']}")
        lines.append("")
        if r.get("intro"):
            lines.append(r["intro"])
            lines.append("")
        for feature in r.get("features", []):
            lines.append(f"- ✨ {feature}")
        if r.get("audience"):
            lines.append(f"- 👥 适合谁：{r['audience']}")
        lines.append("")
        meta = []
        if r["language"]:
            meta.append(f"`{r['language']}`")
        meta.append(f"Fork {r['forks']:,}")
        if r.get("homepage"):
            meta.append(f"🔗 [官网]({r['homepage']})")
        lines.append(" · ".join(meta))
        lines.append("")

    lines += [
        "## 📋 完整榜单",
        "",
        "| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for i, r in enumerate(repos, 1):
        summary = r["summary"].replace("|", "\\|")
        if len(summary) > 45:
            summary = summary[:45] + "…"
        lang = f"`{r['language']}`" if r["language"] else "—"
        lines.append(
            f"| {i} | [{r['full_name']}]({r['url']}) | {summary} | {lang} | {r['stars']:,} | +{r['stars_today']:,} |"
        )
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


_CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
:root {
  --bg: #f6f8fa; --card: #ffffff; --panel: #f6f8fa; --text: #1f2328;
  --muted: #59636e; --border: #d1d9e0; --accent: #0969da; --accent-soft: #ddf4ff;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0d1117; --card: #161b22; --panel: #0d1117; --text: #e6edf3;
    --muted: #8b949e; --border: #30363d; --accent: #4493f8; --accent-soft: #0c2d6b;
  }
}
html { -webkit-text-size-adjust: 100%; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
    "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  background: var(--bg); color: var(--text); line-height: 1.6;
}
a { color: var(--accent); text-decoration: none; }
.hero { text-align: center; padding: 48px 20px 32px; }
.hero h1 { font-size: 1.9rem; margin-bottom: 8px; }
.hero .date { color: var(--muted); }
.hero .sub { color: var(--muted); margin-top: 12px; font-size: .93rem; }
.btn {
  display: inline-block; margin-top: 16px; padding: 9px 20px;
  background: var(--accent); color: #fff !important; border-radius: 999px;
  font-weight: 600; font-size: .93rem;
}
main { max-width: 1080px; margin: 0 auto; padding: 0 20px 56px; }
section h2 { font-size: 1.3rem; margin: 26px 0 14px; }
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(300px, 100%), 1fr));
  gap: 16px;
}
.grid.featured {
  grid-template-columns: repeat(auto-fill, minmax(min(420px, 100%), 1fr));
  gap: 20px;
}
.card {
  display: flex; flex-direction: column; gap: 10px;
  background: var(--card); border: 1px solid var(--border); border-radius: 12px;
  padding: 18px; overflow-wrap: anywhere;
}
.card-head { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.name { font-weight: 700; font-size: 1rem; }
.rank {
  background: var(--accent); color: #fff; border-radius: 8px;
  padding: 1px 10px; font-size: .9rem; font-weight: 700;
}
.summary {
  font-size: .92rem; display: -webkit-box; -webkit-line-clamp: 2;
  -webkit-box-orient: vertical; overflow: hidden;
}
.card.featured .summary { -webkit-line-clamp: unset; }
.intro { font-size: .92rem; }
.card.featured .intro { font-size: .95rem; }
.hl { list-style: none; display: flex; flex-direction: column; gap: 5px; }
.hl li { font-size: .88rem; padding-left: 18px; position: relative; }
.hl li::before { content: "✨"; position: absolute; left: 0; }
.audience { font-size: .86rem; color: var(--muted); }
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chip {
  background: var(--accent-soft); color: var(--accent);
  border-radius: 999px; padding: 2px 10px; font-size: 12px;
}
.chip .dot {
  display: inline-block; width: 8px; height: 8px;
  border-radius: 50%; margin-right: 5px;
}
details.intro-toggle { font-size: .88rem; }
details.intro-toggle summary {
  cursor: pointer; color: var(--accent); font-weight: 600; user-select: none;
}
details.intro-toggle > *:not(summary) { margin-top: 8px; }
.stats {
  display: flex; flex-wrap: wrap; gap: 12px; align-items: center;
  margin-top: auto; padding-top: 10px; border-top: 1px solid var(--border);
  font-size: .85rem; color: var(--muted);
}
.stats .hot { color: #d1242f; font-weight: 600; }
footer { text-align: center; padding: 26px 20px 46px; color: var(--muted); font-size: .85rem; }
"""


def _intro_html(r: dict) -> str:
    """详细介绍区（featured 内联展示，普通卡片折叠展示）。"""
    parts = []
    if r.get("intro"):
        parts.append(f'<p class="intro">{html.escape(r["intro"])}</p>')
    features = r.get("features", [])
    if features:
        items = "".join(f"<li>{html.escape(f)}</li>" for f in features)
        parts.append(f'<ul class="hl">{items}</ul>')
    if r.get("audience"):
        parts.append(
            f'<p class="audience">👥 适合谁：{html.escape(r["audience"])}</p>'
        )
    return "".join(parts)


def _card_html(r: dict, i: int, featured: bool) -> str:
    name = html.escape(r["full_name"])
    summary = html.escape(r["summary"])
    intro_html = _intro_html(r)
    topics = "".join(
        f'<span class="chip">{html.escape(t)}</span>' for t in r.get("topics", [])[:4]
    )
    lang = r.get("language") or ""
    lang_chip = ""
    if lang:
        color = LANGUAGE_COLORS.get(lang, "#8b949e")
        lang_chip = (
            f'<span class="chip"><span class="dot" style="background:{color}"></span>'
            f"{html.escape(lang)}</span>"
        )
    homepage = (
        f'<a href="{html.escape(r["homepage"])}" target="_blank" rel="noopener">🔗 官网</a>'
        if r.get("homepage")
        else ""
    )
    stats = (
        f'<div class="stats"><span>⭐ {r["stars"]:,}</span>'
        f'<span class="hot">🔥 今日 +{r["stars_today"]:,}</span>'
        f'<span>🍴 {r["forks"]:,}</span>{lang_chip}{homepage}</div>'
    )

    cls = "card featured" if featured else "card"
    rank = f'<span class="rank">#{i}</span>' if featured else ""
    head = (
        f'<div class="card-head">{rank}'
        f'<a class="name" href="{html.escape(r["url"])}" target="_blank" rel="noopener">{name}</a></div>'
    )
    chips_html = f'<div class="chips">{topics}</div>' if topics else ""
    body = f'<p class="summary">{summary}</p>'
    if featured:
        body += intro_html + chips_html
    else:
        body += chips_html
        if intro_html:
            body += (
                f'<details class="intro-toggle"><summary>📖 详细介绍</summary>'
                f"{intro_html}</details>"
            )
    return f'<div class="{cls}">{head}{body}{stats}</div>'


def render_html(
    repos: list[dict],
    date_str: str,
    pages_url: str = "",
    repo_url: str = "",
    top_n: int = 10,
    featured: list[dict] | None = None,
) -> str:
    """渲染完全自定义样式的 HTML 报告页（GitHub Pages）。

    精选卡片编号沿用完整榜单里的 GitHub 原始名次（可能不连续）。
    """
    top = list(featured) if featured is not None else repos[:top_n]
    rank_of = {r["full_name"]: i for i, r in enumerate(repos, 1)}
    top_html = "\n".join(
        _card_html(r, rank_of.get(r["full_name"], 0), True) for r in top
    )
    all_html = "\n".join(_card_html(r, i, False) for i, r in enumerate(repos, 1))

    cta = (
        f'<a class="btn" href="{html.escape(repo_url)}" target="_blank" rel="noopener">'
        "⭐ Star 订阅每日推送</a>"
        if repo_url
        else ""
    )
    footer_link = (
        f'<a href="{html.escape(repo_url)}" target="_blank" rel="noopener">GitHub 仓库</a> · '
        if repo_url
        else ""
    )

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>🔥 GitHub 每日 Trending · {date_str}</title>
<style>{_CSS}</style>
</head>
<body>
<header class="hero">
  <h1>🔥 GitHub 每日 Trending</h1>
  <p class="date">{date_str} · 每天 08:00（北京时间）自动更新 · 共 {len(repos)} 个仓库</p>
  <p class="sub">数据来源 <a href="https://github.com/trending?since=daily" target="_blank" rel="noopener">github.com/trending</a></p>
  {cta}
</header>
<main>
  <section>
    <h2>🏆 今日精选（详细介绍）</h2>
    <div class="grid featured">
{top_html}
    </div>
  </section>
  <section>
    <h2>📋 完整榜单（点开卡片查看详细介绍）</h2>
    <div class="grid">
{all_html}
    </div>
  </section>
</main>
<footer>
  {footer_link}每日 {date_str} · 由 GitHub Actions 自动生成 · 本页面与 GitHub 无关
</footer>
</body>
</html>
"""
