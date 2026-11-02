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

### 1. [pingdotgg/t3code](https://github.com/pingdotgg/t3code) — ⭐ 40,567（今日 +3,216）

> 统一控制本机 Claude Code、Codex、Cursor 等 AI 编码代理的跨端控制台。

T3 Code 是一个「agent harness 控制面」：只要你的电脑上已经装好并登录了 Claude Code、Codex、Cursor、Grok Build、OpenCode、Antigravity 或 fx，它就能接管这些代理，给你一个统一界面去派活、看进度、处理权限审批。入口有 Electron 桌面端、网页端和 iOS/Android 手机 App，另有 t3 命令行在本机起服务，可装成后台常驻服务。项目完全免费开源，作者明确说不卖任何东西，只是想要一个性能好、能远程、真正开放的代理开发环境；如果方向不合你意，你可以直接 fork 改成自己要的编辑器。

- ✨ 多代理统一接入：支持 Claude Code、Codex、Cursor、Grok Build、OpenCode、Google Antigravity、fx，本机已认证的代理都能被接管
- ✨ 三种客户端：Electron 桌面端、网页应用和 iOS/Android 手机 App，同一套会话随处继续
- ✨ 远程访问：可从手机或另一台机器连回本机运行的服务，不在电脑前也能盯着代理干活
- ✨ 可配置的权限模式、项目设置、键盘快捷键和外观偏好，按项目调整代理行为
- ✨ 源代码管理集成，并支持通过 MCP 让 Claude Code、Codex、ChatGPT 等外部代理接入
- ✨ 安装省事：curl 脚本或 npx t3@latest 即可跑起来，t3 service install 常驻后台、t3 update 升级；桌面端覆盖 winget、scoop、Homebrew、.deb、AUR、Nix
- 👥 适合谁：已经在用 Claude Code、Codex 等代理命令行，想要更好界面和手机远程能力的开发者。

