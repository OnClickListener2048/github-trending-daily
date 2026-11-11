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

# 🔥 GitHub 每日 Trending · 2026-11-11

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 10 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 今日精选（详细介绍）

### 1. [tidain/YunX-Desktop](https://github.com/tidain/YunX-Desktop) — ⭐ 4,277（今日 +340）

> 云析 YunX 官方 Windows 桌面版，粘贴分享链接即可解析并高速下载网盘、视频和 P2P 资源。

云析（YunX）的官方 Windows 桌面端，AGPL-3.0 开源、完全免费，README 明确说明任何收费版本都是他人二次打包的骗局。它把网盘分享链接、视频作品链接和磁力 / BT / ed2k 链接集中到一个窗口里：登录账号后粘贴链接，即可浏览文件、在线预览并直接多线程下载，全程都在本机完成。提供免安装便携版（整个文件夹拷走即用）和可卸载的安装版两种分发形式；登录凭证加密存放在本机，支持多账号和加密导出备份，换机后不用逐个重新登录。

- ✨ 分享链接解析：夸克 / UC / 迅雷 / 百度 / 139 / 123 / 115 / 光鸭 / 蓝奏云 / 蓝奏云优享版链接自动匹配提取码，另支持 GitHub 仓库、账号与文件直链
- ✨ 视频解析与预览：抖音 / 快手 / 微博 / 小红书 / B站 / AcFun / Pixiv 链接（短链、口令、整段文案均可）解析；在线预览优先用 ffplay 直接读取直链、边下边播，未安装 FFmpeg 时可一键下载引擎到私有目录，图集可放大查看，支持 Live Photo 合成，B站高清分轨两轨并行下载后自动合轨
- ✨ 高速下载：Range 分片并发 + 断点续传 + 慢连接自动换线 + 全局限速，下载进度实时显示为 Windows 通知中心 toast 进度条；另有原生托盘菜单、原生文件对话框和剪贴板分享链接检测
- ✨ P2P 下载：磁力 / BT 种子 / ed2k 链接交由 Gopeed 引擎处理，可导入本地 .torrent 文件、在二级页管理 Tracker 服务器并开关 DHT，下载中可查看种子 / 连接 / 节点概览
- ✨ 多账号与认证备份：内嵌 Chromium 登录、一键导入本机浏览器 Cookie 或手动粘贴 Cookie，凭证加密存本机，设置里的「认证备份」可加密导出 / 导入全部账号，换机免重登
- ✨ 浏览器插件「云析下载助手」（Chrome / Edge，Manifest V3）：嗅探页面媒体与文件并按类型分类预览，接管浏览器下载并按线程数下载（最高 512），可归还原生下载并对该站点写 5 分钟冷却倒计时；扩展通过本机回环地址 + 随机 token 与云析通信，云析未运行时完全不干预浏览器
- 👥 适合谁：常从网盘分享、视频平台或磁力链接下载资源的 Windows 用户，以及需要高速批量下载、偏好开源工具的人。

`Kotlin` · Fork 321

### 2. [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) — ⭐ 17,167（今日 +323）

> 在自有基础设施上运行 AI agent 的隔离沙箱运行时，用 Docker 起步，用 Kubernetes 扩展。

OpenSandbox 为 AI 应用提供隔离环境，让 agent 能安全地执行代码、运行命令、读写文件、操作浏览器或桌面。它要解决的核心问题是：AI 需要真正动手干活，但绝不能碰到宿主机和真实凭证。使用方式很直接：本地一条命令启动沙箱服务，Python 里创建沙箱、执行命令、写入脚本、读取文件，用完销毁；要上生产时换成 Kubernetes，同一套沙箱生命周期 API 不用改。配套五种语言 SDK、osb 命令行和 MCP 接入，主流 agent 框架可以直接对接。

- ✨ Fast Sandbox 运行时：Kubernetes 上高密度快速沙箱，Firecracker 创建延迟 64ms P50（串行）和 125.4ms P99（10 并发），支持暂停恢复并保留内存与磁盘状态
- ✨ Agent 工作环境 API：内置命令执行、文件管理和代码运行接口，示例覆盖编码 agent、浏览器与桌面场景
- ✨ 网络访问控制：入站流量统一走 ingress 网关，出站按沙箱粒度配置 egress 策略
- ✨ Credential Vault：让 agent 调用外部服务，同时不把真实凭证暴露给沙箱内的工作负载
- ✨ 本地到集群的一致体验：Docker 起步与 Kubernetes 部署共用统一生命周期 API，资源池和批量创建支撑 agent 评测与 RL 训练
- ✨ 多语言 SDK 与工具链：提供 Python、Java/Kotlin、TypeScript/JavaScript、C#/.NET、Go SDK，另有 osb CLI、MCP 接入和可扩展的沙箱生命周期与执行协议
- 👥 适合谁：构建 AI agent 的开发者、需要隔离执行 AI 生成代码的平台团队，以及做 agent 评测与 RL 训练的团队。

