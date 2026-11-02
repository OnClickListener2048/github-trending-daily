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

## 🏆 今日之星 TOP 10（详细介绍）

### 1. [pingdotgg/t3code](https://github.com/pingdotgg/t3code) — ⭐ 40,580（今日 +3,216）

> 一个统一控制本机多种 AI 编码代理的开源控制台，手机和桌面都能用。

T3 Code 是一个“agent harness 控制台”：它本身不提供模型，而是接管你电脑上已经装好并登录的编码代理，包括 Claude Code、Codex、Cursor、Grok Build、OpenCode、Antigravity 和 fx，让你用一个界面调度它们。它解决的问题是：这些代理各有一套命令行和窗口，分散在本地，出门在外就没法用。T3 Code 把服务器跑在你的机器上，再用 iOS、Android、网页或 Electron 桌面端连过去，从而在手机上继续操作。安装只需一行脚本，运行 t3 即可启动服务。项目完全免费开源，官方表示若方向跑偏，你可以直接 fork 出自己想要的编辑器。

- ✨ 多代理统一接管：只要是本机已安装并登录的 Claude Code、Codex、Cursor、Grok Build、OpenCode、Antigravity、fx，都能被它控制
- ✨ 远程优先：手机 App、网页端和桌面端都能连接本机服务，在外面也能继续跑代理任务
- ✨ 四种客户端形态：iOS、Android、Web（app.t3.codes）和 Electron 桌面应用，安装方式覆盖 curl 脚本、winget、scoop、Homebrew、.deb、AUR、Nix
- ✨ 命令行工具 t3：一条命令起服务并打开本地 Web 应用，t3 service install 可常驻后台，t3 update 负责升级
- ✨ 权限模式、快捷键、项目设置与外观偏好都可配置，另有源码管理集成和多账号支持（如 Codex、Claude 多账户）
- ✨ 可通过 MCP 让 Claude Code、ChatGPT 等外部代理接入，文档齐全（docs/ 下有安装、远程访问、后台服务等指南）
- 👥 适合谁：日常用多个 AI 编码代理、想统一管理并希望在手机上远程操作的开发者。

