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

# 🔥 GitHub 每日 Trending · 2026-11-10

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 10 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 今日精选（详细介绍）

### 1. [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) — ⭐ 188,091（今日 +898）

> 给 AI 编程助手加上“最懒资深开发”的思维，让它少写代码但不少写安全。

Ponytail 是一个给 AI 编程 Agent 使用的技能包（skill），相当于把团队里那位扎马尾、话不多、五十行变一行的老工程师装进你的 Agent。它要解决的是 AI 编码助手常见的过度工程：为了一个日期选择器手搓 335 行日历，或者随手引入新依赖。Ponytail 让 Agent 先看仓库里已有什么、平台已自带什么，只写任务真正需要的那部分。它的原则不是“最少 token”，而是绝不砍掉校验、错误处理、安全与可访问性——代码小是因为必要，不是因为高尔夫式删减。README 给出的对照基准显示：代码量 -53%、耗时 -41%、成本 -26%、token -45%，同时 98% 的风险逻辑带测试（不用时为 68%），还附有 20 个 Agent 的兼容说明。

- ✨ 懒人式复用优先：先检查仓库现有组件和浏览器原生能力，10 行替代手搓的 335 行日期选择器
- ✨ 克制引入依赖：不为一件事装一个库，能拼装现有能力就不新增包
- ✨ 不牺牲正确性：校验、错误处理、安全、可访问性一律保留，只删冗余
- ✨ 自带测试倾向：基准中 98% 的风险逻辑附带测试，Agent 自写测试能拦住 66% 的注入 bug（对照组 46%）
- ✨ 可量化的收益：官方基准 39 个任务（含真实 FastAPI + React 仓库），代码 -53%、时间 -41%、成本 -26%、token -45%
- ✨ 安全任务全通过：SQL 注入、路径穿越、伪造 token、限流、畸形 CSV、缓存 6 类场景 30 次运行全数通过
- 👥 适合谁：日常用 AI Agent 写业务代码、受够了过度工程和多余依赖的开发者与团队。

