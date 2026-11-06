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

# 🔥 GitHub 每日 Trending · 2026-11-06

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 15 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 TOP 10（详细介绍）

### 1. [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) — ⭐ 7,883（今日 +2,679）

> NVIDIA 开源的企业本体框架，为 LLM 与 Agent 构建语义化上下文层

Auto Ontology 是 NVIDIA 开源的 Python 框架（Apache 2.0），从企业元数据中构建语义化、图谱化的上下文层。Agent 能查数据库、能检索文档，却常常答错数字，因此可靠性才是关键。它告诉 Agent 数据存在哪里、代表什么含义、该不该用、怎么用、来自哪里，并跨系统统一对指标与实体的定义。开发者可通过 MCP、CLI 或 API 把这份上下文接入任意 Agent 框架，也可用 Docker Compose 或 Helm 一键起服务，配置 NVIDIA NIM 的 API Key 后，就能对 Wide World Importers 样例库做自然语言提问。

- ✨ 从企业元数据自动生成本体，也可接入已有本体与语义模型，构建 AI 就绪的知识图谱
- ✨ 为指标、实体和关系提供可信的业务含义，并跨系统对齐不一致的定义
- ✨ 用已认证的定义与数据血缘校验生成的查询，每个答案都附带来源溯源
- ✨ 通过 MCP、CLI 和 API 把上下文暴露给任意 Agent 框架
- ✨ 自然语言转 SQL 并直接执行，推理、嵌入、重排序均由 NVIDIA NIM 端点提供，可用托管服务或自托管
- ✨ 把人工认证的修正与使用反馈回写本体，让共享上下文随每次提问持续改进
- 👥 适合谁：适合做 Agent 分析应用的数据平台与 AI 工程师，以及需要可靠 NL-to-SQL 的团队

`Python` · Fork 634

### 2. [mattpocock/skills](https://github.com/mattpocock/skills) — ⭐ 315,729（今日 +2,071）

> Matt Pocock 日常使用的 AI 编程 agent 技能集，小巧、可组合、可改造。

这是 Matt Pocock 从其 .agents 目录公开的一套 agent 技能（skills），用于配合 Claude Code、Codex、GitHub Copilot、Gemini CLI、Cursor 等编程 agent 做“真正的工程”，而不是 vibe coding。它针对 GSD、BMAD、Spec-Kit 这类框架的痛点：这些框架接管流程的同时也拿走了开发者的控制权，流程一旦出 bug 就很难排查。这些技能刻意做小、可组合，并配一次性 /setup-matt-pocock-skills 初始化（选择 issue tracker、triage 标签、文档存放位置）。安装方式按 agent 分多种：插件会自动更新，skills.sh 则复制可编辑文件、需手动更新。

- ✨ /grill-me 与 /grill-with-docs：开工前让 agent 反过来详细盘问你，先把需求对齐再动手，是作者最受欢迎的技能
- ✨ 共享语言/术语表机制：为项目建立一份词汇表，让 agent 不用 20 个词表达 1 个词能说清的事，减少啰嗦输出
- ✨ /triage 配合你在 setup 时指定的标签，对工单进行分类整理
- ✨ /setup-matt-pocock-skills 一次性初始化：选 issue tracker（GitHub、GitLab、本地文件或自定义）、配置标签、指定文档保存位置
- ✨ 技能小巧、可组合、与模型无关，鼓励改造成自己的版本
- ✨ 覆盖 Claude Code、Codex、GitHub Copilot（CLI 与 VS Code）、Gemini CLI，以及通过 npx skills 支持 Cursor、opencode、devin、windsurf、amp、pi 等
- 👥 适合谁：用 AI 编程 agent 开发真实项目、希望保留流程控制权的工程师

