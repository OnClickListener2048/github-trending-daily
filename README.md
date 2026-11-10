# 🔥 GitHub Trending Daily · 每日热榜推送

[![daily-trending](https://github.com/OnClickListener2048/github-trending-daily/actions/workflows/daily-trending.yml/badge.svg)](https://github.com/OnClickListener2048/github-trending-daily/actions/workflows/daily-trending.yml)
![GitHub stars](https://img.shields.io/github/stars/OnClickListener2048/github-trending-daily)

每天自动抓取 [github.com/trending](https://github.com/trending) 的热门仓库，**给每一位 Star 过本仓库的人发一封邮件**，正文就是当天榜单 + 每个仓库的一句话简介。

## ✨ 怎么接收

1. **Star 本仓库** ⭐
2. 保持 GitHub 邮件通知开启（默认就是开的，不用动）
3. 完成。每天早上 08:30（北京时间）你会收到一封来自 GitHub 的邮件：🏆 今日精选详解（每个仓库"是什么 + 能干什么"，连续在榜较久的自动跳过）+ 📋 完整榜单，并附精美 HTML 报告链接

> 原理：每天自动创建一个 Issue 并 @ 你的用户名，GitHub 会把提及通知默认发送到你的邮箱。不需要填邮箱、不需要注册，**Star 即订阅**。全程使用 GitHub 官方机制，不收集任何个人信息。

## 🧭 今日榜单

<!-- TRENDING:START -->

# 🔥 GitHub 每日 Trending · 2026-11-10

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 11 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 TOP 10（详细介绍）

### 1. [anthropics/skills](https://github.com/anthropics/skills) — ⭐ 191,452（今日 +1,038）

> Anthropic 官方的 Agent Skills 示例库，教 Claude 可复用地完成专项任务。

这是 Anthropic 公开的 Claude Skills 实现集合。Skill 就是一个文件夹，里面装有说明、脚本和资源，Claude 会在需要时动态加载它们，从而学会按可重复的方式完成特定任务，例如按公司品牌规范做文档、按组织流程分析数据，或自动化个人琐事。仓库收录了覆盖创意设计、开发技术、企业沟通和文档处理的示例技能，每个技能都自包含在独立文件夹中，并含一个 SKILL.md；开发者可从中获取灵感，或参考其中的模式。仓库还以 Apache 2.0 开源了支撑 Claude 文档能力的 docx、pdf、pptx、xlsx 技能，作为复杂生产级技能的参考。用法很简单：在 Claude Code 中把仓库注册为插件市场，再安装 document-skills 或 example-skills；在 Claude.ai 付费计划中已内置；也可通过 Claude API 使用。

- ✨ Skill 机制：文件夹 + SKILL.md，Claude 按需动态加载
- ✨ YAML frontmatter 仅需 name 与 description 两个字段
- ✨ 按创意设计、开发技术、企业沟通、文档四类组织的示例技能集
- ✨ 开源 docx / pdf / pptx / xlsx 文档创建与编辑技能，生产环境在用
- ✨ Claude Code 插件市场一键安装 document-skills 或 example-skills
- ✨ 提供 Agent Skills 规范文档与 template 模板起步
- 👥 适合谁：想给 Claude 定制可复用能力、或想学习 Skill 写法的开发者与团队。

`Python` · Fork 22,473

### 2. [meta/astryx](https://github.com/meta/astryx) — ⭐ 20,921（今日 +3,278）

> Meta 开源的设计系统，含 150+ 组件，可深度定制，也面向 AI 编程助手

Astryx 是一个在 Meta 内部发展八年、支撑 13000+ 应用的设计系统，现在以 MIT 协议开源。它把 150+ 无障碍组件、品牌级主题、暗色模式、现成模板和一个 CLI 打包成一套完整方案，解决的是组件库难以定制、样式被锁死、人和 AI 助手各用各的参考这几类问题。使用方式很简单：安装核心包、一个主题和 CLI，引入预构建 CSS，再用带类型的 React 组件，全程不需要配置构建插件或 PostCSS/Babel；组件内部实现可以直接导出，也可用 swizzle 把组件源码弹出到项目里。

- ✨ 150+ 无障碍 React 组件，覆盖常见界面需求
- ✨ 品牌级主题与暗色模式，主题本质上是一组 CSS 自定义属性覆盖，不 fork 源码也能彻底换皮
- ✨ 不锁定样式方案：组件用 StyleX 编写，但消费方可以用 Tailwind、CSS Modules 或普通 CSS 通过 className 覆盖
- ✨ 开放内部实现：组件可在任意层级组合，需要时用 swizzle 把组件完整源码弹出到自己的项目中接管
- ✨ CLI 工具链：查看组件文档、模板与脚手架、主题生成和 codemod，并可全局安装让编码助手随时调用
- ✨ 自带七套现成主题（neutral、butter、chocolate、matcha、stone、gothic、y2k），开箱即用
- 👥 适合谁：需要可深度定制、不锁定样式的 React 19 团队，尤其是希望人和 AI 助手共用同一套工具链的开发者

`TypeScript` · Fork 1,584 · 🔗 [官网](http://astryx.atmeta.com)

### 3. [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) — ⭐ 107,803（今日 +4,267）

> 跨 400+ 社交网络按用户名批量追踪账号的开源命令行工具

Sherlock 是一个用 Python 编写的命令行工具，解决的问题很直接：给你一个用户名，帮你在各大社交平台上找出它是否被注册。它覆盖 400+ 个社交网络，支持一次传入多个用户名批量查询，例如 `sherlock user1 user2 user3`，找到的账号会自动保存为与用户名对应的文本文件（如 user123.txt）。输出格式灵活，支持 txt、CSV、XLSX 以及 JSON 数据加载，还能用 --site 只查指定站点、用 --proxy 走代理、用 --browse 直接在浏览器打开所有命中结果。安装推荐 pipx、pip、uv 或 Docker 一行搞定，也可以指定 --nsfw、--timeout 等参数控制检索范围与请求行为。

- ✨ 按用户名在 400+ 社交网络中检索账号是否存在
- ✨ 支持一次查询多个用户名并分别输出结果
- ✨ 结果可导出为 txt、CSV、XLSX 文件
- ✨ 通过 --site 限定只检查指定站点，可叠加多个
- ✨ 支持代理请求、自定义超时和调试响应输出
- ✨ --browse 一键在浏览器中打开所有找到的账号
- 👥 适合谁：适合做 OSINT 调查、安全研究、渗透测试前期信息收集，以及想核查自己用户名被哪些平台占用的开发者。

`Python` · Fork 12,464 · 🔗 [官网](https://sherlockproject.xyz)

### 4. [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) — ⭐ 17,075（今日 +574）

> Google DeepMind 维护的通用物理引擎，能快速、准确地仿真带接触的多关节刚体系统。

MuJoCo 名称是 Multi-Joint dynamics with Contact 的缩写，由 Google DeepMind 维护，是一个开源物理仿真器。它用于仿真由关节连接的刚体结构在环境中运动时与物体发生的接触和碰撞，主要解决机器人学、生物力学、图形动画和机器学习中对快速、准确仿真的需求。它提供性能高度优化的 C API 运行时，模型由内置 XML 编译器预先分配数据结构，并提供桌面窗口与浏览器中的交互式可视化工具和大量物理量计算函数。此外还有 Python 绑定和 Unity 插件。既可直接下载各平台预编译版本，也可通过 pip install mujoco 安装并快速上手。

- ✨ 高性能 C API 物理仿真运行时，数据结构预分配，专为快速准确仿真优化
- ✨ 内置 XML 模型编译器，用 XML 描述多关节结构的场景
- ✨ 原生桌面窗口与 Web 浏览器中的交互式可视化，附带 simulate 查看器与 MuJoCo Studio
- ✨ 大量物理相关计算工具函数，可直接获取仿真中的各类物理量
- ✨ 官方 Python 绑定，pip install mujoco 即可使用，配有入门、模型编辑、rollout、LQR、最小二乘等 Colab 教程
- ✨ MJX（MuJoCo XLA）JAX 分支，支持在 JAX 中运行并可通过教程训练可微物理策略
- 👥 适合谁：从事机器人、生物力学、图形动画与机器学习研究，需要快速准确刚体仿真的开发者和研究者。

`C++` · Fork 2,012 · 🔗 [官网](https://mujoco.org)

### 5. [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) — ⭐ 20,168（今日 +551）

> Anthropic 官方开源的 Claude API 应用快速上手合集，覆盖客服、金融、浏览器与电脑操作等场景。

这是一组能直接跑起来的示例工程，每个对应一类真实产品形态：客服代理、金融数据分析、电脑操作、浏览器自动化、自主编码、托管代理。它解决的问题很实际——你不需要从零摸索 Claude API 的调用方式、工具定义和前端交互长什么样，挑一个最接近自己需求的项目，填上 API key 就能跑通，再在这个基础上改造成自己的应用。所有示例都以可部署、可定制为出发点，而非只做接口演示。

- ✨ Customer Support Agent：带知识库的 AI 客服示例，展示如何用 Claude 的自然语言理解与生成能力搭建辅助客服系统
- ✨ Financial Data Analyst：通过聊天分析财务数据，并能生成交互式数据可视化
- ✨ Computer Use：既能提供让 Claude 控制桌面电脑的环境与工具（含最新的 computer_toolset 工具集形态），也有原生 macOS 的最佳实践参考实现，示范显式工具定义、图像尺寸与裁剪、提示缓存、服务端压缩、批量工具调用、沙箱 shell 与轨迹记录等可靠性和成本优化模式
- ✨ Browser Use Demo 与 Browser Toolset：前者基于 Playwright 自定义浏览器工具，让 Claude 导航网站、检查并操作 DOM、提取内容、填写表单；后者是最小 CDP 示例，用一个小驱动控制单个 Chromium 标签页
- ✨ Autonomous Coding Agent：基于 Claude Agent SDK 的双代理模式（初始化代理 + 编码代理），跨多个会话逐步构建完整应用，进度通过 git 和功能清单持久化
- ✨ Managed Agents 系列：浏览器聊天应用（同一套 handler 换上 Chat SDK 适配器即可跑在 Slack、Teams、Discord、Telegram、WhatsApp）、用 CopilotKit + AG-UI 把工具调用渲染成交互式生成式 UI、每工作日汇总 Slack 与 GitHub PR 的定时简报代理、把文档语料蒸馏成带出处版本化知识库的尽调维基
- 👥 适合谁：想用 Claude API 做产品的开发者，尤其是要落地客服、数据分析、Agent 自动化类应用的团队和个人。

`Python` · Fork 3,328

### 6. [garrytan/gbrain](https://github.com/garrytan/gbrain) — ⭐ 32,319（今日 +216）

> 给现有 AI Agent 加一个可控、可纠错、跨 Agent 共享的持久记忆大脑。

GBrain 是 Garry Tan 为自己 OpenClaw/Hermes 部署打造的 Agent 记忆层，现已开源。它把明确的事实连同来源一起存下来，支持修正与撤回，并让同一份记忆在多个 Agent 之间共享。它要解决的是 Agent 记不住、记忆不可控、上下文反复丢失的问题。你可以把它挂到现有 Agent 上，让它把记忆保存在该 Agent 的环境中；也可以先使用无需密钥的关键词检索，之后再按需增加语义搜索、综合答案和后台自动丰富。生产实例已承载 15 万级页面，并有 66 个 cron 任务在夜间自动整理记忆。

- ✨ 显式事实存储：每条记忆都带来源出处，可修正、可撤回，不靠模型臆测
- ✨ 关键词检索零门槛起步：先用 keyless 的关键词检索，需要时再开启语义搜索
- ✨ 跨 Agent 共享同一份记忆：持久偏好与事实共用，临时任务状态仍留在本地
- ✨ 综合答案层：跨人物、公司、交易与想法生成带引用的连贯回答，并明确指出大脑还不知道什么
- ✨ 类型化知识图谱：本地写入可自动抽取引用并建边，支持毫秒级广度优先关系遍历（如谁在某公司工作）
- ✨ 24/7 dream cycle：夜间自动摄取会议、邮件、推文、通话，丰富人物与公司信息、修复引用并合并记忆
- 👥 适合谁：已在使用 AI Agent、希望拥有私有可控持久记忆的个人开发者，以及需要团队级共享记忆的工程团队。

`TypeScript` · Fork 4,780

### 7. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) — ⭐ 48,733（今日 +916）

> 让 AI 智能体通过命令行一步步驱动浏览器的原生 Rust CLI 工具

agent-browser 是 Vercel Labs 推出的浏览器自动化 CLI，专门给 AI 智能体使用。核心玩法是“快照—操作—再快照”的循环：snapshot 把页面读成紧凑的可访问性树文本，每个元素带 @e1 这样的 ref；智能体对 ref 执行 click、fill 等命令，再读一次页面确认结果。浏览器在命令之间保持打开，每一步只是一次简短的 shell 调用。它解决了智能体直接啃 HTML 太费 token、又难以稳定定位元素的问题，并提供严格失败语义：点击目标隐藏、禁用、在视口外或被遮挡时直接报错而不是假装成功。安装走 npm 或 Homebrew，首次运行 agent-browser install 下载 Chrome for Testing。

- ✨ snapshot 将页面转成紧凑文本并给每个元素分配 @e1 式 ref，智能体据此定位与操作
- ✨ click、fill、type、hover、select、drag、upload 等完整交互命令，支持 CSS、文本、XPath 与语义查找
- ✨ 目标不可见、被遮挡或被禁用时点击直接报错，避免智能体误判成功
- ✨ 后台 daemon 保持浏览器常驻，命令间会话不中断，支持多 --session 隔离
- ✨ 内置随版本发布的 skills，可用 agent-browser skills get core 让智能体获取与当前 CLI 匹配的操作指南
- ✨ 支持接入运行中的 Chrome（--cdp / --auto-connect）、iOS 模拟器 Safari、Lightpanda 等引擎及 Browserbase 等云浏览器
- 👥 适合谁：构建浏览器智能体的 AI 工程师、需要脚本化网页操作的开发者与自动化测试团队

`Rust` · Fork 3,320 · 🔗 [官网](https://agent-browser.dev)

### 8. [ruvnet/RuView](https://github.com/ruvnet/RuView) — ⭐ 103,685（今日 +172）

> 把普通WiFi信号变成穿墙感知能力，无需摄像头即可检测人、呼吸和心跳

RuView 是一个基于 Rust 的 WiFi 感知平台。它利用低成本 ESP32 传感器采集信道状态信息（CSI），通过分析人体对无线电波的扰动，实现穿墙、黑暗中、无穿戴设备条件下的空间感知。它解决的是传统视频监控侵犯隐私、穿戴设备不便利、暗光失效等问题。使用上，它以单个 --mqtt 参数接入 Home Assistant，或作为 Matter Bridge 配对到 Apple Home、Google Home、Alexa、SmartThings，并提供录 CSI、训练模型、加载 RVF、切换 LoRA 的完整工作流与 HOMECORE 本地自动化。

- ✨ 穿墙人员存在检测、人数统计与进出追踪
- ✨ 非接触式呼吸率与心率监测，支持睡眠中测量
- ✨ 活动识别：行走、坐姿、手势、跌倒
- ✨ 无摄像头 17 关键点人体姿态估计
- ✨ 环境映射与 RF 指纹：识别房间、发现家具移动与新物体
- ✨ 睡眠质量分析：睡眠分期与呼吸暂停筛查
- 👥 适合谁：智能家居玩家、隐私敏感的家庭看护场景开发者，以及做无线感知研究的嵌入式与 Rust 工程师

`Rust` · Fork 13,431 · 🔗 [官网](https://cognitum.one)

### 9. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) — ⭐ 69,262（今日 +506）

> LLM 驱动的多市场自选股分析系统，每日自动生成决策仪表盘并推送到常用 IM。

这是一套基于大模型的股票分析系统：你只需给出自选股代码，它就会把行情、K 线与技术指标、新闻公告、基本面数据聚合起来，让 AI 输出包含核心结论、评分、趋势、买卖点位、风险警报、催化因素和操作清单的决策报告，并推送到企业微信、飞书、Telegram、Discord、Slack 或邮箱。使用时无需服务器：Fork 仓库后配好模型 Key、推送渠道和 STOCK_LIST，即可用 GitHub Actions 零成本定时运行；也支持 Docker、本地定时任务与 FastAPI 服务，还有 Web/桌面工作台可手动分析、翻历史报告、做回测。

- ✨ AI 决策报告：核心结论、评分、趋势、买卖点位、风险警报、催化因素与操作检查清单一次给全
- ✨ 多市场数据聚合：覆盖 A股、港股、美股、日股、韩股、台股和 ETF 的行情、K 线、技术指标、新闻、公告与基本面
- ✨ Web / 桌面工作台：手动分析、任务进度、历史报告、完整 Markdown、回测、持仓与配置管理，支持浅色/深色主题
- ✨ Agent 策略问股：多轮追问，内置均线、缠论、波浪、趋势、热点、事件、成长、预期等 15 种策略，Web/Bot/API 均可调用
- ✨ 智能导入与补全：支持图片、CSV/Excel、剪贴板导入自选股，股票代码/名称/拼音/别名自动补全
- ✨ 自动化与推送：GitHub Actions、Docker、本地定时任务、FastAPI 服务，推送到企业微信/飞书/Telegram/Discord/Slack/邮件
- 👥 适合谁：适合跟踪 A股、港股、美股等多市场的个人投资者，以及想低成本搭自选股日报的开发者。

`Python` · Fork 56,486 · 🔗 [官网](https://dsa.zhulinsen.tech)

### 10. [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) — ⭐ 6,189（今日 +31）

> 让 Claude、ChatGPT 等 AI 助手直接配置和自动化 Home Assistant 的 MCP 服务器

HA-MCP 是一个 Home Assistant 的 MCP 服务器，内置 87 个工具，让 AI 助手能够读取状态、修改配置、编写自动化，省去手写 YAML 的麻烦。最推荐的用法是通过 HACS 或 Home Assistant 2026.11+ 的 Marketplace 把它装成集成，直接在 Home Assistant 进程内运行完整服务器；它兼容 OS、Supervised、Container、Core 全部安装类型，功能完全一致，也取代了插件、Docker、uvx/PyPI 等旧方式（只能选一种）。安装后重启 Home Assistant，在“设置 → 设备与服务”添加 HA-MCP Server，填入管理员长令牌，或为它新建一个仅本地登录的管理员账号，选择远程访问（Secret URL 或 HA 登录）和/或本地网络访问，再从 Configure 界面复制连接 URL 粘进 AI 客户端即可。本地客户端也可直连 9584 端口。

- ✨ 内置 87 个工具，覆盖 Home Assistant 的查询、配置与自动化操作
- ✨ 以集成形式通过 HACS 或 Marketplace 安装，在 Home Assistant 进程内运行，无需另跑 Docker/uvx
- ✨ 兼容 Home Assistant OS、Supervised、Container、Core 全部安装类型，功能完全一致
- ✨ 两种接入方式：经 Home Assistant 的远程 webhook（Secret URL 或 HA 登录），以及本地网络直连
- ✨ 认证灵活：可用自己的长令牌，也可为 HA-MCP 单独建管理员账号并由它自动生成令牌
- ✨ 有端到端测试流水线保障，并把 ha_config_set_yaml 等实验能力放入 beta 通道
- 👥 适合谁：用 Home Assistant 搭建智能家居、希望让 AI 代劳配置与自动化的玩家和自建用户

`Python` · Fork 302 · 🔗 [官网](https://homeassistant-ai.github.io/ha-mcp/)

## 📋 完整榜单

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [anthropics/skills](https://github.com/anthropics/skills) | Anthropic 官方的 Agent Skills 示例库，教 Claude 可复用地完… | `Python` | 191,452 | +1,038 |
| 2 | [meta/astryx](https://github.com/meta/astryx) | Meta 开源的设计系统，含 150+ 组件，可深度定制，也面向 AI 编程助手 | `TypeScript` | 20,921 | +3,278 |
| 3 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 跨 400+ 社交网络按用户名批量追踪账号的开源命令行工具 | `Python` | 107,803 | +4,267 |
| 4 | [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | Google DeepMind 维护的通用物理引擎，能快速、准确地仿真带接触的多关节刚体系… | `C++` | 17,075 | +574 |
| 5 | [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | Anthropic 官方开源的 Claude API 应用快速上手合集，覆盖客服、金融、浏… | `Python` | 20,168 | +551 |
| 6 | [garrytan/gbrain](https://github.com/garrytan/gbrain) | 给现有 AI Agent 加一个可控、可纠错、跨 Agent 共享的持久记忆大脑。 | `TypeScript` | 32,319 | +216 |
| 7 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 让 AI 智能体通过命令行一步步驱动浏览器的原生 Rust CLI 工具 | `Rust` | 48,733 | +916 |
| 8 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 把普通WiFi信号变成穿墙感知能力，无需摄像头即可检测人、呼吸和心跳 | `Rust` | 103,685 | +172 |
| 9 | [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | LLM 驱动的多市场自选股分析系统，每日自动生成决策仪表盘并推送到常用 IM。 | `Python` | 69,262 | +506 |
| 10 | [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) | 让 Claude、ChatGPT 等 AI 助手直接配置和自动化 Home Assista… | `Python` | 6,189 | +31 |
| 11 | [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 开源版 Grok Bot：在聊天应用里管理一支各有虚拟机的 AI 机器人团队 | `TypeScript` | 20,122 | +1,587 |

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
| `top_n` | 详细介绍的仓库数（默认 10，按 GitHub 页面原始顺序取，跳过连续在榜超限的仓库后顺延） |
| `top_n_max_streak_days` | 连续在榜达到该天数的仓库不再进详细介绍（默认 3，仍保留在完整榜单里） |
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

**同一个仓库连续上榜会重复总结吗？**
不会。AI 分析结果缓存在 `data/repos.json`（随仓库提交），再次上榜时直接复用，不再调用 AI；缓存里同时记录首次出现、最近出现日期和连续在榜天数。连续在榜达到 `top_n_max_streak_days`（默认 3 天）的仓库会退出「今日精选」的详细介绍位，由榜单后面的新项目顺延补位，但仍保留在完整榜单中。

## ⚠️ 免责声明

本项目与 GitHub 无关，仅用于学习和技术交流。请勿滥用 @ 提及功能。
