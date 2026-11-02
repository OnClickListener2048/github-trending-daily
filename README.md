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

## 🏆 今日之星 TOP 5（深度解析）

### 1. [pingdotgg/t3code](https://github.com/pingdotgg/t3code) — ⭐ 40,544（今日 +3,216）

> 在手机和桌面远程接管本机各类编程 Agent 的开源控制台

- **🎯 它是什么**：它本身不是新 Agent，而是为已订阅的 Claude Code、Codex、Cursor 等 CLI 加一层统一控制面，集中管理会话、权限模式和源码集成，解决长任务必须守在终端前的问题。
- **⚙️ 技术方案**：本地 t3 服务托管各家 Agent 进程并标准化会话状态，Web、iOS、Android、Electron 作为客户端通过远程访问接入；另有 MCP 桥让外部 Agent 反向调用；构建工具链使用 Vite+。
- **👥 适合谁**：已订阅多个编程 Agent、需要离开工位后仍能盯住长时间任务的独立开发者与小团队
- **🔥 为什么火**：作者 pingdotgg 自带社区流量，项目一发布就全平台上架，恰好切中「多个 Agent 订阅行为分散、只能用桌面端」的痛点，单日 +3216 星。
- 💡 一个界面统管 7 家 Agent CLI，直接复用本机已有的订阅登录态，不额外收费
- 💡 移动端是一等公民，iOS/Android 官方商店可装，随时遥控本机跑着的长任务
- 💡 分发覆盖 Homebrew、winget、scoop、AUR、nixpkgs 与 curl 一键脚本，且完全开源可 fork