`JavaScript` · Fork 10,437 · 🔗 [官网](https://ponytail.dev)

### 2. [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) — ⭐ 42,184（今日 +387）

> 无分词器的端到端TTS系统，支持30种语言、音色设计与高保真克隆

VoxCPM 是一个 tokenizer-free 的文本转语音系统，采用扩散自回归架构直接生成连续语音表征，跳过离散 token 化，让合成结果更自然、更有表现力。最新版 VoxCPM2 是 2B 参数模型，基于 MiniCPM-4 骨干，用超过 200 万小时多语种语音数据训练，支持 30 种语言（含四川话、粤语等中文方言）、音色设计、可控/极致克隆与 48kHz 输出。它提供 Python API、CLI、Web Demo 以及基于 vLLM 的生产部署方式，权重与代码以 Apache-2.0 开源，可商用，也支持 SFT 与 LoRA 微调。

- ✨ 30 语种多语言合成：直接输入文本即可合成，无需语言标签；还支持四川话、粤语、吴语、东北话等 9 种中文方言
- ✨ Voice Design：只用一段自然语言描述（性别、年龄、语气、情绪、语速）就能造出全新音色，不需要任何参考音频
- ✨ 可控克隆：从一段短参考音频克隆音色，并可叠加风格引导来调整情绪、语速和表达，同时保留原始音色
- ✨ 极致克隆：同时给出参考音频和对应文本，模型从参考无缝续写，忠实还原音色、节奏、情绪与风格等每个细节
- ✨ 48kHz 录音棚级输出：接收 16kHz 参考音频，经 AudioVAE V2 非对称编解码直接输出 48kHz 音频，内置超分，无需外部升采样器
- ✨ 实时流式合成：在 NVIDIA RTX 4090 上 RTF 低至约 0.3，经 Nano-vLLM 或 vLLM-Omni 加速可到约 0.13，并提供兼容 OpenAI 的 API
- 👥 适合谁：做多语言语音合成、有声内容、虚拟人配音产品的开发者与研究团队

`Python` · Fork 4,805 · 🔗 [官网](https://voxcpm.com)

### 3. [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) — ⭐ 99,228（今日 +332）

> 美国国家安全局（NSA）开源的全功能软件逆向工程框架，支持反汇编、反编译与脚本扩展。

Ghidra 是 NSA 研究部门开发并开源的软件逆向工程（SRE）框架，最初用于解决复杂逆向任务中的规模化协作问题，同时提供一个可定制、可扩展的研究平台。它能分析 Windows、macOS、Linux 等多个平台上的编译后代码，既可以在图形界面中交互操作，也可以在自动化（批处理）模式下运行。安装只需 JDK 25 加官方发布包，解压后运行 ghidraRun 即可启动，另有 PyGhidra 入口；开发者还能用 Java 或 Python 编写脚本和扩展组件，把 Ghidra 改造成适合自己工作流的工具。

- ✨ 反汇编与汇编：查看和编辑目标程序的机器码与汇编指令
- ✨ 反编译：将编译后的二进制还原为更易读的高级语言形式
- ✨ 图形化分析：函数调用图、控制流图等可视化视图
- ✨ 脚本与扩展：支持用 Java 或 Python 编写自定义脚本，并开发 Ghidra 扩展组件
- ✨ 广泛的处理器指令集与可执行文件格式支持，覆盖多平台二进制
- ✨ 交互与自动化双模式：既可在 GUI 中分析，也可批量自动运行
- 👥 适合谁：适合逆向工程师、恶意代码分析人员、漏洞与安全研究人员，以及需要深入理解二进制程序的高校师生。

`Java` · Fork 11,270

### 4. [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) — ⭐ 78,213（今日 +326）

> 542 节开源课程，带你从零实现模型内部、检索管线和智能体运行时，边写代码边学 AI 工程。

这是一个免费的 MIT 开源 AI 工程课程仓库，目标是让你不止于调包，而是真的把东西造出来：亲手实现模型内部机制、检索管线、智能体运行时，跑测试、排查失败原因，并把代码和评测结果留成自己的作品。全站共 542 节课、20 个阶段，覆盖 Python、TypeScript、Rust、Julia、Go。你可以直接在官网按课时学习，也可以配合编码智能体跟练，或者把仓库拉到本地跑代码。官网提供三条学习路线（模型基础、LLM 系统、智能体与交付），并配有交互式实验和项目挑战，学完就能上手做真实项目。

- ✨ 完整课程体系：542 节课分成 20 个阶段，从开发环境搭建一路走到智能体工程与交付
- ✨ 三条学习路线：模型基础、LLM 系统（从提示工程起步）、智能体与交付（从智能体循环起步），可按职业方向选择
- ✨ 动手实现核心组件：模型内部、检索管线、智能体运行时都要自己写，而不是只调用现成 API
- ✨ 交互式实验：例如梯度下降可视化，20 个起点在二次损失上迭代，实时展示位置与平均损失变化
- ✨ 项目挑战与评测留存：写完要测试、检查失败案例，并把代码和评测结果保留下来作为作品
- ✨ 多语言代码示例（Python、TypeScript、Rust、Julia、Go）与 30 多种语言的 README 翻译
- 👥 适合谁：想真正理解 AI 底层、愿意动手写代码的开发者，以及从后端或前端转向 AI 工程的工程师。

`Python` · Fork 13,907 · 🔗 [官网](https://aiengineeringfromscratch.com)

### 5. [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) — ⭐ 64,045（今日 +318）

> 浏览器中的间谍卫星模拟器：把航班、船舶、卫星、地震等公开实时信号汇聚到一个 3D 地球上。

God's Eye View 把航班应答机、船舶信标、轨道根数、地震仪和公共摄像头这些本就公开的信号，放进同一个可探索的照片级 3D 地球，让你在全局态势与某架飞机、某艘船、某条街道之间自由切换。它解决的痛点在于：数据散落各处、彼此关系看不见。全部在本地浏览器运行，代码可检查、可扩展。用 Pinokio 一键安装，或在终端本地启动，不需要 API key 就能上手，需要时再在应用内填可选密钥；每一层数据都是独立模块，可以自行接入新数据源。

- ✨ 座舱视角：进入被追踪航班的机舱，镜头一路贴着下方地形飞行；另有按机型建模的 3D 机库（787、ATR-72、MQ-9 等），靠近时目标会从图标换成实体模型
- ✨ 点击追踪与 250km 联系人名单：锁定目标后绘制渐隐轨迹并展示完整元数据，追踪火灾或船只可一键交接给最近的实时摄像头
- ✨ 语音控制与语音白板：由实时 AI agent 驱动的免手操作，把标注、真实边界多边形和路线直接“说”到地球上
- ✨ 传感器滤镜与 HUD：CRT、NVG、FLIR 热成像、Noir 等 GLSL 效果叠加在真实地球上，配合屏幕空间探测框和军事风格战术 HUD
- ✨ 天气与卫星过境：GFS/ECMWF 预报风场、雷达回波、云层与闪电共用一条时间轴，可追踪 NHC/CPHC 气旋路径，还能用语音查询某颗卫星何时从头顶升起
- ✨ 分享链接与场景导演：相机、风格、图层乃至被追踪目标都能序列化进 URL（追踪目标是交接而非收藏），Director 场景可导入导出为文件或数据包，另附尼泊尔博特科西洪水回放等打包场景
- 👥 适合谁：对地理空间数据、开源情报与可视化感兴趣的开发者、记者和极客，以及想拿它做演示或视频素材的创作者。

`JavaScript` · Fork 12,618 · 🔗 [官网](https://godseyeview.ai/)

### 6. [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) — ⭐ 33,777（今日 +313）

> 一个开源、可自托管的 AI 图像与视频生成工作室，聚合 600+ 模型，无内容过滤。

Open Generative AI 是商业 AI 视频/图像平台的替代品：你不用订阅 Midjourney、Runway、Kling，而是把这套 MIT 许可的前端应用部署到自己的服务器上，通过 MuAPI 调用 600+ 模型（Flux、Midjourney、Kling、Sora、Veo 等），在 14 个工作室里生成图像、视频、音频、对口型内容和工作流。它最大的卖点是没有任何内容过滤，也不锁定在某个封闭生态里。项目由 MuAPI 提供底层模型、队列和计费能力，README 还提供白标方案：换上自己的 Logo、配色和域名，就能把它变成自己品牌的 AI 工作室并按自己的价格卖给终端用户。

- ✨ 600+ 图像与视频模型统一接入，包括 Flux、Midjourney、Kling、Sora、Veo
- ✨ 14 个独立工作室，覆盖图像、视频、音频、对口型、Cinema 和 Workflows
- ✨ 无内容过滤，不做提示词审查
- ✨ 完全自托管、MIT 许可，代码和数据都在自己手里
- ✨ 通过 MuAPI 统一调度模型、任务队列与计费，无需自建 GPU 基础设施
- ✨ 官方白标方案，支持自定义品牌、域名与定价，直接转售为自己的产品
- 👥 适合谁：想摆脱订阅制与内容审查的创作者、希望自建或转售 AI 生成产品的独立开发者与小团队。

`JavaScript` · Fork 6,419 · 🔗 [官网](https://muapi.ai/open-generative-ai?utm_source=github&utm_medium=about&utm_campaign=open-generative-ai)

### 7. [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) — ⭐ 52,820（今日 +313）

> 把 PS5 可执行文件自动重链接为 Linux、Windows 原生程序的转换工具

AnyPS5 是一个 C++ 编写的转换工具，目标是把 PS5 的可执行文件自动移植到 Linux 和 Windows 上运行。它的核心是 relinker（重链接器），会把 PS5 可执行文件转换成目标系统的原生格式，同时提供一套可动态链接的 system prx 系统库实现，不依赖模拟器，也不需要额外的运行时进程。项目还带有基于网页的转换器，文件全程留在本地设备上，不上传。官方提供了程序构建、架构说明、代码规范、技术债清单等文档，以及各游戏的兼容性讨论区。命令行遇到未支持状态会抛 C++ 异常；着色器重编译器在启用 SPIRV-Tools 的构建中可产出经过验证的 SPIR-V。仅含 relinker 的构建还能在 macOS（包括 Apple silicon）上运行。

- ✨ 自动重链接：把 PS5 可执行文件转换为 Linux、Windows 原生可执行格式
- ✨ 提供 system prx 系统库实现，支持动态链接，无需模拟器或独立运行时进程
- ✨ 着色器重编译器输出 SPIR-V，并可用 Spirv-Tools 校验结果
- ✨ 网页版转换器，所有文件处理都在本地设备完成，不上传服务器
- ✨ 输入映射支持 SDL 手柄（含摇杆与扳机），键鼠可通过 anyps5-input.ini 配置
- ✨ 仅含 relinker 的构建可在 macOS（含 Apple silicon）上运行
- 👥 适合谁：对 PS5 软件互操作性、移植研究与软件保存感兴趣的开发者和研究人员

`C++` · Fork 5,014 · 🔗 [官网](https://boykopovar.github.io/AnyPS5/)

### 8. [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) — ⭐ 118,783（今日 +299）

> 让 AI 编程助手像原始人一样省话的 Go 工具，一套安装砍掉大量 token

Caveman 是一个装在开发者本机的代理与技能包，核心主张是「能少说就少说」：让编码 agent 的回答变短、让喂给模型的日志和网页变小，但代码本身一字不改。一条命令 npx @caveman-ai/cli@latest 即可完成安装，它会自动找到你机器上的 Claude Code、Codex、Gemini CLI、OpenCode 等 30 多个 agent 并完成配置，装完直接照常用 claude 即可，用的还是你自己的 key 和 Claude Pro/Max 登录。官方实测整段会话输入 token 减少 33.2%，回复从 63 token 压到 20 token 而修复方案不变；Adobe Research、JetBrains、Elastic 都做过独立验证。

- ✨ Say less：回答压缩成电报体，代码与命令保持精确，63 token 变 20 token，还分 /caveman、/ultracave、/megacave 三档强度
- ✨ Read less：日志、JSON、CSV、测试输出在进模型之前先瘦身，整段会话输入 token 少 33.2%
- ✨ Auto：按每个请求自动挑选模型与推理强度，相同得分下比 Opus 高强度模式便宜 54%
- ✨ Blocks：code mode，agent 写过的脚本会被保留并重复执行，一次测试运行的 token 从 397 降到 76
- ✨ Waste fixes：定位 token 到底花在哪并修掉，还能在你暂停时保持 prompt 缓存是热的
- ✨ Browse：网页抓回来先压缩，页面体积缩小约 129.8 倍；另有 caveman status / caveman off 逐项开关
- 👥 适合谁：重度使用 Claude Code、Codex 等编码 agent，被 token 账单和上下文塞满困扰的开发者

`Go` · Fork 6,908 · 🔗 [官网](https://docs.caveman.so/caveman)

### 9. [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) — ⭐ 39,548（今日 +279）

> 开源全渠道客服平台，Intercom、Zendesk 的自托管替代方案。

Chatwoot 是一套可以自己部署的现代客服平台，目标是把分散在各个渠道的客户对话收进同一个收件箱。网站实时聊天、电子邮件、Facebook、Instagram、Twitter、WhatsApp、Telegram、Line、SMS 等来源的消息都会汇总到统一后台，客服不用在多个工具之间来回切换。它想解决的是商业客服软件价格高、数据不在自己手里、渠道割裂的问题：自托管意味着客户数据完全由你掌控，同时保留自动化、报表、帮助中心等成熟产品才有的能力。部署方式灵活，提供 Heroku、DigitalOcean 一键部署和 Docker、Helm 方案，开发团队也可以直接基于源码二次开发。

- ✨ 全渠道统一收件箱：网站实时聊天、邮件、社交平台、WhatsApp、Telegram、Line、SMS 等消息集中处理
- ✨ Captain AI 客服代理：自动回复常见问题，减轻人工坐席负担
- ✨ 内置帮助中心：发布帮助文章与 FAQ，让客户自助查找答案
- ✨ 团队协作能力：私有备注、@提及、标签、快捷回复、自动分配、团队与自动化流程
- ✨ 客户数据与主动触达：联系人管理、分组、自定义属性、售前表单与营销活动
- ✨ 集成与报表：Slack、Dialogflow、Shopify、Google Translate、Linear，以及对话、坐席、收件箱、CSAT 等多维报表
- 👥 适合谁：适合希望自托管、掌控客户数据的中小企业与支持团队，以及需要二次开发客服系统的开发者。

`Ruby` · Fork 9,605 · 🔗 [官网](https://www.chatwoot.com/help-center)

### 10. [DeanChensj/jiangshan-map](https://github.com/DeanChensj/jiangshan-map) — ⭐ 5,196（今日 +265）

> 把2400年中国历史装进一张可拖时间轴的交互式羊皮纸地图，从战国一路拖到今天。

这是一个开源的中国历史交互地图集：从《资治通鉴》开篇的三家分晋（公元前403年）一直画到当代，横跨18个历史时期、164张疆域与政区快照。它要解决的是读史、读诗时那个很具体的疑问——“这个地方今天在哪？疆域是怎么一步步从‘秋海棠’变成‘雄鸡’的？”用起来很直接：拖动时间轴换朝代，点里程碑看疆域增益与丧失，悬停任意古城、关隘或州府，就能看到它的古今地名沿革、辖境对应和发生过的关键事件。

- ✨ 时间轴拖拽切换18个历史时期，战国七雄、三国群雄、南北朝、五代十国、宋辽西夏大理金蒙等政权同屏高对比呈现，悬停图例即高亮其领土，点击可直飞该政权
- ✨ 多阶段疆域演化 + 朱红虚线“幽灵边界差异”叠加：在秦取巴蜀、汉武帝开河西、唐安西四镇、元宣政院辖藏、1881年收复伊犁、1898年租借地、1945年台湾光复、1946年“秋海棠”转“雄鸡”等里程碑间切换，前一时段的得失一目了然
- ✨ 时间轴上内联显示在位君主与年号，含庙号/谥号、姓名和在位区间（如“汉武帝·刘彻”“唐太宗·李世民”“清圣祖·玄烨”），并给出对应的帝王纪年
- ✨ 一级政区（郡、道、路、省）以去重的羊皮纸描边绘制，悬停可查看辖境及现代省份对应，还能开启 X-Ray 透镜把当代省界直接投到历史地图上
- ✨ 黄河改道、云梦泽与罗布泊/蒲昌海的盈缩、战国至明的长城、隋唐大运河、丝绸之路、郑和航线，以及渤海湾、苏北、长江口、珠三角的古海岸线，都随年代同步演变
- ✨ 古今地名沿革与诗词、战场地标：长安两千年间的名称变迁与重大事件，苏轼贬谪黄州写《赤壁赋》的路线，韩愈立马的蓝关，岳飞北伐前线的朱仙镇，都能在地图上点开查看
- 👥 适合谁：历史与古典诗词爱好者、读史时想对照今地的学生、需要历史地理可视化素材的开发者与教师。

`JavaScript` · Fork 608 · 🔗 [官网](https://deanchen.me/jiangshan-map/)

## 📋 完整榜单

> ℹ️ 每天只推送首次出现的新仓库，往期出现过的不会重复收录

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 给 AI 编程助手加上“最懒资深开发”的思维，让它少写代码但不少写安全。 | `JavaScript` | 188,091 | +898 |
| 2 | [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | 无分词器的端到端TTS系统，支持30种语言、音色设计与高保真克隆 | `Python` | 42,184 | +387 |
| 3 | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 美国国家安全局（NSA）开源的全功能软件逆向工程框架，支持反汇编、反编译与脚本扩展。 | `Java` | 99,228 | +332 |
| 4 | [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 542 节开源课程，带你从零实现模型内部、检索管线和智能体运行时，边写代码边学 AI 工程… | `Python` | 78,213 | +326 |
| 5 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 浏览器中的间谍卫星模拟器：把航班、船舶、卫星、地震等公开实时信号汇聚到一个 3D 地球上。 | `JavaScript` | 64,045 | +318 |
| 6 | [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | 一个开源、可自托管的 AI 图像与视频生成工作室，聚合 600+ 模型，无内容过滤。 | `JavaScript` | 33,777 | +313 |
| 7 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | 把 PS5 可执行文件自动重链接为 Linux、Windows 原生程序的转换工具 | `C++` | 52,820 | +313 |
| 8 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 让 AI 编程助手像原始人一样省话的 Go 工具，一套安装砍掉大量 token | `Go` | 118,783 | +299 |
| 9 | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | 开源全渠道客服平台，Intercom、Zendesk 的自托管替代方案。 | `Ruby` | 39,548 | +279 |
| 10 | [DeanChensj/jiangshan-map](https://github.com/DeanChensj/jiangshan-map) | 把2400年中国历史装进一张可拖时间轴的交互式羊皮纸地图，从战国一路拖到今天。 | `JavaScript` | 5,196 | +265 |

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
