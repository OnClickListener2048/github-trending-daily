#!/usr/bin/env python3
"""把 Trending 数据渲染成 Markdown 日报和 HTML 报告；可选调用 LLM 生成中文简介。

AI 返回结构（JSON 数组，与输入顺序一致）：
[{"intro": "一句话中文简介", "highlights": ["能干什么 1", "能干什么 2"]}, ...]

支持两种 provider（config.json 的 ai.provider 切换）：
- deepseek（默认）及任何 OpenAI 兼容接口：直接 HTTP 调用，base_url 可配
- anthropic：官方 SDK，需 ANTHROPIC_API_KEY
"""
from __future__ import annotations

import html
import json
import os

import anthropic
import requests

AI_SYSTEM_PROMPT = (
    "你是 GitHub 开源项目编辑。用户会给你一份仓库列表（JSON，含 name 和 desc 字段）。"
    "为每个仓库输出：1) intro：一句话中文介绍（20~40 字），说明它是什么、解决什么问题；"
    "2) highlights：2~3 条中文要点（每条 10~20 字），说明它能做什么、适合谁用。"
    "desc 为空时根据仓库名合理判断；无法判断时 intro 写「暂无介绍」、highlights 为空数组。"
    '只输出一个 JSON 对象数组：[{"intro": str, "highlights": [str]}]，'
    "顺序与输入完全一致，不要输出任何其他文字。"
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


def _anthropic_chat(payload: list[dict], api_key: str, model: str) -> str:
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=model,
        max_tokens=8000,
        system=AI_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": json.dumps(payload, ensure_ascii=False)}],
    )
    return "".join(block.text for block in response.content if block.type == "text")


