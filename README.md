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

# 🔥 GitHub 每日 Trending · 2026-11-19

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 10 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 今日精选（详细介绍）

### 1. [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) — ⭐ 60,043（今日 +389）

> 为任意软件生成 CLI 封装，让 AI Agent 直接调用它，成为原生工具。

CLI-Anything 是一个把现有软件变成 Agent 原生工具的项目：跑一条命令，就为某个软件或服务生成一套结构化的命令行接口（CLI harness）；Cursor、Claude Code、OpenClaw、Pi、nanobot 这类 Agent 都能直接调用它，不必再依赖 GUI 或非结构化接口。它要解决的是「今天的软件给人用，明天的用户是 Agent」这个断层。用法上分两条线：一是用 pip install cli-anything-hub 安装 CLI-Hub，再用 cli-hub install <name> 浏览、安装和管理社区构建的 CLI；二是自己按 CONTRIBUTING 提交一个 harness，PR 合并后立刻出现在 Hub 上。生成出来的命令既输出 JSON，供程序解析，也输出人类可读文本，方便调试。

- ✨ 一条命令行即可让任意软件变成 agent-ready，兼容 Pi、OpenClaw、nanobot、Cursor、Claude Code 等 Agent 宿主
- ✨ CLI-Hub 社区注册中心：pip install cli-anything-hub 后用 cli-hub install <name> 一键浏览、安装、管理所有社区 CLI，合并 PR 后即时上架
- ✨ 每条命令同时提供 JSON 结构化输出和人类可读输出，Agent 解析与人工排查两不误
- ✨ 配套 preview、live preview 和 trajectory loop 机制，Agent 能反复试跑并产出真实产物：CAD 构建、3D 场景、图表、游戏玩法、字幕等，官方 Demos 覆盖 18 个应用
- ✨ 覆盖真实软件生态的现成 CLI：ArcGIS Pro 制图与地理处理、Calibre 书库、搜索、元数据、转换和导出、Joplin 笔记与同步、Obsidian 持久记忆、Sketch、Rekordbox 等
- ✨ 贡献与需求双向通道：通过 wishlist 模板请求想要支持的软件，通过 contributor signup 认领 harness，并在 2,461 项通过的单元与 e2e 测试基线上做质量把关
- 👥 适合谁：想让自家软件被 Agent 调用，或用 Agent 自动化各类桌面与专业软件的开发者。