`TypeScript` · Fork 9,032 · 🔗 [官网](https://t3.codes)

### 2. [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — ⭐ 8,492（今日 +2,243）

> 让 AI 代理通过操作系统无障碍树读取并操作桌面应用，稳定且可重试的电脑操作方案。

agent-desktop 是 Vercel Labs 出品的 CLI 和 C 库，支持 macOS、Windows 与 Linux。它不做像素识别，而是直接读取任意应用真实的无障碍树结构，一次 snapshot 返回 JSON，其中每个可操作元素都带一个 ref；代理对 ref 执行 click 等动作后再次 snapshot 验证，整个循环留在你自己的 agent 里。它解决的是让代理操作界面不再靠猜测，并提供明确的错误码与重试规则。用 npm 全局安装即可使用。

- ✨ snapshot 返回带 ref 的无障碍树 JSON，代理可直接对 ref 执行点击等动作，无需像素匹配
- ✨ ref 绑定所属 snapshot，UI 变化时返回 STALE_REF 或 AMBIGUOUS_TARGET，提示重新快照，操作可安全重试
- ✨ 默认 headless：通过无障碍 API 执行动作，不移动指针、不抢焦点，加 --headed 才使用物理输入
- ✨ 多窗口与密集应用有解：多窗口返回候选 window id 并可用 --window-id 指定；先用 --skeleton 粗览，再用 --root 下钻
- ✨ 每条命令输出统一 JSON 信封（ok 加 data 或 error），错误带 code、disposition 和建议，仅在标记为安全时重试
- ✨ 跨平台支持 macOS、Windows、Linux，含 x64 与 ARM64 原生二进制；内置版本匹配的 skills 文档供 agent 自读
- 👥 适合谁：想让 AI 代理可靠操作桌面应用的开发者，尤其是做 computer use、RPA 或桌面自动化的团队。

`Rust` · Fork 593 · 🔗 [官网](https://agent-browser.dev/desktop)

### 3. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) — ⭐ 110,381（今日 +1,799）

> 给 AI 编码 agent 装上长期记忆，自动记录会话内容、压缩成摘要，并在下次会话自动带回相关上下文。

Claude-Mem 是一个为编码 agent 设计的持久记忆系统，最初专为 Claude Code 打造。它解决的核心痛点是：每次新会话开始时，agent 对项目此前发生过的讨论、尝试和决策一无所知，你必须反复重述背景。Claude-Mem 在后台自动捕获 agent 在会话中的工具使用与操作观察，用 AI 把它们压缩成语义摘要存下来，等下一次会话再自动把相关内容注入上下文，让 agent 接着上次的进度继续干。装起来很简单，一条 npx claude-mem install --ide <你的 IDE/agent> 命令即可；它不只支持 Claude Code，也适配 Codex、Gemini、Copilot、OpenCode 等多种宿主，并带有 MCP 搜索工具让你主动翻查历史记忆。

- ✨ 会话自动捕获：后台记录 agent 在会话中的工具使用与操作观察，无需手动保存
- ✨ AI 语义压缩：把冗长的原始操作记录压缩成简洁摘要，而不是把整段历史塞回上下文
- ✨ 跨会话上下文注入：新会话开始时自动带回与当前任务相关的历史记忆，保持项目知识连续性
- ✨ MCP 搜索工具：提供可调用的检索能力，主动查找过去会话中记录过的内容
- ✨ 广泛兼容：支持 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等多种 agent 与 IDE
- ✨ 一条命令安装（npx claude-mem install --ide ...），并附带配置说明与故障排查文档，社区提供 30 多种语言 README
- 👥 适合谁：长期用 Claude Code、Codex 等 AI 编码 agent 做实际项目、苦于每次会话都要重新交代背景的开发者。

`TypeScript` · Fork 9,631 · 🔗 [官网](https://claude-mem.ai)

### 4. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) — ⭐ 33,163（今日 +1,380）

> 把单次 Claude Code 会话变成 49 个 AI 代理组成的完整游戏工作室

它是给 Claude Code 用的一套配置工程：把一个通用聊天助手，变成有层级、有流程的 AI 游戏工作室。单打独斗用 AI 做游戏最大的问题是没人管——没人拦你硬编码魔法数字、跳过设计文档、写出意大利面代码，也没有 QA 和设计评审。这套东西用导演、部门主管、专家三层代理，加上 15 个 hooks 和 14 条按路径生效的规则，在你提交代码、改动资产、读写设计文档时自动把关。装好后敲 /start 上手，再用 /brainstorm、/design-system、/create-stories、/dev-story 一路走到上线。决定权仍在你手里，只是现在有一支会提问、会提前抓错的团队。

- ✨ 49 个专职子代理，按导演、部门主管、专家三层工作室层级组织，各自有明确职责、上报路径和质量关卡
- ✨ 74 个斜杠命令覆盖全流程：/start、/brainstorm、/map-systems、/design-system、/create-architecture、/create-epics、/create-stories、/dev-story、/sprint-plan、/story-done 等
- ✨ 15 个 hooks 在提交、推送、资产变更、设计文档读写、注册表更新和会话生命周期上自动校验，并保留代理审计轨迹与缺口检测
- ✨ 14 条按路径生效的编码规范，在编辑玩法、引擎、AI、UI、网络代码及场景与资产文件时强制约束
- ✨ 62 份文档模板，涵盖 GDD、UX 规格、ADR、冲刺计划、HUD 设计、无障碍设计等
- ✨ 内置 Godot 4、Unity、Unreal Engine 5 三套引擎专家代理组（含 GDScript、DOTS/ECS、GAS、复制同步等子专家），按项目选用对应一套
- 👥 适合谁：用 Claude Code 做游戏的独立开发者和微型团队，希望给 AI 协作补上设计评审与 QA 纪律的人

`Shell` · Fork 4,486

### 5. [mattpocock/skills](https://github.com/mattpocock/skills) — ⭐ 309,900（今日 +970）

> Matt Pocock 日常使用的 AI 编程代理技能集，主打真实工程而非“氛围编程”。

这是 Matt Pocock 从自己 .agents 目录中整理出的日常 AI 代理技能集合，专为“写真正的应用”而非“氛围编程”（vibe coding）设计。它要解决的核心问题是：GSD、BMAD、Spec-Kit 这类方案试图接管开发流程，却让开发者失去控制，流程中的 bug 也难以排查。这些技能刻意做得小而可改、可组合，兼容任意模型，并附带 `/setup-matt-pocock-skills` 一次性初始化：选定 issue 跟踪方式（GitHub、GitLab、本地文件等）、配置 triage 标签、指定文档存放位置。安装支持 Claude Code、Codex、GitHub Copilot、Gemini CLI 及 Cursor、Windsurf 等任意代理，插件可自动更新，也可手动维护可编辑副本。

- ✨ `/grill-me` 与 `/grill-with-docs`：动手前让代理反问细节，先把需求对齐清楚，避免“做出来的不是我想要的”
- ✨ 共享语言（glossary/上下文文档）：把项目术语沉淀成文档，纠正代理啰嗦、乱猜行话的问题
- ✨ `/setup-matt-pocock-skills` 一次初始化：选择 issue 跟踪系统、配置 triage 标签、指定文档目录
- ✨ 多代理安装方式：Claude Code、Codex、GitHub Copilot（CLI 与 VS Code）、Gemini CLI 及 npx skills 通用路径
- ✨ 插件自动更新与可编辑副本两种模式，按需在“省心”和“可魔改”之间取舍
- ✨ 技能保持小而可组合，可随意修改成自己的版本，且不绑定特定模型
- 👥 适合谁：使用 Claude Code、Codex、Copilot 等编程代理、希望保留流程控制权的工程师。

`Shell` · Fork 26,072 · 🔗 [官网](https://aihero.dev/skills)

## 📋 完整榜单

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 让 AI 代理通过操作系统无障碍树读取并操作桌面应用，稳定且可重试的电脑操作方案。 | `Rust` | 8,492 | +2,243 |
| 2 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 给 AI 编码 agent 装上长期记忆，自动记录会话内容、压缩成摘要，并在下次会话自动带… | `TypeScript` | 110,381 | +1,799 |
| 3 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 一个库搞定从单次请求到全站爬取的 Python 爬虫框架 | `Python` | 92,401 | +858 |
| 4 | [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) | 完全独立、颜值与可定制性兼备的动态平铺 Wayland 合成器，插件生态强大。 | `C++` | 39,729 | +508 |
| 5 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 把单次 Claude Code 会话变成 49 个 AI 代理组成的完整游戏工作室 | `Shell` | 33,163 | +1,380 |
| 6 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | 把数据中心级 MoE 推理搬到个人电脑上的边缘原生服务引擎，让消费级硬件也能跑 290B+… | `Python` | 15,850 | +654 |
| 7 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 统一控制本机 Claude Code、Codex、Cursor 等 AI 编码代理的跨端控… | `TypeScript` | 40,567 | +3,216 |
| 8 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | 首个开源的金融K线基础模型，在45+全球交易所数据上预训练 | `Python` | 45,823 | +855 |
| 9 | [kornia/kornia](https://github.com/kornia/kornia) | 基于 PyTorch 的可微分计算机视觉库，把图像处理与几何视觉算法搬到 GPU 上并保留… | `Python` | 12,034 | +412 |
| 10 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 纯 C 编写、零依赖的轻量推理引擎，让普通电脑也能跑千亿参数 MoE 大模型 | `C` | 46,281 | +655 |
| 11 | [mattpocock/skills](https://github.com/mattpocock/skills) | Matt Pocock 日常使用的 AI 编程代理技能集，主打真实工程而非“氛围编程”。 | `Shell` | 309,900 | +970 |
| 12 | [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | 面向并行 AI agent 工作流的 Git worktree 命令行工具，让 workt… | `Rust` | 9,887 | +115 |
| 13 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 开源的 AI 智能体团队编排平台，像经营一家公司一样管理你的 AI 员工。 | `TypeScript` | 110,189 | +507 |
| 14 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | 一个跑在单节点 GPU 上、代码极简可改的 LLM 全流程训练实验框架，几十美元即可复刻 … | `Python` | 59,701 | +325 |
| 15 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | 无需训练即可改造本地大模型，去除审查、抑制废话、降低谄媚倾向。 | `Python` | 37,865 | +404 |

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
| `top_n` | 详细介绍的仓库数（默认 10，按今日新增排序） |
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