`TypeScript` · Fork 9,032 · 🔗 [官网](https://t3.codes)

### 2. [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — ⭐ 8,497（今日 +2,243）

> 基于操作系统无障碍树的桌面 Agent 工具，让 AI 稳定读取并操作任意桌面应用。

agent-desktop 是 Vercel Labs 出品的 CLI 与 C 库，让 AI Agent 真正"用"电脑：它不靠截图猜像素，而是通过 macOS、Windows、Linux 的系统无障碍树读取应用真实的 UI 结构。每次 snapshot 返回一个 JSON，为每个可操作元素分配 ref；Agent 对 ref 执行 click 等动作，再 snapshot 一次验证结果，这个"观察—操作—再观察"的循环留在你自己的 Agent 里。它默认无头运行，不移动鼠标、不抢焦点，每个命令输出统一的 ok/error 信封，出错时给出 code、disposition 和 suggestion，告诉你能不能在 safe 的情况下重试。

- ✨ snapshot 输出带 ref 的 UI 树，元素粒度可操作，无需像素匹配
- ✨ ref 严格绑定所属快照：裸 @e8 直接拒绝，UI 变化时返回 STALE_REF 或 AMBIGUOUS_TARGET 强制重新观察
- ✨ 默认无头执行，通过无障碍 API 操作，不移动指针不抢焦点；--headed 才允许物理输入
- ✨ 多窗口冲突时在错误里返回候选 window id，用 --window-id 指定；密集应用可先 --skeleton 看骨架再用 --root 钻取局部
- ✨ 跨 macOS、Windows、Linux 的 npm 安装，附带 x64/ARM64 原生二进制与平台辅助程序；macOS 通过私有命令宿主保留原生无障碍对象，避免已删除的行错误匹配到同名存活行
- ✨ 为 Agent 自带版本匹配的文档：skills get desktop / platform 讲解循环、ref、验证与重试规则，可一键装进 agent harness
- 👥 适合谁：做 computer-use Agent 的开发者，需要在桌面应用上稳定自动化与可验证重试的团队。

`Rust` · Fork 594 · 🔗 [官网](https://agent-browser.dev/desktop)

### 3. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) — ⭐ 110,383（今日 +1,799）

> 为 AI 编程助手打造跨会话持久记忆的压缩系统，自动捕捉、压缩并在后续会话注入上下文。

claude-mem 是一个面向 AI 编程 Agent 的持久记忆与上下文压缩系统，最初为 Claude Code 打造，现在也支持 OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等多种 Agent。它要解决的是 Agent 的“失忆”问题：会话一结束，之前读过的代码、做过的决策和排查过程就全没了，下次还得从头讲一遍。claude-mem 会在会话过程中自动记录 Agent 的工具调用与操作观察，用 AI 生成语义摘要压缩存储，并在之后的会话里把相关上下文重新注入。安装方式很简单，通过 npx claude-mem install --ide <你的 IDE 或 Agent> 就能接入，还配套 MCP 搜索工具，方便按需检索历史记忆。

- ✨ 自动捕捉会话中 Agent 的工具调用与操作观察，无需手动记录
- ✨ 用 AI 将原始操作压缩成语义摘要，控制上下文体积
- ✨ 在后续会话中自动注入相关历史上下文，保持项目知识连续性
- ✨ 提供 MCP 搜索工具，可按需检索过往会话记忆
- ✨ 支持 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等多种 Agent
- ✨ 通过 npx claude-mem install --ide <name> 一键接入，并提供配置项与故障排查文档
- 👥 适合谁：长期用 AI 编程 Agent 做项目的开发者，尤其是受困于会话间上下文丢失的人。

`TypeScript` · Fork 9,632 · 🔗 [官网](https://claude-mem.ai)

### 4. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) — ⭐ 33,165（今日 +1,380）

> 把单次 Claude Code 会话变成完整游戏工作室：49 个智能体、74 个技能协同作战。

Claude Code Game Studios 是一套为 Claude Code 准备的游戏开发配置模板。它解决一个人用 AI 做游戏时缺少结构的问题：没有设计评审、没有质量检查，容易硬编码、跳过设计文档、写出难以维护的代码。项目按真实工作室的层级组织 49 个专业子代理，分为总监、部门主管、专员三个层级，覆盖设计、编程、美术、音频、叙事、QA 和制作；再配合 74 个斜杠命令，把从创意脑暴、系统设计、架构决策、史诗与故事拆分、逐故事开发到上线发布的整个流程串起来。此外，15 个 hook 在提交、推送、资产变更、文档读写等环节自动校验，14 条按路径生效的规则约束玩法、引擎、AI、UI、网络等代码的写法，62 个文档模板可直接用于 GDD、UX 规格、ADR、冲刺计划等。模板同时内置 Godot 4、Unity、Unreal Engine 5 三套引擎专家代理，按项目选用即可。最终决策权仍在你手里，但每一步都有“团队”帮你提问、纠错并保持项目有序。

- ✨ 49 个专业子代理，按总监、部门主管、专员三层工作室架构组织，职责与升级路径明确
- ✨ 74 个斜杠命令贯穿全流程：/start、/brainstorm、/design-system、/create-epics、/create-stories、/dev-story、/story-done、/sprint-plan 等
- ✨ 15 个自动化 hook，在提交、推送、资产变更、设计文档读写和会话生命周期等环节做校验与审计
- ✨ 14 条按路径生效的编码规则，在编辑玩法、引擎、AI、UI、网络代码及场景资产时自动约束
- ✨ 62 个文档模板，覆盖 GDD、UX 规格、ADR、冲刺计划、HUD 设计、无障碍设计等
- ✨ 内置 Godot 4、Unity、Unreal Engine 5 三套引擎专家代理，含 GDScript/着色器、DOTS/ECS、GAS/蓝图/网络同步等子专家
- 👥 适合谁：适合用 Claude Code 独立或小团队做游戏的开发者，尤其是需要设计评审与流程约束的独立游戏作者。

`Shell` · Fork 4,487

### 5. [mattpocock/skills](https://github.com/mattpocock/skills) — ⭐ 309,902（今日 +970）

> Matt Pocock 每天自用的 AI 编码代理技能集，小而可组合，跨模型通用。

这是 Matt Pocock 从自己 .agents 目录里整理出来的代理技能（skills）集合，用来做真正的工程开发，而不是凭感觉写代码（vibe coding）。它针对 GSD、BMAD、Spec-Kit 这类“接管整个流程”的方案：那些方案虽然帮你管理流程，却拿走了控制权，一旦流程本身出错就很难排查。这里的每个技能都很小、容易改、可以自由组合，能和任意模型配合，你可以直接改动并变成自己的东西。安装只需一条命令（Claude Code、Codex、Copilot、Gemini CLI 等各有对应方式），然后在仓库里跑一次 /setup-matt-pocock-skills，告诉它你用哪个 issue tracker、分诊时打什么标签、文档存哪里，就可以开始用了。

- ✨ /grill-me 与 /grill-with-docs：开工前让代理反过来逐条追问你的需求，把沟通偏差在写代码之前解决掉
- ✨ 共享语言与术语表：给项目建立一份词汇表，让代理不再用 20 个词说清 1 个词就能说清的事
- ✨ /setup-matt-pocock-skills：每个仓库跑一次，配置 issue tracker（GitHub、GitLab、本地文件或自定义）、分诊标签和文档存放位置
- ✨ 支持主流编码代理：Claude Code、Codex、GitHub Copilot（CLI 与 VS Code）、Gemini CLI，以及 cursor、opencode、windsurf 等其他代理
- ✨ 两种更新方式可选：插件市场自动更新，或用 skills.sh / npx skills 把可编辑文件复制进项目手动维护
- ✨ 刻意保持小而可组合：不接管你的开发流程，任何模型都能用，改坏了也不难修
- 👥 适合谁：使用 Claude Code、Codex 等编码代理做真实项目、希望保留流程控制权的开发者。

`Shell` · Fork 26,073 · 🔗 [官网](https://aihero.dev/skills)

### 6. [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) — ⭐ 92,406（今日 +858）

> 一个 Python 库即可完成从单次请求到全站爬取的完整 Web 抓取流程

Scrapling 是一个把快速 HTTP 请求、隐身浏览器、强大的页面解析与并发爬取整合进同一个库的 Python 爬虫框架。它解决的核心问题是：爬虫开发者常常需要分别维护请求库、浏览器自动化、解析器、代理池和导出逻辑，而 Scrapling 把这些环节统一到同一套 API 下。它能抓取静态页面、渲染 JavaScript、模拟用户与网站交互，还能直接提取页面背后 API 调用返回的数据。使用方式很灵活：可以在 Python 代码里调用，也能在终端用 CLI 运行，还能让 AI Agent 通过 MCP server 和 Agent Skill 来驱动。

- ✨ 统一抓取能力：支持 HTTP 请求与隐身浏览器，既能处理静态页面，也能渲染 JavaScript 并模拟交互
- ✨ 页面解析与选择器：提供多种选择方法从 HTML 中精准提取字段，并能拿到页面背后 API 调用的数据
- ✨ 完整爬虫架构：用可复用的 session 组织爬虫，支持并发爬取
- ✨ 代理轮换与自动重试：内置代理轮换机制和失败自动重试，让抓取更稳定
- ✨ 暂停与恢复：爬取任务可以中途暂停再继续，不必从头重跑
- ✨ 内置数据导出：爬取结果可以直接导出，也能把整站内容整理成干净的 Markdown
- 👥 适合谁：需要从单页提取数据到全站采集的 Python 开发者、数据工程师，以及想用 AI Agent 驱动抓取的人

`Python` · Fork 9,748 · 🔗 [官网](https://scrapling.readthedocs.io/en/latest/)

### 7. [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) — ⭐ 45,824（今日 +855）

> 首个开源的金融K线基础模型，用45+交易所数据预训练，可直接预测行情。

Kronos 是第一个专门为金融K线（蜡烛图）打造的开源基础模型，用全球 45 个以上交易所的数据预训练而成，论文已被 AAAI 2026 接收。它解决的是通用时间序列模型在金融数据上「水土不服」的问题：金融数据噪声大、维度多，Kronos 先用专门的 tokenizer 把连续的 OHLCV 多维K线量化成分层离散 token，再用自回归 Transformer 在这些 token 上预训练，从而用一个模型统一支撑多种量化任务。使用上也很省心：从 Hugging Face 加载 tokenizer 和模型，套上 KronosPredictor，它自动完成预处理、归一化、预测和反归一化，几行代码就能从原始K线拿到未来走势预测。官方还提供了微调脚本，方便适配自己的任务。

- ✨ 首个面向金融K线的开源基础模型，预训练数据覆盖 45+ 家全球交易所
- ✨ 两阶段框架：专用 tokenizer 将 OHLCV 多维K线量化为分层离散 token，再由自回归 Transformer 建模
- ✨ KronosPredictor 一条龙封装：预处理、归一化、预测、反归一化全自动，几行代码出结果
- ✨ 提供 Kronos-mini / small / base 三档开源模型（4.1M 到 102.3M 参数），按算力自由选择
- ✨ 超过上下文长度自动截断，Kronos-mini 支持 2048、small/base 支持 512 的上下文
- ✨ 官方发布微调脚本，可迁移到自己的预测任务；另有 BTC/USDT 未来 24 小时的在线 Demo 可直接看效果
- 👥 适合谁：做量化研究和金融时序预测的开发者、算法交易团队，以及想把基础模型用到K线数据上的研究者。

`Python` · Fork 7,554

### 8. [JustVugg/colibri](https://github.com/JustVugg/colibri) — ⭐ 46,282（今日 +655）

> 纯 C 编写的轻量推理引擎，靠磁盘流式加载专家，在现有硬件上跑千亿级 MoE 大模型。

colibri 是一个纯 C 实现、零依赖的推理引擎，专门用来在普通电脑上运行超大规模的开源 MoE 模型。它的思路是：MoE 模型每生成一个 token 只用到一小部分专家，所以把常驻部分留在内存、其余专家放在磁盘上按需读取。它内置 13 个引擎，覆盖 GLM-5.2/5.3、Kimi K3、DeepSeek V4 Flash、Qwen3.6、OLMoE 等十来种语言模型，外加文生图和决策模型，并可直接读取已发布的 GGUF 文件。使用门槛很低：装好脚本后自动检测机器、推荐能装下的模型、编译或下载预编译引擎、断点续传下载权重，最后启动浏览器面板，并暴露 OpenAI 与 Anthropic 兼容接口，已有应用改个 base URL 就能接上。

- ✨ 专家流式加载：常驻内存的只留必要部分，其余专家从磁盘按需读取，744B MoE 模型实测常驻内存约 9.9 GB
- ✨ 纯 C 实现、零第三方依赖，一个模型家族对应一个源文件，无需 GPU 也能跑
- ✨ 13 个引擎开箱即用，含 GLM-5.2/5.3、Kimi K3、DeepSeek V4/V4.1 Flash、MiMo-V2.6、Qwen3.8-Flash-Next、Qwen3.6、OLMoE，以及 Qwen-Image-2.1 文生图与 Laya、GLiNER2.5-Decide、Clef 决策模型
- ✨ 直接读取社区已发布的 GGUF 文件，不用转换、不用重新量化
- ✨ 三种后端：CPU、Vulkan（跨厂商 GPU）、CUDA（NVIDIA），安装脚本会按硬件决定是否为 GPU 编译
- ✨ 一键安装脚本 START-HERE.bat / start-here.sh：探测内存、磁盘、CPU 与 GPU，推荐装得下的模型，下载支持断点续传，下次启动无需重新构建
- 👥 适合谁：想在消费级硬件上本地跑大 MoE 模型、又不想被 Python 框架和 GPU 显存卡住的开发者与自部署爱好者。

`C` · Fork 5,349 · 🔗 [官网](https://justvugg.github.io/colibri)

### 9. [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) — ⭐ 15,852（今日 +654）

> 把 290B+ 级 MoE 大模型跑在个人电脑上的边缘推理引擎

FreeToken 是一个面向个人和消费级硬件的 MoE 推理引擎，目标是把数据中心级的模型能力搬到你已经拥有的设备上：在游戏台式机、笔记本或工作站上，以可交互的速度运行 290B+ 参数的前沿开源 MoE 模型。它把 GPU、CPU、主机内存和互联带宽当成一个统一、弹性的推理平台，靠带宽自适应的 CPU–GPU 协同执行、全层双缓冲 prefill 流式加载和全局 LRU 专家缓存，解决显存装不下大模型的现实问题。用法上有 Windows/Linux 桌面应用（图形界面运行模型、聊天、调参），也可以用 uv 安装 CLI；对外提供 Anthropic/OpenAI 兼容 API，可直接接 Codex、Claude Code 这类编码智能体。

- ✨ 带宽自适应的 CPU–GPU 协同执行（q* 策略），配合全层双缓冲 prefill 流式加载和全局 LRU 专家缓存，在消费级硬件上跑到交互级速度
- ✨ 语义感知缓存：用语义锚点保存 recurrent state 和 KV cache，工具调用、thinking 块等上下文编辑不必重算整段上下文
- ✨ 弹性显存管理：运行时在专家缓存和 KV 内存之间动态重新分配显存，无需重启引擎或重新加载权重
- ✨ 广泛的 MoE 与量化支持：覆盖 DeepSeek-V4-Flash、Qwen3.6-35B-A3B、GLM-5.2 等模型与 MXFP4/NVFP4/FP8/BF16 格式，并提供 FTW 快速权重格式
- ✨ 提供 Anthropic/OpenAI 兼容 API，可无缝接入 Codex、Claude Code、OpenCode 等编码与工具调用智能体
- ✨ 面向消费级硬件：覆盖笔记本、游戏台式机和工作站 GPU，原生支持 NVIDIA RTX 30/40/50 系，并有开箱即用的桌面 GUI 与 CLI 两种形态
- 👥 适合谁：想在本地跑大模型、又不想添置数据中心显卡的开发者、Agent 玩家和研究者

`Python` · Fork 1,576 · 🔗 [官网](flashml.ai)

### 10. [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) — ⭐ 39,729（今日 +508）

> 独立的动态平铺 Wayland 合成器，兼顾颜值与深度可定制

Hyprland 是一个 100% 独立实现的动态平铺 Wayland 合成器，不基于 wlroots、libweston、kwin 或 mutter，代码自成一派。它要解决的是平铺窗口管理器长期存在的取舍问题：要么好看但没有动画特效，要么好看却难以深度定制。Hyprland 两者都要——渐变边框、多种模糊、辉光、阴影和自定义贝塞尔/弹簧动画曲线一应俱全，同时提供插件系统、Socket IPC、窗口/显示器/图层规则等可编程能力。安装、快速上手和配置都有官方 Wiki 指引（Install / Quick Start / Configure），配置文件保存后即时生效，不用重启会话。

- ✨ 全套视觉特效：渐变边框、多种模糊、动画、辉光、阴影，动画曲线支持自定义贝塞尔与弹簧
- ✨ 完全独立实现，不依赖 wlroots / libweston / kwin / mutter
- ✨ 强大的插件支持并内置插件管理器，可自行扩展功能与布局
- ✨ 窗口形态灵活：平铺 / 伪平铺 / 浮动 / 全屏，支持窗口组（标签模式）与特殊工作区（scratchpad）
- ✨ 布局体系丰富：Dwindle、Scrolling、Master、Monocle，可用 Lua 写自定义布局，并支持按工作区指定布局
- ✨ 面向高级用户的控制力：窗口/显示器/图层规则、全局快捷键转发给应用、Socket IPC、保存即热重载配置、原生 IME 与输入面板支持
- 👥 适合谁：适合追求高颜值桌面、愿意花时间调配置的 Linux 进阶用户与折腾党，以及想写插件扩展合成器的开发者。

`C++` · Fork 2,145 · 🔗 [官网](https://hypr.land)

## 📋 完整榜单

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 基于操作系统无障碍树的桌面 Agent 工具，让 AI 稳定读取并操作任意桌面应用。 | `Rust` | 8,497 | +2,243 |
| 2 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 为 AI 编程助手打造跨会话持久记忆的压缩系统，自动捕捉、压缩并在后续会话注入上下文。 | `TypeScript` | 110,383 | +1,799 |
| 3 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 一个 Python 库即可完成从单次请求到全站爬取的完整 Web 抓取流程 | `Python` | 92,406 | +858 |
| 4 | [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) | 独立的动态平铺 Wayland 合成器，兼顾颜值与深度可定制 | `C++` | 39,729 | +508 |
| 5 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 把单次 Claude Code 会话变成完整游戏工作室：49 个智能体、74 个技能协同作… | `Shell` | 33,165 | +1,380 |
| 6 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | 把 290B+ 级 MoE 大模型跑在个人电脑上的边缘推理引擎 | `Python` | 15,852 | +654 |
| 7 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 一个统一控制本机多种 AI 编码代理的开源控制台，手机和桌面都能用。 | `TypeScript` | 40,580 | +3,216 |
| 8 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | 首个开源的金融K线基础模型，用45+交易所数据预训练，可直接预测行情。 | `Python` | 45,824 | +855 |
| 9 | [kornia/kornia](https://github.com/kornia/kornia) | 基于 PyTorch 的可微视觉库，把图像处理与几何视觉算法搬上 GPU 并支持自动求导 | `Python` | 12,034 | +412 |
| 10 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 纯 C 编写的轻量推理引擎，靠磁盘流式加载专家，在现有硬件上跑千亿级 MoE 大模型。 | `C` | 46,282 | +655 |
| 11 | [mattpocock/skills](https://github.com/mattpocock/skills) | Matt Pocock 每天自用的 AI 编码代理技能集，小而可组合，跨模型通用。 | `Shell` | 309,902 | +970 |
| 12 | [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | 一个把 Git worktree 变得像分支操作一样简单的 Rust 命令行工具，专为并行… | `Rust` | 9,888 | +136 |
| 13 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 开源的 AI 智能体团队编排应用，像经营一家公司一样管理你的 AI 员工。 | `TypeScript` | 110,190 | +507 |
| 14 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | 一个约百美元就能从零训练出 GPT-2 级模型的最小化实验框架 | `Python` | 59,701 | +325 |
| 15 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | 无需训练就能改造本地大模型行为的工具，默认帮你去除审查拒答，也能按需抑制废话、减少谄媚等 | `Python` | 37,866 | +404 |

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
