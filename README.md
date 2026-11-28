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

# 🔥 GitHub 每日 Trending · 2026-11-28

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 10 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 今日精选（详细介绍）

### 1. [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) — ⭐ 26,489（今日 +1,608）

> 装进 Claude Code 的漏洞赏金与外部红队技能包，83 个技能开箱即用

Claude-BugHunter 是一个可直接安装的 Claude Code 技能包：装一次，Claude 就从聊天机器人变成有经验的漏洞赏金研究员或红队操作员。它把方法论、58 个按漏洞类别整理的 hunt-* 技能、企业身份与基础设施攻击链、以及定级报告与证据脱敏流程分层堆叠起来；这些 hunt-* 技能源自 681 份公开 HackerOne 报告。使用时不用记技能名，直接用日常语言描述你在测什么，相关技能就会自动加载。支持通过插件市场一键安装，也可以用脚本复制安装，并能同时装进 OpenCode、Codex CLI 等其他 agent 工具。

- ✨ 83 个技能 + 15 个斜杠命令，按主题自动触发，无需按名称调用
- ✨ 58 个 hunt-* 漏洞类别技能，整理自 681 份公开 HackerOne 报告，含检测模式、payload、绕过表和链式利用模板
- ✨ bb-methodology 与 redteam-mindset 提供五阶段非线性工作流、批判性思维框架和红队操作纪律
- ✨ 企业外围攻击矩阵：M365/Entra、Okta、vCenter、SSL-VPN、SharePoint、云 IAM 的 2024–2026 CVE 链与凭据后提权
- ✨ triage-validation 七问门、VRT 感知定级、OOS 反驳话术、PII 脱敏与红队交付物
- ✨ 插件市场一键安装或脚本复制安装，附带 hunt 接驳目录脚手架、cbh CLI 与 Burp MCP 集成，可同时装到多个 agent harness
- 👥 适合谁：从事授权漏洞赏金、外部红队与 Web 应用安全测试的安全研究员