`Python` · Fork 1,622 · 🔗 [官网](https://open-sandbox.ai)

### 3. [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — ⭐ 56,396（今日 +225）

> 一款 Claude Code 学术研究技能包，覆盖从调研到定稿的完整论文流程。

这是一套以 Claude Code 插件形式分发的学术研究技能集，把论文工作拆成 research → write → review → revise → finalize 五个阶段，每到一个阶段就停下来等你确认；它可以起草整篇论文，但选题、方法、数据解读和结论必须由你决定。它主要解决的事情包括：查找并核对文献、按格式整理引用、检查数据与逻辑是否一致，以及避免 AI 自己编造引用或结果。安装只需两条命令：先把插件市场加到本地环境，再安装插件；随后输入 /ars-plan，它就会用苏格拉底式提问帮你梳理论文结构。它也支持在 claude.ai 或 Claude Desktop 上安装，不过 hooks 和插件 agent 在纯聊天界面不会运行。

- ✨ 五个阶段的流程（调研、写作、审稿、修改、定稿）在每阶段都会暂停并等待你确认，AI 担任副驾驶，不替你做出决定
- ✨ /ars-plan 通过苏格拉底式对话逐步问出论文结构，另外提供可选的审稿人校准模式，用你给的 gold set 测量它自身的漏报率 FNR 和误报率 FPR
- ✨ 引用可信链：使用 source provenance frontmatter 和三层引用定位锚点，为后续在论断层面进行审计打下基础
- ✨ 可选开启的论断审计（设置 ARS_CLAIM_AUDIT=1）会按每个锚点回抓被引原文，判断原文是否真的支持该论断；五类 HIGH-WARN 由格式化终端的硬性校验统一拦截
- ✨ Stage 2.5 与 Stage 4.5 设置完整性校验关卡，执行 7 条 AI 研究失败模式阻断清单（包括实施 bug、编造结果、方法论捏造、引用幻觉、框架锁死等）
- ✨ Style Calibration 从你过去的作品学习并贴合你的行文风格，Writing Quality Check 识别机器味浓的句式，目标是提高质量，并不教你怎么掩盖使用 AI 的痕迹
- 👥 适合谁：用 Claude Code 做文献综述、投稿论文的研究生与科研人员，也适合需要把控引用真实性的写作者。

`Python` · Fork 4,293 · 🔗 [官网](https://buymeacoffee.com/crucify020v)

### 4. [orailnoor/cross-platform-llm-client](https://github.com/orailnoor/cross-platform-llm-client) — ⭐ 2,143（今日 +211）

> 一个 Flutter 跨平台 AI 聊天客户端，把本地 GGUF 离线推理和多家云端 API 统一在同一个界面里。

PrivateLM 是一个可以直接安装使用的跨平台 AI 聊天客户端。它想解决的核心问题是：用云端 API 聊天时，模型无法离线使用且隐私不可控；运行本地模型时，又缺少统一好用的客户端。在 Android 和 iOS 上，你可以下载 GGUF 模型直接跑在设备上，借助 Vulkan 或 Metal 的 GPU 加速，下载完成后完全不需要联网；在 Web 端或不方便本地推理时，可以切换到 OpenAI、Anthropic、Gemini、Kimi 四家云端服务。四家 API 在代码中被统一整理，共用一套调用接口，聊天记录和设置全部存在本地的 Hive 里，除非你主动选择云模式，否则数据不会离开设备。首次启动时，它会根据设备可用内存推荐上下文长度和 token 上限。iOS 版以 IPA 形式分发，需要通过 AltStore 侧载安装。

- ✨ Android 与 iOS 本地 GGUF 推理，GPU 加速（Vulkan / Metal），下载后离线可用
- ✨ 云端 API 接入 OpenAI、Anthropic、Google Gemini、Kimi（Moonshot），四套 API 统一到一个接口
- ✨ 多模态聊天：文本加图片输入，本地 Qwen2-VL 与云端视觉模型都支持
- ✨ 会话与设置全部通过 Hive 本地持久化，API Key 只发往对应服务商
- ✨ 根据设备 RAM 和 GPU 等级自动推荐上下文大小、token 限制与线程数
- ✨ 后台服务与 Firebase 推送通知，支持后台任务处理，附 5 秒空闲检测与 180 秒超时兜底
- 👥 适合谁：想在手机上离线运行自定义或未审查模型，同时又需要随时切换到主流云端 API 的开发者与进阶用户。

`C++` · Fork 420

### 5. [WhiteTowerAI/ohmygame](https://github.com/WhiteTowerAI/ohmygame) — ⭐ 2,055（今日 +170）

> 开源的一人游戏工作室：在一个应用里用 AI 设计、生成素材、构建、试玩并发布游戏。

做游戏要同时用到设计文档、2D 美术、3D 模型、视频、代码和发布渠道，这些往往散落在五六个工具里。OhMyGame 把它们收进一个桌面应用：你用自然语言描述游戏，智能体就会写设计文档、在画布上生成图片、视频、3D 和音频素材、写代码、在实时预览里试玩并尝试修复问题，最后发布成一个浏览器可玩的链接。它开源、采用 BYOK，密钥留在你自己机器上，通过 Pi 支持 40+ 模型提供商，没有按次计费的积分。

- ✨ 智能体驱动画布：像人一样排版画布、起草设计文档，并在画布节点上直接生成图片、视频、3D 模型和音频
- ✨ 智能体自动试玩：把游戏跑在可观看的窗口里实际玩一遍（含实时 Canvas 和 WebGL 游戏），发现问题就改，改完再玩
- ✨ 统一的设计空间：主设计文档与美术、视频、3D、音频并列在同一块画布上，节点之间可互相引用，产物进入共享素材库供游戏直接使用
- ✨ 一键发布与社区：发布后得到一个任何人用浏览器就能玩的链接，重新发布会更新同一链接；应用内社区可按最新、最多浏览、最多点赞排序，也能逛创作者主页
- ✨ 交互式故事：做视觉小说、互动电影和剧情游戏，每一屏都是智能体根据描述生成的网页，可以放视频、对话、选项甚至小游戏
- ✨ 可扩展与自带智能体：Claude Code、Codex、OpenCode 可以接管对话；插件支持 Godot、Unity、Unreal、Cocos Creator 构建，Blender、Aseprite、Tiled 做素材，并发布到微信小游戏、抖音小游戏、TapTap
- 👥 适合谁：想独立做游戏、又不想在五六个工具之间来回切换的个人开发者、独立创作者和小团队。

`TypeScript` · Fork 259 · 🔗 [官网](https://ohmygame.ai/)

### 6. [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) — ⭐ 34,057（今日 +166）

> 用一个菜单栏图标替代十几个付费 Mac 工具，免费开源、无账号、无遥测。

Vorssaint 是一款面向 macOS 14+（Apple Silicon）的菜单栏工具箱，采用 GPL-3.0 开源许可。它要解决的是 Mac 用户为了音量混音、系统监控、窗口管理、剪贴板历史这类小功能，不得不分别购买、分别订阅好几个 App 的问题，把十几种常用工具集中到一个菜单栏图标下。它最大的特点是模块化：在设置里的 Features hub 中，你可以按需安装单个功能，也可以从一个预设开始；卸载某个功能后，它就不再加载，并从界面上消失，重新安装时会恢复原有设置；首次配置时，它只申请你选中的功能所需的权限。面板分区可以重排或隐藏，可以切换紧凑布局，设置还能导出到另一台 Mac，或放进 dotfiles 里管理。界面支持十多种语言，全程无账号、无订阅、无遥测。

- ✨ 按应用音量混音：为每个 App 单独设置音量，将偏小的声音放大到 100% 以上，收藏并排序常用应用，无需安装音频驱动；还支持按应用指定输出设备，比如音乐走音箱、通话走耳机
- ✨ 系统监控：显示 CPU、GPU、内存、温度、电池健康与功耗，提供历史曲线，并列出高耗能 App；另含测试阶段的 Fan Control，可手动设置风扇转速或温度曲线
- ✨ 窗口与应用管理：内置更好用的 App 切换器、窗口吸附和 Dock 预览
- ✨ 剪贴板历史、文本片段与文件架，另有卸载器和 Homebrew、媒体工具等实用小工具
- ✨ 音频外围功能：快捷键切换输出设备、耳机断开时自动降低音量、选择首选麦克风输入、一键静音或调节输入音量，以及阻止误按播放键时自动启动 Music
- ✨ 模块化安装与个性化：按需安装或卸载整个功能模块，权限按需申请，面板分区可重排隐藏、切换紧凑布局，设置可导出到其他 Mac 或放进 dotfiles
- 👥 适合谁：希望用一个开源工具替掉一堆付费小 App 的 Mac 用户，尤其是注重隐私、爱折腾配置的开发者。

`Swift` · Fork 1,705 · 🔗 [官网](https://vorssaint.com)

### 7. [CYQawa/YunX](https://github.com/CYQawa/YunX) — ⭐ 7,147（今日 +153）

> 粘贴分享链接就能高速下载的 Android 网盘与视频解析下载开源应用

云析（YunX）是一个 Kotlin 写的 Android 开源应用，专门解决「别人发来网盘或短视频链接，却要开一堆 App、手动找提取码、下载还龟速」的麻烦。把链接粘进「解析」页，它自动识别平台并补上提取码；浏览分享目录点文件即可拿到直链下载，抖音、小红书、B 站等视频与图文也能直出直链。下载使用 Range 分片并发 + 断点续传，图片视频音频可在线预览，批量下载会自动收纳成可折叠分组。

- ✨ 网盘分享链接解析：识别夸克 / UC / 迅雷 / 百度 / 139 / 123 / 115 / 光鸭 / 蓝奏云 / 蓝奏云优享版 链接，并自动匹配提取码
- ✨ 视频与图集解析：抖音 / 小红书 / 快手 / 微博 / AcFun 免登录直出直链，哔哩哔哩登录后画质更高且音视频分轨在应用内合轨（不依赖 ffmpeg），Pixiv 粘贴浏览器 Cookie 可解析全部作品
- ✨ 高速下载：Range 分片并发 + 断点续传，任务保存请求头与固定分片规划，并发上限 32
- ✨ 在线预览与播放：图片 / 视频 / 音频直接在线播放，逐请求带上 Referer / Cookie 避免直链 403，网盘里的常见文本文件也能打开
- ✨ 图集两列网格：点开可翻页、双指放大、单张下载，长按进入多选批量下载；整文件夹或一次批量下载会在下载页收成一个可折叠分组
- ✨ 多平台登录与认证备份：WebView Cookie、账号密码 / 短信验证码、JWT 等多种方式登录，并用口令派生密钥以 AES-GCM 加密备份 Cookie / JWT；复制分享链接后回应用会提示一键粘贴解析
- 👥 适合谁：常收到网盘或短视频分享链接、想少装几个 App 就高速保存素材的 Android 用户

`Kotlin` · Fork 375

### 8. [every-app/open-seo](https://github.com/every-app/open-seo) — ⭐ 27,241（今日 +141）

> 开源 SEO 工具，按需付费的 Semrush、Ahrefs 替代方案，自带 MCP 与 AI 技能。

OpenSEO 是面向普通人的 SEO 工具：如果你觉得 Semrush、Ahrefs 订阅太贵、功能太臃肿，它把关键词研究、排名追踪、竞品分析等常用工作流拆出来，做成一个简洁、可自行控制的界面。它不自带数据源，你需要绑定自己的 DataForSEO API key，用多少付多少，没有订阅费；官方托管版每月 10 美元，支持项目。最大特色是把 SEO 数据通过 MCP 暴露给 Claude Code、ChatGPT、Codex、Cursor 等 AI 代理，配合可复用的 Agent Skills，让 AI 直接干活。你可以用 Docker 在服务器上自托管，也可以用一条命令部署到自己的 Cloudflare 账户。

- ✨ 关键词研究：覆盖搜索量、难度等核心指标
- ✨ 排名追踪：持续监控目标关键词的搜索排名
- ✨ 竞品洞察：分析和对比竞争对手的 SEO 表现
- ✨ 外链分析：查看和分析反向链接数据
- ✨ 站点审计：发现站内 SEO 问题
- ✨ AI Visibility：跟踪品牌在 AI 搜索中的可见度
- 👥 适合谁：预算有限的独立开发者、SEO 从业者和小团队，以及想用 AI 代理自动化 SEO 工作流的人。

`TypeScript` · Fork 3,787 · 🔗 [官网](https://openseo.so)

### 9. [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) — ⭐ 42,364（今日 +139）

> 一款跨平台、界面友好的实时网络流量监控桌面应用，让人轻松看清电脑在连接什么。

Sniffnet 是一个用 Rust 编写的开源网络流量监控应用，把原本需要命令行抓包工具才能做的事变成可视化桌面体验。它会实时展示你机器上的网络连接、流量走向和统计数据，支持按协议、地址、应用等维度筛选和检查单个连接，还能在出现异常流量时发出通知。提供 Windows、macOS、Linux 的安装包，下载即用，界面内置多重主题和缩略图模式，并已翻译成二十多种语言。无论你是想排查后台偷跑流量的程序，还是单纯好奇网络状况，它都能让你不写一行命令就看懂网络。

- ✨ 实时监控网络流量与连接概览，图表化展示整体网络活动
- ✨ 逐个连接深入检查，查看对端地址、协议、端口等详细信息
- ✨ 按协议、IP 地址、应用等条件过滤，快速定位关注的流量
- ✨ 自定义通知规则，在满足特定条件的流量出现时提醒你
- ✨ 多种配色主题与缩略图小窗模式，可自定义界面外观
- ✨ 跨平台支持 Windows、macOS 与 Linux，并提供二十多种语言界面
- 👥 适合谁：适合想直观了解本机网络状况的开发者、运维人员，以及关心隐私与后台流量的普通用户。

`Rust` · Fork 1,992 · 🔗 [官网](https://sniffnet.app)

### 10. [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) — ⭐ 128,972（今日 +135）

> 用 Rust 编写的开源远程桌面，可自托管，是 TeamViewer 的开源替代品

RustDesk 是一个用 Rust 编写的开源远程桌面应用，定位是 TeamViewer 的自托管替代品。它开箱即用、无需配置，安装后即可建立远程连接；同时把数据的控制权完全交给你：你可以使用官方提供的 rendezvous/relay 服务器，也可以按官方文档自建服务器，甚至参照 rustdesk-server-demo 写一个自己的中继服务。官方提供 Windows、macOS、Linux 的安装包与 nightly 构建，Android 可从 F-Droid 获取，Linux 上还有 Flathub 版本；如需进阶功能可选 RustDesk Server Pro。

- ✨ 开箱即用的远程桌面连接，安装后无需额外配置即可使用
- ✨ 支持自建 rendezvous/relay 服务器，数据完全由自己掌控
- ✨ 可选用官方公共服务器，或基于 server-demo 自行实现中继服务端
- ✨ 跨平台：Windows、macOS、Linux 桌面端，Android 可通过 F-Droid 安装，Linux 另有 Flathub 版本
- ✨ 提供正式 release 与 nightly 构建，可直接下载二进制文件
- ✨ 界面与文档支持数十种语言的社区翻译，含中文、日语、法语、德语、西班牙语等
- 👥 适合谁：注重数据隐私、希望自托管远程桌面来替代 TeamViewer 的个人用户、IT 运维与企业团队

`Rust` · Fork 20,540 · 🔗 [官网](https://rustdesk.com)

## 📋 完整榜单

> ℹ️ 同一仓库 3 天内不会重复出现，往期出现过的不会重复收录

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [tidain/YunX-Desktop](https://github.com/tidain/YunX-Desktop) | 云析 YunX 官方 Windows 桌面版，粘贴分享链接即可解析并高速下载网盘、视频和 … | `Kotlin` | 4,277 | +340 |
| 2 | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | 在自有基础设施上运行 AI agent 的隔离沙箱运行时，用 Docker 起步，用 Ku… | `Python` | 17,167 | +323 |
| 3 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 一款 Claude Code 学术研究技能包，覆盖从调研到定稿的完整论文流程。 | `Python` | 56,396 | +225 |
| 4 | [orailnoor/cross-platform-llm-client](https://github.com/orailnoor/cross-platform-llm-client) | 一个 Flutter 跨平台 AI 聊天客户端，把本地 GGUF 离线推理和多家云端 AP… | `C++` | 2,143 | +211 |
| 5 | [WhiteTowerAI/ohmygame](https://github.com/WhiteTowerAI/ohmygame) | 开源的一人游戏工作室：在一个应用里用 AI 设计、生成素材、构建、试玩并发布游戏。 | `TypeScript` | 2,055 | +170 |
| 6 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | 用一个菜单栏图标替代十几个付费 Mac 工具，免费开源、无账号、无遥测。 | `Swift` | 34,057 | +166 |
| 7 | [CYQawa/YunX](https://github.com/CYQawa/YunX) | 粘贴分享链接就能高速下载的 Android 网盘与视频解析下载开源应用 | `Kotlin` | 7,147 | +153 |
| 8 | [every-app/open-seo](https://github.com/every-app/open-seo) | 开源 SEO 工具，按需付费的 Semrush、Ahrefs 替代方案，自带 MCP 与 … | `TypeScript` | 27,241 | +141 |
| 9 | [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | 一款跨平台、界面友好的实时网络流量监控桌面应用，让人轻松看清电脑在连接什么。 | `Rust` | 42,364 | +139 |
| 10 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 用 Rust 编写的开源远程桌面，可自托管，是 TeamViewer 的开源替代品 | `Rust` | 128,972 | +135 |

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
