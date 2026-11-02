#!/usr/bin/env python3
"""把 Trending 数据渲染成 Markdown 日报和 HTML 报告；逐个仓库调用 LLM 深度分析。

每个仓库单独调用一次 LLM，输入为仓库元数据 + README 原文（截断），输出：
{"summary": "一句话定位", "what": "是什么/解决什么痛点", "tech": "技术方案",
 "highlights": ["亮点"], "audience": "适合谁", "why_trending": "为什么火"}

支持两种 provider（config.json 的 ai.provider 切换）：
- deepseek（默认）及任何 OpenAI 兼容接口：直接 HTTP 调用，base_url 可配
- anthropic：官方 SDK，需 ANTHROPIC_API_KEY
"""
from __future__ import annotations

import html
import json
import os
from concurrent.futures import ThreadPoolExecutor

import anthropic
import requests

ANALYSIS_SYSTEM_PROMPT = (
    "你是一名资深技术分析师，为 GitHub Trending 仓库撰写个性化深度分析。"
    "必须基于给定的 README 内容和数据给出具体、有洞察的判断，禁止套话空话"
    "（如「为开发者提供强大能力」「提升开发效率」这类泛泛之谈）。"
    "只输出一个 JSON 对象，不要输出任何其他文字。"
)

# GitHub 常见语言色（用于 HTML 报告的语言标签圆点）
LANGUAGE_COLORS = {
    "Python": "#3572A5", "JavaScript": "#f1e05a", "TypeScript": "#3178c6",
    "Go": "#00ADD8", "Rust": "#dea584", "C++": "#f34b7d", "C": "#555555",
    "C#": "#178600", "Java": "#b07219", "Shell": "#89e051", "HTML": "#e34c26",
    "CSS": "#563d7c", "Ruby": "#701516", "Swift": "#F05138", "Kotlin": "#A97BFF",
    "PHP": "#4F5D95", "Vue": "#41b883", "Dart": "#00B4AB", "Zig": "#ec915c",
    "Lua": "#000080", "Jupyter Notebook": "#DA5B0B", "MDX": "#fcb32c",
}


def _analysis_user_prompt(repo: dict, readme: str) -> str:
    return (
        f"仓库：{repo['full_name']}\n"
        f"语言：{repo['language'] or '未知'}\n"
        f"总 Star：{repo['stars']:,}，今日新增：+{repo['stars_today']:,}，Fork：{repo['forks']:,}\n"
        f"官方描述：{repo['description'][:300] or '（无）'}\n"
        f"README 内容（截断）：\n{readme or '（未获取到）'}\n\n"
        '输出 JSON：{"summary": "一句话定位，20~40字", '
        '"what": "它是什么、解决什么痛点，40~80字", '
        '"tech": "核心技术方案或架构亮点，40~80字", '
        '"highlights": ["亮点1", "亮点2", "亮点3"], '
        '"audience": "适合谁使用，20~40字", '
        '"why_trending": "结合今日新增数据，分析它为什么火，30~60字"}'
    )


def _anthropic_chat(user_prompt: str, api_key: str, model: str) -> str:
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=model,
        max_tokens=2000,
        system=ANALYSIS_SYSTEM_PROMPT,
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
                {"role": "system", "content": ANALYSIS_SYSTEM_PROMPT},
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
        "summary": (repo["description"][:50] or "（暂无介绍）"),
        "what": "",
        "tech": "",
        "highlights": [],
        "audience": "",
        "why_trending": "",
    }


def analyze_repo(repo: dict, cfg: dict) -> dict:
    """对单个仓库做一次独立的深度分析；失败时抛异常由调用方回退。"""
    api_key = os.environ.get(cfg.get("api_key_env", "DEEPSEEK_API_KEY"))
    if not api_key:
        raise ValueError(f"未配置环境变量 {cfg.get('api_key_env', 'DEEPSEEK_API_KEY')}")
    model = cfg.get("model", "deepseek-flash")
    readme = (repo.get("readme") or "")[: int(cfg.get("readme_chars", 6000))]
    user_prompt = _analysis_user_prompt(repo, readme)

    if cfg.get("provider", "deepseek") == "anthropic":
        text = _anthropic_chat(user_prompt, api_key, model)
    else:
        text = _openai_compatible_chat(
            user_prompt, api_key, model, cfg.get("base_url", "https://api.deepseek.com/v1")
        )

    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end <= start:
        raise ValueError(f"AI 返回中找不到 JSON 对象: {text[:200]}")
    data = json.loads(text[start : end + 1])
    if not isinstance(data, dict):
        raise ValueError("AI 返回的不是 JSON 对象")

    result = {
        "summary": str(data.get("summary") or "").strip() or fallback_details(repo)["summary"],
        "what": str(data.get("what") or "").strip(),
        "tech": str(data.get("tech") or "").strip(),
        "audience": str(data.get("audience") or "").strip(),
        "why_trending": str(data.get("why_trending") or "").strip(),
    }
    highlights = data.get("highlights")
    result["highlights"] = (
        [str(h).strip() for h in highlights if str(h).strip()][:3]
        if isinstance(highlights, list)
        else []
    )
    return result