`Python` · Fork 5,454 · 🔗 [官网](https://clianything.cc/)

### 2. [nvm-sh/nvm](https://github.com/nvm-sh/nvm) — ⭐ 96,198（今日 +237）

> POSIX 兼容的 Node.js 版本管理脚本，一条命令即可安装、切换多个 Node 版本。

nvm 是一个用 Shell 编写的 Node.js 版本管理器，按用户安装、按 shell 生效，可在 sh、dash、ksh、zsh、bash 等任意 POSIX 兼容 shell 中运行，支持 unix、macOS 和 Windows WSL。它解决的问题很直接：不同项目依赖不同 Node 版本，全局只能装一个版本时来回折腾非常麻烦。装上 nvm 后，nvm install 24 装新版本，nvm use 22 一行切回旧版本，node -v 立刻确认当前生效版本。安装方式是一条 curl 或 wget 脚本，脚本会把仓库克隆到 ~/.nvm 并自动把加载语句写进 ~/.bashrc、~/.zshrc 等配置文件。

- ✨ 一条命令安装并切换任意 Node 版本，nvm install / nvm use 即时生效
- ✨ 支持 LTS 等版本类别，可直接指定 lts/* 等别名安装长期支持版
- ✨ 读取项目目录下的 .nvmrc 文件，配合 bash/zsh/fish 的 shell 集成可在进入目录时自动切换版本
- ✨ 安装新版本时可自动迁移全局 npm 包，也可在已装版本之间迁移全局包
- ✨ 支持从文件声明默认全局包，安装时一并装上，方便统一开发环境
- ✨ 支持离线安装、使用 Node 二进制镜像源（可带 Authorization 头），以及无官方二进制平台
- 👥 适合谁：需要同时维护多个 Node 版本、复现旧项目环境的 Node 开发者与 CI 维护者。

`Shell` · Fork 10,791

### 3. [astral-sh/uv](https://github.com/astral-sh/uv) — ⭐ 92,332（今日 +258）

> Rust 编写的极速 Python 包与项目管理器，一个工具顶替 pip、poetry、pyenv 等一整排

uv 由 Astral（Ruff 的作者）用 Rust 打造，瞄准的是 Python 工具链碎片化与安装慢这两件老毛病：把 pip、pip-tools、pipx、poetry、pyenv、twine、virtualenv 等合并成一个命令。安装只要一行 curl 脚本，或者 pip install uv；之后 uv init 建项目、uv add 装依赖、uv lock 与 uv sync 管锁文件、uv run 直接跑命令和脚本。它同时提供 pip 兼容接口，原有使用习惯几乎不用改就能拿到 10-100 倍提速，macOS、Linux、Windows 全支持。

- ✨ 一个工具替代 pip、pip-tools、pipx、poetry、pyenv、twine、virtualenv 等
- ✨ 比 pip 快 10-100 倍，官方的基准测试图表直接印证
- ✨ 完整的项目管理：通用 lockfile、Cargo 风格 workspace、uv init/add/lock/sync 一条龙
- ✨ 单文件脚本可直接运行，支持内联依赖元数据（uv add --script 写入脚本）
- ✨ 能安装和切换 Python 版本（uv python install 多版本并存，按需下载）
- ✨ 以临时环境运行或全局安装 Python 包形式的 CLI 工具（uvx、uv tool install）
- 👥 适合谁：Python 开发者、数据与 ML 工程师、需要统一团队环境和 CI 流程的工程团队，以及嫌 pip 慢、工具太杂的人。

`Rust` · Fork 3,928 · 🔗 [官网](https://docs.astral.sh/uv)

### 4. [jquery/jquery](https://github.com/jquery/jquery) — ⭐ 60,069（今日 +266）

> 老牌跨浏览器 DOM 操作与 AJAX 库，现已发布 4.0.0，支持按模块裁剪体积。

jQuery 是一个经典的 JavaScript 库，用于简化 HTML 文档遍历、事件处理、动画与 AJAX 交互，帮助开发者抹平不同浏览器之间的差异。它既可以作为传统 script 标签引入，也提供 ESM 模块版本，还能在 Node、浏览器扩展等非浏览器环境中使用。版本方面，4.x 为主力全量支持，3.x 仅接收关键修复，2.x 和 1.x 已停止支持，官方建议升级到最新版本。构建也很灵活，克隆仓库后执行 npm install、npm run build 即可，产物落在 dist/ 目录；通过 --exclude 和 --include 参数可按需裁剪模块，生成定制版本。

- ✨ 跨浏览器的 DOM 选择、遍历与操作 API，统一各浏览器行为差异
- ✨ 完整 AJAX 能力，包含 $.ajax、$.get、$.post、各类 transport 与 ajax 事件简写
- ✨ 动画与特效体系，.animate() 及 slideUp 等简写，配合 css 模块使用
- ✨ 尺寸与位置方法，如 .width()、.height() 及 inner、outer 变体
- ✨ ESM 模块产物，jquery.module.js 以命名导出方式提供 jQuery 与 $
- ✨ 自定义构建，可通过 --exclude/--include 裁剪模块生成精简版本，核心 core 不可移除
- 👥 适合谁：需要兼容老浏览器、快速完成 DOM 与 AJAX 开发的前端开发者，以及维护存量 jQuery 项目的团队。

`JavaScript` · Fork 20,713 · 🔗 [官网](https://jquery.com)

### 5. [appwrite/appwrite](https://github.com/appwrite/appwrite) — ⭐ 58,322（今日 +232）

> Appwrite 是一个开源的一站式云端开发平台，内置 MCP，专为 AI 代理与开发者打造。

Appwrite 把后端所需的基础能力打包成一个统一平台：它是 MCP 和 agent-first 的开源云，既可以直接托管到 Appwrite Cloud，也可以在自己的 Docker 环境里一键自托管。你可以把 Cursor、Claude Code、Codex 这类编码代理通过官方托管的 MCP Server 接到真实项目上，让代理直接操作 Appwrite 项目；也可以照常在自己的应用里集成 SDK。项目从 Auth、数据库、存储到函数、站点、消息、实时推送、防火墙都保持模块化却彼此统一，所以从原型到生产不用中途换工具。

- ✨ Auth 用户认证：支持邮箱、短信、OAuth、匿名会话和魔法链接
- ✨ Databases 数据建模与查询，支持托管 PostgreSQL 和 MySQL
- ✨ Storage 文件存储，带压缩、加密、图片变换和访问控制
- ✨ Functions 无服务器函数，隔离运行时并支持事件驱动执行
- ✨ Sites 从 Git 部署静态、SSR、CSR 前端，带即时预览
- ✨ Messaging 统一发送邮件、短信和推送通知
- 👥 适合谁：适合想用 AI 编码代理加速开发、又需要自托管或统一后端能力的应用开发团队与独立开发者。

`TypeScript` · Fork 5,889 · 🔗 [官网](https://appwrite.io)

### 6. [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) — ⭐ 11,411（今日 +24）

> OpenVINO 是一个用于深度学习模型推理优化与跨平台部署的开源工具包。

OpenVINO 解决的是“训练好的模型怎么在真实硬件上跑得快、跑得省”这个问题。它可以把 PyTorch、TensorFlow、ONNX、Keras、PaddlePaddle、JAX/Flax 等框架训练的模型转换后直接部署，不需要原框架参与推理；也能通过 Optimum Intel 直接接入 Hugging Face Hub 上的 transformers 和 diffusers 模型。使用时先用 ov.convert_model 转换，再用 core.compile_model 指定设备编译，随后即可推理，pip install openvino 就能上手，官方还提供 Notebooks 和 C++/Python 示例。

- ✨ 推理优化：面向计算机视觉、语音识别、生成式 AI 与 NLP（含大小语言模型）等常见任务提升性能
- ✨ 多框架模型支持：兼容 PyTorch、TensorFlow、ONNX、Keras、PaddlePaddle、JAX/Flax，并可脱离原框架转换部署
- ✨ Hugging Face 集成：通过 Optimum Intel 直接使用 transformers 与 diffusers 模型
- ✨ 广泛硬件覆盖：支持 CPU（x86、ARM）、GPU（Intel 集显与独显）以及 Intel NPU 等 AI 加速器，覆盖边缘到云端
- ✨ 简单部署 API：convert_model 转换 + compile_model 指定设备编译，几行代码完成模型推理
- ✨ 丰富学习资源：OpenVINO Notebooks 提供 LLM 聊天机器人、YOLOv11 优化、文生图、LLaVa 多模态、Whisper 语音识别等实战示例
- 👥 适合谁：需要在 Intel CPU、GPU、NPU 或边缘设备上高效部署和优化深度学习模型的 AI 应用开发者。

`C++` · Fork 3,609 · 🔗 [官网](https://docs.openvino.ai)

### 7. [n8n-io/n8n](https://github.com/n8n-io/n8n) — ⭐ 211,270（今日 +325）

> 可自托管或云端的 fair-code 工作流自动化平台，原生支持构建和运营 AI 智能体。

n8n 是一个 fair-code（源码可见、可自托管、可扩展）的工作流自动化平台，把可视化画布和自定义代码结合起来。它要解决的是：AI 自动化从原型走向生产时，既能编排多步智能体、接入自有数据和模型，又能保留逻辑分支、人工审批和可观测性，而不是把业务流程绑死在某一家模型厂商上。用法很直接：有 Docker 就能用官方脚本或一条 docker run 命令在本地 5678 端口启动编辑器，也可以直接用云端版；在画布上拖拽节点搭建流程，需要时插入 JavaScript、Python 或 npm 包，再连接 1500+ 集成把 AI 接入现有系统。

- ✨ AI 原生：用自有数据、模型和工具构建并运营多步 AI 智能体与工作流
- ✨ 模型不锁定：可接 OpenAI、Anthropic、Google 或开源模型，切换供应商无需改动架构
- ✨ 从原型到生产：支持逻辑分支、工具调用、人工审批和完整可观测性
- ✨ 可视化 + 代码：画布拖拽搭建，按需嵌入 JavaScript、Python 和 npm 包
- ✨ 企业级能力：自托管部署，提供基于角色的访问控制、审计追踪，适配敏感数据
- ✨ 生态丰富：1500+ 集成与 9000+ 工作流模板，快速对接现有系统
- 👥 适合谁：需要把 AI 工作流落到生产、又想自托管掌控数据的开发者和自动化团队。

`TypeScript` · Fork 61,579 · 🔗 [官网](https://n8n.io)

### 8. [solidjs/solid](https://github.com/solidjs/solid) — ⭐ 36,695（今日 +40）

> Solid 是一个用细粒度响应式直接更新真实 DOM 的声明式 JavaScript UI 库，不依赖虚拟 DOM。

Solid 用编译器把 JSX 模板编译成真实的 DOM 操作，再用细粒度响应式精确更新数据变化所影响的那部分代码。它要解决的是虚拟 DOM diff 带来的运行时开销，以及组件反复重渲染带来的心智负担：组件函数只在挂载时执行一次，之后的更新精确到具体的 DOM 节点和表达式。用法上，用 createSignal、createMemo、createStore 声明状态，在 JSX 里读取即可自动建立依赖；更新会在微任务中批量执行，也可以调用 flush() 同步刷新。它通过 @solidjs/vite-plugin 接入 Vite，开箱即用，还支持流式 SSR 与渐进式水合。

- ✨ 细粒度响应式更新真实 DOM，没有虚拟 DOM diff
- ✨ render-once 组件：组件函数只运行一次，更新精确到单个表达式
- ✨ 声明式响应式原语：createSignal、createMemo、createStore，读取即自动追踪依赖
- ✨ 微任务批量更新，并提供 flush() 用于同步互操作
- ✨ 一等公民的异步支持：任意计算可返回 Promise/AsyncIterable，以 <Loading> 作为边界
- ✨ 乐观 UI 原语 createOptimistic/createOptimisticStore 与结构化 action 变更
- 👥 适合谁：适合追求极致运行时性能、喜欢 JSX 与 TypeScript、希望组件逻辑简单可预测的前端开发者。

`TypeScript` · Fork 1,190 · 🔗 [官网](https://solidjs.com)

### 9. [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — ⭐ 98,158（今日 +53）

> 一份精选的 MCP 服务器目录，帮你快速找到能接进 AI 的工具

这是一个精选的 Model Context Protocol（MCP）服务器清单。MCP 是一套开放协议，让 AI 模型通过标准化的服务端实现，安全地访问本地和远程资源。这个仓库要解决的是「我知道 MCP 有用，但不知道有哪些现成服务器可用」的问题：它按聚合器、浏览器自动化、数据库、文件系统、搜索、金融、安全、社交媒体等几十个分类收录了生产可用和实验性的服务器实现，每条都标注了开发语言、云端还是本地、支持的操作系统，还有官方实现的标记。除了服务器列表，仓库还提供客户端推荐、教程、框架、社区入口和选型技巧，并附有多语言 README 与同步更新的网页版目录。


Fork 20,380 · 🔗 [官网](https://glama.ai/mcp/servers)

### 10. [pingdotgg/t3code](https://github.com/pingdotgg/t3code) — ⭐ 65,582（今日 +1,220）

> T3 Code 是 agent 控制台，可用手机、网页或桌面端远程操控本机上的编码智能体。

T3 Code 是一个「agent harness 控制面」：它自己不训练模型，而是接管你电脑上已经装好并登录的编码智能体，让你在 iOS、Android、网页和 Electron 桌面端统一查看和控制它们运行。它解决的是 agent 只能在单机终端里跑、离开工位就断线的问题，并沿用你已有的 Claude Code、Codex、Cursor 等订阅，不必另买 API key。装一行 curl 脚本或 npx t3@latest 即可试用；运行 t3 会启动服务并打开本地 Web 应用，t3 service install 能让它常驻后台，再从手机远程接入。

- ✨ 一个界面统管本机多个编码智能体：Claude Code、Codex、Cursor、Grok Build、OpenCode、Antigravity、fx
- ✨ iOS、Android、Web、Electron 桌面四端覆盖，支持从手机或另一台机器远程访问
- ✨ 复用你已有的订阅和 CLI 登录状态，前提是这些工具已在本机安装并认证
- ✨ 安装轻量：一行 curl / PowerShell 脚本，或 npx t3@latest 免安装试用，t3 update 升级
- ✨ 可注册为后台服务常驻运行，并支持通过 MCP 让外部 agent 接入
- ✨ 提供权限模式、键盘快捷键、项目设置、外观偏好和多账号切换等细粒度控制
- 👥 适合谁：已经在用 Claude Code、Codex 等命令行 agent 写代码，并希望多端或远程操控它们的开发者。

`TypeScript` · Fork 11,482 · 🔗 [官网](https://t3.codes)

## 📋 完整榜单

> ℹ️ 同一仓库 3 天内不会重复出现，往期出现过的不会重复收录

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 为任意软件生成 CLI 封装，让 AI Agent 直接调用它，成为原生工具。 | `Python` | 60,043 | +389 |
| 2 | [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | POSIX 兼容的 Node.js 版本管理脚本，一条命令即可安装、切换多个 Node 版… | `Shell` | 96,198 | +237 |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv) | Rust 编写的极速 Python 包与项目管理器，一个工具顶替 pip、poetry、p… | `Rust` | 92,332 | +258 |
| 4 | [jquery/jquery](https://github.com/jquery/jquery) | 老牌跨浏览器 DOM 操作与 AJAX 库，现已发布 4.0.0，支持按模块裁剪体积。 | `JavaScript` | 60,069 | +266 |
| 5 | [appwrite/appwrite](https://github.com/appwrite/appwrite) | Appwrite 是一个开源的一站式云端开发平台，内置 MCP，专为 AI 代理与开发者打… | `TypeScript` | 58,322 | +232 |
| 6 | [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) | OpenVINO 是一个用于深度学习模型推理优化与跨平台部署的开源工具包。 | `C++` | 11,411 | +24 |
| 7 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 可自托管或云端的 fair-code 工作流自动化平台，原生支持构建和运营 AI 智能体。 | `TypeScript` | 211,270 | +325 |
| 8 | [solidjs/solid](https://github.com/solidjs/solid) | Solid 是一个用细粒度响应式直接更新真实 DOM 的声明式 JavaScript UI… | `TypeScript` | 36,695 | +40 |
| 9 | [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 一份精选的 MCP 服务器目录，帮你快速找到能接进 AI 的工具 | — | 98,158 | +53 |
| 10 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | T3 Code 是 agent 控制台，可用手机、网页或桌面端远程操控本机上的编码智能体。 | `TypeScript` | 65,582 | +1,220 |

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
