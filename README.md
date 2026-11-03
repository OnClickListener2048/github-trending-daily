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

## 🏆 今日之星 TOP 10（详细介绍）

### 1. [pingdotgg/t3code](https://github.com/pingdotgg/t3code) — ⭐ 42,540（今日 +3,229）

> T3 Code 是一个本地 AI 编程代理的统一控制台，支持手机、网页和桌面多端远程操作。

T3 Code 把自己定位为 "agent harness control surface"（代理框架控制界面）：它本身不是模型，也不卖服务，而是在你电脑上启动一个本地服务，接管你已经安装并登录的 AI 编程代理，包括 Claude Code、Codex、Cursor、Grok Build、OpenCode、Antigravity 和 fx。你可以继续使用已有的订阅，用 iOS、Android、网页或 Electron 桌面端来驱动这些代理，并且可以远程从手机或另一台机器接入。作者称灵感来自 Codex 桌面版、Conductor、Claude Desktop、Cursor Glass，但认为它们都不够好，于是自己做了个性能好、可远程操作、真正开源、随时可 fork 的版本。安装方式灵活：一条 curl 命令安装 CLI（Windows 为 PowerShell），也可以 npx 直接试用；桌面端覆盖 winget、scoop、Homebrew、deb、AUR、Nix。项目仍处于早期，作者提醒会有 bug，而且基本不接受大型贡献。

- ✨ 统一接管本机已登录的多种 AI 编程代理：Claude Code、Codex、Cursor、Grok Build、OpenCode、Antigravity、fx
- ✨ 多端接入：iOS、Android 移动应用，网页应用，以及基于 Electron 的桌面应用
- ✨ 远程访问：可从手机或另一台机器控制运行在家用电脑上的代理
- ✨ CLI 工具 t3：一键启动服务并打开本地 Web 应用，支持 service install 后台常驻和 t3 update 升级
- ✨ 覆盖主流包管理器的桌面端分发：winget、scoop、Homebrew、.deb、AUR（含 nightly 频道）、nixpkgs
- ✨ 支持多账号，例如 Claude 与 Codex 可分别配置多套账号；还可通过 MCP 把 T3 Code 接入其他外部代理
- 👥 适合谁：已经在用 Claude Code、Codex 等 AI 编程代理，希望多端和远程操控、又重视开源的开发者。

