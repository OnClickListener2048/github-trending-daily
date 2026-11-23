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

# 🔥 GitHub 每日 Trending · 2026-11-23

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 10 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 今日精选（详细介绍）

### 1. [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) — ⭐ 63,043（今日 +699）

> 为任意软件生成 CLI 封装，让 AI Agent 直接调用它，成为原生工具。

CLI-Anything 是一个把现有软件变成 Agent 原生工具的项目：跑一条命令，就为某个软件或服务生成一套结构化的命令行接口（CLI harness）；Cursor、Claude Code、OpenClaw、Pi、nanobot 这类 Agent 都能直接调用它，不必再依赖 GUI 或非结构化接口。它要解决的是「今天的软件给人用，明天的用户是 Agent」这个断层。用法上分两条线：一是用 pip install cli-anything-hub 安装 CLI-Hub，再用 cli-hub install <name> 浏览、安装和管理社区构建的 CLI；二是自己按 CONTRIBUTING 提交一个 harness，PR 合并后立刻出现在 Hub 上。生成出来的命令既输出 JSON，供程序解析，也输出人类可读文本，方便调试。

- ✨ 一条命令行即可让任意软件变成 agent-ready，兼容 Pi、OpenClaw、nanobot、Cursor、Claude Code 等 Agent 宿主
- ✨ CLI-Hub 社区注册中心：pip install cli-anything-hub 后用 cli-hub install <name> 一键浏览、安装、管理所有社区 CLI，合并 PR 后即时上架
- ✨ 每条命令同时提供 JSON 结构化输出和人类可读输出，Agent 解析与人工排查两不误
- ✨ 配套 preview、live preview 和 trajectory loop 机制，Agent 能反复试跑并产出真实产物：CAD 构建、3D 场景、图表、游戏玩法、字幕等，官方 Demos 覆盖 18 个应用
- ✨ 覆盖真实软件生态的现成 CLI：ArcGIS Pro 制图与地理处理、Calibre 书库、搜索、元数据、转换和导出、Joplin 笔记与同步、Obsidian 持久记忆、Sketch、Rekordbox 等
- ✨ 贡献与需求双向通道：通过 wishlist 模板请求想要支持的软件，通过 contributor signup 认领 harness，并在 2,461 项通过的单元与 e2e 测试基线上做质量把关
- 👥 适合谁：想让自家软件被 Agent 调用，或用 Agent 自动化各类桌面与专业软件的开发者。

