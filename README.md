# 🔥 GitHub Trending Daily · 每日热榜推送

[![daily-trending](https://github.com/OnClickListener2048/github-trending-daily/actions/workflows/daily-trending.yml/badge.svg)](https://github.com/OnClickListener2048/github-trending-daily/actions/workflows/daily-trending.yml)
![GitHub stars](https://img.shields.io/github/stars/OnClickListener2048/github-trending-daily)

每天自动抓取 [github.com/trending](https://github.com/trending) 的热门仓库，**给每一位 Star 过本仓库的人发一封邮件**，正文就是当天榜单 + 每个仓库的一句话简介。

## ✨ 怎么接收

1. **Star 本仓库** ⭐
2. 保持 GitHub 邮件通知开启（默认就是开的，不用动）
3. 完成。每天早上 08:30（北京时间）你会收到一封来自 GitHub 的邮件：🏆 今日精选详解（每个仓库"是什么 + 能干什么"，同一仓库 3 天内不会重复出现）+ 📋 完整榜单，并附精美 HTML 报告链接

> 原理：每天自动创建一个 Issue 并 @ 你的用户名，GitHub 会把提及通知默认发送到你的邮箱。不需要填邮箱、不需要注册，**Star 即订阅**。全程使用 GitHub 官方机制，不收集任何个人信息。

## 🧭 今日榜单

<!-- TRENDING:START -->

# 🔥 GitHub 每日 Trending · 2026-11-12

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 10 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 今日精选（详细介绍）

### 1. [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) — ⭐ 2,020（今日 +159）

> 一套为编码智能体注入现代 Web 平台知识与最佳实践的技能库源仓库。

Modern Web Guidance 是一组「技能」，把 Web 平台专业知识、最佳实践和浏览器兼容数据直接嵌入你的编码智能体，让编码智能体不再默认沿用训练数据里堆积的旧写法，转而使用平台原生、高性能的方案。这个仓库是它的源仓库，包含编写、校准与评估这些指南的代码和文档。使用起来很简单：运行 npx modern-web-guidance@latest install 走一遍交互式向导即可安装；不安装也能直接用 search 搜索指南、用 retrieve 按 ID 取回指南、用 legacy-scan 扫描代码库中的遗留模式。项目由 Chrome、Edge、Firefox 和 MDN 团队与 Web 开发社区共同维护。

- ✨ 一条 npx 命令启动交互式安装向导，把指南接入编码智能体
- ✨ search 命令用自然语言检索相关指南（如动画化对话框遮罩）
- ✨ retrieve 命令按 ID 取回完整指南，直接放进智能体的上下文窗口
- ✨ legacy-scan 扫描现有代码库，找出需要现代化的遗留写法
- ✨ 覆盖 250+ 现代 Web 特性，分为用户体验、CSS 布局、性能、表单与 UI、无障碍、内置 AI 六大方向
- ✨ 指南刻意做成 token 高效，并用评估仪表盘跑 evals 剔除模型已掌握的冗余内容
- 👥 适合谁：使用 AI 编码助手的前端/Web 开发者，以及想贡献或评估指南内容的社区作者。

`TypeScript` · Fork 151 · 🔗 [官网](https://goo.gle/modern-web-guidance)

### 2. [shadcn/improve](https://github.com/shadcn/improve) — ⭐ 11,180（今日 +361）

> 用最强模型审计代码库并写出可执行计划，再把实现交给便宜模型的 Agent 技能

improve 是一个 Agent 技能：用你最贵的模型去读懂代码库、判断什么值得改，并把结论写成 plans/ 目录里的自包含实施计划，执行交给便宜模型。它自己从不写实现——计划就是产品。安装只要一行 npx skills add shadcn/improve，任何支持 Agent Skills 格式的 agent 都能跑；产出的计划是纯 markdown，其他 agent 或人也能直接接手。

- ✨ 一条命令跑完整审计：/improve 先梳理仓库结构并审计，回来一张按影响、成本与置信度排序的发现表，你挑编号（比如“plan 1, 3 and 5”）再让它写计划
- ✨ 多种模式按需切换：quick 只看热点和头部问题，deep 逐包逐类穷举，security、perf、tests、bugs 等单类专注审计，branch 只审当前分支的改动，next 给出有仓库证据支撑的功能方向建议，plan 和 review-plan 则跳过审计直接写或收紧单份计划
- ✨ 九类并行子代理审计：正确性、安全、性能、测试覆盖、技术债、依赖与迁移、DX、文档、方向；每条发现都带 file:line 证据、影响、工作量和置信度，方向类建议必须引用仓库自身证据，不许泛泛而谈
- ✨ 审计后再复核：子代理容易多报，主模型会亲自重读每一处被引用的位置，删掉误报、修正归因，并把被否决的结论连同理由记录下来，避免下次重复出现
- ✨ 计划是为“最弱执行者”写的：上下文全部内联（精确路径、现状代码片段、仓库惯例与范例文件、已验证的命令），每步都配命令与预期输出的验证门，另有明确的越界清单和“若 X 则停下并汇报”的 STOP 条件，并戳上编写时的 commit 供执行前做漂移检查
- ✨ 闭环执行与维护：/improve execute 在隔离的 git worktree 里派发便宜执行者，然后像技术负责人一样重跑每个完成标准、检查范围合规、对照意图读 diff 并给结论（合不合由你定）；/improve reconcile 复核已落地项、刷新漂移的计划、解阻卡住的条目；加 --issues 还能把计划直接发成 GitHub issue
- 👥 适合谁：手里有真实代码库、想用强模型做审计与规划、把执行交给便宜模型的团队和个人开发者

Fork 453

### 3. [openai/codex-security](https://github.com/openai/codex-security) — ⭐ 11,942（今日 +52）

> OpenAI 官方出品的代码安全扫描工具，提供 CLI 和 TypeScript SDK，能发现、验证并修复漏洞。

Codex Security 是 OpenAI 推出的安全工作流工具，目标是帮开发者在自己的代码库里找出漏洞、查清影响范围并直接修复。它有三种用法：在 Codex 会话里让代理执行安全扫描，返回报告、源码证据和覆盖范围限制；在终端用 `cs` 命令行扫描仓库、指定路径或 Git 变更；在 CI 和自动化流程里通过 TypeScript SDK 或 GitHub Action 调用。扫描结果会保存为 Markdown 报告和 findings，可继续生成补丁、验证已有修复、评估严重程度并提出 owner 建议，还能把结果导出或同步到 Linear、Jira、GitHub。

- ✨ 扫描整个仓库、指定路径或 Git diff，Deep 模式会重复 Standard 扫描并返回去重后的发现
- ✨ 校验候选漏洞、生成补丁，并验证已有修复是否有效
- ✨ 起草 SECURITY.md 策略文档，保存威胁模型供后续评审
- ✨ 浏览历史扫描、识别重复项，按自定义标准评估严重程度，并依据源码和 Git 历史推荐负责人
- ✨ 导入第三方扫描器结果，发布到 Codex Security Cloud，或导出 SARIF、JSON、CSV
- ✨ 把 findings 同步到 Linear、Jira、GitHub，支持跨仓库批量扫描与可续跑的 CI、容器自动化
- 👥 适合谁：需要为代码库做安全审计的开发团队、安全工程师和 DevSecOps 人员。

`TypeScript` · Fork 952 · 🔗 [官网](https://developers.openai.com/codex/security)

### 4. [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java) — ⭐ 67,151（今日 +51）

> 用 Java 实现各类算法的开源学习仓库，面向教学而非生产性能。

这是一个把常见算法用 Java 逐一实现出来的开源仓库，目标是给学习者提供可读、可运行的参考代码，而不是替代 Java 标准库。你可以直接浏览 DIRECTORY.md 找到对应实现，也可以点开 Gitpod 在浏览器里一键运行和修改代码。想参与的话，先读贡献指南，再按目录补充或改进算法实现。

- ✨ 用 Java 实现算法，代码以教学可读性为先，并明确说明性能可能不及 Java 标准库
- ✨ 提供 Gitpod 一键在线开发环境，无需本地配置即可运行和修改算法
- ✨ DIRECTORY.md 汇总全部算法入口，方便按目录检索目标实现
- ✨ 配套贡献指南，说明参与补充算法和改进代码的流程
- ✨ 接入 CI 构建与 Codecov 覆盖率徽章，持续检查仓库代码状态
- ✨ 提供 Discord 社区入口，便于交流算法与贡献问题
- 👥 适合谁：Java 学习者、算法初学者、需要参考实现或想参与开源贡献的开发者。

`Java` · Fork 21,519

### 5. [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) — ⭐ 68,767（今日 +636）

> 本地代理把 12 种编码 agent 接到 61 家模型供应商，每月可用 13 亿+ 免费 token

Free Claude Code（FCC）是一个独立开源项目：它在本地启动一个代理，把 Claude Code、Codex、Pi、OpenCode、Cline、Aider 等 12 种编码 agent，连接到包括免费、付费、订阅和本地模型在内的 61 家供应商，官方称每月可用 13 亿以上免费 token。安装脚本一条命令完成，启动后在 Admin UI 里添加 API key、从下拉框选模型、点 Apply，就能继续用你熟悉的终端、IDE 或桌面客户端写代码，无需改动原有工作流。

- ✨ 12 种 harness 与 61 家供应商可自由组合，在 Claude Code 里还能把 Fable、Opus、Sonnet、Haiku 分别路由到不同模型
- ✨ 保留原生的流式输出、工具调用和交错思考，路由后不牺牲使用体验
- ✨ 终端、桌面应用（Codex App、Claude Desktop、DeepSeek Desktop）、VS Code 与 JetBrains 插件、Discord 与 Telegram 手机端，以及浏览器原生 Code 会话皆可接入
- ✨ Discord 与 Telegram 支持语音消息，可选本地 Whisper 或 NVIDIA NIM 转写
- ✨ 借助 RTK 与 Headroom 最高降低 90% token 消耗
- ✨ 面向供应商故障的可靠性设计：自动重试、可配置限流与并发、模型与供应商自动降级、多 API key 自动切换
- 👥 适合谁：想低成本用编码 agent 的个人开发者，以及需要多模型冗余、手机或浏览器远程接入的团队

`Python` · Fork 10,711

### 6. [experientiallabs/experiential](https://github.com/experientiallabs/experiential) — ⭐ 16,620（今日 +589）

> 开源 LLM 网关与路由器，用一个兼容 OpenAI 的接口接入托管、BYOK 与本地模型

Experiential 是面向 agent 工作流的开源网关与路由器。它把托管模型、自带密钥（BYOK）和本地模型统一放在一个 OpenAI 兼容 API 后面，让你按用户或 agent 限定可用模型、使用场景和花费上限；同时把生产流量沉淀成数据，用真实 trace 训练出专属的路由或模型。运行 pip install experiential 后执行 exp 启动本地网关，首次配置向导会选好 provider、模型、推理强度与预算，签发一次性 key，之后用 curl 或官方 SDK 直接调用；不想自建也可以用 platform.experientiallabs.ai 的托管网关，接口路径一致。

- ✨ 统一入口：一个兼容 OpenAI 的 API 同时调用托管模型、自带密钥和本地模型，托管平台还支持 Anthropic Messages 协议
- ✨ 权限与预算控制：按身份和 agent 限定可用模型、适用场景与花费上限，首次配置默认给出 50 美元的命令预算
- ✨ 从流量拟合路由：导入 OpenTelemetry trace 或官方公开数据集，exp build 会针对质量、速度和成本模拟并优化出项目专属路由器
- ✨ 训练自有模型：基于路由器收集的 trace，用 Tinker 微调一个你拥有的开源模型（exp optimize model）
- ✨ 内置编码 agent：exp code 提供终端交互界面，print、JSON、RPC 模式同样可用，直接复用本地或托管网关
- ✨ 流量采集：exp capture 在请求仍直连 OpenAI/Anthropic 的前提下，从 Codex 和 Claude Code 桌面端采集 trace（目前实验性，限 macOS）
- 👥 适合谁：需要在多模型间权衡成本与质量的 AI 平台团队、agent 开发者，以及想用自有流量训练专属模型的人

`Python` · Fork 300 · 🔗 [官网](https://experientiallabs.ai)

### 7. [xtool-org/xtool](https://github.com/xtool-org/xtool) — ⭐ 15,345（今日 +283）

> 在 Linux、Windows、macOS 上用 SwiftPM 构建和部署 iOS 应用的开源 Xcode 替代品。

xtool 用开放标准复刻了 Xcode 的核心能力，让没有 Mac 的开发者也能开发 iOS 应用。它能把 SwiftPM 包直接构建成 iOS App，完成签名与安装，并以编程方式对接 Apple Developer Services。使用时先用 setup、auth、sdk 配置环境，再用 new 创建项目、dev 构建运行，通过 devices/install/launch 等子命令操作真机。除 CLI 外，还可把 XKit 或 XToolSupport 作为 SwiftPM 依赖引入自己的项目，复用其设备通信与开发者服务能力。

- ✨ 把 SwiftPM 包直接构建成 iOS 应用
- ✨ 对 iOS 应用进行签名并安装到设备
- ✨ 以编程方式对接 Apple Developer Services
- ✨ 跨平台运行：Linux、WSL/Windows、macOS
- ✨ 提供 new、dev、devices、install、launch、uninstall 等完整 CLI 子命令
- ✨ 可作为 Swift Package 引入（XKit、XToolSupport），在自己的 App 中复用其能力
- 👥 适合谁：需要在非 macOS 环境开发 iOS 应用，或想把 iOS 构建、签名、装包流程脚本化、自动化的开发者。

`Swift` · Fork 911 · 🔗 [官网](https://xtool.sh)

### 8. [soxoj/maigret](https://github.com/soxoj/maigret) — ⭐ 40,432（今日 +260）

> Maigret 只需一个用户名，就能在近 6000 个网站上查找该用户名对应的账号，并汇总成一份完整的人物档案。

Maigret 是一个用 Python 编写的 OSINT（开源情报）工具，用于账号调查。你只要给它一个用户名，它就会在约 5900 个网站上逐一检查这个用户名是否已被注册，并从可以访问的页面和站点 API 中提取昵称、简介、头像、其他关联账号等信息，最终输出可下载的报告。它不需要任何 API key，默认扫描流量排名前 500 的站点，加上 -a 参数即可全量扫描，也可以用标签按类别或国家缩小范围。安装只需一条 pip 命令，命令行、Python 库、Web 界面和 Telegram 机器人等多种用法都支持。

- ✨ 覆盖 5900 个站点，默认检查前 500 个，支持用 -a 全量扫描、用 --tags 按类别和国家筛选
- ✨ 能从个人主页和站点 API 抓取账号资料，并提取指向其他账号的链接
- ✨ 利用发现的用户名和其他 ID 进行递归搜索，继续扩大线索
- ✨ 可嵌入 Python 项目，直接 import maigret 以编程方式调用
- ✨ 能检测并部分绕过封锁、审查和 CAPTCHA，支持 Tor 与 I2P 站点及域名查询
- ✨ 提供 Web 界面，以关系图展示结果并下载报告；每次运行自动更新站点库，离线时回退到内置数据库
- 👥 适合谁：适合 OSINT 研究者、安全与取证人员、记者、招聘或风控人员，以及调查网络账号归属的开发者。

`Python` · Fork 3,246 · 🔗 [官网](https://maigret.app/gh)

### 9. [multica-ai/multica](https://github.com/multica-ai/multica) — ⭐ 55,798（今日 +200）

> 把 AI 编码 agent 当队友派活的开源自托管工作区，工作进度全程留在看板上

Multica 是一个可自托管的协作工作区，用来解决「同时开了好几个 agent 终端标签、每个都要重新解释上下文、还要全程盯着」的问题。它把你已经在用的编码 agent（Claude Code、Codex、Cursor、Copilot、Kimi、OpenCode 等）变成看板上的正式成员：给 agent 起名、指定 provider 和 runtime 后，就能像给同事派活一样把 issue 指派给它。agent 自己领取任务、在你自己机器或云主机上的 daemon runtime 里执行、边跑边评论、遇到阻塞会抛出来，最后交回给人类 review。意图、执行过程、决策和 diff 都挂在同一个 issue 上，没人需要重建上下文，也没有东西能在人类点头前上线。

- ✨ Agent 即队友：给每个 agent 起名字、绑定 provider 和 runtime，它会像普通成员一样出现在看板上并被指派 issue
- ✨ 兼容现有 agent CLI：Claude Code、Codex、Cursor、Copilot、Kimi、OpenCode 等直接用，不锁定厂商
- ✨ 自托管 runtime：agent 的「工位」是你笔记本或云主机上的 daemon，代码不离开你的机器
- ✨ 执行日志与实时干预：每次工具调用、命令和报错都带时间戳可回放，运行中回复消息会落进当前 run 而不是下一个
- ✨ Squads 与 Skills：人和 agent 混编成队由 leader 分派任务，把解决过的问题沉淀成所有 agent 可复用的 playbook
- ✨ Autopilots、Chat 与 Projects：用 cron 跑站会、审计和报告，直接向工作区提问或不起单就开始干活，并给项目挂上仓库和文档作为上下文
- 👥 适合谁：已经同时使用多个编码 agent、想要可审计可自托管的团队与独立开发者

`Go` · Fork 7,369 · 🔗 [官网](https://multica.ai)

### 10. [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) — ⭐ 24,514（今日 +198）

> 一个可自托管的免费影视聚合搜索与观看平台，部署只需一分钟。

LibreTV 是一个自托管的在线影视聚合搜索与播放站：你把它部署到自己的服务器上，填写采集站地址，它就能帮你跨多个资源站并行搜索影片，并把结果整理成可以直接播放的页面。它解决的核心痛点是——免费影视资源分散在大量采集站里，手动一个个找片很麻烦，而且播放器体验差、广告多、不能续播。LibreTV 用服务端并行搜索把多个源的结果合并，同名影片合成一张卡片让你比价挑源，再用 ArtPlayer + hls.js 提供过滤广告分片、自动跳过片头片尾、倍速、自动连播的播放体验。部署上支持 Docker 一条命令起站、预构建包免 Docker 运行，也可以源码手动构建，只需设置一个访问密码即可使用。

- ✨ 聚合搜索：多个采集站服务端并行搜索，同名影片跨源合并成一张卡片，展开后可对比并选择来源
- ✨ HLS 播放器：ArtPlayer + hls.js，支持广告分片过滤、片头/中段/片尾标记与自动跳过、自动连播、倍速、快捷键、移动端长按 3 倍速
- ✨ 直播 / IPTV：解析 M3U 订阅，在 /live 页面按分组浏览、搜索频道并站内播放（HLS + HTTP-FLV），支持 XMLTV 节目单和频道收藏
- ✨ 换源测速与续播：跨源搜索同名资源并测速排序，一键切换且保留集数位置；播放进度与历史存入本机 IndexedDB，精确到秒续播
- ✨ 源测试与订阅：一键探活点播源和直播源，记录各源健康度，连续失败的源按 30 分钟→24 小时→长期阶梯自动停用并可一键恢复；支持订阅远程源列表与 TVBOX 配置，可导出分享
- ✨ 首页推荐与 PWA：可选豆瓣分类浏览、Bangumi 新番放送表或影视榜单作为首页推荐，服务端直连加缓存、免 key 免配置；支持安装到桌面与亮暗双主题
- 👥 适合谁：想自建私人影视站、有点服务器或 Docker 基础的个人用户和小团队。

`TypeScript` · Fork 31,148 · 🔗 [官网](https://libretv.is-an.org)

## 📋 完整榜单

> ℹ️ 同一仓库 3 天内不会重复出现，往期出现过的不会重复收录

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src) | 一套为编码智能体注入现代 Web 平台知识与最佳实践的技能库源仓库。 | `TypeScript` | 2,020 | +159 |
| 2 | [shadcn/improve](https://github.com/shadcn/improve) | 用最强模型审计代码库并写出可执行计划，再把实现交给便宜模型的 Agent 技能 | — | 11,180 | +361 |
| 3 | [openai/codex-security](https://github.com/openai/codex-security) | OpenAI 官方出品的代码安全扫描工具，提供 CLI 和 TypeScript SDK，… | `TypeScript` | 11,942 | +52 |
| 4 | [TheAlgorithms/Java](https://github.com/TheAlgorithms/Java) | 用 Java 实现各类算法的开源学习仓库，面向教学而非生产性能。 | `Java` | 67,151 | +51 |
| 5 | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | 本地代理把 12 种编码 agent 接到 61 家模型供应商，每月可用 13 亿+ 免费… | `Python` | 68,767 | +636 |
| 6 | [experientiallabs/experiential](https://github.com/experientiallabs/experiential) | 开源 LLM 网关与路由器，用一个兼容 OpenAI 的接口接入托管、BYOK 与本地模型 | `Python` | 16,620 | +589 |
| 7 | [xtool-org/xtool](https://github.com/xtool-org/xtool) | 在 Linux、Windows、macOS 上用 SwiftPM 构建和部署 iOS 应用… | `Swift` | 15,345 | +283 |
| 8 | [soxoj/maigret](https://github.com/soxoj/maigret) | Maigret 只需一个用户名，就能在近 6000 个网站上查找该用户名对应的账号，并汇总… | `Python` | 40,432 | +260 |
| 9 | [multica-ai/multica](https://github.com/multica-ai/multica) | 把 AI 编码 agent 当队友派活的开源自托管工作区，工作进度全程留在看板上 | `Go` | 55,798 | +200 |
| 10 | [LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV) | 一个可自托管的免费影视聚合搜索与观看平台，部署只需一分钟。 | `TypeScript` | 24,514 | +198 |

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

## ⚠️ 免责声明

本项目与 GitHub 无关，仅用于学习和技术交流。请勿滥用 @ 提及功能。