def _openai_compatible_chat(
    payload: list[dict], api_key: str, model: str, base_url: str
) -> str:
    """DeepSeek 等 OpenAI 兼容接口。"""
    resp = requests.post(
        f"{base_url.rstrip('/')}/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": model,
            "temperature": 0.3,
            "max_tokens": 8000,
            "messages": [
                {"role": "system", "content": AI_SYSTEM_PROMPT},
                {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
            ],
        },
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def generate_details(repos: list[dict], cfg: dict) -> list[dict]:
    """用 LLM 为每个仓库生成中文简介和要点；失败时抛异常由调用方回退。"""
    payload = [
        {"name": repo["full_name"], "desc": repo["description"][:200]}
        for repo in repos
    ]
    api_key = os.environ.get(cfg.get("api_key_env", "DEEPSEEK_API_KEY"))
    if not api_key:
        raise ValueError(f"未配置环境变量 {cfg.get('api_key_env', 'DEEPSEEK_API_KEY')}")
    model = cfg.get("model", "deepseek-flash")

    if cfg.get("provider", "deepseek") == "anthropic":
        text = _anthropic_chat(payload, api_key, model)
    else:
        text = _openai_compatible_chat(
            payload, api_key, model, cfg.get("base_url", "https://api.deepseek.com/v1")
        )

    start, end = text.find("["), text.rfind("]")
    if start == -1 or end <= start:
        raise ValueError(f"AI 返回中找不到 JSON 数组: {text[:200]}")
    raw = json.loads(text[start : end + 1])
    if not isinstance(raw, list) or len(raw) != len(repos):
        raise ValueError("AI 返回的 JSON 数组与仓库数量不匹配")

    details = []
    for item, repo in zip(raw, repos):
        if not isinstance(item, dict):
            raise ValueError("AI 返回的元素不是对象")
        intro = str(item.get("intro") or "").strip() or repo["description"] or "（暂无介绍）"
        highlights = item.get("highlights")
        if not isinstance(highlights, list):
            highlights = []
        highlights = [str(h).strip() for h in highlights if str(h).strip()][:3]
        details.append({"intro": intro, "highlights": highlights})
    return details


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
    lines += ["", "## 🏆 今日之星 TOP 5", ""]

    for i, r in enumerate(top5, 1):
        lines.append(
            f"### {i}. [{r['full_name']}]({r['url']}) — ⭐ {r['stars']:,}（今日 +{r['stars_today']:,}）"
        )
        lines.append("")
        lines.append(f"> {r['intro']}")
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
        "| # | 仓库 | 一句话简介 | 语言 | ⭐ | 今日 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for i, r in enumerate(repos, 1):
        intro = r["intro"].replace("|", "\\|")
        if len(intro) > 45:
            intro = intro[:45] + "…"
        lang = f"`{r['language']}`" if r["language"] else "—"
        lines.append(
            f"| {i} | [{r['full_name']}]({r['url']}) | {intro} | {lang} | {r['stars']:,} | +{r['stars_today']:,} |"
        )
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


_CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
:root {
  --bg: #f6f8fa; --card: #ffffff; --text: #1f2328; --muted: #59636e;
  --border: #d1d9e0; --accent: #0969da; --accent-soft: #ddf4ff;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0d1117; --card: #161b22; --text: #e6edf3; --muted: #8b949e;
    --border: #30363d; --accent: #4493f8; --accent-soft: #0c2d6b;
  }
}
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC",
    "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  background: var(--bg); color: var(--text); line-height: 1.6;
}
.hero { text-align: center; padding: 56px 20px 40px; }
.hero h1 { font-size: 2rem; margin-bottom: 10px; }
.hero .date { color: var(--muted); font-size: 1rem; }
.hero .sub { color: var(--muted); margin-top: 14px; font-size: .95rem; }
.hero a, footer a { color: var(--accent); text-decoration: none; }
.btn {
  display: inline-block; margin-top: 18px; padding: 10px 22px;
  background: var(--accent); color: #fff !important; border-radius: 999px;
  font-weight: 600; font-size: .95rem; text-decoration: none;
}
main { max-width: 1080px; margin: 0 auto; padding: 0 20px 60px; }
section h2 { font-size: 1.35rem; margin: 28px 0 16px; }
.grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 16px;
}
.grid.top5 { grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); }
.card {
  display: flex; flex-direction: column; gap: 10px;
  background: var(--card); border: 1px solid var(--border); border-radius: 12px;
  padding: 18px; text-decoration: none; color: var(--text);
  transition: transform .12s ease, box-shadow .12s ease;
}
.card:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,.12); }
.card-head { display: flex; align-items: center; gap: 8px; }
.card-head .name { font-weight: 700; font-size: 1.02rem; color: var(--accent); }
.rank {
  background: var(--accent); color: #fff; border-radius: 8px;
  padding: 1px 10px; font-size: .9rem; font-weight: 700;
}
.intro { color: var(--text); font-size: .92rem; }
.highlights { list-style: none; display: flex; flex-direction: column; gap: 4px; }
.highlights li { font-size: .88rem; color: var(--muted); padding-left: 18px; position: relative; }
.highlights li::before { content: "▸"; position: absolute; left: 2px; color: var(--accent); }
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chip {
  background: var(--accent-soft); color: var(--accent);
  border-radius: 999px; padding: 2px 10px; font-size: 12px;
}
.chip .dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 5px; }
.stats {
  display: flex; flex-wrap: wrap; gap: 12px; align-items: center;
  margin-top: auto; padding-top: 10px; border-top: 1px solid var(--border);
  font-size: .85rem; color: var(--muted);
}
.stats .hot { color: #d1242f; font-weight: 600; }
.stats .home { color: var(--accent); text-decoration: none; }
footer { text-align: center; padding: 30px 20px 50px; color: var(--muted); font-size: .85rem; }
"""


def _card_html(r: dict, i: int, featured: bool) -> str:
    name = html.escape(r["full_name"])
    intro = html.escape(r["intro"])
    highlights = "".join(
        f"<li>{html.escape(h)}</li>" for h in r.get("highlights", [])
    )
    topics = "".join(
        f'<span class="chip">{html.escape(t)}</span>' for t in r.get("topics", [])
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
        f'<a class="home" href="{html.escape(r["homepage"])}" target="_blank" rel="noopener">🔗 官网</a>'
        if r.get("homepage")
        else ""
    )
    rank = f'<span class="rank">{i}</span>' if featured else ""
    cls = "card featured" if featured else "card"
    return (
        f'<a class="{cls}" href="{html.escape(r["url"])}" target="_blank" rel="noopener">'
        f'<div class="card-head">{rank}<span class="name">{name}</span></div>'
        f'<p class="intro">{intro}</p>'
        + (f'<ul class="highlights">{highlights}</ul>' if highlights else "")
        + (f'<div class="chips">{topics}</div>' if topics else "")
        + (
            f'<div class="stats"><span>⭐ {r["stars"]:,}</span>'
            f'<span class="hot">🔥 今日 +{r["stars_today"]:,}</span>'
            f'<span>🍴 {r["forks"]:,}</span>{lang_chip}{homepage}</div>'
        )
        + "</a>"
    )


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
    <h2>🏆 今日之星 TOP 5</h2>
    <div class="grid top5">
{top5_html}
    </div>
  </section>
  <section>
    <h2>📋 完整榜单</h2>
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