`Shell` · Fork 26,424 · 🔗 [官网](https://aihero.dev/skills)

### 3. [garrytan/gstack](https://github.com/garrytan/gstack) — ⭐ 140,160（今日 +612）

> 把 Claude Code 变成一支虚拟工程团队：CEO、设计、工程经理、QA、发布各自出场的 23 个斜杠命令。

gstack 是 YC 总裁 Garry Tan 开源的 Claude Code 配置集，全部由 Markdown 斜杠命令组成，MIT 协议免费使用。它解决的问题很具体：直接用 AI 写代码时，提示词空白、缺少角色分工，AI 产出的设计千篇一律，代码能通过 CI 却会在生产环境出问题。gstack 给编码 Agent 装上固定角色——CEO 重新思考产品、工程经理确定架构、设计师挑出 AI 生成的俗套设计、审查者找生产 bug、QA 开真实浏览器复现问题、安全官跑 OWASP + STRIDE 审计、发布工程师提交 PR。安装只需两条粘贴命令，约 30 秒；推荐开启团队模式，团队成员共用同一版本并自动更新。

- ✨ /office-hours：挑战你对产品的最初定义，产出一份供其他 skill 读取的设计文档
- ✨ /review：审查任意分支改动，找出能过 CI 却在生产环境出问题的 bug，并直接修掉显而易见的问题
- ✨ /qa：对 staging URL 或本地 API、CLI、定时任务、webhook 打开真实浏览器，复现并修复 bug
- ✨ /autoplan 与 /ship：端到端评审整份计划，然后跑测试、review 并提交 PR，覆盖完整 sprint
- ✨ /cso 安全官：执行 OWASP + STRIDE 审计，需要原生工具链，缺失时 setup 会明确提示并禁用
- ✨ 团队模式：仓库内一条命令完成引导，无 vendored 文件、无版本漂移，每小时静默检查更新，跟随稳定版通道
- 👥 适合谁：想继续亲手交付的技术型创始人、CEO，第一次用 Claude Code 需要结构化角色的人，以及要在每个 PR 上做严格评审、QA 与发布自动化的 tech lead 和 staff 工程师。

`TypeScript` · Fork 20,707

### 4. [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) — ⭐ 17,932（今日 +240）

> 基于 Playwright 和 AI 的闲鱼多任务实时监控系统，自带完整 Web 管理后台，从海量商品中筛出心仪好物。

这是一个用 Python 写的闲鱼商品监控工具。你在 Web 界面里建任务，设定关键词、价格区间、包邮、发布时间、省市区域等筛选条件，系统用 Playwright 自动搜索闲鱼，把新出现的商品详情和卖家信息抓下来，交给多模态 AI 模型按你写的标准判断值不值得买，推荐的就通过 ntfy.sh、企业微信、Bark、Telegram、Webhook 推给你。支持多任务并发、Cron 定时调度、多账号绑定和代理轮换，遇到风控会自动换号重试。Docker 一键部署，镜像内置 Chromium，开箱即用。

- ✨ Web 可视化管理：任务管理、账号管理、AI 标准编辑、运行日志、结果浏览一站式操作
- ✨ AI 驱动：用自然语言描述需求即可异步生成分析标准，再由多模态模型深度分析商品图文
- ✨ 多任务并发：每个任务独立配置关键词、价格、筛选条件和 AI Prompt
- ✨ 高级筛选：包邮、新发布时间范围、省/市/区三级区域筛选
- ✨ 多渠道即时通知：ntfy.sh、企业微信、Bark、Telegram、Webhook
- ✨ Cron 定时调度、多账号绑定与代理池轮换，风控失败自动重试并带任务熔断保护
- 👥 适合谁：想蹲守闲鱼捡漏、盯特定商品的买家，以及需要长期监控商品行情的开发者和小团队。

`Python` · Fork 2,973

### 5. [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) — ⭐ 98,337（今日 +1,655）

> Scrapling 是一个 Python 爬虫框架，把请求、浏览器渲染、解析与并发爬取合为一体。

Scrapling 想做的是把网页抓取的整条链路收进一个库：用普通 HTTP 请求拿静态页面，用具备反检测能力的浏览器渲染 JavaScript、和页面交互，还能顺带抓取页面背后 API 调用返回的数据。它解决的是开发者平时要在 requests、Playwright、解析库、爬虫调度之间来回拼装的问题——现在用同一套 API 就能从单次请求扩展到整站爬取，支持可复用会话、代理轮换、自动重试、暂停与恢复，以及内置的数据导出。除了 Python 代码，它也能从命令行运行，或通过 MCP server 和 Agent Skill 交给 AI agent 调用，甚至把整站内容整理成干净的 Markdown。

- ✨ 统一抓取入口：支持静态 HTTP 请求与可渲染 JavaScript、可交互的隐身浏览器
- ✨ 强大的选择器解析能力，从页面中精准提取所需字段
- ✨ 并发爬虫（Spiders）：可复用会话、代理轮换、自动重试、暂停与恢复
- ✨ 内置数据导出，便于把抓取结果整理成可用格式
- ✨ 同时提供 CLI 命令行与 Python API 两种使用方式
- ✨ 提供 MCP server 与 Agent Skill，可直接接入 AI agent 工作流
- 👥 适合谁：需要从单页提取到整站采集的 Python 开发者、数据工程师，以及想把抓取能力交给 AI agent 使用的团队。

`Python` · Fork 10,299 · 🔗 [官网](https://scrapling.readthedocs.io/en/latest/)

### 6. [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — ⭐ 17,334（今日 +2,173）

> 通过操作系统无障碍树让 AI Agent 看见并操作桌面应用的 CLI 与 C 库。

agent-desktop 是 Vercel Labs 出品的桌面自动化工具，它让 AI Agent 具备 computer use 能力，但完全不用截图和像素匹配。它把应用的 accessibility tree 读成 JSON，并为每个可操作元素分配一个 ref；Agent 点击或输入某个 ref，再重新观察界面确认结果，如此循环。整个控制循环由调用方自己实现，工具本身不含模型。它同时提供 CLI 和 C 库，覆盖 macOS、Windows、Linux 三大平台，默认以 headless 方式驱动，不移动鼠标也不抢焦点。

- ✨ 把桌面应用的无障碍树解析为 JSON 快照，每个可交互元素带唯一 ref
- ✨ 支持 click、type、set-value、clipboard 等基于 ref 的操作，无需坐标与像素匹配
- ✨ 快照与 ref 强绑定，界面变化返回 STALE_REF / AMBIGUOUS_TARGET 促使重新观察验证
- ✨ 默认 headless 操作，不移动指针不抢焦点；加 --headed 才使用物理输入
- ✨ 跨平台：macOS 走 AX API、Windows 走 UI Automation、Linux 走 AT-SPI
- ✨ 内置与版本匹配的 skills 指南和 --help，方便 Agent 自行学习用法
- 👥 适合谁：构建桌面端 computer use Agent 的开发者，以及需要脚本化操作桌面应用的团队。

`Rust` · Fork 1,234 · 🔗 [官网](https://agent-browser.dev/desktop)

### 7. [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) — ⭐ 11,648（今日 +546）

> 面向并行 AI agent 工作流的 Git worktree 管理 CLI，让 worktree 像分支一样易用

Worktrunk 是一个用 Rust 写的 Git worktree 命令行工具。现在 Claude Code、Codex 这类 AI agent 能长时间无人值守地跑任务，开发者经常要同时管理 5 到 10 个以上的任务；git 原生 worktree 可以让每个 agent 拥有独立的工作目录，避免互相干扰，但用起来很麻烦，光是新建一个 worktree 就要把分支名重复输入三次，还得手动 cd 过去。Worktrunk 改用分支名来定位 worktree，路径由可配置的模板自动计算，并用 wt switch、wt remove、wt list 三条核心命令覆盖切换、创建、清理和状态查看，创建时还能顺带执行命令，直接启动 Claude。

- ✨ wt switch：按分支名切换 worktree，路径根据可配置模板自动计算，也接受 worktree 的实际路径
- ✨ wt switch -c -x claude：一条命令完成创建 worktree、新建分支并直接拉起 AI agent，替代 git 的三步操作
- ✨ wt remove：删除 worktree 的同时一并清理对应分支，无需先 cd 回主仓库再执行 git worktree remove
- ✨ wt list：列出所有 worktree 及其状态，而原生 git worktree list 只给出路径
- ✨ Hooks：在创建、移除等生命周期节点自动执行命令，把本地工作流自动化
- ✨ 写时复制（copy-on-write）构建缓存，让多个并行工作副本共享同一份构建产物，降低磁盘与重建开销
- 👥 适合谁：需要同时跑多个 Claude Code、Codex 等 AI agent 的开发者，以及频繁在多个分支间切换的 Git 用户

`Rust` · Fork 445 · 🔗 [官网](https://worktrunk.dev)

### 8. [lz4/lz4](https://github.com/lz4/lz4) — ⭐ 12,466（今日 +23）

> 极速无损压缩算法库，单核压缩超 500 MB/s，解压可达数 GB/s，接近内存带宽上限。

LZ4 是一个用 C 写的无损压缩算法及其参考实现，核心卖点是「快到几乎不构成瓶颈」：单核压缩速度 500 MB/s 以上，解压可达数 GB/s，多核下常常直接撞上内存带宽。它适合那些压缩率不是第一诉求、但对延迟和吞吐极其敏感的场景——比如缓存、日志、网络传输、列存和游戏资源。用起来也很直接：`make && make install` 就能装上库和 `lz4` 命令行工具，也可以通过 CMake、Meson、Visual Studio 构建，或用 vcpkg 及各大发行版的包管理器安装。库采用 BSD 2-Clause 许可，命令行工具则是 GPL-2.0-or-later，商用集成时需要注意这个区别。

- ✨ 极致速度：单核压缩 >500 MB/s、解压数 GB/s，多核可线性扩展，官方基准中解压速度远超 Snappy、zlib、Zstandard 同级别配置
- ✨ 动态可调的 acceleration 因子：可以按需在压缩率和速度之间滑块式调节，同一份数据按场景选择快一点还是小一点
- ✨ 附带高压缩版本 LZ4_HC：用更多 CPU 时间换取更高压缩率，但解压速度与普通版本完全一致，读多写少的场景可以放心用
- ✨ 字典压缩支持：API 和命令行（-D）都能把任意文件当字典（只取末尾 64 KB），还能配合 Zstandard 的字典构建器显著提升小文件的压缩效果
- ✨ 格式规范清晰且有文档：block 格式和 frame 格式都有独立文档，多块组成帧以支持任意长度的流式数据，保证不同实现之间可互操作
- ✨ 生态完善：除 C 参考实现外还有 Java、C#、Python、Perl、Ruby 等多语言移植版本，构建系统覆盖 Make、CMake、Meson、VS 和 vcpkg
- 👥 适合谁：适合对吞吐和延迟敏感的开发者：缓存/存储、日志管道、网络协议、数据库、游戏与嵌入式等场景。

`C` · Fork 1,639 · 🔗 [官网](http://www.lz4.org)

### 9. [google/skills](https://github.com/google/skills) — ⭐ 22,520（今日 +211）

> Google 官方 Agent Skills 合集，让 AI 编程助手学会用 Google 云与 AI 产品干活。

这是 Google 官方维护的 Agent Skills 仓库，把 Google Cloud、Gemini、Genkit、BigQuery 等产品的使用知识封装成 AI Agent 可以直接加载的技能包。它解决的问题很实际：AI 助手虽然会写代码，但不懂你的云上具体怎么配 IAM、怎么搭 RAG、怎么调 GKE 上的推理服务。安装只需一条 npx skills add google/skills，按提示选择技能、目标 Agent 和安装范围（项目级或全局），之后用 npx skills update 即可更新并清理废弃技能。

- ✨ 一条命令 npx skills add google/skills 安装，可挑选单个技能或全量安装，并指定目标 Agent 与项目级/全局作用域
- ✨ 覆盖 Google Cloud 入门三件套：IAM 认证授权、Onboarding、Foundation Builder 基础搭建
- ✨ 多产品方案级技能：方案架构工作流、多 Agent 安全网关、RAG 企业搜索、AlloyDB 混合检索、无边界数据湖仓、n 层无服务器 Web 应用等
- ✨ AI/ML 技能矩阵：Agent Platform 的模型部署、微调、Prompt 管理、RAG Engine、评测飞轮、故障排查，以及 Gemini API / Live API / Interactions API
- ✨ Genkit 四语言开发技能：Dart、Go、JS、Python 各一份，按技术栈对号入座
- ✨ 基础设施技能：Cloud Storage 基础/桶架构/诊断/FUSE、Compute Engine 预留实例、网络洞察、Application Design Center 设计部署，以及 GKE TPU 挂起与性能退化排障
- 👥 适合谁：使用 AI 编程助手开发、且工作涉及 Google Cloud、Gemini 或 Genkit 的开发者与架构师。

`Python` · Fork 1,897

### 10. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) — ⭐ 46,093（今日 +150）

> 给 AI Agent 用的浏览器自动化 CLI，用一条条 shell 命令驱动浏览器。

agent-browser 是一个 Rust 编写的原生命令行工具，让 AI Agent 像人一样操作浏览器：open 打开页面，snapshot 把页面压成带 @e1 这类 ref 的紧凑文本，Agent 按 ref 点击、填表，再重新快照确认结果，如此循环。浏览器在命令之间保持开启，每步只是一次短小的 shell 调用。它解决的是让 Agent 用文本而非截图理解页面、并稳定定位元素的问题：点击目标若被遮挡、禁用或不可见会直接报错而不是假成功。全局安装 npm 包后跑一次 agent-browser install 下载 Chrome for Testing 即可上手。

- ✨ snapshot 把页面转成带 ref（如 @e1）的紧凑可访问性树文本，Agent 可直接引用操作
- ✨ click、fill、type、press、hover、select、check、scroll、drag、upload 等完整交互命令
- ✨ 支持 CSS 选择器、文本、XPath 和语义定位，例如按 role 和 name 查找按钮
- ✨ 后台 daemon 常驻，浏览器在命令间不关闭，每个 --session 独立拥有自己的 daemon 和浏览器
- ✨ 内置与 CLI 版本匹配的 skills（agent-browser skills get core），让 Agent 指令始终对得上当前版本
- ✨ 可切换 Chrome for Testing、连接的 Chrome（--cdp/--auto-connect）、Lightpanda、Obscura、iOS 模拟器 Safari 及多家云浏览器
- 👥 适合谁：构建浏览器自动化 Agent 的开发者，尤其是用 shell 或 MCP 驱动 Agent 的团队。

`Rust` · Fork 3,155 · 🔗 [官网](https://agent-browser.dev)

## 📋 完整榜单

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | NVIDIA 开源的企业本体框架，为 LLM 与 Agent 构建语义化上下文层 | `Python` | 7,883 | +2,679 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Matt Pocock 日常使用的 AI 编程 agent 技能集，小巧、可组合、可改造。 | `Shell` | 315,729 | +2,071 |
| 3 | [garrytan/gstack](https://github.com/garrytan/gstack) | 把 Claude Code 变成一支虚拟工程团队：CEO、设计、工程经理、QA、发布各自出… | `TypeScript` | 140,160 | +612 |
| 4 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | 基于 Playwright 和 AI 的闲鱼多任务实时监控系统，自带完整 Web 管理后台… | `Python` | 17,932 | +240 |
| 5 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | Scrapling 是一个 Python 爬虫框架，把请求、浏览器渲染、解析与并发爬取合为… | `Python` | 98,337 | +1,655 |
| 6 | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 通过操作系统无障碍树让 AI Agent 看见并操作桌面应用的 CLI 与 C 库。 | `Rust` | 17,334 | +2,173 |
| 7 | [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | 面向并行 AI agent 工作流的 Git worktree 管理 CLI，让 work… | `Rust` | 11,648 | +546 |
| 8 | [lz4/lz4](https://github.com/lz4/lz4) | 极速无损压缩算法库，单核压缩超 500 MB/s，解压可达数 GB/s，接近内存带宽上限。 | `C` | 12,466 | +23 |
| 9 | [google/skills](https://github.com/google/skills) | Google 官方 Agent Skills 合集，让 AI 编程助手学会用 Google… | `Python` | 22,520 | +211 |
| 10 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 给 AI Agent 用的浏览器自动化 CLI，用一条条 shell 命令驱动浏览器。 | `Rust` | 46,093 | +150 |
| 11 | [scenario-labs/skills](https://github.com/scenario-labs/skills) | 让 AI 编程代理通过 Scenario MCP 产出可交付的图像、视频、3D 和音频素材… | `Python` | 3,244 | +667 |
| 12 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | 一套开箱即用的 Agent Skills 合集，让 AI 编程助手获得设计、视频、图像与知… | `JavaScript` | 14,329 | +175 |
| 13 | [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | 微软开源的前沿语音 AI 模型家族，覆盖长音频语音识别与实时语音合成。 | `Python` | 56,232 | +223 |
| 14 | [floci-io/floci](https://github.com/floci-io/floci) | 免费开源的本地 AWS 模拟器，一条 docker compose up 即可跑起全套云服… | `Java` | 30,608 | +779 |
| 15 | [JiaFeiMiao-K-Cat/DiscImageStudio](https://github.com/JiaFeiMiao-K-Cat/DiscImageStudio) | 把图片转成光盘物理层数据，刻录后在 CD / DVD / BD 盘面显出肉眼可见图案的工具 | `C#` | 7,465 | +984 |

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
| `top_n` | 详细介绍的仓库数（默认 10，按 GitHub 页面原始顺序取前 N 个） |
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
