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

# 🔥 GitHub 每日 Trending · 2026-11-03

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 15 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 TOP 10（详细介绍）

### 1. [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — ⭐ 11,334（今日 +2,275）

> 让 AI 代理通过系统无障碍树读取并操作桌面应用的命令行工具

agent-desktop 是 Vercel Labs 推出的命令行工具和 C 库，支持 macOS、Windows、Linux，解决的是「AI 代理怎么像人一样使用桌面软件」这个问题。它不靠截图和像素匹配，而是通过操作系统的无障碍树给窗口里每个可操作元素生成一个 ref，代理点一下 ref、再快照一次确认结果，整个循环逻辑留在你自己的代理里。安装只需 npm install -g agent-desktop，用 snapshot --app Finder -i 看界面，用 click @快照id:e8 操作元素，每条命令输出一个含 ok 和 data 或 error 的 JSON 信封。

- ✨ 快照返回 JSON 树，每个可操作元素带唯一 ref 和可用动作列表
- ✨ 基于 ref 的点击、输入、设值、勾选、展开、滚动等 56 个可操作命令
- ✨ 观察-操作-再观察的校验循环，UI 变化时返回 STALE_REF 或 AMBIGUOUS_TARGET 并提示重新快照
- ✨ 默认无头运行，不移动指针、不抢焦点，也不会合成输入造成的干扰
- ✨ 内置按版本匹配的代理技能文档，skills get desktop/platform 即可读取，也可用 npx skills 装入代理框架
- ✨ 统一的 JSON 输出契约，错误带 code、disposition 和 suggestion，明确标注可否安全重试
- 👥 适合谁：做 computer-use 代理的开发者，以及需要让 AI 操作桌面 GUI 的团队

