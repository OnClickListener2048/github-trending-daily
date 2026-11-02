# 🔥 GitHub Trending Daily · 每日热榜推送

[![daily-trending](https://github.com/OnClickListener2048/github-trending-daily/actions/workflows/daily-trending.yml/badge.svg)](https://github.com/OnClickListener2048/github-trending-daily/actions/workflows/daily-trending.yml)
![GitHub stars](https://img.shields.io/github/stars/OnClickListener2048/github-trending-daily)

每天自动抓取 [github.com/trending](https://github.com/trending) 的热门仓库，**给每一位 Star 过本仓库的人发一封邮件**，正文就是当天榜单 + 每个仓库的一句话简介。

## ✨ 怎么接收

1. **Star 本仓库** ⭐
2. 保持 GitHub 邮件通知开启（默认就是开的，不用动）
3. 完成。每天早上 08:30（北京时间）你会收到一封来自 GitHub 的邮件：🏆 TOP 5 详细解析（每个仓库"是什么 + 能干什么"）+ 📋 完整榜单，并附精美 HTML 报告链接

> 原理：每天自动创建一个 Issue 并 @ 你的用户名，GitHub 会把提及通知默认发送到你的邮箱。不需要填邮箱、不需要注册，**Star 即订阅**。全程使用 GitHub 官方机制，不收集任何个人信息。

## 🧭 今日榜单

<!-- TRENDING:START -->

# 🔥 GitHub 每日 Trending · 2026-11-02

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 15 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 今日之星 TOP 5（详细介绍）

### 1. [pingdotgg/t3code](https://github.com/pingdotgg/t3code) — ⭐ 40,561（今日 +3,216）

> 统一管控本机多种 AI 编程代理的跨平台控制台，覆盖手机、网页与桌面。

T3 Code 是一个“agent harness 控制面”：它本身不提供模型，而是接管你电脑上已经装好并登录的 Claude Code、Codex、Cursor、Grok Build、OpenCode、Antigravity 和 fx，把它们的会话统一到一个界面里操作。官方说得很直白——不卖任何东西，只是嫌现有 Codex 桌面端、Conductor、Claude Desktop、Cursor Glass 都不够快、不够远程、不够开放，于是自己造了一个，并且保证你随时能 fork 出走。用法很简单：先在本机装好并登录至少一个 provider，然后执行 curl 安装脚本或 npx t3@latest 启动服务并打开本地 Web 应用，也可以从 GitHub Releases、Homebrew、winget、scoop、AUR、nixpkgs 安装桌面版；t3 service install 可让它常驻后台，t3 update 负责升级。

- ✨ 一处接管多家代理：Claude Code、Codex、Cursor、Grok Build、OpenCode、Antigravity、fx 只要本机装好并登录，就能被统一控制
- ✨ 多端同源：iOS、Android 原生应用、app.t3.codes 网页端和基于 Electron 的桌面端共享同一套服务
- ✨ 远程访问：可从手机或另一台机器连回自己电脑上的 agent 会话，不必守在桌前
- ✨ 命令行一体化：curl/irm 一行装好，t3 启动服务，t3 service install 常驻后台，t3 update 升级，npx t3@latest 免安装试用
- ✨ 通过 MCP 与外部 agent 互通：Claude Code、Codex、ChatGPT 等可以反过来连接 T3 Code
- ✨ 开发体验细节：权限模式、键盘快捷键、项目设置、外观偏好，以及源码管理集成和多账号（Codex、Claude）支持
- 👥 适合谁：已在本机使用多个 AI 编程 agent、希望统一管理并能远程操控的开发者。

`TypeScript` · Fork 9,032 · 🔗 [官网](https://t3.codes)

### 2. [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — ⭐ 8,489（今日 +2,243）

> Agent Desktop gives any agent reliable computer us

Agent Desktop gives any agent reliable computer use on the desktop. Built with Rust, it sees any app's real UI structure through OS accessibility trees and operates it — refs stay stable and actions stay safe to retry, instead of guessing from pixels.


`Rust` · Fork 593 · 🔗 [官网](https://agent-browser.dev/desktop)

### 3. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) — ⭐ 110,380（今日 +1,799）

> 为 AI 编程 Agent 提供跨会话持久记忆，自动记录、压缩并回注上下文。

claude-mem 是一个面向 Claude Code 等 AI 编程 Agent 的持久记忆压缩系统。它解决的是 Agent 每次会话结束后就忘记此前工作的麻烦：会话期间，它自动捕获 Agent 的工具使用观察记录，用 AI 将其压缩成语义摘要并保存下来，然后在之后的会话中把相关上下文注入回去。这样即使中途断开重连或开启新会话，Agent 依然记得这个项目做过什么、怎么做的。安装很轻量，一条 npx claude-mem install --ide <你的 IDE/Agent> 命令即可接入，支持 Claude Code、Codex、Gemini、Copilot、OpenCode 等多种宿主，提供 MCP 搜索工具来检索历史记忆，还带有配置项与故障排查文档，并附有多语言 README。

- ✨ 自动捕获：会话过程中持续记录 Agent 的工具使用观察，不需要手动保存
- ✨ AI 压缩：把冗长的会话记录压缩成语义摘要，避免把原始日志全部写入上下文窗口
- ✨ 上下文回注：在后续会话中自动注入相关记忆，让 Agent 保持项目知识的连续性
- ✨ MCP 搜索工具：通过 MCP 接口在历史记忆中检索，按需取用过去的上下文
- ✨ 多 Agent 兼容：除 Claude Code 外，还支持 Codex、Gemini、Copilot、OpenCode、Hermes、OpenClaw 等宿主
- ✨ 一条 npx 命令安装，并支持配置与故障排查文档
- 👥 适合谁：长期用 Claude Code 等 AI 编程 Agent 做项目的开发者。

`TypeScript` · Fork 9,631 · 🔗 [官网](https://claude-mem.ai)

### 4. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) — ⭐ 33,161（今日 +1,380）

> 把单次 Claude Code 会话变成有层级、有质量门的游戏开发工作室。

Claude Code Game Studios 是一套面向 Claude Code 的配置模板：装上它，你的 AI 会话就从单个通用助手变成 49 个分工明确的角色——创意总监守愿景、部门主管管领域、专员干具体活，配 74 个斜杠命令和 15 个自动钩子。它解决的是单人用 AI 做游戏时缺少结构的问题：没人拦你写魔法数字、跳过设计文档、堆出难维护的代码，也没有 QA 和设计评审。现在每个角色都有职责、升级路径和质量门，决策仍由你做，但团队会替你追问、早发现问题，把项目从脑暴一路管到上线。

- ✨ 49 个专业 agent 按三级工作室层级组织，覆盖设计、程序、美术、音频、叙事、QA 与制作
- ✨ 74 个斜杠命令贯通全流程：从 /start、/brainstorm、/design-system 到 /create-epics、/create-stories、/dev-story、/story-done
- ✨ 15 个 hooks 在提交、推送、资源变更、设计文档读写与会话生命周期上做自动校验和缺口检测
- ✨ 14 条按路径生效的编码规范，编辑玩法、引擎、AI、UI、网络代码及场景资源时自动约束
- ✨ 内置 Godot 4、Unity、Unreal Engine 5 三套引擎专家 agent，含 GDScript、DOTS/ECS、GAS、蓝图等子专员
- ✨ 62 份文档模板覆盖 GDD、UX 规格、ADR、冲刺计划、HUD 设计、无障碍等产出物
- 👥 适合谁：适合用 Claude Code 独立或小团队做游戏、想要设计评审与工程规范的开发者。

`Shell` · Fork 4,486

### 5. [mattpocock/skills](https://github.com/mattpocock/skills) — ⭐ 309,895（今日 +970）

> 一套小巧、可组合、跨模型的 AI 编程 Agent 技能集，用来做真正的工程，而非 vibe coding。

这是 Matt Pocock 从自己日常使用的 .agents 目录里整理出来的一组 Agent 技能，覆盖 Claude Code、Codex、GitHub Copilot、Gemini CLI 等主流编码 Agent。它要解决的问题很具体：GSD、BMAD、Spec-Kit 这类方案试图替你接管整个开发流程，代价是你失去了控制权，而且流程本身出 bug 时很难排查。这些技能反其道而行：每个都很小、容易改、可以自由组合，不绑定模型，你可以直接改造成自己的版本。安装走插件市场命令或 npx skills 拷入项目，第一次在每个仓库里跑一次 /setup-matt-pocock-skills 完成配置即可。

- ✨ /grill-me 和 /grill-with-docs：动手前先让 Agent 反过来“拷问”你，把需求问透，解决最常见的“Agent 做的不是我想要的”对齐失败
- ✨ 共享语言/术语表机制：给 Agent 一份项目行话对照文档，让它不再用 20 个词说 1 个词的事，输出明显更简短
- ✨ 多 Agent 覆盖安装：Claude Code、Codex、GitHub Copilot（CLI 与 VS Code）、Gemini CLI，以及通过 npx skills 支持 cursor、opencode、devin、windsurf、amp、pi 等
- ✨ 两种更新模式可选：插件方式自动更新，skills.sh 方式把可编辑文件拷进项目由你手动维护、随手魔改
- ✨ /setup-matt-pocock-skills 一次性初始化：选定 issue tracker（GitHub、GitLab、本地文件或自定义）、triage 用的标签、文档保存位置
- ✨ 技能按 engineering 与 productivity 分类，配合 /triage 使用你设定的标签做工单分诊
- 👥 适合谁：日常用 Claude Code、Codex 等 Agent 写真实项目的工程师，尤其是受够重型流程框架、想保留控制权的人。

`Shell` · Fork 26,072 · 🔗 [官网](https://aihero.dev/skills)

## 📋 完整榜单

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Agent Desktop gives any agent reliable comput… | `Rust` | 8,489 | +2,243 |
| 2 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 为 AI 编程 Agent 提供跨会话持久记忆，自动记录、压缩并回注上下文。 | `TypeScript` | 110,380 | +1,799 |
| 3 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | Scrapling 是一个 Python 网页抓取框架，把快速请求、隐身浏览器、解析和并发… | `Python` | 92,401 | +858 |
| 4 | [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) | 独立的动态平铺 Wayland 合成器，在极致美化与高度可定制之间都不妥协 | `C++` | 39,729 | +508 |
| 5 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 把单次 Claude Code 会话变成有层级、有质量门的游戏开发工作室。 | `Shell` | 33,161 | +1,380 |
| 6 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | FreeToken brings datacenter-scale model servi… | `Python` | 15,850 | +654 |
| 7 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 统一管控本机多种 AI 编程代理的跨平台控制台，覆盖手机、网页与桌面。 | `TypeScript` | 40,561 | +3,216 |
| 8 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | 首个开源金融K线基础模型，基于45+全球交易所数据预训练 | `Python` | 45,822 | +855 |
| 9 | [kornia/kornia](https://github.com/kornia/kornia) | 🐍 Geometric Computer Vision Library for Spati… | `Python` | 12,034 | +412 |
| 10 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 纯 C 编写的 MoE 推理引擎，专家按需从磁盘流式读取，让普通电脑也能跑数百亿参数大模型… | `C` | 46,280 | +655 |
| 11 | [mattpocock/skills](https://github.com/mattpocock/skills) | 一套小巧、可组合、跨模型的 AI 编程 Agent 技能集，用来做真正的工程，而非 vib… | `Shell` | 309,895 | +970 |
| 12 | [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | 用 Rust 写的 Git worktree 管理命令行工具，专为并行运行 AI 编程代理… | `Rust` | 9,886 | +115 |
| 13 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 开源 AI 智能体团队编排应用：给 agent 定目标、分角色、控预算，像经营公司一样管它… | `TypeScript` | 110,189 | +507 |
| 14 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | 花约 48 美元、两小时在单节点 GPU 上训出 GPT-2 级别模型的最小实验框架 | `Python` | 59,701 | +325 |
| 15 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | 免训练即可改造 LLM：去除审查、压制废话、降低谄媚，一台游戏 PC 一个下午搞定 | `Python` | 37,864 | +404 |

<!-- TRENDING:END -->

## 🎨 HTML 报告

每天同步生成一个卡片式样式的精美报告页（深色模式自适应），托管在 GitHub Pages：

👉 **[打开 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)**

## 📚 历史日报

- 每天的报告存档在 [`data/daily/`](data/daily/)
- 每天的 Issue 都带有 `daily-trending` 标签：[查看全部](https://github.com/OnClickListener2048/github-trending-daily/issues?q=label%3Adaily-trending)

## 🛠 自定义（Fork 后改 `config.json`）

| 配置 | 说明 |
| --- | --- |
| `languages` | 只看某些语言，如 `["python", "go", "rust"]`；`[]` 表示全部语言 |
| `since` | `daily` / `weekly` / `monthly` |
| `limit` | 榜单数量（默认 25） |
| `pages_url` | HTML 报告地址（GitHub Pages，邮件和日报里带这个链接） |
| `repo_url` | 仓库地址（HTML 报告页的订阅按钮用） |
| `mentions.enabled` | 是否 @ 提及 stargazer（关闭后改为纯 Issue 模式，需用户 Watch 才能收到通知） |
| `mentions.chunk_size` | 每条评论 @ 的人数（默认 10，分批 @ 降低被判定骚扰的风险） |
| `ai.enabled` | 是否用 AI 逐个仓库生成详细介绍（需在仓库 Secrets 配置对应 Key） |
| `ai.provider` | AI 提供商：`deepseek`（默认）或 `anthropic` |
| `ai.model` | 模型名（DeepSeek 默认 `deepseek-flash`；Anthropic 如 `claude-opus-5-5`） |
| `ai.base_url` | OpenAI 兼容接口地址（仅 deepseek 类 provider 使用，默认 DeepSeek 官方接口） |
| `ai.api_key_env` | 密钥所在环境变量（默认 `DEEPSEEK_API_KEY`；用 Claude 时改成 `ANTHROPIC_API_KEY`） |
| `ai.readme_chars` | 每个仓库喂给 AI 的 README 截断长度（默认 6000 字符） |
| `ai.workers` | 并发分析线程数（默认 5） |

## ❓ 常见问题

**为什么 Star 后就能收到邮件？**
GitHub 不提供 stargazer 的邮箱，本项目每天读取 star 名单并在 Issue 评论里 @ 他们；GitHub 的提及通知默认发送到邮箱。无需也不收集用户的邮箱地址。

**不想再收怎么办？**
任选其一：取消 Star；把自己的用户名加进 [`data/opt_out.json`](data/opt_out.json) 提个 PR；在 GitHub 通知设置里关闭提及通知。

**人多了会被限流吗？**
@ 提及走的是 GitHub 官方通知机制。本项目已做分批 @（每条评论 10 人）和限速保护。如果 star 数量很大（数千人）被 GitHub 处置，可关闭 `mentions` 改纯 Issue 模式。

**为什么邮件里没有自定义样式？**
GitHub 通知邮件由 GitHub 统一渲染，无法注入自定义 CSS。所以邮件内容用 GitHub 支持的排版元素（标题、表格、列表）呈现，需要精美样式时点邮件里的链接打开 HTML 报告页即可。

**数据来源可靠吗？**
数据来自 [github.com/trending](https://github.com/trending) 官方页面（GitHub 没有 trending API，本项目解析其页面）。偶发反爬失败时当天会跳过，第二天自动重试。

**AI 介绍是怎么做的？**
每个仓库单独调用一次 AI（不是批量），输入是该仓库的 README 原文（截断 6000 字符）+ 仓库数据，输出"一句话定位 + 详细介绍（100~200 字）+ 核心功能列表 + 适合谁"。默认走 DeepSeek：在仓库 Settings → Secrets and variables → Actions 添加 `DEEPSEEK_API_KEY`（或命令行 `gh secret set DEEPSEEK_API_KEY`），第二天自动生效。想用 Claude：把 `config.json` 的 `ai.provider` 改成 `anthropic`、`ai.api_key_env` 改成 `ANTHROPIC_API_KEY`，并设置对应 Secret。没有 Key 时回退显示仓库原始英文描述。

## ⚠️ 免责声明

本项目与 GitHub 无关，仅用于学习和技术交流。请勿滥用 @ 提及功能。