`Python` · Fork 5,733 · 🔗 [官网](https://clianything.cc/)

### 2. [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) — ⭐ 207,305（今日 +915）

> 把任意网页和文档转成 LLM 可用的干净数据，并提供搜索、抓取、交互和 550+ 数据源的一站式知识基础设施。

Firecrawl 是一个面向 AI 应用和智能体的网页数据层：你给它一个 URL 或者一句搜索词，它返回干净的 Markdown、结构化 JSON 或截图，省掉代理轮换、JS 渲染、限流这些脏活。README 强调它覆盖 96% 的网页（包括重 JS 的站点），P95 延迟约 3.4 秒，输出对 LLM 友好，能少烧 token。除了单页抓取，它还支持整站爬取、URL 发现、批量异步抓取、内容变更监控，以及用 Actions 先点击、滚动、输入再抽取，甚至用 AI 提示词在页面上继续操作。既可以开源自托管，也可以直接用托管服务，Python、Node、cURL、CLI 都提供一行调用的入口。

- ✨ Search：搜索网页并直接返回结果页的完整内容（markdown），省去二次抓取
- ✨ Scrape：把任意 URL 转成 Markdown、HTML、截图或结构化 JSON，自带代理、JS 渲染和限流处理
- ✨ Interact：先抓页面再用 AI 提示词或代码与页面交互，Actions 支持点击、滚动、输入、等待、按键
- ✨ Crawl 与 Map：一次请求爬完整站所有 URL，或快速发现站点全部链接
- ✨ Batch Scrape 与 Monitor：异步批量抓取上千 URL，并在网页内容变化时收到通知
- ✨ Parse 与 Alexandria：把 PDF、DOCX 等文档解析成 Markdown/JSON，并通过 Firecrawl Cloud 接入 550+ 数据提供商
- 👥 适合谁：适合做 AI Agent、RAG、知识库和数据采集的开发者与团队，需要稳定网页数据的后端与全栈工程师。

`TypeScript` · Fork 10,836 · 🔗 [官网](https://firecrawl.dev)

### 3. [nginx/nginx](https://github.com/nginx/nginx) — ⭐ 32,938（今日 +163）

> 官方 NGINX 开源仓库：高性能 Web 服务器、反向代理与负载均衡器

这是 NGINX 官方开源代码仓库，采用类 BSD 2-clause 许可，可免费使用。NGINX 不是单一进程，而是由一个 master 进程读取并校验配置、管理多个 worker 进程处理实际请求，因此能突破操作系统进程数限制并横向扩展。它通过文本配置文件中的指令（directives）完成配置，功能由模块拆分扩展，模块可分静态编译进二进制或作为动态模块加载。除源码构建外，官方为主流 Linux 发行版、FreeBSD 和 Windows 提供二进制包，README 还给出了安装 SSL 证书启用 TLS、负载均衡、限流和内容缓存的上手路径。

- ✨ 作为 Web 服务器、反向代理、负载均衡器、API 网关和内容缓存多合一使用
- ✨ master/worker 多进程架构，可通过 worker_processes 等指令调优并发能力
- ✨ 模块化设计，功能按模块拆分，支持静态编译与动态模块两种分发方式
- ✨ 纯文本配置文件和指令体系，可灵活组合出所需行为
- ✨ 官方提供 Linux、FreeBSD、Windows 等多平台二进制包及源码构建流程
- ✨ README 覆盖 TLS 证书配置、负载均衡、限流、内容缓存等常见场景入门指引
- 👥 适合谁：需要部署 Web 服务、反向代理或负载均衡的后端与运维开发者，以及想从源码构建定制 NGINX 的工程师

`C` · Fork 8,393 · 🔗 [官网](https://nginx.org/)

### 4. [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) — ⭐ 12,162（今日 +158）

> OpenVINO 是一个用于深度学习模型推理优化与跨平台部署的开源工具包。

OpenVINO 解决的是“训练好的模型怎么在真实硬件上跑得快、跑得省”这个问题。它可以把 PyTorch、TensorFlow、ONNX、Keras、PaddlePaddle、JAX/Flax 等框架训练的模型转换后直接部署，不需要原框架参与推理；也能通过 Optimum Intel 直接接入 Hugging Face Hub 上的 transformers 和 diffusers 模型。使用时先用 ov.convert_model 转换，再用 core.compile_model 指定设备编译，随后即可推理，pip install openvino 就能上手，官方还提供 Notebooks 和 C++/Python 示例。

- ✨ 推理优化：面向计算机视觉、语音识别、生成式 AI 与 NLP（含大小语言模型）等常见任务提升性能
- ✨ 多框架模型支持：兼容 PyTorch、TensorFlow、ONNX、Keras、PaddlePaddle、JAX/Flax，并可脱离原框架转换部署
- ✨ Hugging Face 集成：通过 Optimum Intel 直接使用 transformers 与 diffusers 模型
- ✨ 广泛硬件覆盖：支持 CPU（x86、ARM）、GPU（Intel 集显与独显）以及 Intel NPU 等 AI 加速器，覆盖边缘到云端
- ✨ 简单部署 API：convert_model 转换 + compile_model 指定设备编译，几行代码完成模型推理
- ✨ 丰富学习资源：OpenVINO Notebooks 提供 LLM 聊天机器人、YOLOv11 优化、文生图、LLaVa 多模态、Whisper 语音识别等实战示例
- 👥 适合谁：需要在 Intel CPU、GPU、NPU 或边缘设备上高效部署和优化深度学习模型的 AI 应用开发者。

`C++` · Fork 3,669 · 🔗 [官网](https://docs.openvino.ai)

### 5. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) — ⭐ 70,524（今日 +518）

> 给 AI 编码助手用的图表技能，一条命令产出编辑级设计的单文件 HTML+SVG 图表。

diagram-design 是一个 Agent Skill，可被 Claude Code、Cursor、Codex、GitHub Copilot、Qoder 等能读取技能的宿主加载。你只需用自然语言说明需求，例如画一张应用架构图、一个 Q2 项目影响与投入象限图，或一次带 401 刷新令牌的 Bearer 调用序列；代理会先确定图表类型、说明方案，再写出一个自包含的 .html 文件，双击即可打开。它主要想解决 Mermaid 一类工具产出的图千篇一律、带阴影、设计师看不下去的问题：内置 51 种图表类型，统一走编辑级设计风格，还能读取你的网站配色和字体，让图表与品牌保持一致。

- ✨ 覆盖 51 种图表类型，架构图、序列图、象限图等常见表达基本齐备
- ✨ 产物是单个自包含 HTML + SVG 文件，无外部依赖，双击就能打开和分享
- ✨ 编辑级设计取向：明确不要阴影、不要 Mermaid 那种同质化的观感
- ✨ 品牌对齐：让它抓取你的站点，提取配色与字体，之后每张图都自动匹配
- ✨ 支持从 draw.io、Mermaid、Excalidraw、PlantUML 导入已有图表
- ✨ 可导出 PNG / SVG，另提供 /export-diagram、/import-mermaid 等斜杠命令
- 👥 适合谁：需要在文档、演示或 PR 里放架构图、流程图，又不想折腾设计工具的开发者与技术写作者。

`HTML` · Fork 4,733 · 🔗 [官网](https://diagramdesign.dev)

### 6. [mjmirza/app-store-compliance](https://github.com/mjmirza/app-store-compliance) — ⭐ 4,267（今日 +621）

> 一套开源的 App Store 与 Google Play 上架合规手册，外加提交前的自动扫描守卫。

这是一个把「上架被拒」从靠运气变成可检查项的项目。它整理了 117 个有据可查的拒审模式及对应修复，覆盖隐私清单（privacy manifest）、Android Data safety 表单等最常翻车的检查点，并追踪 95 个监管截止日期（EU AI Act、DSA、COPPA、各州年龄法）。用法很简单：git clone 后用 bash 运行 agent-os/hooks/app-store-compliance-guard.sh 指向你的工程目录，它只读不改，几秒到一分钟内打印结果，末尾一行是 BLOCKED、CLEAR 或 NOT CHECKED，告诉你接下来该做什么。它还能挂进 Claude Code、Codex、Gemini CLI、Copilot、Cursor 等 AI 编码工具，在每次提交前自动先跑一遍。

- ✨ 117 个已记录的拒审模式，每条都对应具体条款与可执行的修复方式
- ✨ 提交前自动扫描：运行一条 bash 命令即可得到 BLOCKED / CLEAR / NOT CHECKED 结论，不会改动你的代码
- ✨ 优先覆盖两大高频拒审原因：可用的演示账号与真实后端，以及与运行时行为一致的隐私声明（含每个 SDK）
- ✨ 隐私清单与 Google Play Data safety 检查，兼容 Expo 的 app.json / app.config 读取
- ✨ 追踪 95 个合规截止日期：EU AI Act、DSA、COPPA 与各州年龄相关法规
- ✨ 面向 AI 编码代理的技能包，可安装进 Claude Code、Codex、Gemini CLI、Copilot、Cursor 等工具，在每次提交前自动拦截
- 👥 适合谁：iOS/Android 开发者、独立开发者与小团队，以及需要走通上架流程但不写代码的产品或运营人员。

`Shell` · Fork 273 · 🔗 [官网](https://mjmirza.github.io/app-store-compliance/)

### 7. [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) — ⭐ 14,549（今日 +399）

> 开源 CI/CD 可靠性 agent，自动排查失败构建并提交修复供你审阅。

OpenSRE 是一个自托管的 CLI agent，专门用来处理 CI 失败：CI 只会告诉你构建失败了，却不会告诉你原因和修复方法。运行时，它会读取失败的运行日志、验证假设，定位根本原因，然后把修复推送出来交给你 review。它还能区分是 CI 环境自身的问题还是代码问题，避免团队只靠重跑绕过。用一条 curl 安装脚本装好之后，在代码仓库里执行 opensre 就能启动，模型用你自己的。目前处于 public alpha 阶段，核心流程可用但还不完全稳定，接口和集成可能变化。

- ✨ 失败即调查：CI 运行失败时自动读取日志、验证假设并定位根因
- ✨ 自动推送修复补丁，交由开发者审阅
- ✨ 区分 CI 环境导致的失败与代码本身导致的失败，避免只靠重跑掩盖问题
- ✨ 统计 CI 失败率、因 CI 不可靠损失的开发者工时、main 分支保持红色的时长
- ✨ 自托管部署，支持接入用户自己的模型
- ✨ 端到端测试覆盖真实云端场景，并维护语义化测试目录便于区分 e2e/单元、本地/云端边界
- 👥 适合谁：适用于经常被红色构建和 flaky 检查拖累的研发团队，以及希望把 CI 排障自动化、并保持代码和数据不出自建环境的工程组织。

`Python` · Fork 1,978 · 🔗 [官网](https://opensre.com)

### 8. [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) — ⭐ 77,011（今日 +542）

> AFFiNE 是一个隐私优先、本地优先的开源一体化工作区，可以看作 Notion 与 Miro 的结合与延伸。

AFFiNE（读音 [ə‘fain]）把文档、白板、表格、演示和知识库整合到同一个平台里，解决的是「知识管理要开好几个工具」的割裂问题。它的核心思路是「万物皆块」：富文本、便签、嵌入网页、多维表格、链接页面、形状乃至幻灯片，都能作为块放在无边界画布上，文档与白板不再是两个割裂的模块。数据默认保存在本地磁盘，同时支持 Web 与跨平台客户端的实时同步和多人协作；既可以开箱即用，也可以自行部署、fork 定制，还配套了 AFFiNE AI 帮你从大纲生成幻灯片、把文章整理成思维导图、规划任务。

- ✨ 文档与白板完全融合：任意块都能放到无边界画布上，富文本、便签、嵌入网页、多维表格、形状、幻灯片随处摆放
- ✨ 多视图数据库：支持表格等多种视图组织信息，兼具笔记与结构化数据管理
- ✨ AFFiNE AI：把大纲转成演示幻灯片、把文章整理成思维导图、梳理任务计划，甚至一句话生成原型页面
- ✨ 本地优先：数据保存在你自己的磁盘上，不依赖云端也能完整使用
- ✨ 跨端实时协作：Web 与各平台客户端之间实时同步，多人同时编辑
- ✨ 可自托管与可定制：自由部署、fork、自行构建，基于 BlockSuite 的插件与第三方块生态
- 👥 适合谁：适合需要同时做笔记、画白板、管任务与做演示的创作者、产品与研发团队，以及重视数据隐私、愿意自托管的开发者。

`TypeScript` · Fork 5,646 · 🔗 [官网](https://affine.pro)

### 9. [XiaoYouChR/Ghost-Downloader-3](https://github.com/XiaoYouChR/Ghost-Downloader-3) — ⭐ 15,646（今日 +701）

> 一个跨四大平台、通吃几乎所有下载协议的多合一开源下载器，专治网络差和资源分散。

Ghost-Downloader-3 是一个用 Python 编写、基于 Qt 的跨平台下载器，目标是把日常可能用到的下载场景全部收进一个应用里。它起源于帮一位 Bilibili 创作者管理资源的个人项目，如今已支持 Windows、macOS、Linux、Android 四个平台。它解决的问题很直接：以前下 HTTP 资源用一个工具、下 BT 用另一个、下视频又要装扩展或第三方软件，而它对 HTTP、Magnet/BT、FTP、M3U8、MPEG-DASH、eD2k 全都原生支持，还能直接解析 YouTube、Bilibili 的视频（可选清晰度、字幕、播放列表与多 P），并对 GitHub、HuggingFace 做镜像加速。除了图形界面，它还提供 ghd 命令行工具和兼容 aria2 的 RPC API，方便脚本化与第三方集成。

- ✨ 多协议统一支持：HTTP、Magnet/BT、FTP、M3U8、MPEG-DASH、eD2k 一个应用全搞定
- ✨ 智能分块下载且无需文件合并，自动检测带宽，在弱网环境下依然能保持速度
- ✨ 内置真实浏览器 TLS 指纹，降低被反爬机制拦截的概率
- ✨ 视频站点深度解析：YouTube、Bilibili 可选清晰度与字幕，支持播放列表和多 P 剧集
- ✨ 浏览器扩展可嗅探页面所有媒体资源，一键接管下载并沿用登录状态，无需复制链接
- ✨ 跨平台原生体验，Android 端支持直播 M3U8 录制与后台持续下载
- 👥 适合谁：需要频繁下载各类资源的普通用户、追剧与收藏视频的内容爱好者，以及希望用 CLI/RPC 做自动化的开发者。

`Python` · Fork 950 · 🔗 [官网](https://gd.xychr.com/)

### 10. [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) — ⭐ 13,844（今日 +641）

> 把播客、访谈、课程等长视频一键剪成适配全平台短视频的开源桌面工具。

AutoClip 是一款开源的 AI 视频剪辑桌面工具，解决的正是「长视频剪成短视频」这件费力的事：播客、访谈、课程动辄一两个小时，人工挑高光、卡字幕、套画幅、写文案，一条成片能耗掉大半天。它的用法很简单——贴一个视频链接，选好要发的平台，剩下的交给它：自动挑出值得剪的片段，配上分页字幕、封面和发布文案，直接出片。剪辑与渲染都在你自己的电脑上完成，软件本身免费，只有调用云端模型时按量计费。对自动结果不满意，还能进编辑器手动调整。

- ✨ 贴链接一键出片：给一个 YouTube、B 站等长视频地址，自动挑片段、剪辑、配字幕，直接输出可发布的短视频
- ✨ 多平台画幅与排版：竖版访谈式、满屏播客式适配抖音、小红书、TikTok、Reels、YouTube Shorts，横版保留原画幅给 B 站与 YouTube
- ✨ 视频、字幕、封面、发布文案一起生成，字幕支持中文、英文等多语言
- ✨ 本地剪辑与渲染：素材和成片都在自己电脑上处理，MIT 开源，软件免费，云端模型按量计费
- ✨ 内置编辑器：自动结果需要微调时手动改，字幕分页、人物取景都能调
- ✨ 桌面端之外还有 CLI 与 MCP，可脚本化跑长视频队列，也能接进支持 MCP 的 AI 客户端
- 👥 适合谁：做播客、访谈、课程的内容创作者，需要批量做短视频分发的运营与自媒体团队，以及想把剪辑流程脚本化的开发者。

`Python` · Fork 2,173 · 🔗 [官网](https://zhouxiaoka.github.io/autoclip_intro/)


## 🚀 Show HN 今日新品

[I built a game where you are an LLM's subagent](https://news.ycombinator.com/item?id=50599762) · ⬆️ 309 · 💬 74

> 在Show HN上，有人发布了一款游戏：玩家扮演LLM的分代理，该帖获得309分和74条评论。

[ExitPath – Open-source ways out of Slack, Notion and Microsoft 365](https://news.ycombinator.com/item?id=50547980) · ⬆️ 251 · 💬 94

> ExitPath 是一个开源项目，提供从 Slack、Notion 和 Microsoft 365 迁移或退出的方案。

[Take Voyager 1 apart, down to a single memory chip](https://news.ycombinator.com/item?id=50548161) · ⬆️ 240 · 💬 60

> 新项目带你逐层拆解旅行


## 🧡 Product Hunt 今日榜

[MeshLive](https://www.producthunt.com/products/meshlive) · Product Hunt

> MeshLive 推出基于蓝牙 mesh 的离线视频通话与直播功能。

[Mockreel](https://www.producthunt.com/products/mockreel) · Product Hunt

> Mockreel 可将屏幕录制放进 3D 手机画面展示，免费且无需注册。

[Daymaker](https://www.producthunt.com/products/daymaker) · Product Hunt

> Daymaker 推出一款能送出高度个性化礼物的工具，让潜在客户更愿意接受会面。

[Creavit Studio 4.0](https://www.producthunt.com/products/creavit-studio) · Product Hunt

> Creavit Studio 4.0 登陆 Product Hunt，为 Mac 带来屏幕录制、iPhone 摄像头和电影级演示功能。

[Yoroll](https://www.producthunt.com/products/yoroll) · Product Hunt

> Yoroll 让你无需游戏引擎即可构建可玩的故事。


## 🇨🇳 中文独立开发 · V2EX 分享创造

[GPT-Team 账号免费领取 Codex 4375 Credit（$175 账单金额）](https://www.v2ex.com/t/1259157) · 💬 2 回复

> GPT-Team 账号可免费领取 Codex 4375 Credit，价值 175 美元账单金额。

[失业大半年，开始尝试独立开发，做了个猫咪陪伴学英语的小程序](https://www.v2ex.com/t/1259152) · 💬 4 回复

> 失业大半年的独立开发者分享作品：一个用猫咪陪伴学英语的小程序。

[用 DeepSeek 写了一个原生跨平台文本编辑器 Zpad，邀请大家体验](https://www.v2ex.com/t/1259151) · 💬 3 回复

> 开发者用 DeepSeek 编写了原生跨平台文本编辑器 Zpad，并邀请大家体验。

[做了个纯浏览器本地运行的免费 OCR 工具，免登录不上传，支持粘贴截图对照校对](https://www.v2ex.com/t/1259146) · 💬 0 回复

> 开发者做了个纯浏览器本地运行的免费 OCR 工具，免登录不上传，支持粘贴截图对照校对。

[16 个字符就够写下一切 - 极客风 16 进制主题小网站](https://www.v2ex.com/t/1259142) · 💬 1 回复

> 独立开发者分享极

## 📋 完整榜单

> ℹ️ 同一仓库 3 天内不会重复出现，往期出现过的不会重复收录

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 为任意软件生成 CLI 封装，让 AI Agent 直接调用它，成为原生工具。 | `Python` | 63,043 | +699 |
| 2 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 把任意网页和文档转成 LLM 可用的干净数据，并提供搜索、抓取、交互和 550+ 数据源的… | `TypeScript` | 207,305 | +915 |
| 3 | [nginx/nginx](https://github.com/nginx/nginx) | 官方 NGINX 开源仓库：高性能 Web 服务器、反向代理与负载均衡器 | `C` | 32,938 | +163 |
| 4 | [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) | OpenVINO 是一个用于深度学习模型推理优化与跨平台部署的开源工具包。 | `C++` | 12,162 | +158 |
| 5 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | 给 AI 编码助手用的图表技能，一条命令产出编辑级设计的单文件 HTML+SVG 图表。 | `HTML` | 70,524 | +518 |
| 6 | [mjmirza/app-store-compliance](https://github.com/mjmirza/app-store-compliance) | 一套开源的 App Store 与 Google Play 上架合规手册，外加提交前的自动… | `Shell` | 4,267 | +621 |
| 7 | [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre) | 开源 CI/CD 可靠性 agent，自动排查失败构建并提交修复供你审阅。 | `Python` | 14,549 | +399 |
| 8 | [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | AFFiNE 是一个隐私优先、本地优先的开源一体化工作区，可以看作 Notion 与 Mi… | `TypeScript` | 77,011 | +542 |
| 9 | [XiaoYouChR/Ghost-Downloader-3](https://github.com/XiaoYouChR/Ghost-Downloader-3) | 一个跨四大平台、通吃几乎所有下载协议的多合一开源下载器，专治网络差和资源分散。 | `Python` | 15,646 | +701 |
| 10 | [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) | 把播客、访谈、课程等长视频一键剪成适配全平台短视频的开源桌面工具。 | `Python` | 13,844 | +641 |

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
