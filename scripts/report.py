#!/usr/bin/env python3
"""把 Trending 数据渲染成 Markdown 日报；可选调用 LLM 生成中文简介。

支持两种 provider（config.json 的 ai.provider 切换）：
- deepseek（默认）及任何 OpenAI 兼容接口：直接 HTTP 调用，base_url 可配
- anthropic：官方 SDK，需 ANTHROPIC_API_KEY
"""
from __future__ import annotations

import json
import os

import anthropic
import requests

AI_SYSTEM_PROMPT = (
    "你是 GitHub 开源项目编辑。用户会给你一份仓库列表（JSON，含 name 和 desc 字段），"
    "请为每个仓库写一句中文简介（20~40 字），说明它是什么、有何亮点。"
    "desc 为空时根据仓库名合理判断；无法判断就写「暂无介绍」。"
    "只输出一个 JSON 字符串数组，顺序与输入完全一致，不要输出任何其他文字。"
)


def _anthropic_chat(payload: list[dict], api_key: str, model: str) -> str:
    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=model,
        max_tokens=4000,
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
            "max_tokens": 4000,
            "messages": [
                {"role": "system", "content": AI_SYSTEM_PROMPT},
                {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
            ],
        },
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def generate_intros(repos: list[dict], cfg: dict) -> list[str]:
    """用 LLM 为每个仓库生成一句中文简介；失败时抛异常由调用方回退。"""
    payload = [
        {"name": repo["full_name"], "desc": repo["description"][:200]}
        for repo in repos
    ]
    api_key = os.environ.get(cfg.get("api_key_env", "DEEPSEEK_API_KEY"))
    if not api_key:
        raise ValueError(f"未配置环境变量 {cfg.get('api_key_env', 'DEEPSEEK_API_KEY')}")
    model = cfg.get("model", "deepseek-chat")

    if cfg.get("provider", "deepseek") == "anthropic":
        text = _anthropic_chat(payload, api_key, model)
    else:
        text = _openai_compatible_chat(
            payload, api_key, model, cfg.get("base_url", "https://api.deepseek.com/v1")
        )

    start, end = text.find("["), text.rfind("]")
    if start == -1 or end <= start:
        raise ValueError(f"AI 返回中找不到 JSON 数组: {text[:200]}")
    intros = json.loads(text[start : end + 1])
    if not isinstance(intros, list) or len(intros) != len(repos) or not all(
        isinstance(item, str) for item in intros
    ):
        raise ValueError("AI 返回的 JSON 数组与仓库数量不匹配")
    return intros


def render_report(repos: list[dict], date_str: str, intros: list[str] | None) -> str:
    """渲染 Markdown 日报。"""
    lines = [
        f"# 🔥 GitHub 每日 Trending · {date_str}",
        "",
        f"> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 {len(repos)} 个仓库",
        "",
    ]
    for index, repo in enumerate(repos, 1):
        intro = (intros[index - 1] if intros else "") or repo["description"] or "（暂无介绍）"
        lines.append(
            f"### {index}. [{repo['full_name']}]({repo['url']}) — ⭐ {repo['stars']:,}（今日 +{repo['stars_today']:,}）"
        )
        lines.append("")
        lines.append(f"> {intro}")
        meta = []
        if repo["language"]:
            meta.append(f"`{repo['language']}`")
        meta.append(f"Fork {repo['forks']:,}")
        lines.append(" · ".join(meta))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"
