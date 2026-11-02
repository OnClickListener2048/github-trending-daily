# 🔥 GitHub Trending Daily · 每日热榜推送

[![daily-trending](https://github.com/OnClickListener2048/github-trending-daily/actions/workflows/daily-trending.yml/badge.svg)](https://github.com/OnClickListener2048/github-trending-daily/actions/workflows/daily-trending.yml)
![GitHub stars](https://img.shields.io/github/stars/OnClickListener2048/github-trending-daily)

每天自动抓取 [github.com/trending](https://github.com/trending) 的热门仓库，**给每一位 Star 过本仓库的人发一封邮件**，正文就是当天榜单 + 每个仓库的一句话简介。

## ✨ 怎么接收

1. **Star 本仓库** ⭐
2. 保持 GitHub 邮件通知开启（默认就是开的，不用动）
3. 完成。每天早上 08:30（北京时间）你会收到一封来自 GitHub 的邮件，正文就是今日 Trending

> 原理：每天自动创建一个 Issue 并 @ 你的用户名，GitHub 会把提及通知默认发送到你的邮箱。不需要填邮箱、不需要注册，**Star 即订阅**。全程使用 GitHub 官方机制，不收集任何个人信息。

## 🧭 今日榜单

<!-- TRENDING:START -->

# 🔥 GitHub 每日 Trending · 2026-11-02

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 15 个仓库

### 1. [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — ⭐ 8,424（今日 +2,243）

> 基于 Rust 的桌面代理工具，通过操作系统无障碍树读取任意应用的真实 UI 结构并稳定操作。
`Rust` · Fork 590

### 2. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) — ⭐ 110,366（今日 +1,799）

> 为 AI 代理提供跨会话持久记忆，自动压缩会话内容并在未来对话中注入相关上下文。
`TypeScript` · Fork 9,631

### 3. [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) — ⭐ 92,375（今日 +892）

> Python 网页抓取框架，从单次请求到大规模爬取全覆盖，内置反爬与自适应解析能力。
`Python` · Fork 9,748

### 4. [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) — ⭐ 39,719（今日 +508）

> 独立且高度可定制的动态平铺 Wayland 合成器，外观与性能兼得。
`C++` · Fork 2,143

### 5. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) — ⭐ 33,134（今日 +1,380）

> 把 Claude Code 变成完整游戏开发工作室，含 49 个 AI 代理与 72 项工作流技能。
`Shell` · Fork 4,486

### 6. [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) — ⭐ 15,845（今日 +654）

> 在桌面本地高效运行大规模模型，把数据中心级推理服务带到个人电脑。
`Python` · Fork 1,575

### 7. [pingdotgg/t3code](https://github.com/pingdotgg/t3code) — ⭐ 40,462（今日 +3,216）

> 暂无介绍
`TypeScript` · Fork 9,026

### 8. [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) — ⭐ 45,810（今日 +855）

> 面向金融市场的语言基础模型，用大模型理解与预测金融时序数据。
`Python` · Fork 7,554

### 9. [kornia/kornia](https://github.com/kornia/kornia) — ⭐ 12,032（今日 +412）

> 基于 PyTorch 的几何计算机视觉库，为空间 AI 提供可微图像处理与视觉算法。
`Python` · Fork 1,484

### 10. [JustVugg/colibri](https://github.com/JustVugg/colibri) — ⭐ 46,269（今日 +655）

> 纯 C 零依赖的推理引擎，将 MoE 专家流式加载，在自有硬件上运行前沿大模型。
`C` · Fork 5,345

### 11. [mattpocock/skills](https://github.com/mattpocock/skills) — ⭐ 309,879（今日 +970）

> 来自作者 .agents 目录的实用技能集，为真实工程师提供 AI 代理可用的技能。
`Shell` · Fork 26,072

### 12. [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) — ⭐ 9,882（今日 +115）

> 管理 Git worktree 的命令行工具，专为并行 AI 代理工作流设计。
`Rust` · Fork 353

### 13. [paperclipai/paperclip](https://github.com/paperclipai/paperclip) — ⭐ 110,181（今日 +507）

> 开源应用，用于在工作场景中统一管理和调度 AI 代理。
`TypeScript` · Fork 18,255

### 14. [karpathy/nanochat](https://github.com/karpathy/nanochat) — ⭐ 59,697（今日 +325）

> Karpathy 的极简 ChatGPT 项目，用约 100 美元成本训练出完整对话模型。
`Python` · Fork 8,394

### 15. [p-e-w/heretic](https://github.com/p-e-w/heretic) — ⭐ 37,855（今日 +404）

> 无需训练即可修改语言模型，可去除审查、抑制废话并降低谄媚等行为。
`Python` · Fork 4,310

<!-- TRENDING:END -->

## 📚 历史日报

- 每天的报告存档在 [`data/daily/`](data/daily/)
- 每天的 Issue 都带有 `daily-trending` 标签：[查看全部](https://github.com/OnClickListener2048/github-trending-daily/issues?q=label%3Adaily-trending)

## 🛠 自定义（Fork 后改 `config.json`）

| 配置 | 说明 |
| --- | --- |
| `languages` | 只看某些语言，如 `["python", "go", "rust"]`；`[]` 表示全部语言 |
| `since` | `daily` / `weekly` / `monthly` |
| `limit` | 榜单数量（默认 25） |
| `mentions.enabled` | 是否 @ 提及 stargazer（关闭后改为纯 Issue 模式，需用户 Watch 才能收到通知） |
| `mentions.chunk_size` | 每条评论 @ 的人数（默认 10，分批 @ 降低被判定骚扰的风险） |
| `ai.enabled` | 是否用 AI 生成一句话中文简介（需在仓库 Secrets 配置对应 Key） |
| `ai.provider` | AI 简介提供商：`deepseek`（默认）或 `anthropic` |
| `ai.model` | 模型名（DeepSeek 默认 `deepseek-chat`；Anthropic 如 `claude-opus-5-5`） |
| `ai.base_url` | OpenAI 兼容接口地址（仅 deepseek 类 provider 使用，默认 DeepSeek 官方接口） |
| `ai.api_key_env` | 密钥所在环境变量（默认 `DEEPSEEK_API_KEY`；用 Claude 时改成 `ANTHROPIC_API_KEY`） |

## ❓ 常见问题

**为什么 Star 后就能收到邮件？**
GitHub 不提供 stargazer 的邮箱，本项目每天读取 star 名单并在 Issue 评论里 @ 他们；GitHub 的提及通知默认发送到邮箱。无需也不收集用户的邮箱地址。

**不想再收怎么办？**
任选其一：取消 Star；把自己的用户名加进 [`data/opt_out.json`](data/opt_out.json) 提个 PR；在 GitHub 通知设置里关闭提及通知。

**人多了会被限流吗？**
@ 提及走的是 GitHub 官方通知机制。本项目已做分批 @（每条评论 10 人）和限速保护。如果 star 数量很大（数千人）被 GitHub 处置，可关闭 `mentions` 改纯 Issue 模式。

**数据来源可靠吗？**
数据来自 [github.com/trending](https://github.com/trending) 官方页面（GitHub 没有 trending API，本项目解析其页面）。偶发反爬失败时当天会跳过，第二天自动重试。

**AI 简介怎么开？**
默认走 DeepSeek：在仓库 Settings → Secrets and variables → Actions 添加 `DEEPSEEK_API_KEY`（或命令行 `gh secret set DEEPSEEK_API_KEY`），第二天自动生效。想用 Claude：把 `config.json` 的 `ai.provider` 改成 `anthropic`、`ai.api_key_env` 改成 `ANTHROPIC_API_KEY`，并设置对应 Secret。没有 Key 时回退显示仓库原始英文描述。

## ⚠️ 免责声明

本项目与 GitHub 无关，仅用于学习和技术交流。请勿滥用 @ 提及功能。