`Rust` · Fork 775 · 🔗 [官网](https://agent-browser.dev/desktop)

### 2. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) — ⭐ 111,200（今日 +1,803）

> 为 AI 编程助手打造的持久记忆压缩系统，让跨会话的上下文不再丢失。

claude-mem 是一个面向 Claude Code 等 AI 编程助手的持久化记忆系统。它解决的是每个开发者都遇到过的痛点：会话一结束，助手对项目的理解就清零，下次开工得从头解释。它会在会话过程中自动记录助手调用过的工具、做过的操作，用 AI 把这些原始记录压缩成语义摘要存起来，等到未来的会话再把相关上下文注入回去，让助手真正“记得”你的项目。安装只需一条 npx 命令，按你使用的 IDE 选择对应参数即可，Node 20 起步，Apache 2.0 开源。

- ✨ 自动捕获会话中助手的所有工具调用与操作观察，无需手动记录
- ✨ 用 AI 将冗长的原始日志压缩为语义摘要，保留关键信息而非堆砌原文
- ✨ 在新会话中自动检索并注入相关历史上下文，保持项目知识的连续性
- ✨ 提供 MCP 搜索工具，让助手主动查询过往会话记忆
- ✨ 支持 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等多种 agent 与 IDE
- ✨ 可通过配置文件调整行为，并有完整文档与故障排查指引
- 👥 适合谁：长期用 Claude Code 等 AI 助手做项目的开发者，尤其是需要跨多次会话推进同一代码库的人。

`TypeScript` · Fork 9,689 · 🔗 [官网](https://claude-mem.ai)

### 3. [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) — ⭐ 93,627（今日 +706）

> 一个 Python 爬虫框架，把请求、隐身浏览器、解析和并发爬取整合在一起

Scrapling 是一个 Python Web 抓取框架，把快速 HTTP 请求、隐身浏览器、强大的选择器解析和并发爬取整合到同一个库里。它解决的是爬虫工作流被拆散的问题：静态页面、需要渲染 JavaScript 的页面、需要交互的站点，都可以用同一套 API 处理，还能顺带抓取页面背后 API 调用返回的数据。写爬虫时可以直接使用可复用会话、代理轮换、自动重试、暂停/恢复和内置数据导出。除了 Python 代码，你还能从终端 CLI 调用它，或通过内置的 MCP server 与 Agent Skill 让 AI agent 直接驱动它，从抽取几个字段到把一个网站整站抓成干净的 Markdown 都能覆盖。

- ✨ 多种抓取请求方式统一：静态请求、浏览器渲染、页面交互与背后 API 数据抓取
- ✨ 强大的选择器解析能力，用于从 HTML 中精确提取字段
- ✨ 爬虫支持可复用会话、代理轮换、自动重试与暂停/恢复
- ✨ 内置数据导出，可把整站内容整理成干净的 Markdown
- ✨ 终端 CLI 直接调用，无需写 Python 脚本
- ✨ MCP server 与 Agent Skill，让 AI agent 直接使用抓取能力
- 👥 适合谁：需要从简单请求扩展到整站爬取的 Python 开发者、数据采集工程师，以及想给 AI agent 接入抓取能力的团队

`Python` · Fork 9,834 · 🔗 [官网](https://scrapling.readthedocs.io/en/latest/)

### 4. [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) — ⭐ 40,149（今日 +509）

> 完全独立开发的动态平铺 Wayland 合成器，颜值与可定制性兼得。

Hyprland 是一个 100% 独立实现的动态平铺 Wayland 合成器——不基于 wlroots、libweston、kwin 或 mutter，而是自己啃下了合成器的底层实现。它要解决的是 Linux 桌面长期以来的两难：平铺窗口管理器高效但往往简陋，好看的桌面又难深度定制。Hyprland 两边都要——提供最新 Wayland 特性、即时生效的配置重载、socket 化 IPC，以及一整套视觉与交互上的细节体验。安装、快速上手与配置都可以在官方 wiki 找到，改完配置保存即生效，适合按自己的手感逐步调教。

- ✨ 丰富的视觉表现：渐变边框、多种模糊、动画、发光与阴影
- ✨ 自定义贝塞尔与弹簧曲线，动画手感可精细调节
- ✨ 强大的插件生态与内置插件管理器
- ✨ 100% 独立实现，不依赖 wlroots/libweston/kwin/mutter
- ✨ 窗口形态齐全：平铺、伪平铺、浮动、全屏，外加窗口组（标签模式）与特殊工作区（scratchpad）
- ✨ 布局体系灵活：Dwindle、Scrolling、Master、Monocle，支持按工作区切换布局与 Lua 自定义布局
- 👥 适合谁：适合追求高效平铺操作、又不想牺牲桌面美观的 Linux 用户，尤其是喜欢折腾配置和插件的人。

`C++` · Fork 2,162 · 🔗 [官网](https://hypr.land)

### 5. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) — ⭐ 34,066（今日 +1,379）

> 把单次 Claude Code 会话变成 49 个 AI 角色组成的游戏开发工作室

这是一个为 Claude Code 准备的配置工程：49 个按真实工作室层级组织的 AI 子代理、74 个覆盖全流程的斜杠命令、15 个钩子和 14 条路径级编码规范。它解决的是单人用 AI 做游戏时缺乏结构的问题——没人拦你硬编码魔法数字、跳过设计文档、写面条代码，也没有 QA 和设计评审。装上之后，导演层守愿景、部门主管管领域、专家动手干活，每个角色有明确职责和升级路径；你依然做所有决策，但会有人提前问对问题、及早抓错，从头脑风暴到上线都保持有序。

- ✨ 49 个专业代理分三层：3 位导演、8 位部门主管、38 位专家，覆盖设计、程序、美术、音频、叙事、QA、制作
- ✨ 74 个斜杠命令串起完整工作流：/start、/design-system、/create-epics、/create-stories、/dev-story、/story-done 等
- ✨ 内置 Godot 4、Unity、Unreal Engine 5 三套引擎专属代理，各带子专家（GDScript/Shader/GDExtension、DOTS/Addressables/UI Toolkit、GAS/蓝图/网络同步/UMG）
- ✨ 15 个钩子在提交、推送、资源变更、设计文档读写和会话生命周期上自动校验，并保留代理审计轨迹与缺口检测
- ✨ 14 条按路径生效的编码规范，编辑玩法、引擎、AI、UI、网络代码及场景资源文件时自动约束
- ✨ 62 份文档模板，涵盖 GDD、UX 规格、ADR、冲刺计划、HUD 设计、无障碍等产出物
- 👥 适合谁：用 Claude Code 独立或小团队做游戏的开发者，尤其是需要设计文档与质量关卡的个人开发者

`Shell` · Fork 4,560

### 6. [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) — ⭐ 16,375（今日 +653）

> 在消费级硬件上本地运行 290B+ MoE 大模型的边缘推理引擎

FreeToken 是一个面向个人电脑和工作站的 MoE 推理引擎，目标是把原本只在数据中心才能跑的开放权重超大模型搬到你已经拥有的硬件上。它把 GPU、CPU、主机内存和互联带宽当成一个统一、可弹性伸缩的推理平台，通过带宽自适应的 CPU-GPU 协同执行，让你在自己的游戏主机上以交互级速度跑 290B+ 级别的 MoE 模型。使用上可以直接下载 Windows/Linux 桌面应用（自带 GUI，可运行模型、对话和调参），也可以用 uv/pip 安装命令行版本接入自己的工具链。

- ✨ 边缘原生高性能运行时：带宽自适应的 CPU-GPU 协同执行（q* 策略）、全层双缓冲 prefill 流式加载、全局 LRU 专家缓存、图兼容执行，以及 FTW 快速权重格式
- ✨ 语义感知缓存：为循环状态和 KV 缓存提供语义锚点检查点，Agent 的工具调用、思考块等上下文编辑无需重复计算整段上下文
- ✨ 弹性显存管理：运行时可在专家缓存与 KV 内存之间动态重新分配显存，无需重启引擎或重新加载权重
- ✨ 广泛的 MoE 与生态支持：支持 DeepSeek-V4-Flash、Qwen3.6-35B-A3B、GLM-5.2 等前沿开放权重 MoE 模型，覆盖多种参数规模和 MXFP4/NVFP4/FP8/BF16 量化格式
- ✨ 开箱对接现有 Agent 工具：提供 Anthropic/OpenAI 兼容 API，可直接接 Codex、Claude Code、OpenCode、OpenClaw、DeepSeek Harness 等编码与工具调用 Agent
- ✨ 覆盖常见消费级硬件：从笔记本、游戏台式机到工作站 GPU 均可扩展，原生支持 NVIDIA RTX 30/40/50 系列
- 👥 适合谁：想在本地或消费级硬件上跑大模型的开发者、Agent 用户和研究者

`Python` · Fork 1,604 · 🔗 [官网](flashml.ai)

### 7. [pingdotgg/t3code](https://github.com/pingdotgg/t3code) — ⭐ 42,890（今日 +3,229）

> T3 Code 是 agent 控制台，可用手机、网页或桌面端远程操控本机上的编码智能体。

T3 Code 是一个「agent harness 控制面」：它自己不训练模型，而是接管你电脑上已经装好并登录的编码智能体，让你在 iOS、Android、网页和 Electron 桌面端统一查看和控制它们运行。它解决的是 agent 只能在单机终端里跑、离开工位就断线的问题，并沿用你已有的 Claude Code、Codex、Cursor 等订阅，不必另买 API key。装一行 curl 脚本或 npx t3@latest 即可试用；运行 t3 会启动服务并打开本地 Web 应用，t3 service install 能让它常驻后台，再从手机远程接入。

- ✨ 一个界面统管本机多个编码智能体：Claude Code、Codex、Cursor、Grok Build、OpenCode、Antigravity、fx
- ✨ iOS、Android、Web、Electron 桌面四端覆盖，支持从手机或另一台机器远程访问
- ✨ 复用你已有的订阅和 CLI 登录状态，前提是这些工具已在本机安装并认证
- ✨ 安装轻量：一行 curl / PowerShell 脚本，或 npx t3@latest 免安装试用，t3 update 升级
- ✨ 可注册为后台服务常驻运行，并支持通过 MCP 让外部 agent 接入
- ✨ 提供权限模式、键盘快捷键、项目设置、外观偏好和多账号切换等细粒度控制
- 👥 适合谁：已经在用 Claude Code、Codex 等命令行 agent 写代码，并希望多端或远程操控它们的开发者。

`TypeScript` · Fork 9,158 · 🔗 [官网](https://t3.codes)

### 8. [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) — ⭐ 46,192（今日 +857）

> 首个开源金融K线基础模型，预训练覆盖45+全球交易所，可做K线序列预测。

Kronos是专门针对金融市场K线序列（OHLCV）预训练的decoder-only基础模型家族，不同于通用时间序列模型，它针对金融数据的高噪声特性做了专门设计：先用专用tokenizer把连续多维K线数据量化成分层离散token，再在这些token上预训练自回归Transformer，从而作为一个统一模型服务多种量化任务。使用上，加载Hugging Face上的tokenizer和模型后，用KronosPredictor几行代码即可完成预处理、归一化、预测与反归一化，得到未来K线预测；项目还提供微调脚本，便于适配自有任务。

- ✨ 首个开源的金融K线（candlestick）基础模型，预训练数据来自45+全球交易所
- ✨ 分层离散tokenizer将连续多维OHLCV K线量化成token，再由自回归Transformer建模
- ✨ KronosPredictor封装预处理、归一化、预测和反归一化，几行代码完成预测
- ✨ 提供Kronos-mini、small、base、large多种规格模型，参数从4.1M到499.2M，按算力需求选择
- ✨ 模型权重托管在Hugging Face Hub，可直接from_pretrained加载
- ✨ 提供微调脚本，可将Kronos适配到自己的量化任务
- 👥 适合谁：量化研究者、金融时序预测开发者，以及想把K线基础模型微调到自己任务的人。

`Python` · Fork 7,614

### 9. [kornia/kornia](https://github.com/kornia/kornia) — ⭐ 12,275（今日 +412）

> 基于 PyTorch 的可微分计算机视觉库，把 1200+ 图像处理与几何视觉算子做成可批量、可求导的 GPU 模块。

Kornia 是一个构建在 PyTorch 之上的可微分计算机视觉库：它把图像变换、增强、相机模型、对极几何、最小求解器、特征检测与匹配等算法，实现为可直接接入现有 AI 工作流的张量算子，让这些运算支持批处理、自动求导与 GPU 加速。当你用 torchvision 凑不齐算子、手写实现又长又脆、或者算法必须保留梯度时，它就是替代方案。安装后像普通 PyTorch 模块一样调用即可，还提供浏览器 Playground、教程与示例仓库。

- ✨ 提供 1200+ 公开算子，覆盖 torchvision 基本没有的领域：相机模型与对极几何、最小求解器与 RANSAC、特征检测、描述与匹配、边缘检测、形态学、Lab 与 Bayer 色彩、图像损失与指标
- ✨ 单次批调用支持逐样本参数：gaussian_blur2d 接受 (B,2) 的 sigma，rotate 接受 (B,) 角度，warp_affine 与 warp_perspective 接受 (B,2,3) 和 (B,3,3) 矩阵，无需逐图循环
- ✨ 批量最小求解器与鲁棒估计：find_fundamental 支持 7 点法并返回全部实数解，另有 8 点法、5 点本质矩阵、DLT 单应与 solve_pnp_dlt，RANSAC 在设备上采样与打分
- ✨ 可微分几何：depth_to_3d_v2、unproject_points、project_points、warp_frame_depth、remap，支持 Brown–Conrady 与 Kannala–Brandt 畸变相机模型，以及 So3/Se3 李群，梯度可回传到深度、位姿和相机参数
- ✨ 标注同步增强：AugmentationSequential 用同一个采样变换同时作用于图像、掩码、框和关键点，并支持可逆的 2D 增强；CUDA 上参数迁移不会阻塞主机
- ✨ GPU 上的局部特征与匹配：SIFT、HardNet、DISK、ALIKED、XFeat、DeDoDe、LoFTR、LightGlue，配套互为最近邻与比率测试匹配器，并有任意结构元素的批量形态学
- 👥 适合谁：需要批量、可求导、跑在 GPU 上的视觉算法研究者与工程师，尤其是做几何视觉、3D 与空间 AI 的 PyTorch 用户。

`Python` · Fork 1,505 · 🔗 [官网](https://kornia.readthedocs.io)

### 10. [JustVugg/colibri](https://github.com/JustVugg/colibri) — ⭐ 46,867（今日 +675）

> 纯 C 编写的小引擎，让你在现有电脑上跑千亿参数 MoE 大模型，专家按需从磁盘流式读取。

colibri 解决的是一个具体问题：想在本机跑几百亿到上千亿参数的开源大模型，但显存和内存都不够。它利用 MoE 模型每个 token 只激活一小部分专家的特性，把常驻部分留在 RAM，其余专家在需要时从磁盘读取，因此不需要 GPU 也能跑。整个引擎用纯 C 写，零依赖，每个模型家族一个文件。上手很简单：Windows 双击 START-HERE.bat，Linux 和 macOS 跑 ./start-here.sh，脚本会自动检测内存、磁盘和显卡，推荐能装下的模型，编译或下载预编译引擎，断点续传下载模型，然后启动并打开网页控制台，同时给出 OpenAI 与 Anthropic 兼容的接口地址。

- ✨ 专家流式加载：不常用的 MoE 专家放在磁盘上按需读取，只有常驻权重和最小专家缓存占用内存，744B 模型常驻约 9.9 GB
- ✨ 十三个引擎覆盖十余个模型家族：GLM-5.2/5.3、Kimi K3、DeepSeek V4 Flash、Qwen3.6、OLMoE 等语言模型，另有 Qwen-Image-2.1 出图与 Laya、GLiNER2.5-Decide 决策模型
- ✨ 直接读取社区已发布的 GGUF 文件，无需转换格式，原样加载
- ✨ 纯 C 实现，零依赖，每个模型家族一个文件，不强制要求显卡；可用 CPU，也可通过 Vulkan 走任意 GPU，或通过 CUDA 走 NVIDIA 卡
- ✨ 一步式安装脚本：自动探测内存、空闲磁盘、CPU 与 GPU，推荐装得下的模型，缺少编译器时回退到预编译版本，缺少依赖时打印确切的安装命令后继续用 CPU 跑
- ✨ 模型下载支持进度显示和断点续传，中断后重跑会从断开处继续
- 👥 适合谁：想在消费级硬件或已有工作站上本地跑大模型的开发者、研究者与爱好者，8 GB 内存起步即可。

`C` · Fork 5,412 · 🔗 [官网](https://justvugg.github.io/colibri)

## 📋 完整榜单

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 让 AI 代理通过系统无障碍树读取并操作桌面应用的命令行工具 | `Rust` | 11,334 | +2,275 |
| 2 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 为 AI 编程助手打造的持久记忆压缩系统，让跨会话的上下文不再丢失。 | `TypeScript` | 111,200 | +1,803 |
| 3 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 一个 Python 爬虫框架，把请求、隐身浏览器、解析和并发爬取整合在一起 | `Python` | 93,627 | +706 |
| 4 | [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) | 完全独立开发的动态平铺 Wayland 合成器，颜值与可定制性兼得。 | `C++` | 40,149 | +509 |
| 5 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 把单次 Claude Code 会话变成 49 个 AI 角色组成的游戏开发工作室 | `Shell` | 34,066 | +1,379 |
| 6 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | 在消费级硬件上本地运行 290B+ MoE 大模型的边缘推理引擎 | `Python` | 16,375 | +653 |
| 7 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | T3 Code 是 agent 控制台，可用手机、网页或桌面端远程操控本机上的编码智能体。 | `TypeScript` | 42,890 | +3,229 |
| 8 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | 首个开源金融K线基础模型，预训练覆盖45+全球交易所，可做K线序列预测。 | `Python` | 46,192 | +857 |
| 9 | [kornia/kornia](https://github.com/kornia/kornia) | 基于 PyTorch 的可微分计算机视觉库，把 1200+ 图像处理与几何视觉算子做成可批… | `Python` | 12,275 | +412 |
| 10 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 纯 C 编写的小引擎，让你在现有电脑上跑千亿参数 MoE 大模型，专家按需从磁盘流式读取。 | `C` | 46,867 | +675 |
| 11 | [mattpocock/skills](https://github.com/mattpocock/skills) | Matt Pocock 日常自用的 AI 编程助手技能集，小而可组合，帮你做真工程，而不是… | `Shell` | 310,707 | +858 |
| 12 | [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | 把 git worktree 变得像分支一样简单的 CLI，专为并行跑 AI 编程代理而设… | `Rust` | 10,208 | +77 |
| 13 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 开源的多 AI Agent 团队编排应用，像管理公司一样管理 AI 员工团队。 | `TypeScript` | 110,666 | +412 |
| 14 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | 单台 GPU 节点上训练 LLM 的极简实验框架，约 48 美元即可复现 GPT-2 级别… | `Python` | 60,115 | +321 |
| 15 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | 免训练修改语言模型行为：去审查、压废话、降谄媚，本地机器就能跑。 | `Python` | 38,388 | +420 |

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