`Python` · Fork 2,708 · 🔗 [官网](https://elementalsouls.github.io/Claude-BugHunter/)

### 2. [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) — ⭐ 13,674（今日 +311）

> Google Stitch 官方 Agent Skills 库：让编码 Agent 直接操作设计稿与设计系统

这是 Google Labs 为 Stitch（Google 的 AI 界面设计工具）整理的一套 Agent Skills 和插件合集，遵循 Agent Skills 开放标准，因此能直接用在 Codex、Antigravity、Gemini CLI、Claude Code、Cursor、OpenCode 等编码 Agent 里。它要解决的是「设计和写代码各干各的、需要人工来回搬运」的问题：Agent 通过 Stitch MCP 服务器连上 Stitch 后，就能用自然语言生成界面、修改现有屏幕、批量产出设计变体，也能把已有的前端代码反向转成设计稿，或者从源码里抽出 DESIGN.md 设计系统再统一套用到所有屏幕上。安装方式按客户端分：Codex 通过插件市场，Claude Code 和 Cursor 用 npx plugins 安装，OpenCode 则需要手动拷贝 skill 目录并自行配置远程 MCP 条目。前提是先在 Agent 环境中完成 Stitch MCP 的注册和凭据配置。

- ✨ 从文本或图片生成新界面，支持编辑已有屏幕、批量生成设计变体
- ✨ 把 React、Vue 等前端代码转成 Stitch 设计稿（HTML 提取 + 设计系统 + 上传）
- ✨ 从源码自动抽取 DESIGN.md 设计系统，并一键套用到全部屏幕
- ✨ 管理 Stitch 设计系统，上传 DESIGN.md、应用主题
- ✨ 提取自包含的静态 HTML，便于交付或迁移
- ✨ 多客户端插件化安装：Codex 市场、Claude Code/Cursor 的 npx 安装、OpenCode 手动接入
- 👥 适合谁：需要把 UI 设计稿与代码库打通的前端工程师、全栈开发者和设计工程师，尤其是已在 Claude Code、Cursor、Codex 等 Agent 中工作的人。

`TypeScript` · Fork 1,635 · 🔗 [官网](https://stitch.withgoogle.com/docs/mcp/setup)

### 3. [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) — ⭐ 62,931（今日 +753）

> 把 PS5 可执行文件自动重链接为 Linux、Windows 原生程序的转换工具

AnyPS5 是一个 C++ 编写的转换工具，目标是把 PS5 的可执行文件自动移植到 Linux 和 Windows 上运行。它的核心是 relinker（重链接器），会把 PS5 可执行文件转换成目标系统的原生格式，同时提供一套可动态链接的 system prx 系统库实现，不依赖模拟器，也不需要额外的运行时进程。项目还带有基于网页的转换器，文件全程留在本地设备上，不上传。官方提供了程序构建、架构说明、代码规范、技术债清单等文档，以及各游戏的兼容性讨论区。命令行遇到未支持状态会抛 C++ 异常；着色器重编译器在启用 SPIRV-Tools 的构建中可产出经过验证的 SPIR-V。仅含 relinker 的构建还能在 macOS（包括 Apple silicon）上运行。

- ✨ 自动重链接：把 PS5 可执行文件转换为 Linux、Windows 原生可执行格式
- ✨ 提供 system prx 系统库实现，支持动态链接，无需模拟器或独立运行时进程
- ✨ 着色器重编译器输出 SPIR-V，并可用 Spirv-Tools 校验结果
- ✨ 网页版转换器，所有文件处理都在本地设备完成，不上传服务器
- ✨ 输入映射支持 SDL 手柄（含摇杆与扳机），键鼠可通过 anyps5-input.ini 配置
- ✨ 仅含 relinker 的构建可在 macOS（含 Apple silicon）上运行
- 👥 适合谁：对 PS5 软件互操作性、移植研究与软件保存感兴趣的开发者和研究人员

`C++` · Fork 6,143 · 🔗 [官网](https://boykopovar.github.io/AnyPS5/)

### 4. [superdesigndev/treg](https://github.com/superdesigndev/treg) — ⭐ 9,826（今日 +282）

> 面向 agent 的工具版 OpenRouter：一个 token 调用数千个按次计费的第三方 API

treg 把 agent 真正干活需要的工具集中到一个网关后面：SEO 与反链、社交与趋势、人物与公司信息补全、广告、抓取、图像视频生成，覆盖数千个端点，按次计费、最低一分钱起，不用去各家注册账号。它替团队持有 Semrush、Moz、Crunchbase、Apollo 这类订阅，让你按调用付费，而不是按席位买月费。装好 CLI 后执行 treg login，用 treg catalog search 按「要做什么」找工具，treg call 直接调用，treg balance 看这一单花了多少。你还可以把团队自己的 API 账号、OAuth、厂商 CLI 或 SKILL.md 注册进来，用自己的 key 调用且不计费。

- ✨ 策展目录覆盖数千个端点：SEO 与反链、社交趋势、人物与公司信息补全、广告、爬取、图像视频生成，按次计价，最低一分钱起
- ✨ 无需向供应商注册：上游账号由 treg 持有，也支持无需 key 的公开路由；自有 key 永远优先于 treg 的 key，且这类调用从不计费
- ✨ 三类自带工具统一注册：endpoint（base_url + 多个凭证绑定，一次请求可同时注入 OAuth bearer 和 developer-token 头）、CLI（stripe、gh、vercel 等二进制）、skill/bundle（SKILL.md + secrets + tools）
- ✨ 代理只转发、不建模，并在服务端注入鉴权：上游 API 改动不会波及调用方，调用者永远拿不到密钥
- ✨ 换 base URL 即可迁移：把 https://api.dataforseo.com/v3 换成 https://treg.to/call/dataforseo，已有客户端就能跑对应目录工具，目录未列出的路径一律 404、不做转发
- ✨ strict_query 工具做严格参数校验：未声明、重复、超范围或类型不符的参数直接返回 400 catalog_parameter_invalid 并指明参数，且不计费
- 👥 适合谁：把 agent 用于真实业务的开发者与团队，尤其是做增长、SEO、数据补全类 agent，且需要共享凭证、可自托管的人

`Python` · Fork 1,021 · 🔗 [官网](https://treg.to)

### 5. [anomalyco/opencode](https://github.com/anomalyco/opencode) — ⭐ 229,674（今日 +277）

> 开源 AI 编码智能体，在终端里直接帮你写代码、查代码、跑命令。

OpenCode 是一个开源的 AI 编码智能体，官方定位就是「The open source coding agent」。它把 AI 助手放进你的终端：既能直接改代码、跑 bash 命令干开发活，也能切成只读模式，先摸清陌生代码库再动手。安装很轻，一条 curl 脚本或 npm、brew、pacman、mise、nix 都能装好，另外还提供处于 Beta 阶段的桌面应用（macOS、Windows、Linux）。想深入了解配置可以看官方文档，社区在 Discord 和 X 上。

- ✨ 终端 UI（TUI）形式的编码智能体，直接在命令行里工作
- ✨ 内置 build 与 plan 两个 agent，用 Tab 键随时切换
- ✨ plan 为只读模式：默认拒绝文件编辑，执行 bash 前先征求许可，适合探索陌生代码库
- ✨ general 子代理用于复杂搜索和多步任务，可在消息中用 @general 调用
- ✨ 安装方式覆盖 curl 脚本、npm/bun/pnpm/yarn、Homebrew、Arch 的 pacman 与 AUR、mise、Nix
- ✨ 提供 Beta 桌面应用，支持 macOS（Apple Silicon/Intel）、Windows 和 Linux 的 deb/rpm/AppImage
- 👥 适合谁：适合习惯在终端工作的开发者，尤其是需要 AI 辅助读代码、改代码、执行命令的人。

`TypeScript` · Fork 31,282 · 🔗 [官网](https://opencode.ai)

### 6. [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) — ⭐ 119,712（今日 +216）

> 一份系统整理 macOS 优质软件的精选清单，按类别归纳，方便查找和使用。

awesome-mac 是一个面向 Mac 用户的软件精选合集，目标是把散落在各处的优质 macOS 应用集中起来，并按类别系统化整理，解决“想找某个功能的 Mac 软件却不知道用什么好”的问题。它不是代码库，而是一份持续维护的清单：你可以直接在目录里按分类浏览，比如效率工具、开发工具、设计、系统增强等，快速定位到具体应用。遇到合适的项目，按清单里的链接前往官网或商店获取即可。适合当作日常查阅的 Mac 软件选型参考。

- ✨ 按类别系统整理 macOS 软件，便于按用途快速查找
- ✨ 持续收录高质量 Mac 应用，形成可长期参考的清单
- ✨ 覆盖效率、开发、设计、系统工具等多个方向
- ✨ 每个条目提供应用名称与跳转链接，方便直接获取
- ✨ 以 Markdown 清单形式维护，阅读和检索成本低
- ✨ 由社区参与补充和更新，保持内容与时俱进
- 👥 适合谁：适合所有 Mac 用户，尤其是想按类别发掘优质应用、需要软件选型参考的开发者与效率爱好者。

`Swift` · Fork 10,708 · 🔗 [官网](https://git.io/macx)

### 7. [NYLLON-SOFTWARE/SignuDoc](https://github.com/NYLLON-SOFTWARE/SignuDoc) — ⭐ 3,599（今日 +197）

> 开源电子签名平台，部署在自己的 Vercel 账号上，按席位零成本，文档与审计证据自持。

SignuDoc 是一个 MIT 协议的开源电子签名应用，用来替代 DocuSign 这类按席位收费的服务。它解决三个问题：席位费贵（15 人团队用 DocuSign 一年 5400~8100 美元）、信封额度受限、合同文件存放在第三方手里。用法很直接：点 Deploy 按钮，在免费的 Vercel、Neon、Resend 计划上自动建好数据库、文件存储和邮件服务；然后上传 PDF、拖放签署字段、按顺序添加签署人，系统发出签署链接，签署人无需注册账号即可在手机或电脑上输入或手绘签名，完成后所有各方拿到带 PAdES 密封和审计证书的最终 PDF。

- ✨ 上传 PDF 后可视化放置签名、姓名、日期、文本、数字、复选框、下拉框、单选按钮等字段，每个字段可设必填或选填并绑定到指定签署人
- ✨ 最多 25 名签署人，支持顺序签署或部分人同时签署，也可添加只接收成品的抄送人
- ✨ 签署人免注册，通过邮件链接打开，在任意设备上输入或手绘签名；可先下载原文，也可填理由拒签并通知发起人
- ✨ 身份核验：可要求签署人输入你线下告知的访问码，或由系统在打开链接时发送一次性验证码，审计证书记录核验方式、IP 和浏览器
- ✨ 信封管理：卡片式仪表盘显示首页缩略图与状态（草稿、已发送、已完成、已拒绝、已作废、已过期），支持搜索和状态筛选，签署期限 3~90 天可中途修改，支持每 1/2/3/7 天自动提醒及手动催办
- ✨ 发错邮箱可更正，旧链接失效、新地址收到新邀请；已完成信封可复制为新草稿（沿用文档、签署人和字段）；可存为模板
- 👥 适合谁：需要频繁收发合同、又在意成本与数据归属的中小团队、律所、代理机构和自托管爱好者。

`TypeScript` · Fork 772

### 8. [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) — ⭐ 34,409（今日 +183）

> 把多账号管理、协议转换与请求调度装进一个桌面端的本地 AI 中转站。

Antigravity Tools 是一款面向开发者和 AI 爱好者的桌面应用，核心思路是把多账号矩阵管理、协议转换和智能请求调度合到一起，在本地搭一个稳定、快速、低成本的 AI 中转站。它最实用的一点是能把常见的 Web Session（Google、Anthropic）转换成标准化的 API 接口，省掉不同供应商之间的协议差异，让你用统一的接口去调用。日常使用时，你在图形界面里集中看所有账号的配额健康度，由系统挑出当前最合适的账号一键切换，再配合请求调度把流量分摊到多个账号上。项目用 Tauri v2 + React 构建界面、Rust 写后端，属于安装即用的跨平台桌面程序，不必自己搭服务。

- ✨ 智能账号面板：集中查看所有账号的健康状况，实时掌握 Gemini Pro、Gemini Flash、Claude 与 Gemini 图像生成的剩余配额
- ✨ 智能推荐与一键切换：按配额冗余度实时算出“最佳账号”并推荐，支持一键切换，无需手动改配置
- ✨ 当前账号快照：用可视化方式呈现活跃账号状态，切换前后一目了然
- ✨ 协议转换：把 Google / Anthropic 的 Web Session 转成标准化 API 接口，抹平不同供应商之间的协议差异
- ✨ 智能请求调度与多账号矩阵分发：按策略把请求分配到多个账号上，避免单一账号被打满
- ✨ 本地 AI 中转站：以桌面应用形式在本地提供统一 API 入口，配合文档中的集成示例可直接接入现有工具链
- 👥 适合谁：手里有多个 AI 账号、想把网页会话转成标准 API 并统一调度请求的开发者与 AI 爱好者。

`Rust` · Fork 3,610 · 🔗 [官网](https://lbjlaq.github.io/Antigravity-Manager/)

### 9. [microsoft/markitdown](https://github.com/microsoft/markitdown) — ⭐ 198,798（今日 +167）

> 微软出品的轻量 Python 工具，把各类文档转成适合 LLM 处理的 Markdown。

MarkItDown 是一个轻量级 Python 工具，用来把 PDF、Office 文档、图片、音频、HTML 等多种格式转换成 Markdown。它和 textract 定位相似，但重点是保留标题、列表、表格、链接等文档结构，方便喂给 LLM 和文本分析流水线。可以用命令行直接转换（markitdown file.pdf > out.md，支持 -o 和管道输入），也可以作为库调用。它更偏向给分析工具消费，而不是追求人类阅读级的高保真排版。

- ✨ 支持 PDF、Word、PowerPoint、Excel、EPub、HTML、CSV/JSON/XML、ZIP 等多种输入格式
- ✨ 保留标题、列表、表格、链接等关键文档结构，而不是退化为纯文本
- ✨ 图片可提取 EXIF 元数据并做描述，音频可提取元数据并转写（依赖托管服务）
- ✨ 支持 YouTube URL 转录和 Outlook 邮件转换
- ✨ 可选依赖按格式拆分安装（如 [pdf, docx, pptx]），也可用 [all] 一次装齐
- ✨ 支持第三方插件，默认关闭，需用 --list-plugins / --use-plugins 管理，官方还提供 markitdown-ocr 插件为 PDF、DOCX、PPTX、XLSX 中的内嵌图片补充 OCR
- 👥 适合谁：需要给 LLM 或文本分析流水线批量准备文档数据的 Python 开发者、数据工程师和 AI 应用团队。

`Python` · Fork 15,109

### 10. [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — ⭐ 58,896（今日 +162）

> 一款 Claude Code 学术研究技能包，覆盖从调研到定稿的完整论文流程。

这是一套以 Claude Code 插件形式分发的学术研究技能集，把论文工作拆成 research → write → review → revise → finalize 五个阶段，每到一个阶段就停下来等你确认；它可以起草整篇论文，但选题、方法、数据解读和结论必须由你决定。它主要解决的事情包括：查找并核对文献、按格式整理引用、检查数据与逻辑是否一致，以及避免 AI 自己编造引用或结果。安装只需两条命令：先把插件市场加到本地环境，再安装插件；随后输入 /ars-plan，它就会用苏格拉底式提问帮你梳理论文结构。它也支持在 claude.ai 或 Claude Desktop 上安装，不过 hooks 和插件 agent 在纯聊天界面不会运行。

- ✨ 五个阶段的流程（调研、写作、审稿、修改、定稿）在每阶段都会暂停并等待你确认，AI 担任副驾驶，不替你做出决定
- ✨ /ars-plan 通过苏格拉底式对话逐步问出论文结构，另外提供可选的审稿人校准模式，用你给的 gold set 测量它自身的漏报率 FNR 和误报率 FPR
- ✨ 引用可信链：使用 source provenance frontmatter 和三层引用定位锚点，为后续在论断层面进行审计打下基础
- ✨ 可选开启的论断审计（设置 ARS_CLAIM_AUDIT=1）会按每个锚点回抓被引原文，判断原文是否真的支持该论断；五类 HIGH-WARN 由格式化终端的硬性校验统一拦截
- ✨ Stage 2.5 与 Stage 4.5 设置完整性校验关卡，执行 7 条 AI 研究失败模式阻断清单（包括实施 bug、编造结果、方法论捏造、引用幻觉、框架锁死等）
- ✨ Style Calibration 从你过去的作品学习并贴合你的行文风格，Writing Quality Check 识别机器味浓的句式，目标是提高质量，并不教你怎么掩盖使用 AI 的痕迹
- 👥 适合谁：用 Claude Code 做文献综述、投稿论文的研究生与科研人员，也适合需要把控引用真实性的写作者。

`Python` · Fork 4,486 · 🔗 [官网](https://buymeacoffee.com/crucify020v)


## 🚀 Show HN 今日新品

[bouncemarket – a live prediction market game for a bouncing ball](https://news.ycombinator.com/item?id=50667726) · ⬆️ 367 · 💬 124

> bouncemarket 是一个围绕弹跳球实时走势的预测市场小游戏，登上 Hacker News 后获 367 分、124 条评论。


## 🧡 Product Hunt 今日榜

[RetainIQ](https://www.producthunt.com/products/retainiq-2) · Product Hunt

> RetainIQ 帮你识别哪些

[Microsoft-Decision-1.1](https://www.producthunt.com/products/microsoft-decision-1-1) · Product Hunt

> 微软决策模型 Microsoft-Decision-1.1 正式 GA，经过校准且速度提升 2 倍。

[Slopie](https://www.producthunt.com/products/slopie) · Product Hunt

> Slopie 推出免费浏览器端 3D 地图，覆盖所有滑雪场。

[overads.io](https://www.producthunt.com/products/overads-io) · Product Hunt

> overads.io 在 Product Hunt 发布，主打在你睡觉时也能自动运转的营销与 GTM 方案。

[Tano](https://www.producthunt.com/products/tano) · Product Hunt

> Tano 是一款韩语词汇应用，能跳过你已经掌握的单词。


## 🇨🇳 中文独立开发 · V2EX 分享创造

[robots.txt 早写了，爬虫还是把我免费的 Worker 刷到 8840 次超限](https://www.v2ex.com/t/1260570) · 💬 4 回复

> 独立开发者吐槽已写 robots.txt，爬虫仍把免费 Worker 刷到 8840 次超限。

[分享一个磁盘清理工具-黑五限时免费！](https://www.v2ex.com/t/1260569) · 💬 0 回复

> V2EX 独立开发者分享一款磁盘清理工具，黑五期间限时免费领取。

[做了一个 100% 本地的 Chrome 浏览记忆插件：关掉未读标签不怕忘，支持按正文关键词找回（无需账号）](https://www.v2ex.com/t/1260557) · 💬 0 回复

> 独立开发者推出100%本地Chrome浏览记忆插件，关闭未读标签也不怕忘，可按正文关键词找回，且无需账号。

[\[开源\] 受 Hermes 启发，做了个会记经验的 AI 浏览器插件](https://www.v2ex.com/t/1260543) · 💬 0 回复

> 一位开发者受 Hermes 启发，开源了一款能记录经验的 AI 浏览器插件。

[一个可以在浏览器里撸猫的游戏，不用养猫也能吸猫 🐈](https://www.v2ex.com/t/1260539) · 💬 0 回复

> V2EX 开发者分享了一款浏览器撸猫游戏，不用养猫也能在线吸猫。

## 📋 完整榜单

> ℹ️ 同一仓库 3 天内不会重复出现，往期出现过的不会重复收录

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | 装进 Claude Code 的漏洞赏金与外部红队技能包，83 个技能开箱即用 | `Python` | 26,489 | +1,608 |
| 2 | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | Google Stitch 官方 Agent Skills 库：让编码 Agent 直接操… | `TypeScript` | 13,674 | +311 |
| 3 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | 把 PS5 可执行文件自动重链接为 Linux、Windows 原生程序的转换工具 | `C++` | 62,931 | +753 |
| 4 | [superdesigndev/treg](https://github.com/superdesigndev/treg) | 面向 agent 的工具版 OpenRouter：一个 token 调用数千个按次计费的第… | `Python` | 9,826 | +282 |
| 5 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 开源 AI 编码智能体，在终端里直接帮你写代码、查代码、跑命令。 | `TypeScript` | 229,674 | +277 |
| 6 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 一份系统整理 macOS 优质软件的精选清单，按类别归纳，方便查找和使用。 | `Swift` | 119,712 | +216 |
| 7 | [NYLLON-SOFTWARE/SignuDoc](https://github.com/NYLLON-SOFTWARE/SignuDoc) | 开源电子签名平台，部署在自己的 Vercel 账号上，按席位零成本，文档与审计证据自持。 | `TypeScript` | 3,599 | +197 |
| 8 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | 把多账号管理、协议转换与请求调度装进一个桌面端的本地 AI 中转站。 | `Rust` | 34,409 | +183 |
| 9 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 微软出品的轻量 Python 工具，把各类文档转成适合 LLM 处理的 Markdown。 | `Python` | 198,798 | +167 |
| 10 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 一款 Claude Code 学术研究技能包，覆盖从调研到定稿的完整论文流程。 | `Python` | 58,896 | +162 |

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