`TypeScript` · Fork 9,029 · 🔗 [官网](https://t3.codes)

### 2. [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — ⭐ 8,480（今日 +2,243）

> 基于操作系统无障碍树的桌面 Agent 操作层，用快照 ref 代替像素猜测

- **🎯 它是什么**：让 AI agent 操作桌面应用时不再靠截图猜像素，而是先读取应用真实的 UI 结构，再执行点击和输入。它以统一的 CLI 和 C 库覆盖 macOS、Windows 和 Linux，每条命令输出一个 JSON 响应，便于 agent 循环调用。
- **⚙️ 技术方案**：Rust 直接读取 macOS AX、Windows UIA、Linux AT-SPI 无障碍树；ref 绑定快照命名空间（@s8f3k2p9:e8），直接使用裸 ref 会报 INVALID_ARGS，UI 变化则返回 STALE_REF 或 AMBIGUOUS_TARGET；macOS 侧有常驻命令宿主保留原生 AX 对象，防止被删除的行被错误解析到同名的存活行，动作默认不移动指针也不抢占焦点。
- **👥 适合谁**：做 computer-use agent 的框架作者、跨平台桌面自动化与 RPA 工程、UI 端到端测试团队
- **🔥 为什么火**：Vercel Labs 品牌加上 computer-use 热潮，且给出「不靠截图、改用无障碍树」的明确替代路线；单日新增 2,243 约占总量 26%，属于集中发布后爆发，而非自然增长。
- 💡 ref 带快照与构建版本命名空间，UI 变化时显式报 STALE_REF，动作可安全重试
- 💡 默认 headless：走无障碍 API 而非合成输入，不改焦点、不移动指针，--headed 才用物理输入
- 💡 错误响应带 disposition.retry，agent 只在标记 safe 时重试，重试策略由程序判断而非自然语言描述

`Rust` · Fork 593 · 🔗 [官网](https://agent-browser.dev/desktop)

### 3. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) — ⭐ 110,376（今日 +1,799）

> 为多款 AI 编程 Agent 提供跨会话持久记忆与上下文压缩的中间层。

- **🎯 它是什么**：它把 Agent 会话中的工具调用、观察与决策自动记录下来，用 AI 压缩成语义摘要，并在后续会话注入相关片段，解决重开对话即丢失项目上下文的痛点。
- **⚙️ 技术方案**：基于 Claude Code 钩子捕获会话事件，后台生成语义摘要进入记忆库，再通过 MCP 搜索工具按需回注；TypeScript 编写、要求 Node 20+，并以适配层兼容多种 IDE/Agent。
- **👥 适合谁**：长期使用 Claude Code、Codex 等编码 Agent 的开发者，以及需要跨会话续接大型项目的团队。
- **🔥 为什么火**：Agent 记忆是编码助手最大短板，今日 +1,799 反映跨会话续接需求集中释放；多 Agent 兼容与 Claude Code 生态热度助推传播。
- 💡 跨 Agent 兼容 Claude Code、Codex、Gemini、Copilot、OpenCode 等，用统一记忆层避免被单一助手锁定
- 💡 自动捕获→AI 压缩→相关上下文回注形成闭环，减少手动维护 CLAUDE.md 或粘贴历史
- 💡 提供 MCP 搜索工具供 Agent 主动检索历史观察，npx 一条命令安装，并有 30+ 语言 README

`TypeScript` · Fork 9,631 · 🔗 [官网](https://claude-mem.ai)

### 4. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) — ⭐ 33,151（今日 +1,380）

> 用 49 个 AI 子代理，把 Claude Code 改造成单人独立游戏工作室的流程模板。

- **🎯 它是什么**：它是一套纯配置模板，往 .claude/ 里放入 49 个子代理、74 个斜杠命令、15 个 hooks 和 14 条规则，专门解决单人用 AI 做游戏时没人做设计评审、没有 QA、随手硬编码魔法数字的失控问题。
- **⚙️ 技术方案**：核心是用 .claude/agents 的 frontmatter 声明模型档位：三位导演用 Opus，主程等 16 个用 Sonnet，其余 30 个继承会话模型；hooks 在 commit、push、资产变更时自动校验，rules 按路径作用域强制编码规范，另有 Godot、Unity、UE5 三套引擎专家。
- **👥 适合谁**：适合用 Claude Code 单干的独立游戏开发者；项目在 Godot、Unity、UE5 上尤其对口，也适合想借鉴多代理编排思路的人。
- **🔥 为什么火**：它搭上 Claude Code 生态热度，模板拷进目录即用、门槛极低；4,486 fork 对 33k star 约 13% 的 fork 率说明大量人是真把它复制进自己项目，而不只是点个星。
- 💡 采用导演、部门主管、专家三层工作室结构，为每个 agent 定义职责、升级路径和质量门，而不是堆一层平级 prompt
- 💡 用 14 条路径规则和 15 个自动组合 hooks，把「不许硬编码魔法数字」这类口头约定变成提交时真正触发的检查
- 💡 62 个模板覆盖 GDD、UX 规格、ADR、冲刺计划、HUD、无障碍，搭配从 /create-epics 到 /dev-story 再到 /story-done 的闭环命令

`Shell` · Fork 4,486

### 5. [mattpocock/skills](https://github.com/mattpocock/skills) — ⭐ 309,887（今日 +970）

> Matt Pocock 日常自用的可组合 AI 编码 Agent 技能集，反「氛围编程」

- **🎯 它是什么**：把工程经验沉淀成几十个可改可拼的 Agent 技能（斜杠命令），针对「Agent 没理解需求」和「输出啰嗦」两大失败模式，替代 GSD/BMAD/Spec-Kit 那套接管流程的黑盒方案。
- **⚙️ 技术方案**：纯 Shell 组织 SKILL.md 文件，跨 Claude Code、Codex、Copilot、Gemini CLI、Cursor 等多家 Agent 分发；/setup-matt-pocock-skills 一次性把 issue tracker、triage 标签、文档目录写入项目约定，/grill-me 与 /grill-with-docs 用反问对齐需求，CONTEXT.md 式共享词汇表压缩输出。
- **👥 适合谁**：已在 Claude Code、Codex 等工具里做真实项目的资深开发者，想拿回流程控制权而非被框架绑架的人。
- **🔥 为什么火**：单日 +970 由 Matt Pocock 60k 订阅者的 newsletter 与插件市场一条命令安装共同推动，恰好踩中「Spec 框架太重、要小而可改」的反弹情绪。
- 💡 安装路径按 Agent 分流：Claude/Codex/Copilot 走插件市场自动更新，Gemini 与 Cursor 等走 npx skills 手动拷可编辑文件，README 明确只装一种以免技能重复两份
- 💡 把「需求对齐」做成可复用仪式——/grill-me 强制 Agent 先反问细节，作者称是其最常用技能，而非依赖一次性 prompt
- 💡 自托管配置层：初始化时问清 issue tracker 与标签体系，让 /triage 等技能直接对接 GitHub/GitLab/本地文件的真实工单流程

`Shell` · Fork 26,072 · 🔗 [官网](https://aihero.dev/skills)

## 📋 完整榜单

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 基于操作系统无障碍树的桌面 Agent 操作层，用快照 ref 代替像素猜测 | `Rust` | 8,480 | +2,243 |
| 2 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 为多款 AI 编程 Agent 提供跨会话持久记忆与上下文压缩的中间层。 | `TypeScript` | 110,376 | +1,799 |
| 3 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 一站式 Python 爬虫框架，把 HTTP 请求、隐身浏览器、解析与并发爬取收进同一个库 | `Python` | 92,398 | +892 |
| 4 | [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) | 用 C++ 从零自研的 Wayland 动态平铺合成器，以动画特效和插件生态见长。 | `C++` | 39,728 | +508 |
| 5 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 用 49 个 AI 子代理，把 Claude Code 改造成单人独立游戏工作室的流程模板… | `Shell` | 33,151 | +1,380 |
| 6 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | 边缘原生 MoE 推理引擎，让游戏 PC 本地运行 290B+ 前沿大模型 | `Python` | 15,850 | +654 |
| 7 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 在手机和桌面远程接管本机各类编程 Agent 的开源控制台 | `TypeScript` | 40,544 | +3,216 |
| 8 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | 首个面向金融K线的开源基础模型，覆盖45+交易所 | `Python` | 45,819 | +855 |
| 9 | [kornia/kornia](https://github.com/kornia/kornia) | 基于 PyTorch 的可微分计算机视觉库，把几何视觉算法与图像算子全部纳入自动求导 | `Python` | 12,034 | +412 |
| 10 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 用纯 C 把超大 MoE 模型搬上消费级机器，专家权重按需从磁盘流式读取。 | `C` | 46,277 | +655 |
| 11 | [mattpocock/skills](https://github.com/mattpocock/skills) | Matt Pocock 日常自用的可组合 AI 编码 Agent 技能集，反「氛围编程」 | `Shell` | 309,887 | +970 |
| 12 | [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | 面向并行 AI agent 工作流的 Rust git worktree 管理 CLI | `Rust` | 9,886 | +115 |
| 13 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 把多个 AI 编码代理当作员工来雇、管、发预算的开源「AI 公司」编排台 | `TypeScript` | 110,188 | +507 |
| 14 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | Karpathy 的极简 LLM 训练脚手架，用一个 --depth 旋钮花几十美元复刻 … | `Python` | 59,701 | +325 |
| 15 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | 免训练改写 LLM 行为的工具，一条命令即可去除模型审查、压制 slop 与谄媚。 | `Python` | 37,864 | +404 |

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