def analyze_all(repos: list[dict], cfg: dict) -> list[dict]:
    """并发地对每个仓库做独立深度分析；单个失败不影响整体。"""
    results: list[dict] = [fallback_details(r) for r in repos]

    def work(index: int) -> tuple[int, dict]:
        try:
            return index, analyze_repo(repos[index], cfg)
        except Exception as exc:  # 单个仓库失败回退
            print(f"⚠️ {repos[index]['full_name']} 分析失败，已回退：{exc}")
            return index, fallback_details(repos[index])

    workers = int(cfg.get("workers", 5))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for index, detail in pool.map(work, range(len(repos))):
            results[index] = detail
    return results


def render_report(repos: list[dict], date_str: str, pages_url: str = "") -> str:
    """渲染 Markdown 日报（Issue 正文 / README 区块 / @提及邮件内容）。"""
    top5 = sorted(repos, key=lambda r: r["stars_today"], reverse=True)[:5]

    lines = [
        f"# 🔥 GitHub 每日 Trending · {date_str}",
        "",
        f"> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 {len(repos)} 个仓库",
    ]
    if pages_url:
        lines.append(f"> 🎨 [打开精美 HTML 报告]({pages_url})（推荐浏览器查看）")
    lines += ["", "## 🏆 今日之星 TOP 5（深度解析）", ""]

    for i, r in enumerate(top5, 1):
        lines.append(
            f"### {i}. [{r['full_name']}]({r['url']}) — ⭐ {r['stars']:,}（今日 +{r['stars_today']:,}）"
        )
        lines.append("")
        lines.append(f"> {r['summary']}")
        lines.append("")
        deep_rows = [
            ("🎯 它是什么", r.get("what", "")),
            ("⚙️ 技术方案", r.get("tech", "")),
            ("👥 适合谁", r.get("audience", "")),
            ("🔥 为什么火", r.get("why_trending", "")),
        ]
        for label, text in deep_rows:
            if text:
                lines.append(f"- **{label}**：{text}")
        for h in r.get("highlights", []):
            lines.append(f"- 💡 {h}")
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
.grid.top5 {
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
.deep {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(230px, 100%), 1fr));
  gap: 10px 16px;
}
.deep-item {
  background: var(--panel); border: 1px solid var(--border);
  border-radius: 8px; padding: 10px 12px;
}
.deep-item .label {
  display: block; font-size: .78rem; font-weight: 700;
  color: var(--muted); margin-bottom: 4px;
}
.deep-item p, .deep-item li { font-size: .86rem; }
.hl { list-style: none; display: flex; flex-direction: column; gap: 4px; }
.hl li { padding-left: 16px; position: relative; }
.hl li::before { content: "▸"; position: absolute; left: 2px; color: var(--accent); }
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chip {
  background: var(--accent-soft); color: var(--accent);
  border-radius: 999px; padding: 2px 10px; font-size: 12px;
}
.chip .dot {
  display: inline-block; width: 8px; height: 8px;
  border-radius: 50%; margin-right: 5px;
}
details.deep-toggle { font-size: .88rem; }
details.deep-toggle summary {
  cursor: pointer; color: var(--accent); font-weight: 600; user-select: none;
}
details.deep-toggle .deep { margin-top: 10px; }
.stats {
  display: flex; flex-wrap: wrap; gap: 12px; align-items: center;
  margin-top: auto; padding-top: 10px; border-top: 1px solid var(--border);
  font-size: .85rem; color: var(--muted);
}
.stats .hot { color: #d1242f; font-weight: 600; }
footer { text-align: center; padding: 26px 20px 46px; color: var(--muted); font-size: .85rem; }
"""


def _deep_html(r: dict) -> str:
    """深度分析区（featured 内联展示，普通卡片折叠展示）。"""
    items = []
    highlights = "".join(f"<li>{html.escape(h)}</li>" for h in r.get("highlights", []))
    if highlights:
        items.append(
            f'<div class="deep-item"><span class="label">💡 亮点</span>'
            f'<ul class="hl">{highlights}</ul></div>'
        )
    for label, key in [
        ("🎯 它是什么", "what"),
        ("⚙️ 技术方案", "tech"),
        ("👥 适合谁", "audience"),
        ("🔥 为什么火", "why_trending"),
    ]:
        text = r.get(key, "")
        if text:
            items.append(
                f'<div class="deep-item"><span class="label">{label}</span>'
                f"<p>{html.escape(text)}</p></div>"
            )
    return f'<div class="deep">{"".join(items)}</div>' if items else ""


def _card_html(r: dict, i: int, featured: bool) -> str:
    name = html.escape(r["full_name"])
    summary = html.escape(r["summary"])
    deep = _deep_html(r)
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
        body += deep
        body += chips_html
    else:
        body += chips_html
        if deep:
            body += f'<details class="deep-toggle"><summary>🔍 深度分析</summary>{deep}</details>'
    return f'<div class="{cls}">{head}{body}{stats}</div>'


def render_html(
    repos: list[dict], date_str: str, pages_url: str = "", repo_url: str = ""
) -> str:
    """渲染完全自定义样式的 HTML 报告页（GitHub Pages）。"""
    top5 = sorted(repos, key=lambda r: r["stars_today"], reverse=True)[:5]
    top5_html = "\n".join(_card_html(r, i, True) for i, r in enumerate(top5, 1))
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
    <h2>🏆 今日之星 TOP 5（深度解析）</h2>
    <div class="grid top5">
{top5_html}
    </div>
  </section>
  <section>
    <h2>📋 完整榜单（点开卡片查看深度分析）</h2>
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