`TypeScript` · Fork 9,136 · 🔗 [官网](https://t3.codes)

### 2. [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — ⭐ 10,833（今日 +2,275）

> 让 AI agent 通过操作系统无障碍树观察并操作桌面应用的命令行工具

agent-desktop 是 Vercel Labs 推出的 CLI 与 C 库，支持 macOS、Windows 和 Linux。它不借助像素匹配或模拟鼠标键盘，而是通过操作系统无障碍树给桌面应用做快照，为每个可操作元素生成 ref；agent 对 ref 执行点击、输入、滚动等动作后，再次快照进行校验，整个循环留在你自己的 agent 里。默认无头执行，不抢占焦点也不移动指针。用 npm 全局安装即可，每条命令都输出统一的 JSON envelope。

- ✨ 快照返回完整的 JSON 元素树，每个可交互元素带 ref、角色、名称和可用动作列表
- ✨ 提供 60 个命令名、56 个可用操作，覆盖观察、ref 操作、键盘鼠标三类场景
- ✨ ref 严格绑定所属快照，UI 变化时返回 STALE_REF 或 AMBIGUOUS_TARGET，强制重新快照而不是盲目重试
- ✨ 默认无头执行，通过无障碍 API 完成操作，不移动指针也不抢焦点；只有加 --headed 才允许物理输入
- ✨ 二进制内置与版本匹配的技能文档，skills get desktop 和 skills get platform 让 agent 自己学会循环、校验、重试规则与平台差异
- ✨ 面向元素密集的应用支持先用 skeleton 加 compact 做骨架映射，再用 --root 钻取单个区域，避免一次拉取过大的树
- 👥 适合谁：做桌面端 computer use 的 AI agent 开发者，以及需要在 macOS、Windows、Linux 上构建 GUI 自动化流程的工程师。

`Rust` · Fork 724 · 🔗 [官网](https://agent-browser.dev/desktop)

### 3. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) — ⭐ 111,060（今日 +1,803）

> 为 AI 编程 Agent 提供跨会话持久记忆：自动记录会话过程，用 AI 压缩成摘要，并在未来的会话中回注相关上下文。

claude-mem 是一个面向开发者、用于 AI 编程 Agent 的持久记忆压缩系统，最初为 Claude Code 打造，同时兼容 Codex、Gemini、Copilot、OpenCode、Grok Bot 等多家 Agent。它解决的是每个开发者都遇到的痛点：会话一结束，Agent 对项目的了解就归零，下次还得重新解释架构、约定和上次改到哪。装上之后，它会在后台自动捕获 Agent 在会话中做了哪些事，包括工具调用等；再用 AI 把这些原始记录压缩成语义摘要存起来；新会话开始时，它会把与当前任务相关的记忆重新注入上下文。安装很轻量，一条 npx claude-mem install --ide <你的 IDE/Agent> 即可，针对没有 host hooks 的环境（如 Grok Bot）也做了适配。

- ✨ 跨会话持久记忆：会话结束后仍保留对项目的认知，新会话不用从头交代背景
- ✨ 自动捕获会话行为：记录 Agent 在会话中的工具使用与操作轨迹，无需手动写笔记
- ✨ AI 语义压缩：把冗长的原始操作记录压缩成精炼摘要，控制上下文开销
- ✨ 上下文智能回注：在新会话中自动挑选并注入与当前任务相关的历史记忆
- ✨ 多 Agent 兼容：支持 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等
- ✨ MCP 搜索工具：提供搜索接口，让 Agent 主动检索过往记忆
- 👥 适合谁：长期用 AI 编程 Agent 做同一项目、苦于每次会话都要重新交代背景的开发者

`TypeScript` · Fork 9,680 · 🔗 [官网](https://claude-mem.ai)

### 4. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) — ⭐ 33,898（今日 +1,379）

> 把单次 Claude Code 会话变成 49 个 AI 角色组成的完整游戏工作室

这是一个面向 Claude Code 的开源配置模板，包含 49 个 AI 子代理、74 个斜杠命令技能、15 个自动化钩子、14 条按路径生效的编码规则和 62 份文档模板。它解决的核心问题是：单靠一个通用 AI 助手做游戏，没有设计评审、没有 QA、没人拦你写魔法数字和意大利面代码。装好后，你的会话会被拆成导演、部门主管、专家三层工作室架构，每个角色有明确职责和质量关卡；通过 /start、/design-system、/create-epics、/dev-story 等命令覆盖从头脑风暴到上线的完整流程。最终决策权仍在你手里，但会有人替你问对问题、提早发现错误。

- ✨ 49 个专用子代理，分导演、部门主管、专家三层，覆盖设计、程序、美术、音频、叙事、QA、制作
- ✨ 74 个斜杠命令技能，贯穿 /start 上手、系统设计、Epics/Stories 拆分、开发与验收全流程
- ✨ Godot 4、Unity、Unreal Engine 5 三套引擎专属代理，各含 GDScript/着色器/GAS 等子专家
- ✨ 15 个自动化钩子，在提交、推送、资产变更、文档读写、会话生命周期等节点做校验
- ✨ 14 条路径作用域编码规则，编辑玩法、引擎、AI、UI、网络、场景与资产文件时自动生效
- ✨ 62 份文档模板，含 GDD、UX 规格、ADR、冲刺计划、HUD 设计、无障碍等
- 👥 适合谁：用 Claude Code 独立开发或小团队做游戏的开发者，希望借助流程约束提升项目质量

`Shell` · Fork 4,543

### 5. [mattpocock/skills](https://github.com/mattpocock/skills) — ⭐ 310,533（今日 +858）

> 一套小而可组合的 AI 编码代理技能集，帮助开发者做真正的工程实践。

这是 Matt Pocock 从自己 .agents 目录里整理出来的日常 AI 编码技能集合。它针对的痛点很明确：现有的 GSD、BMAD、Spec-Kit 等方案替你把整个流程管起来，代价是失去控制权，流程本身出问题还很难排查。这些技能则刻意做小、易改、可组合，不绑定具体模型，每个技能对应一种常见失效模式的修法，比如开工前先用“拷问”让代理把需求问清楚，或先建立共享术语表让代理少说废话。安装方式按代理区分：Claude Code、Codex、GitHub Copilot 走插件自动更新，Gemini CLI 和其他代理可手动安装或通过 npx skills 拉取可编辑文件；装完先在仓库里跑一次 /setup-matt-pocock-skills 配置好 issue tracker、标签和文档位置即可使用。

- ✨ /grill-me 与 /grill-with-docs：开工前由代理反向提问、深挖需求，解决“代理没做我想要的”这一最常见错位问题
- ✨ 共享语言（术语表）机制：用一份文档帮代理解读项目行话，减少啰嗦表达和理解偏差
- ✨ 按代理区分的安装路径：Claude Code、Codex、GitHub Copilot 支持插件自动更新，Gemini CLI 等走手动或 npx 安装
- ✨ /setup-matt-pocock-skills 一次性初始化：选择 issue tracker（GitHub、GitLab、本地文件或自定义）、配置 triage 标签、指定文档存放位置
- ✨ /triage 等面向真实工程流程的技能，覆盖分诊、文档等日常环节
- ✨ 技能刻意保持小体积、易改造、可自由组合，不锁定模型，鼓励使用者改成自己的版本
- 👥 适合谁：使用 Claude Code、Codex、Copilot 等编码代理，想要可控、可改造工作流的开发者。

`Shell` · Fork 26,122 · 🔗 [官网](https://aihero.dev/skills)

### 6. [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) — ⭐ 46,119（今日 +857）

> 首个开源金融K线基础模型，在45+全球交易所数据上预训练，提供预测与微调能力。

Kronos 是一个专门为金融市场「语言」——K线序列——打造的开源基础模型系列，采用 decoder-only 架构，在超过 45 个全球交易所的数据上预训练。它不像通用时间序列模型那样忽视金融数据的高噪声特性，而是用两阶段框架解决问题：先用专用 tokenizer 把连续的多维 OHLCV 数据量化成分层离散 token，再让自回归 Transformer 在这些 token 上预训练，从而用一个统一模型覆盖多种量化任务。使用上非常直接：从 Hugging Face 加载 tokenizer 与模型，实例化 KronosPredictor，它自动完成预处理、归一化、预测和反归一化，几行代码即可从原始行情得到预测结果。模型提供 mini、small、base 等多个规格，按算力和场景选择；官方还放出了微调脚本，方便适配自己的任务。

- ✨ 首个面向金融 K 线（OHLCV）的开源基础模型，预训练覆盖 45+ 全球交易所
- ✨ 两阶段框架：专用 tokenizer 将多维 K 线量化为分层离散 token，再由自回归 Transformer 建模
- ✨ KronosPredictor 一站式封装预处理、归一化、预测与反归一化，几行代码出结果
- ✨ Model Zoo 提供多规格预训练权重：Kronos-mini（4.1M）、small（24.7M）、base（102.3M），均可从 Hugging Face 直接加载
- ✨ 兼容不同上下文长度：mini 支持 2048，small/base 为 512，超长输入由 Predictor 自动截断
- ✨ 提供微调脚本，可将模型适配到自定义量化任务
- 👥 适合谁：量化研究员、金融时序建模开发者，以及想把基础模型用于行情预测的算法工程师。

`Python` · Fork 7,600

### 7. [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) — ⭐ 93,369（今日 +706）

> 一个库覆盖从单次请求到大规模爬取的完整 Web 抓取流程

Scrapling 是一个 Python 爬虫框架，把快速 HTTP 请求、隐身浏览器、强大的解析选择和并发爬取放进同一个库里。它解决抓取流程分散的问题：静态页面、需要渲染 JavaScript 的页面、需要点击交互的站点，以及页面背后 API 调用返回的数据，都能在同一套接口里拿到。编写爬虫时，可以复用会话、轮换代理、自动重试、暂停与恢复，并直接导出数据；除了用 Python 编写，也能在终端使用 CLI，或交给 AI agent 通过 MCP server 和 Agent Skill 调用。

- ✨ 按场景切换 Fetcher：从轻量 HTTP 请求到能应对反爬的隐身浏览器
- ✨ 既能处理静态页面和 JavaScript 渲染页面，也能与页面交互并抓取背后的 API 数据
- ✨ 丰富的选择器解析能力，用于精准定位并提取结构化字段
- ✨ 并发爬虫（Spiders）：复用会话、代理轮换、自动重试、暂停与恢复
- ✨ 内置数据导出，整站抓取可直接产出干净的 Markdown
- ✨ 三种入口：Python 库、命令行 CLI、通过 MCP server 或 Agent Skill 接入 AI agent
- 👥 适合谁：需要抓取网页数据的 Python 开发者和数据工程师，以及希望用 AI agent 完成采集任务的团队

`Python` · Fork 9,817 · 🔗 [官网](https://scrapling.readthedocs.io/en/latest/)

### 8. [JustVugg/colibri](https://github.com/JustVugg/colibri) — ⭐ 46,764（今日 +675）

> 纯 C 无依赖的推理引擎，让普通电脑也能跑起千亿级 MoE 大模型。

colibri 是一个用纯 C 写的轻量推理引擎，目标是在你已有的硬件上运行前沿规模的 MoE 模型。MoE 模型处理每个 token 时只用到自身一小部分专家，colibri 就只把那部分常驻内存，其余专家按需从磁盘流式读取，因此数百亿到数千亿参数的模型也能在 8 GB 内存起步的机器上跑起来。它内置 13 个引擎，覆盖 GLM-5.2/5.3、Kimi K3、DeepSeek V4 Flash、Qwen3.6 等语言模型，以及图像和决策模型，直接读取现成的 GGUF 文件，CPU 可跑，也能通过 Vulkan、CUDA 用上显卡。安装只需运行 start-here.sh 或 START-HERE.bat：脚本会检测机器配置、推荐装得下的模型、编译或下载引擎、断点续传下载权重，最后启动服务并打开浏览器面板。

- ✨ 专家流式加载：常驻内存的只有当前 token 需要的专家，其余从磁盘按需读取，README 示例中 744B 的 GLM-5.2 int4 常驻仅约 9.9 GB，32 秒内就绪
- ✨ 13 个引擎覆盖十余款前沿模型：GLM-5.2/5.3（兼跑 Mistral-Large-4）、GLM-5.3-Flash、Inkling、Kimi K3、DeepSeek V4/V4.1 Flash、MiMo-V2.6 Flash/Pro、Qwen3.8-Flash-Next、Qwen3.6（兼跑 Qwen3-Coder、Qwen3.8-27B、Flint、Muse Spark Open、LFM3-VL）、OLMoE，另有图像模型 Qwen-Image-2.1 和决策模型 Laya、GLiNER2.5-Decide
- ✨ 纯 C 实现、零依赖，每个模型家族一个文件，没有 GPU 也能运行；有显卡时可通过 Vulkan（跨平台）或 CUDA（NVIDIA）加速，脚本会判断值不值得为你的 GPU 编译
- ✨ 直接读取社区已发布的 GGUF 文件，不需要转换或重新打包
- ✨ 一步到位的安装脚本：自动探测内存、磁盘、CPU 和 GPU，推荐真正装得下的模型，缺编译器就用预编译版本，权重下载支持中断续传
- ✨ 开箱即用的浏览器 dashboard，同时暴露 OpenAI（/v1）和 Anthropic 兼容的 API 地址，现有应用改个 base URL 就能接上；配套 coli status / coli stop 管理启停
- 👥 适合谁：想在本地或私有硬件上跑大模型、但只有普通电脑的开发者、研究者与自建服务爱好者。

`C` · Fork 5,400 · 🔗 [官网](https://justvugg.github.io/colibri)

### 9. [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) — ⭐ 16,282（今日 +653）

> 把数据中心级的 MoE 推理搬到你自己的游戏本上，让 290B+ 大模型在本地以交互速度运行

FreeToken 是一个面向个人设备的边缘原生 MoE 推理引擎。它把 GPU、CPU、主机内存和互联带宽视为一个统一的弹性推理平台，让你能在游戏本、台式机或工作站上以交互级速度运行 290B+ 参数的前沿开源 MoE 模型，而不必把数据送到云端。使用方式有两种：下载 Windows/Linux 桌面应用，它自带 GUI，可聊天并调整参数；或者用 uv pip install "freetoken[accel]" 安装 CLI，也支持从源码构建。它对外提供 Anthropic/OpenAI 兼容 API，可以直接接入 Codex、Claude Code、OpenCode 等编码与工具调用 Agent。

- ✨ 带宽自适应的 CPU–GPU 协同执行，根据硬件带宽动态分配计算，在消费级机器上实现交互级吞吐
- ✨ 全层双缓冲的 prefill 流式加载、全局 LRU 专家缓存与图兼容执行，减少专家权重的重复搬运
- ✨ FTW 快速权重格式，加快模型加载与复用，并配套旧检查点修复与加载诊断脚本
- ✨ 语义感知缓存：用语义锚点 checkpoint 保存循环状态和 KV cache，当 Agent 修改上下文（工具调用、thinking 块）时避免重复计算
- ✨ 弹性显存管理：运行时可把显存动态分配给专家缓存或 KV 内存，无需重启引擎或重新加载权重
- ✨ 支持 DeepSeek-V4-Flash、Qwen3.6-35B-A3B、GLM-5.2 等前沿开源 MoE，覆盖 MXFP4/NVFP4/FP8/BF16 量化，并原生适配 RTX 30/40/50 系
- 👥 适合谁：想在本地硬件上运行大模型的开发者、独立开发者和 AI Agent 重度用户，尤其是手上有 RTX 显卡的人

`Python` · Fork 1,599 · 🔗 [官网](flashml.ai)

### 10. [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) — ⭐ 40,085（今日 +509）

> 一个独立开发、高度可定制且外观出众的动态平铺 Wayland 合成器。

Hyprland 是一个完全独立实现的动态平铺 Wayland 合成器，不基于 wlroots、libweston、kwin 或 mutter。它要解决的问题是：传统的平铺合成器往往外观简陋、动画生硬、配置受限，而 Hyprland 在保留平铺高效工作流的同时，提供了渐变边框、多种模糊、动画、发光、阴影等视觉效果，还有自定义贝塞尔曲线和弹簧曲线，让动画顺畅自然。配置保存后即时重载，可以快速调整窗口、监视器和图层的规则；它提供基于 socket 的 IPC 和全局快捷键转发，方便与脚本、状态栏以及你自己的应用集成。它还支持撕裂，有助于提升游戏性能，并提供内置插件管理器以及强大的插件生态，方便扩展布局和功能。

- ✨ 丰富的视觉效果：渐变边框、多种模糊、动画、发光、阴影
- ✨ 自定义贝塞尔与弹簧动画曲线
- ✨ 内置插件管理器与强大的插件支持
- ✨ 撕裂支持，提升游戏性能
- ✨ 配置保存后即时重载，提供强大的窗口、监视器和图层规则
- ✨ 基于 socket 的 IPC 与全局快捷键转发
- 👥 适合谁：适合追求高性能平铺工作流、又想要精致动画与视觉效果的 Linux 桌面用户和开发者。

`C++` · Fork 2,159 · 🔗 [官网](https://hypr.land)

## 📋 完整榜单

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 让 AI agent 通过操作系统无障碍树观察并操作桌面应用的命令行工具 | `Rust` | 10,833 | +2,275 |
| 2 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 为 AI 编程 Agent 提供跨会话持久记忆：自动记录会话过程，用 AI 压缩成摘要，并… | `TypeScript` | 111,060 | +1,803 |
| 3 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 一个库覆盖从单次请求到大规模爬取的完整 Web 抓取流程 | `Python` | 93,369 | +706 |
| 4 | [hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) | 一个独立开发、高度可定制且外观出众的动态平铺 Wayland 合成器。 | `C++` | 40,085 | +509 |
| 5 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 把单次 Claude Code 会话变成 49 个 AI 角色组成的完整游戏工作室 | `Shell` | 33,898 | +1,379 |
| 6 | [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) | 把数据中心级的 MoE 推理搬到你自己的游戏本上，让 290B+ 大模型在本地以交互速度运… | `Python` | 16,282 | +653 |
| 7 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | T3 Code 是一个本地 AI 编程代理的统一控制台，支持手机、网页和桌面多端远程操作。 | `TypeScript` | 42,540 | +3,229 |
| 8 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | 首个开源金融K线基础模型，在45+全球交易所数据上预训练，提供预测与微调能力。 | `Python` | 46,119 | +857 |
| 9 | [kornia/kornia](https://github.com/kornia/kornia) | 基于 PyTorch 的可微分几何计算机视觉库，为空间 AI 提供 1200+ 可微算子。 | `Python` | 12,229 | +412 |
| 10 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 纯 C 无依赖的推理引擎，让普通电脑也能跑起千亿级 MoE 大模型。 | `C` | 46,764 | +675 |
| 11 | [mattpocock/skills](https://github.com/mattpocock/skills) | 一套小而可组合的 AI 编码代理技能集，帮助开发者做真正的工程实践。 | `Shell` | 310,533 | +858 |
| 12 | [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | 为并行 AI 代理工作流设计的 Git worktree 管理 CLI，让 worktre… | `Rust` | 10,159 | +77 |
| 13 | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | Paperclip 是一个用于管理 AI 代理团队的开源应用，把多个 AI 代理当成公司员… | `TypeScript` | 110,581 | +412 |
| 14 | [karpathy/nanochat](https://github.com/karpathy/nanochat) | 用不到100美元，在单台GPU节点上训练出GPT-2级大模型的极简实验框架。 | `Python` | 60,044 | +321 |
| 15 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | 无需训练即可改造开源大模型行为的工具，在消费级显卡上就能移除审查、压制废话与谄媚。 | `Python` | 38,280 | +420 |

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
