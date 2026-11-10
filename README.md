# 🔥 GitHub Trending Daily · 每日热榜推送

[![daily-trending](https://github.com/OnClickListener2048/github-trending-daily/actions/workflows/daily-trending.yml/badge.svg)](https://github.com/OnClickListener2048/github-trending-daily/actions/workflows/daily-trending.yml)
![GitHub stars](https://img.shields.io/github/stars/OnClickListener2048/github-trending-daily)

每天自动抓取 [github.com/trending](https://github.com/trending) 的热门仓库，**给每一位 Star 过本仓库的人发一封邮件**，正文就是当天榜单 + 每个仓库的一句话简介。

## ✨ 怎么接收

1. **Star 本仓库** ⭐
2. 保持 GitHub 邮件通知开启（默认就是开的，不用动）
3. 完成。每天早上 08:30（北京时间）你会收到一封来自 GitHub 的邮件：🏆 今日精选详解（每个仓库"是什么 + 能干什么"，连续在榜较久的自动跳过）+ 📋 完整榜单，并附精美 HTML 报告链接

> 原理：每天自动创建一个 Issue 并 @ 你的用户名，GitHub 会把提及通知默认发送到你的邮箱。不需要填邮箱、不需要注册，**Star 即订阅**。全程使用 GitHub 官方机制，不收集任何个人信息。

## 🧭 今日榜单

<!-- TRENDING:START -->

# 🔥 GitHub 每日 Trending · 2026-11-10

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 12 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 今日精选（详细介绍）

### 3. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — ⭐ 114,770（今日 +465）

> 为 AI 编程代理打包的 25 个生产级工程技能，把资深工程师的工作流和质量关卡固化下来。

这是一套面向 AI 编程代理的「技能包」：把资深工程师在造软件时用的工作流、质量门禁和最佳实践写成结构化技能，让代理在开发的每个阶段都按同一套规矩办事。它解决的是 AI 写代码时流程随意、跳过测试、缺少评审的问题——用 9 个斜杠命令把开发切成定义、规划、构建、验证、评审、上线六段，每个命令自动挂载对应技能。通过 npx skills add 可一键装进 Claude Code、Cursor、Codex、Copilot、Cline 等 70 多个代理，也支持插件市场和本地目录方式集成。

- ✨ 9 个生命周期斜杠命令：/spec、/plan、/build、/test、/constraints、/review、/webperf、/code-simplify、/ship，每个自动激活对应技能
- ✨ 共 25 个技能，也可按需单独安装，例如 code-review-and-quality 做五维评审、interview-me 一次一问地追问需求、test-driven-development 强制红绿重构
- ✨ /build auto 模式：批准一次计划后自动实现所有任务，仍然每任务测试驱动、逐个提交，遇失败或高风险步骤会暂停
- ✨ 技能按上下文自动触发：设计 API 时启用 api-and-interface-design，写 UI 时启用 frontend-ui-engineering
- ✨ 一条命令跨代理安装（npx skills add，支持 70+ 代理），并提供 Claude Code 插件市场、Cursor 的 .cursor/skills 与 rules 分离方案、Antigravity CLI 原生插件等集成方式
- ✨ 把项目级的硬性约束集中到 /constraints：一次决定、处处强制执行，避免规则散落
- 👥 适合谁：使用 Claude Code、Cursor、Codex 等 AI 编程代理，希望让代理稳定产出生产级代码的开发者与团队。

`JavaScript` · Fork 11,994 · 🔗 [官网](https://skills.addy.ie)

### 4. [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) — ⭐ 20,244（今日 +530）

> Anthropic 官方开源的 Claude API 应用快速上手合集，覆盖客服、金融、浏览器与电脑操作等场景。

这是一组能直接跑起来的示例工程，每个对应一类真实产品形态：客服代理、金融数据分析、电脑操作、浏览器自动化、自主编码、托管代理。它解决的问题很实际——你不需要从零摸索 Claude API 的调用方式、工具定义和前端交互长什么样，挑一个最接近自己需求的项目，填上 API key 就能跑通，再在这个基础上改造成自己的应用。所有示例都以可部署、可定制为出发点，而非只做接口演示。

- ✨ Customer Support Agent：带知识库的 AI 客服示例，展示如何用 Claude 的自然语言理解与生成能力搭建辅助客服系统
- ✨ Financial Data Analyst：通过聊天分析财务数据，并能生成交互式数据可视化
- ✨ Computer Use：既能提供让 Claude 控制桌面电脑的环境与工具（含最新的 computer_toolset 工具集形态），也有原生 macOS 的最佳实践参考实现，示范显式工具定义、图像尺寸与裁剪、提示缓存、服务端压缩、批量工具调用、沙箱 shell 与轨迹记录等可靠性和成本优化模式
- ✨ Browser Use Demo 与 Browser Toolset：前者基于 Playwright 自定义浏览器工具，让 Claude 导航网站、检查并操作 DOM、提取内容、填写表单；后者是最小 CDP 示例，用一个小驱动控制单个 Chromium 标签页
- ✨ Autonomous Coding Agent：基于 Claude Agent SDK 的双代理模式（初始化代理 + 编码代理），跨多个会话逐步构建完整应用，进度通过 git 和功能清单持久化
- ✨ Managed Agents 系列：浏览器聊天应用（同一套 handler 换上 Chat SDK 适配器即可跑在 Slack、Teams、Discord、Telegram、WhatsApp）、用 CopilotKit + AG-UI 把工具调用渲染成交互式生成式 UI、每工作日汇总 Slack 与 GitHub PR 的定时简报代理、把文档语料蒸馏成带出处版本化知识库的尽调维基
- 👥 适合谁：想用 Claude API 做产品的开发者，尤其是要落地客服、数据分析、Agent 自动化类应用的团队和个人。

`Python` · Fork 3,383

### 5. [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) — ⭐ 17,153（今日 +453）

> Google DeepMind 维护的通用物理引擎，能快速、准确地仿真带接触的多关节刚体系统。

MuJoCo 名称是 Multi-Joint dynamics with Contact 的缩写，由 Google DeepMind 维护，是一个开源物理仿真器。它用于仿真由关节连接的刚体结构在环境中运动时与物体发生的接触和碰撞，主要解决机器人学、生物力学、图形动画和机器学习中对快速、准确仿真的需求。它提供性能高度优化的 C API 运行时，模型由内置 XML 编译器预先分配数据结构，并提供桌面窗口与浏览器中的交互式可视化工具和大量物理量计算函数。此外还有 Python 绑定和 Unity 插件。既可直接下载各平台预编译版本，也可通过 pip install mujoco 安装并快速上手。

- ✨ 高性能 C API 物理仿真运行时，数据结构预分配，专为快速准确仿真优化
- ✨ 内置 XML 模型编译器，用 XML 描述多关节结构的场景
- ✨ 原生桌面窗口与 Web 浏览器中的交互式可视化，附带 simulate 查看器与 MuJoCo Studio
- ✨ 大量物理相关计算工具函数，可直接获取仿真中的各类物理量
- ✨ 官方 Python 绑定，pip install mujoco 即可使用，配有入门、模型编辑、rollout、LQR、最小二乘等 Colab 教程
- ✨ MJX（MuJoCo XLA）JAX 分支，支持在 JAX 中运行并可通过教程训练可微物理策略
- 👥 适合谁：从事机器人、生物力学、图形动画与机器学习研究，需要快速准确刚体仿真的开发者和研究者。

`C++` · Fork 2,068 · 🔗 [官网](https://mujoco.org)

### 6. [we-promise/sure](https://github.com/we-promise/sure) — ⭐ 11,390（今日 +184）

> 社区接手维护的开源自托管个人财务应用，接替已停止运营的 Maybe Finance

Sure 是一个可以完全自托管的个人财务与财富管理应用。它最初由 Maybe Finance 团队投入近百万美元开发，2023 年停摆后开源，如今由社区 fork 继续维护。你能用它集中查看现金流、净资产、支出与资金流出，内置 AI 助手可以直接回答类似于「我的储蓄情况怎么样」的问题。部署方式很简单：用 Docker 自托管，或通过 Render 一键部署（有带 AI 和不带 AI 两个版本）。应用可以通过浏览器、macOS 桌面端、移动端、API 客户端和 LLM agent 访问。本地开发只需 Ruby、PostgreSQL 和 Redis，跑 bin/setup 后执行 rake demo_data:default 就能加载演示数据试玩。

- ✨ 可视化仪表盘：一屏查看现金流、净资产、支出与资金流出
- ✨ 内置 AI 助手：用自然语言提问，直接回答关于你财务状况的问题
- ✨ 多种客户端接入：浏览器、macOS 桌面应用、移动端、API 客户端和 LLM agent
- ✨ 用 Docker 自托管，也可以借助 Render 一键部署，部署版本可选带 AI 或不带 AI
- ✨ 完整的本地开发流程和演示数据集：执行 rake demo_data:default 即可得到可登录的示例账户
- ✨ 公开的 Skylight 性能面板，暴露 demo 站上的慢请求和调用栈，方便社区针对性优化
- 👥 适合谁：希望自己托管财务数据、注重隐私的个人用户，以及愿意参与 Ruby 开源项目贡献的开发者

`Ruby` · Fork 798 · 🔗 [官网](https://sure.am)

### 7. [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) — ⭐ 6,315（今日 +792）

> 让 Claude、ChatGPT 等 AI 助手直接配置和自动化 Home Assistant 的 MCP 服务器

HA-MCP 是一个 Home Assistant 的 MCP 服务器，内置 87 个工具，让 AI 助手能够读取状态、修改配置、编写自动化，省去手写 YAML 的麻烦。最推荐的用法是通过 HACS 或 Home Assistant 2026.11+ 的 Marketplace 把它装成集成，直接在 Home Assistant 进程内运行完整服务器；它兼容 OS、Supervised、Container、Core 全部安装类型，功能完全一致，也取代了插件、Docker、uvx/PyPI 等旧方式（只能选一种）。安装后重启 Home Assistant，在“设置 → 设备与服务”添加 HA-MCP Server，填入管理员长令牌，或为它新建一个仅本地登录的管理员账号，选择远程访问（Secret URL 或 HA 登录）和/或本地网络访问，再从 Configure 界面复制连接 URL 粘进 AI 客户端即可。本地客户端也可直连 9584 端口。

- ✨ 内置 87 个工具，覆盖 Home Assistant 的查询、配置与自动化操作
- ✨ 以集成形式通过 HACS 或 Marketplace 安装，在 Home Assistant 进程内运行，无需另跑 Docker/uvx
- ✨ 兼容 Home Assistant OS、Supervised、Container、Core 全部安装类型，功能完全一致
- ✨ 两种接入方式：经 Home Assistant 的远程 webhook（Secret URL 或 HA 登录），以及本地网络直连
- ✨ 认证灵活：可用自己的长令牌，也可为 HA-MCP 单独建管理员账号并由它自动生成令牌
- ✨ 有端到端测试流水线保障，并把 ha_config_set_yaml 等实验能力放入 beta 通道
- 👥 适合谁：用 Home Assistant 搭建智能家居、希望让 AI 代劳配置与自动化的玩家和自建用户

`Python` · Fork 348 · 🔗 [官网](https://homeassistant-ai.github.io/ha-mcp/)

### 10. [tokio-rs/topcoat](https://github.com/tokio-rs/topcoat) — ⭐ 6,581（今日 +192）

> Tokio 出品的全栈 Rust Web 框架，内置组件、路由与客户端响应式能力，开箱即用。

Topcoat 是 tokio-rs 团队打造的模块化、开箱即用的全栈 Rust Web 框架，主打简单和开发效率。它把 markup 全部放在服务端渲染，组件可以是 async 并直接查数据库，省掉单独写 API 层的样板代码；需要交互时，用 $(...) 表达式写普通 Rust，框架同时把它编译成 JavaScript 在浏览器即时执行，不需要 wasm 包和前端构建步骤。路由、UI 组件、模板语法都内置，项目处于早期实验阶段，API 可能会有破坏性变更。

- ✨ 服务端渲染所有组件，组件可为 async 并直接访问数据库，无需单独 API 层
- ✨ $(...) 表达式同时用于服务端首屏和浏览器执行，实现无 wasm、无前端构建的客户端响应式
- ✨ #[shard] 组件在参数变化时由服务端重渲染并原位替换 HTML，支持实时搜索等场景
- ✨ view! 宏贴近 HTML 与 Rust，模板中可直接使用 for、if 等控制流
- ✨ 基于模块目录结构自动推断路由树，无需构建步骤，支持布局文件与 API 路由
- ✨ topcoat ui CLI 将基于 Tailwind、仿 shadcn/ui 的组件复制进项目，可自由修改
- 👥 适合谁：想用 Rust 一套语言写完整 Web 应用、又不想折腾 wasm 和前后端分层的前后端开发者。

`Rust` · Fork 235

### 12. [mattpocock/skills](https://github.com/mattpocock/skills) — ⭐ 320,284（今日 +1,223）

> 从 Matt Pocock 日常使用的 .agents 目录整理的、小巧可组合的 AI 编码代理技能集

这是 Matt Pocock 每天实际使用的一套 agent skills，目标是用它们做真正的工程开发，而不是让 AI 随意生成代码（俗称 vibe coding）。README 明确指出 GSD、BMAD、Spec-Kit 这类方案虽然想帮忙，但通过接管流程夺走了开发者的控制权，出了问题也难以排查；这些技能则反过来追求小而可改、可自由组合，并且不绑定任何模型。安装上支持 Claude Code、Codex、GitHub Copilot、Gemini CLI，也能通过 npx skills 装到 cursor、opencode、devin、windsurf、amp 等代理里；插件方式会自动更新，也可以复制成可编辑文件手动维护。装完在每个仓库跑一次 /setup-matt-pocock-skills，告诉它你用哪个 issue tracker、triage 打什么标签、文档存哪里，就能开工。

- ✨ grill-me：在动手前让 agent 反过来追问你细节，先对齐需求再写代码
- ✨ grill-with-docs：grill-me 的加强版，额外带上文档与上下文资料一起盘问
- ✨ setup-matt-pocock-skills：每个仓库跑一次，配置 issue tracker、triage 标签和文档存放位置
- ✨ /triage 配合自定义标签做工单分类
- ✨ 共享语言（glossary）文档，让 agent 用项目自己的术语说话，避免啰嗦绕圈
- ✨ 小而可组合的技能设计，不接管流程、任何模型都能用，改起来没有负担
- 👥 适合谁：用 Claude Code、Codex、Copilot 等代理写真实项目、想在保留控制权的前提下提升协作效率的开发者

`Shell` · Fork 26,818 · 🔗 [官网](https://aihero.dev/skills)

## 📋 完整榜单

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [meta/astryx](https://github.com/meta/astryx) | Meta 开源的设计系统，含 150+ 组件，可深度定制，也面向 AI 编程助手 | `TypeScript` | 21,330 | +3,111 |
| 2 | [anthropics/skills](https://github.com/anthropics/skills) | Anthropic 官方的 Agent Skills 示例库，教 Claude 可复用地完… | `Python` | 191,740 | +1,676 |
| 3 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 为 AI 编程代理打包的 25 个生产级工程技能，把资深工程师的工作流和质量关卡固化下来。 | `JavaScript` | 114,770 | +465 |
| 4 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | Anthropic 官方开源的 Claude API 应用快速上手合集，覆盖客服、金融、浏… | `Python` | 20,244 | +530 |
| 5 | [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | Google DeepMind 维护的通用物理引擎，能快速、准确地仿真带接触的多关节刚体系… | `C++` | 17,153 | +453 |
| 6 | [we-promise/sure](https://github.com/we-promise/sure) | 社区接手维护的开源自托管个人财务应用，接替已停止运营的 Maybe Finance | `Ruby` | 11,390 | +184 |
| 7 | [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 让 Claude、ChatGPT 等 AI 助手直接配置和自动化 Home Assista… | `Python` | 6,315 | +792 |
| 8 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 让 AI 智能体通过命令行一步步驱动浏览器的原生 Rust CLI 工具 | `Rust` | 48,872 | +775 |
| 9 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 跨 400+ 社交网络按用户名批量追踪账号的开源命令行工具 | `Python` | 108,158 | +2,387 |
| 10 | [tokio-rs/topcoat](https://github.com/tokio-rs/topcoat) | Tokio 出品的全栈 Rust Web 框架，内置组件、路由与客户端响应式能力，开箱即用… | `Rust` | 6,581 | +192 |
| 11 | [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) | 一个面向长会话的上下文压缩插件，小窗口省 5 倍 token，让单次会话跑到几十亿 tok… | `TypeScript` | 5,939 | +374 |
| 12 | [mattpocock/skills](https://github.com/mattpocock/skills) | 从 Matt Pocock 日常使用的 .agents 目录整理的、小巧可组合的 AI 编… | `Shell` | 320,284 | +1,223 |

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
| `top_n` | 详细介绍的仓库数（默认 10，按 GitHub 页面原始顺序取，跳过连续在榜超限的仓库后顺延） |
| `top_n_max_streak_days` | 连续在榜达到该天数的仓库不再进详细介绍（默认 3，仍保留在完整榜单里） |
| `top_n_fill.enabled` | 精选不足 `top_n` 时，是否用榜单外的 trending 新仓库补满（默认开） |
| `top_n_fill.languages` | 补位来源：这些语言的 trending 页（默认 python / typescript / javascript / rust / go / c++） |
| `top_n_fill.cooldown_days` | 补位仓库的冷却期：最近 N 天内展示过的不再重复补（默认 7） |
| `pages_url` | HTML 报告地址（GitHub Pages，邮件和日报里带这个链接） |
| `repo_url` | 仓库地址（HTML 报告页的订阅按钮用） |
| `mentions.enabled` | 是否 @ 提及 stargazer（关闭后改为纯 Issue 模式，需用户 Watch 才能收到通知） |
| `mentions.chunk_size` | 每批 @ 的人数（默认 10）：第一批写进 Issue 正文，超出部分分批发评论 |
| `ai.enabled` | 是否用 AI 逐个仓库生成详细介绍（需在仓库 Secrets 配置对应 Key） |
| `ai.provider` | AI 提供商：`deepseek`（默认）或 `anthropic` |
| `ai.model` | 模型名（DeepSeek 默认 `deepseek-flash`；Anthropic 如 `claude-opus-5-5`） |
| `ai.base_url` | OpenAI 兼容接口地址（仅 deepseek 类 provider 使用，默认 DeepSeek 官方接口） |
| `ai.api_key_env` | 密钥所在环境变量（默认 `DEEPSEEK_API_KEY`；用 Claude 时改成 `ANTHROPIC_API_KEY`） |
| `ai.readme_chars` | 每个仓库喂给 AI 的 README 截断长度（默认 6000 字符） |
| `ai.workers` | 并发分析线程数（默认 5） |

## ❓ 常见问题

**为什么 Star 后就能收到邮件？**
GitHub 不提供 stargazer 的邮箱，本项目每天读取 star 名单并在当天 Issue 正文里 @ 他们；GitHub 的提及通知默认发送到邮箱。无需也不收集用户的邮箱地址。

**为什么每天只收到一封邮件？**
GitHub 每产生一次「Issue 创建 / 评论」事件就发一封邮件。@ 提及直接写进 Issue 正文，创建 Issue 只算一个事件，所以被 @ 的人和 Watch 仓库的人每天合计只收到一封邮件（正文里既有提及也有完整榜单）。

**不想再收怎么办？**
任选其一：取消 Star；把自己的用户名加进 [`data/opt_out.json`](data/opt_out.json) 提个 PR；在 GitHub 通知设置里关闭提及通知。

**人多了会被限流吗？**
@ 提及走的是 GitHub 官方通知机制。本项目已做分批 @（每批 10 人）和限速保护。如果 star 数量很大（数千人）被 GitHub 处置，可关闭 `mentions` 改纯 Issue 模式。

**为什么邮件里没有自定义样式？**
GitHub 通知邮件由 GitHub 统一渲染，无法注入自定义 CSS。所以邮件内容用 GitHub 支持的排版元素（标题、表格、列表）呈现，需要精美样式时点邮件里的链接打开 HTML 报告页即可。

**数据来源可靠吗？**
数据来自 [github.com/trending](https://github.com/trending) 官方页面（GitHub 没有 trending API，本项目解析其页面）。偶发反爬失败时当天会跳过，第二天自动重试。

**AI 介绍是怎么做的？**
每个仓库单独调用一次 AI（不是批量），输入是该仓库的 README 原文（截断 6000 字符）+ 仓库数据，输出"一句话定位 + 详细介绍（100~200 字）+ 核心功能列表 + 适合谁"。默认走 DeepSeek：在仓库 Settings → Secrets and variables → Actions 添加 `DEEPSEEK_API_KEY`（或命令行 `gh secret set DEEPSEEK_API_KEY`），第二天自动生效。想用 Claude：把 `config.json` 的 `ai.provider` 改成 `anthropic`、`ai.api_key_env` 改成 `ANTHROPIC_API_KEY`，并设置对应 Secret。没有 Key 时回退显示仓库原始英文描述。

**同一个仓库连续上榜会重复总结吗？**
不会。AI 分析结果缓存在 `data/repos.json`（随仓库提交），再次上榜时直接复用，不再调用 AI；缓存里同时记录首次出现、最近出现日期和连续在榜天数。连续在榜达到 `top_n_max_streak_days`（默认 3 天）的仓库会退出「今日精选」的详细介绍位，但仍保留在完整榜单中。精选位不够 `top_n` 时，会从各语言 trending 页补充「同样在 trending、但不在今日榜单、且最近 `top_n_fill.cooldown_days` 天没展示过」的新项目补满，标为 🆕。

## ⚠️ 免责声明

本项目与 GitHub 无关，仅用于学习和技术交流。请勿滥用 @ 提及功能。
