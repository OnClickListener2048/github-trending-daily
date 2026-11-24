# 🔥 GitHub Trending Daily · 每日热榜推送

[![daily-trending](https://github.com/OnClickListener2048/github-trending-daily/actions/workflows/daily-trending.yml/badge.svg)](https://github.com/OnClickListener2048/github-trending-daily/actions/workflows/daily-trending.yml)
![GitHub stars](https://img.shields.io/github/stars/OnClickListener2048/github-trending-daily)

每天自动抓取 [github.com/trending](https://github.com/trending) 的热门仓库，**给每一位 Star 过本仓库的人发一封邮件**，正文就是当天榜单 + 每个仓库的一句话简介。

## ✨ 怎么接收

1. **Star 本仓库** ⭐
2. 保持 GitHub 邮件通知开启（默认就是开的，不用动）
3. 完成。每天早上 08:30（北京时间）你会收到一封来自 GitHub 的邮件：🏆 今日精选详解（每个仓库"是什么 + 能干什么"，同一仓库 3 天内不会重复出现）+ 🚀 Show HN 新品 + 🧡 Product Hunt 今日榜 + 🇨🇳 V2EX 独立开发 + 📋 完整榜单，并附精美 HTML 报告链接

> 原理：每天自动创建一个 Issue 并 @ 你的用户名，GitHub 会把提及通知默认发送到你的邮箱。不需要填邮箱、不需要注册，**Star 即订阅**。全程使用 GitHub 官方机制，不收集任何个人信息。

## 🧭 今日榜单

<!-- TRENDING:START -->

# 🔥 GitHub 每日 Trending · 2026-11-24

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 10 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 今日精选（详细介绍）

### 1. [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) — ⭐ 20,470（今日 +2,029）

> 装进 Claude Code 的漏洞赏金与外部红队技能包，83 个技能开箱即用

Claude-BugHunter 是一个可直接安装的 Claude Code 技能包：装一次，Claude 就从聊天机器人变成有经验的漏洞赏金研究员或红队操作员。它把方法论、58 个按漏洞类别整理的 hunt-* 技能、企业身份与基础设施攻击链、以及定级报告与证据脱敏流程分层堆叠起来；这些 hunt-* 技能源自 681 份公开 HackerOne 报告。使用时不用记技能名，直接用日常语言描述你在测什么，相关技能就会自动加载。支持通过插件市场一键安装，也可以用脚本复制安装，并能同时装进 OpenCode、Codex CLI 等其他 agent 工具。

- ✨ 83 个技能 + 15 个斜杠命令，按主题自动触发，无需按名称调用
- ✨ 58 个 hunt-* 漏洞类别技能，整理自 681 份公开 HackerOne 报告，含检测模式、payload、绕过表和链式利用模板
- ✨ bb-methodology 与 redteam-mindset 提供五阶段非线性工作流、批判性思维框架和红队操作纪律
- ✨ 企业外围攻击矩阵：M365/Entra、Okta、vCenter、SSL-VPN、SharePoint、云 IAM 的 2024–2026 CVE 链与凭据后提权
- ✨ triage-validation 七问门、VRT 感知定级、OOS 反驳话术、PII 脱敏与红队交付物
- ✨ 插件市场一键安装或脚本复制安装，附带 hunt 接驳目录脚手架、cbh CLI 与 Burp MCP 集成，可同时装到多个 agent harness
- 👥 适合谁：从事授权漏洞赏金、外部红队与 Web 应用安全测试的安全研究员

`Python` · Fork 2,166 · 🔗 [官网](https://elementalsouls.github.io/Claude-BugHunter)

### 2. [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) — ⭐ 12,472（今日 +422）

> Google Stitch 官方 Agent Skills 库：让编码 Agent 直接操作设计稿与设计系统

这是 Google Labs 为 Stitch（Google 的 AI 界面设计工具）整理的一套 Agent Skills 和插件合集，遵循 Agent Skills 开放标准，因此能直接用在 Codex、Antigravity、Gemini CLI、Claude Code、Cursor、OpenCode 等编码 Agent 里。它要解决的是「设计和写代码各干各的、需要人工来回搬运」的问题：Agent 通过 Stitch MCP 服务器连上 Stitch 后，就能用自然语言生成界面、修改现有屏幕、批量产出设计变体，也能把已有的前端代码反向转成设计稿，或者从源码里抽出 DESIGN.md 设计系统再统一套用到所有屏幕上。安装方式按客户端分：Codex 通过插件市场，Claude Code 和 Cursor 用 npx plugins 安装，OpenCode 则需要手动拷贝 skill 目录并自行配置远程 MCP 条目。前提是先在 Agent 环境中完成 Stitch MCP 的注册和凭据配置。

- ✨ 从文本或图片生成新界面，支持编辑已有屏幕、批量生成设计变体
- ✨ 把 React、Vue 等前端代码转成 Stitch 设计稿（HTML 提取 + 设计系统 + 上传）
- ✨ 从源码自动抽取 DESIGN.md 设计系统，并一键套用到全部屏幕
- ✨ 管理 Stitch 设计系统，上传 DESIGN.md、应用主题
- ✨ 提取自包含的静态 HTML，便于交付或迁移
- ✨ 多客户端插件化安装：Codex 市场、Claude Code/Cursor 的 npx 安装、OpenCode 手动接入
- 👥 适合谁：需要把 UI 设计稿与代码库打通的前端工程师、全栈开发者和设计工程师，尤其是已在 Claude Code、Cursor、Codex 等 Agent 中工作的人。

`TypeScript` · Fork 1,519 · 🔗 [官网](https://stitch.withgoogle.com/docs/mcp/setup)

### 3. [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) — ⭐ 61,145（今日 +792）

> 把 PS5 可执行文件自动重链接为 Linux、Windows 原生程序的转换工具

AnyPS5 是一个 C++ 编写的转换工具，目标是把 PS5 的可执行文件自动移植到 Linux 和 Windows 上运行。它的核心是 relinker（重链接器），会把 PS5 可执行文件转换成目标系统的原生格式，同时提供一套可动态链接的 system prx 系统库实现，不依赖模拟器，也不需要额外的运行时进程。项目还带有基于网页的转换器，文件全程留在本地设备上，不上传。官方提供了程序构建、架构说明、代码规范、技术债清单等文档，以及各游戏的兼容性讨论区。命令行遇到未支持状态会抛 C++ 异常；着色器重编译器在启用 SPIRV-Tools 的构建中可产出经过验证的 SPIR-V。仅含 relinker 的构建还能在 macOS（包括 Apple silicon）上运行。

- ✨ 自动重链接：把 PS5 可执行文件转换为 Linux、Windows 原生可执行格式
- ✨ 提供 system prx 系统库实现，支持动态链接，无需模拟器或独立运行时进程
- ✨ 着色器重编译器输出 SPIR-V，并可用 Spirv-Tools 校验结果
- ✨ 网页版转换器，所有文件处理都在本地设备完成，不上传服务器
- ✨ 输入映射支持 SDL 手柄（含摇杆与扳机），键鼠可通过 anyps5-input.ini 配置
- ✨ 仅含 relinker 的构建可在 macOS（含 Apple silicon）上运行
- 👥 适合谁：对 PS5 软件互操作性、移植研究与软件保存感兴趣的开发者和研究人员

`C++` · Fork 5,939 · 🔗 [官网](https://boykopovar.github.io/AnyPS5/)

### 4. [anomalyco/opencode](https://github.com/anomalyco/opencode) — ⭐ 228,879（今日 +263）

> 开源 AI 编码智能体，在终端里直接帮你写代码、查代码、跑命令。

OpenCode 是一个开源的 AI 编码智能体，官方定位就是「The open source coding agent」。它把 AI 助手放进你的终端：既能直接改代码、跑 bash 命令干开发活，也能切成只读模式，先摸清陌生代码库再动手。安装很轻，一条 curl 脚本或 npm、brew、pacman、mise、nix 都能装好，另外还提供处于 Beta 阶段的桌面应用（macOS、Windows、Linux）。想深入了解配置可以看官方文档，社区在 Discord 和 X 上。

- ✨ 终端 UI（TUI）形式的编码智能体，直接在命令行里工作
- ✨ 内置 build 与 plan 两个 agent，用 Tab 键随时切换
- ✨ plan 为只读模式：默认拒绝文件编辑，执行 bash 前先征求许可，适合探索陌生代码库
- ✨ general 子代理用于复杂搜索和多步任务，可在消息中用 @general 调用
- ✨ 安装方式覆盖 curl 脚本、npm/bun/pnpm/yarn、Homebrew、Arch 的 pacman 与 AUR、mise、Nix
- ✨ 提供 Beta 桌面应用，支持 macOS（Apple Silicon/Intel）、Windows 和 Linux 的 deb/rpm/AppImage
- 👥 适合谁：适合习惯在终端工作的开发者，尤其是需要 AI 辅助读代码、改代码、执行命令的人。

`TypeScript` · Fork 31,127 · 🔗 [官网](https://opencode.ai)

### 5. [microsoft/markitdown](https://github.com/microsoft/markitdown) — ⭐ 198,159（今日 +246）

> 微软出品的轻量 Python 工具，把各类文档转成适合 LLM 处理的 Markdown。

MarkItDown 是一个轻量级 Python 工具，用来把 PDF、Office 文档、图片、音频、HTML 等多种格式转换成 Markdown。它和 textract 定位相似，但重点是保留标题、列表、表格、链接等文档结构，方便喂给 LLM 和文本分析流水线。可以用命令行直接转换（markitdown file.pdf > out.md，支持 -o 和管道输入），也可以作为库调用。它更偏向给分析工具消费，而不是追求人类阅读级的高保真排版。

- ✨ 支持 PDF、Word、PowerPoint、Excel、EPub、HTML、CSV/JSON/XML、ZIP 等多种输入格式
- ✨ 保留标题、列表、表格、链接等关键文档结构，而不是退化为纯文本
- ✨ 图片可提取 EXIF 元数据并做描述，音频可提取元数据并转写（依赖托管服务）
- ✨ 支持 YouTube URL 转录和 Outlook 邮件转换
- ✨ 可选依赖按格式拆分安装（如 [pdf, docx, pptx]），也可用 [all] 一次装齐
- ✨ 支持第三方插件，默认关闭，需用 --list-plugins / --use-plugins 管理，官方还提供 markitdown-ocr 插件为 PDF、DOCX、PPTX、XLSX 中的内嵌图片补充 OCR
- 👥 适合谁：需要给 LLM 或文本分析流水线批量准备文档数据的 Python 开发者、数据工程师和 AI 应用团队。

`Python` · Fork 15,026

### 6. [Tencent/LoopForge](https://github.com/Tencent/LoopForge) — ⭐ 5,937（今日 +235）

> 自托管编码智能体交付平台，用 SOP 与人工审批把 AI 写代码变成团队可重复的流程。

LoopForge 是腾讯开源的自托管工作台，让团队用编码智能体真正交付软件，而不只是演示。在聊天里向 Main Bot 描述需求，它会按需拉起 Docker 沙箱、检出仓库、把任务分派给不同项目角色，最后提交 PR。当某种做法被验证有效，就可以固化成 SOP（智能体、脚本与人工审批节点组成的标准流程），下个需求照同样方式交付。底层调用 CodeBuddy、Codex、Claude Code 等编码 CLI，LoopForge 在其上补齐角色、沙箱、检查点与历史记录，全部跑在自己的服务器上，MIT 协议。

- ✨ 聊窗式主控（Main Bot）：用自然语言提需求，按需创建带仓库的 Docker 会话沙箱，按 @ 调用角色、技能、需求或 SOP，可中途排队消息、暂停、接管
- ✨ SOP 流程引擎：按序执行 Agent、Script、Human-gate 与子 SOP 节点，每个节点在独立沙箱运行，内置后端、前端、Bug 修复、产品等模板
- ✨ 角色分离：规划、实现、评审、测试各自拥有独立的提示词、执行器、模型、规则、Skills 与 MCP 工具，既能当 SOP 节点也能当聊天子智能体
- ✨ 人工审批关卡：在关键节点停下等待审批，可阅读报告后批准放行，或把工作退回指定步骤，失败步骤支持重试、从任意节点重跑
- ✨ 可观测与可恢复：节点状态、工具调用轨迹、日志与产物集中展示，随时暂停、继续或从某个节点重跑
- ✨ 多执行器与自有基础设施：支持 CodeBuddy、Codex、Claude Code、OpenCode、Cursor CLI、Antigravity、Kimi Code 等十种编码 CLI，集成 GitHub、Skills、MCP，Docker 沙箱或本机运行时，MIT 自托管
- 👥 适合谁：希望把 AI 编码纳入规范交付流程的研发团队、平台工程与需要审批留痕的技术负责人。

`Go` · Fork 831 · 🔗 [官网](https://loopforge.cn)

### 7. [p-e-w/heretic](https://github.com/p-e-w/heretic) — ⭐ 42,907（今日 +194）

> 无需训练即可改造本地大模型，去掉拒答、减少废话和谄媚。

Heretic 是一个让普通开发者在自己的显卡上直接改造语言模型的工具。过去这类修改（例如去除审查）通常只有算力充足的大公司才能做，而 Heretic 不做昂贵的训练，而是利用一组数学方法，根据对比示例提示和对应的评分器来引导模型行为。安装后执行一条命令（如 heretic Qwen/Qwen3-4B-Instruct-2507）即可运行，默认行为是去除模型的拒绝回答倾向；在 RTX 3090 上处理 Qwen3-4B 大约需要 30-40 分钟，完成后可以选择保存模型、上传到 Hugging Face、直接对话测试或运行基准评测。

- ✨ 去除审查、抑制拒答（默认行为）
- ✨ 通过配置文件切换目标：减少废话、减少幽默、降低谄媚、调整情绪倾向
- ✨ 支持通过插件自定义 scorer，控制优化目标
- ✨ 支持多数稠密模型、多种 MoE 架构、多模态与混合模型
- ✨ 支持 bitsandbytes 4-bit 动态量化，降低显存占用
- ✨ 运行前自动测试硬件以确定最优批大小，完成后可保存、上传、对话测试或跑基准
- 👥 适合谁：想在本地改造开源大模型行为、但缺乏大规模训练算力的开发者与爱好者。

`Python` · Fork 5,355 · 🔗 [官网](https://heretic-project.org)

### 8. [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — ⭐ 58,349（今日 +160）

> 一款 Claude Code 学术研究技能包，覆盖从调研到定稿的完整论文流程。

这是一套以 Claude Code 插件形式分发的学术研究技能集，把论文工作拆成 research → write → review → revise → finalize 五个阶段，每到一个阶段就停下来等你确认；它可以起草整篇论文，但选题、方法、数据解读和结论必须由你决定。它主要解决的事情包括：查找并核对文献、按格式整理引用、检查数据与逻辑是否一致，以及避免 AI 自己编造引用或结果。安装只需两条命令：先把插件市场加到本地环境，再安装插件；随后输入 /ars-plan，它就会用苏格拉底式提问帮你梳理论文结构。它也支持在 claude.ai 或 Claude Desktop 上安装，不过 hooks 和插件 agent 在纯聊天界面不会运行。

- ✨ 五个阶段的流程（调研、写作、审稿、修改、定稿）在每阶段都会暂停并等待你确认，AI 担任副驾驶，不替你做出决定
- ✨ /ars-plan 通过苏格拉底式对话逐步问出论文结构，另外提供可选的审稿人校准模式，用你给的 gold set 测量它自身的漏报率 FNR 和误报率 FPR
- ✨ 引用可信链：使用 source provenance frontmatter 和三层引用定位锚点，为后续在论断层面进行审计打下基础
- ✨ 可选开启的论断审计（设置 ARS_CLAIM_AUDIT=1）会按每个锚点回抓被引原文，判断原文是否真的支持该论断；五类 HIGH-WARN 由格式化终端的硬性校验统一拦截
- ✨ Stage 2.5 与 Stage 4.5 设置完整性校验关卡，执行 7 条 AI 研究失败模式阻断清单（包括实施 bug、编造结果、方法论捏造、引用幻觉、框架锁死等）
- ✨ Style Calibration 从你过去的作品学习并贴合你的行文风格，Writing Quality Check 识别机器味浓的句式，目标是提高质量，并不教你怎么掩盖使用 AI 的痕迹
- 👥 适合谁：用 Claude Code 做文献综述、投稿论文的研究生与科研人员，也适合需要把控引用真实性的写作者。

`Python` · Fork 4,450 · 🔗 [官网](https://buymeacoffee.com/crucify020v)

### 9. [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) — ⭐ 33,858（今日 +149）

> 把多账号管理、协议转换与请求调度装进一个桌面端的本地 AI 中转站。

Antigravity Tools 是一款面向开发者和 AI 爱好者的桌面应用，核心思路是把多账号矩阵管理、协议转换和智能请求调度合到一起，在本地搭一个稳定、快速、低成本的 AI 中转站。它最实用的一点是能把常见的 Web Session（Google、Anthropic）转换成标准化的 API 接口，省掉不同供应商之间的协议差异，让你用统一的接口去调用。日常使用时，你在图形界面里集中看所有账号的配额健康度，由系统挑出当前最合适的账号一键切换，再配合请求调度把流量分摊到多个账号上。项目用 Tauri v2 + React 构建界面、Rust 写后端，属于安装即用的跨平台桌面程序，不必自己搭服务。

- ✨ 智能账号面板：集中查看所有账号的健康状况，实时掌握 Gemini Pro、Gemini Flash、Claude 与 Gemini 图像生成的剩余配额
- ✨ 智能推荐与一键切换：按配额冗余度实时算出“最佳账号”并推荐，支持一键切换，无需手动改配置
- ✨ 当前账号快照：用可视化方式呈现活跃账号状态，切换前后一目了然
- ✨ 协议转换：把 Google / Anthropic 的 Web Session 转成标准化 API 接口，抹平不同供应商之间的协议差异
- ✨ 智能请求调度与多账号矩阵分发：按策略把请求分配到多个账号上，避免单一账号被打满
- ✨ 本地 AI 中转站：以桌面应用形式在本地提供统一 API 入口，配合文档中的集成示例可直接接入现有工具链
- 👥 适合谁：手里有多个 AI 账号、想把网页会话转成标准 API 并统一调度请求的开发者与 AI 爱好者。

`Rust` · Fork 3,587 · 🔗 [官网](https://lbjlaq.github.io/Antigravity-Manager/)

### 10. [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) — ⭐ 78,562（今日 +123）

> 为 AI 编码代理预建代码知识图谱，减少 token 与工具调用，完全本地运行

CodeGraph 是一个预索引的代码知识图谱工具，专为 Claude Code、Cursor、Codex、Gemini、Copilot 等 AI 编码代理服务。它解决了代理在大型仓库中反复搜索、读取大量文件导致 token 消耗高、工具调用次数多的问题：提前把跨文件的符号、引用、路由关系建成图，代码变更时自动同步，代理通过 MCP 工具直接查询到「精准上下文」，而不是靠一次次 grep。安装只需一条命令，不依赖本机 Node.js，内置运行时，跨 Windows、macOS、Linux，数据 100% 留在本地。

- ✨ 预索引代码知识图谱，跨文件符号与引用关系开箱即查
- ✨ 代码变更自动同步索引，无需手动重建
- ✨ 通过 MCP 工具接入 Claude Code、Cursor、Codex、Gemini、Copilot 等十余种代理
- ✨ 框架感知的路由识别，能追踪 Web 框架的请求路径
- ✨ 支持 iOS、React Native、Expo 混合项目的跨语言桥接分析
- ✨ 完全本地运行，带 CLI（index/status/upgrade）与库调用接口
- 👥 适合谁：使用 AI 编码代理、维护中大型多语言仓库的开发者与团队

`TypeScript` · Fork 5,230 · 🔗 [官网](https://colbymchenry.github.io/codegraph/)


## 🚀 Show HN 今日新品

[Cornhole News – A Hacker News inspired site for news across the Midwest](https://news.ycombinator.com/item?id=50561515) · ⬆️ 237 · 💬 122

> 受 H

[Alloy CSS, dialogs, menus and tabs that work with JavaScript off](https://news.ycombinator.com/item?id=50532385) · ⬆️ 211 · 💬 40

> Alloy CSS 发布，提供无需 JavaScript 即可运行的对话框、菜单和标签页组件。


## 🧡 Product Hunt 今日榜

[Even G2 Enterprise SDK](https://www.producthunt.com/products/even-g2) · Product Hunt

> Even G2 企业级 SDK 发布，支持为 Even G2 智能眼镜开发定制业务应用。

[Adanotch](https://www.producthunt.com/products/adanotch) · Product Hunt

> Adanotch 为 MacBook 刘海带来实时动态岛功能。

[Viktor Code](https://www.producthunt.com/products/viktor) · Product Hunt

> Coding agents know your repo. Viktor knows your company.

[tday.com](https://www.producthunt.com/products/tday) · Product Hunt

> tday.com 让你向编码智能体索取任意功能的带旁白演示。

[Prates](https://www.producthunt.com/products/prates) · Product Hunt

> Prates 能学习你的写作习惯，然后完全按你的风格和口吻代写内容。


## 🇨🇳 中文独立开发 · V2EX 分享创造

[做了个 GTA 6 主线任务清单，查章节进度时少踩剧透](https://www.v2ex.com/t/1259516) · 💬 0 回复

> 开发者做了个 GTA 6 主线任务清单，方便玩家查章节进度时避开剧透。

[Deskbell：面向桌面零碎问题设计的轻量级 AI 浮窗助手](https://www.v2ex.com/t/1259514) · 💬 0 回复

> Deskbell 是一款轻量级 AI 浮窗助手，专门解决桌面上的零碎问题。

[结合自身的婚恋经历 vibe coding 了一个小网站 超级想恋爱·在线](https://www.v2ex.com/t/1259511) · 💬 2 回复

> 开发者结合自身婚恋经历，用 vibe coding 做了「超级想恋爱·在线」小网站。

[做了一个内容互助工具：奇伴批阅，给创作者找真实反馈](https://www.v2ex.com/t/1259509) · 💬 1 回复

> 开发者分享内容互助工具「奇伴批阅」，帮创作者获取真实反馈。

[做了个浏览器指纹收集工具 应该是全网最全的](https://www.v2ex.com/t/1259506) · 💬 1 回复

> 开发者做了一个号称全网最全的浏览器指纹收集工具。

## 📋 完整榜单

> ℹ️ 同一仓库 3 天内不会重复出现，往期出现过的不会重复收录

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | 装进 Claude Code 的漏洞赏金与外部红队技能包，83 个技能开箱即用 | `Python` | 20,470 | +2,029 |
| 2 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | Google Stitch 官方 Agent Skills 库：让编码 Agent 直接操… | `TypeScript` | 12,472 | +422 |
| 3 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | 把 PS5 可执行文件自动重链接为 Linux、Windows 原生程序的转换工具 | `C++` | 61,145 | +792 |
| 4 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 开源 AI 编码智能体，在终端里直接帮你写代码、查代码、跑命令。 | `TypeScript` | 228,879 | +263 |
| 5 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 微软出品的轻量 Python 工具，把各类文档转成适合 LLM 处理的 Markdown。 | `Python` | 198,159 | +246 |
| 6 | [Tencent/LoopForge](https://github.com/Tencent/LoopForge) | 自托管编码智能体交付平台，用 SOP 与人工审批把 AI 写代码变成团队可重复的流程。 | `Go` | 5,937 | +235 |
| 7 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | 无需训练即可改造本地大模型，去掉拒答、减少废话和谄媚。 | `Python` | 42,907 | +194 |
| 8 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 一款 Claude Code 学术研究技能包，覆盖从调研到定稿的完整论文流程。 | `Python` | 58,349 | +160 |
| 9 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | 把多账号管理、协议转换与请求调度装进一个桌面端的本地 AI 中转站。 | `Rust` | 33,858 | +149 |
| 10 | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 为 AI 编码代理预建代码知识图谱，减少 token 与工具调用，完全本地运行 | `TypeScript` | 78,562 | +123 |

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
| `top_n` | 每天推送的仓库数（默认 10，全部不在最近 `cooldown_days` 天出现过） |
| `cooldown_days` | 冷却天数：一个仓库出现后，N 天内不再重复出现（默认 3，即第 4 天起可再次上榜） |
| `top_n_fill.enabled` | 今日榜单可用仓库不足 `top_n` 时，是否从其他语言的 trending 页补满（默认开） |
| `top_n_fill.languages` | 补充来源：这些语言的 trending 页（默认 python / typescript / javascript / rust / go / c++ / java / c# / php / ruby / swift / kotlin） |
| `posts.enabled` | 是否开启独立创业板块（Show HN / Product Hunt / V2EX 分享创造，默认开） |
| `posts.show_hn.count` / `min_points` | Show HN 展示条数（默认 3）与最低分数过滤（默认 20） |
| `posts.product_hunt.count` | Product Hunt 今日榜条数（默认 5，来自官方 Atom feed） |
| `posts.v2ex.count` | V2EX「分享创造」节点条数（默认 5） |
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

**同一个仓库会重复出现吗？**
不会在短时间内重复。`data/repos.json`（随仓库提交）记录所有出现过的仓库和最近出现日期，冷却期默认为 3 天：一个仓库上榜后，接下来 3 天内不会再出现在日报里，第 4 天起可以再次上榜。每次运行先从今日 trending 榜单里挑不在冷却期内的仓库；不够 `top_n` 时，再从各语言 trending 页补充同样不在冷却期内的仓库（同样在 trending、但不在今日榜单）。AI 介绍缓存在缓存里，冷却结束后再次上榜可直接复用，不重复消耗。

**除了 Trending 还有哪些内容？**
日报还聚合了三个独立创业/一人公司渠道（`config.json` 的 `posts` 可调）：🚀 Show HN（Hacker News 的新品发布帖，按分数取 Top N）、🧡 Product Hunt 今日榜（官方 Atom feed）、🇨🇳 V2EX「分享创造」节点（中文独立开发者作品）。每条内容同样遵守 3 天冷却期，并用 AI 生成一句话中文摘要（缓存在 `data/posts.json`）；单个渠道抓取失败只跳过该栏目，不影响整封邮件。

## ⚠️ 免责声明

本项目与 GitHub 无关，仅用于学习和技术交流。请勿滥用 @ 提及功能。
