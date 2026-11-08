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

# 🔥 GitHub 每日 Trending · 2026-11-08

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 15 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 TOP 10（详细介绍）

### 1. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) — ⭐ 47,010（今日 +190）

> 给 AI 智能体用的浏览器自动化 CLI，一条命令执行一步操作

agent-browser 是 Vercel Labs 出品的原生 Rust 命令行工具，把浏览器交给 AI 智能体来驱动。它的核心循环很简单：snapshot 把当前页面转成一段紧凑文本，每个可交互元素都带 @e1 这样的 ref；智能体对 ref 执行点击或填写，再读一次页面确认结果，如此往复。浏览器在命令之间保持打开，所以每一步只是一次很短的 shell 调用，不用写 Playwright 脚本。通过 npm 或 Homebrew 即可安装，首次运行 agent-browser install 下载 Chrome for Testing，也能直接用 npx 试用。

- ✨ snapshot 把页面输出为带 ref（如 @e1）的紧凑可访问性树文本，智能体按引用操作元素，不必解析整页 HTML
- ✨ 浏览器常驻后台 daemon，页面在多次命令间保持打开；每个 --session 有独立的 daemon 和浏览器，空闲一小时后自动关闭并保存状态
- ✨ 操作失败会如实报错：目标隐藏、禁用、在视口外或被 consent 弹窗遮挡时不会谎报成功，需要处理遮挡后重新 snapshot 再试
- ✨ 除 ref 外还支持 CSS 选择器、文本、XPath 和语义定位，例如 find role button click --name "Submit"
- ✨ 浏览器后端可替换：默认 Chrome for Testing，也可用 --cdp / --auto-connect 接管已有 Chrome，或切换 Lightpanda、Obscura、iOS 模拟器 Safari 及 Browserbase 等云浏览器
- ✨ 自带与 CLI 版本匹配的 skills（core、electron、slack、dogfood 等）和 stdio MCP server，方便直接接入 agent 框架或 MCP 客户端
- 👥 适合谁：构建浏览器自动化 Agent 的开发者，以及需要给 LLM 接上网页操作能力的团队

`Rust` · Fork 3,222 · 🔗 [官网](https://agent-browser.dev)

### 2. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) — ⭐ 66,032（今日 +2,085）

> 把编码 Agent 变成安全审计员的多阶段审计技能，输出可机器校验的漏洞结论

这是一个装进编码 Agent 的安全审计技能：让 Agent 依次执行侦察、按覆盖清单狩猎、候选验证、结构化输出、独立复核、中立报告六个阶段，解决人工审计容易漏掉攻击面、结论不可复现的问题。用 npx skills add 安装后，直接对 Agent 说"security audit this codebase"即可触发，审计产物写入 findings.json 与 REPORT.md。它是 Cloudflare 漏洞挖掘 harness 的单仓库起点。

- ✨ 六阶段编排：侦察产出 architecture.md 与覆盖账本，再依次狩猎、验证、输出、复核、报告
- ✨ 覆盖账本 coverage-ledger.json 驱动狩猎，并用覆盖批评者找出未审区域，避免漏审
- ✨ 每个候选漏洞交给全新的验证 Agent 尝试证伪，结论分为 confirmed、needs_validation、rejected 三态
- ✨ findings.json 对照 report-schema.json 校验，附带零依赖校验脚本 validate-findings.cjs 与 validate-coverage-ledger.cjs
- ✨ Phase 5 独立记录复核，被替换的结论必须再经一名独立验证者确认
- ✨ 十余份攻击类提示词库，覆盖内存安全与二进制、LLM 提示注入、Web 协议与认证、客户端、供应链、云与部署、RPC 消息、资源耗尽、数据隔离、桌面移动端本地 IPC
- 👥 适合谁：已有支持工具调用与并行子 Agent 的编码 Agent、想对代码库做系统化安全审计的开发者与安全团队

`JavaScript` · Fork 4,296

### 3. [google/skills](https://github.com/google/skills) — ⭐ 23,523（今日 +443）

> Google 官方 Agent Skills 合集，一条 npx 命令即可安装到 AI 编码助手。

这是把 Google 产品（主要是 Google Cloud）的专业知识打包成 Agent Skills 的官方仓库。AI 助手通常擅长通用编程，但面对 IAM 授权、Agent Platform 模型部署、GKE 推理迁移这类具体场景时往往不够准确，而这里每个 skill 都是一份可被 Agent 直接加载的操作指南。安装只需执行 npx skills add google/skills，过程中可以选择需要的技能、要配置的目标 Agent 以及作用域（项目级或全局），后续用 npx skills update 统一升级，并可顺手清理已废弃的技能。

- ✨ Google Cloud 起步技能：涵盖 IAM 认证与授权、Onboarding 流程、Foundation Builder 基础搭建
- ✨ 多产品解决方案技能：提供 solution-architecture 工作流、RAG 企业搜索、AlloyDB 混合搜索、多智能体安全网关和 n-tier 无服务器架构等端到端方案
- ✨ AI/ML 与 Agent Platform 全套能力：模型部署、调优与调优管理、Prompt 管理、Model Registry、RAG Engine、评测飞轮、访问审计和故障排查
- ✨ Gemini API 相关技能：包括 LiveAPI 实时流式、Interactions API、Managed Agents API，以及从 AI Studio 迁移到 Agent Platform 的指南
- ✨ Genkit 多语言开发技能：分别覆盖 Dart、Go、JS、Python 四个语言生态
- ✨ 基础设施技能：包括 Cloud Storage 基础配置、诊断与 Bucket 架构设计，Cloud Storage FUSE、Compute Engine 预留、网络洞察、Application Design Center 部署等
- 👥 适合谁：在 Claude Code、Cursor 等 AI 编码工具中工作，需要在 Google Cloud 上实施 AI 应用与基础设施的开发者、架构师。

`Python` · Fork 1,967

### 4. [mattpocock/skills](https://github.com/mattpocock/skills) — ⭐ 317,925（今日 +1,100）

> 从 Matt Pocock 日常使用的 .agents 目录整理的、小巧可组合的 AI 编码代理技能集

这是 Matt Pocock 每天实际使用的一套 agent skills，目标是用它们做真正的工程开发，而不是让 AI 随意生成代码（俗称 vibe coding）。README 明确指出 GSD、BMAD、Spec-Kit 这类方案虽然想帮忙，但通过接管流程夺走了开发者的控制权，出了问题也难以排查；这些技能则反过来追求小而可改、可自由组合，并且不绑定任何模型。安装上支持 Claude Code、Codex、GitHub Copilot、Gemini CLI，也能通过 npx skills 装到 cursor、opencode、devin、windsurf、amp 等代理里；插件方式会自动更新，也可以复制成可编辑文件手动维护。装完在每个仓库跑一次 /setup-matt-pocock-skills，告诉它你用哪个 issue tracker、triage 打什么标签、文档存哪里，就能开工。

- ✨ grill-me：在动手前让 agent 反过来追问你细节，先对齐需求再写代码
- ✨ grill-with-docs：grill-me 的加强版，额外带上文档与上下文资料一起盘问
- ✨ setup-matt-pocock-skills：每个仓库跑一次，配置 issue tracker、triage 标签和文档存放位置
- ✨ /triage 配合自定义标签做工单分类
- ✨ 共享语言（glossary）文档，让 agent 用项目自己的术语说话，避免啰嗦绕圈
- ✨ 小而可组合的技能设计，不接管流程、任何模型都能用，改起来没有负担
- 👥 适合谁：用 Claude Code、Codex、Copilot 等代理写真实项目、想在保留控制权的前提下提升协作效率的开发者

`Shell` · Fork 26,602 · 🔗 [官网](https://aihero.dev/skills)

### 5. [anthropics/skills](https://github.com/anthropics/skills) — ⭐ 188,933（今日 +390）

> Anthropic 官方开源的 Claude Agent Skills 示例、规范与模板仓库，教 Claude 可复用地完成专项任务。

这是 Anthropic 官方维护的 Agent Skills 仓库。Skill 就是一个文件夹，里面有 SKILL.md 指令、脚本和资源，Claude 会在需要时动态加载，从而把某类任务做得稳定可重复，比如按公司品牌规范做文档、按组织流程分析数据。仓库收录创意设计、开发技术、企业沟通、文档处理等多类示例，并公开了支撑 Claude 文档能力的 docx、pdf、pptx、xlsx 四个生产级 Skill 供开发者参考。可在 Claude Code 通过插件市场安装，也能在 Claude.ai 和 API 中使用，或照着 template 自己写一个。

- ✨ 每个 Skill 自包含在一个文件夹中，用 SKILL.md 的 YAML frontmatter（name + description）加 Markdown 指令定义行为
- ✨ 开源 Claude 文档能力的底层实现：docx、pdf、pptx、xlsx 四个复杂 Skill，可作为生产级参考
- ✨ 覆盖创意设计、开发技术（如 Web 应用测试、MCP server 生成）、企业沟通与品牌等多样示例
- ✨ 提供 Agent Skills 规范文档（spec）和入门模板（template），方便从零创建自定义 Skill
- ✨ Claude Code 中可一键注册为插件市场，直接安装 document-skills 或 example-skills 插件
- ✨ 同一套 Skill 可在 Claude Code、Claude.ai 付费版与 Claude API 中复用，并收录 Notion 等合作伙伴示例
- 👥 适合谁：想让 Claude 稳定完成特定任务的开发者、提示词与 AI 应用工程师，以及需要自定义企业工作流的团队。

`Python` · Fork 22,270

### 6. [meta/astryx](https://github.com/meta/astryx) — ⭐ 14,750（今日 +96）

> Meta 开源的设计系统，150+ 可访问组件，主题完全可定制，并支持 AI 助手使用。

Astryx 是 Meta 内部使用了八年的设计系统，已开源且处于 Beta。它提供 150+ 无障碍组件、品牌级主题、暗色模式、现成模板和 CLI，打包成一个完整体系。安装后导入预构建 CSS，再用带类型的 React 组件即可，无需构建插件，也不用从零引入样式库。它的关键差异是内部开放：组件可以在任意层级组合，需要深入改动时，可用 swizzle 将组件源码直接弹出到项目；样式虽用 StyleX 编写，但使用者无感知，可以直接用 Tailwind、CSS Modules 或原生 CSS 通过 className 覆盖；主题本质上是一组 CSS 自定义属性覆盖，设计师不改组件源码就能做出专属风格。它要求 React 19+。

- ✨ 150+ 无障碍 React 组件，涵盖品牌主题、暗色模式和开箱即用的页面模板
- ✨ 主题即 CSS 自定义属性覆盖，无需 fork 或包裹组件源码即可深度换肤
- ✨ 不绑定样式方案，可用 Tailwind、CSS Modules 或原生 CSS 通过 className 覆盖
- ✨ 开放式内部结构，底层构件直接导出，swizzle 可把组件完整源码弹出到项目自有
- ✨ 配套 CLI 提供组件文档、模板、脚手架、主题和 codemod，支持本地与全局安装
- ✨ 七套现成主题（neutral、butter、chocolate、matcha、stone、gothic、y2k）
- 👥 适合谁：需要统一设计语言、又不想被样式方案锁死的 React 团队，以及希望 AI 助手按同一套规范产出界面的开发者。

`TypeScript` · Fork 1,210 · 🔗 [官网](http://astryx.atmeta.com)

### 7. [prometheus/prometheus](https://github.com/prometheus/prometheus) — ⭐ 67,487（今日 +322）

> CNCF 旗下的系统与服务监控系统，内置时序数据库和告警能力。

Prometheus 是一套开源的系统与服务监控系统，同时自带时序数据库。它按设定的时间间隔从目标抓取指标，用规则表达式做计算，把结果画成图表，并在满足条件时触发告警。和很多监控系统不同，它采用多维数据模型（指标名加一组键值标签定义一条时间序列），配合自研查询语言 PromQL，可以灵活切片和聚合；不依赖分布式存储，单个服务节点即可自治运行；采集走 HTTP pull 模型，批处理任务可以通过中间网关推送数据；目标支持服务发现或静态配置，并支持分层与水平联邦。安装方式很省事：直接下载官方预编译二进制，或一条 docker run 命令把容器跑起来，访问 9090 端口就能用；从源码构建则需要 Go、NodeJS 和 npm，构建出的镜像和二进制都包含 React UI。

- ✨ 多维数据模型，时间序列由指标名和一组 key/value 维度定义
- ✨ PromQL 查询语言，充分利用多维标签做筛选、聚合与运算
- ✨ 不依赖分布式存储，单节点自治运行，部署运维简单
- ✨ HTTP pull 拉取模型采集指标，批处理任务可经中间网关推送
- ✨ 支持服务发现与静态配置两种目标发现方式，内置多种服务发现插件
- ✨ 内置规则表达式求值、告警触发，以及多种图形与仪表盘支持
- 👥 适合谁：需要监控云原生环境、微服务与基础设施的运维、SRE 和开发者。

`Go` · Fork 11,011 · 🔗 [官网](https://prometheus.io/)

### 8. [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) — ⭐ 101,068（今日 +1,766）

> 一条命令在 400+ 社交网络上按用户名追踪账号的开源工具。

Sherlock 是一个用 Python 写的命令行工具，给它一个用户名，它会去 400 多个社交网络上逐个探测这个用户名是否已被注册，把命中的站点链接收集起来。它解决的是跨平台账号排查的问题：无论是做安全研究、渗透测试前的信息收集，还是想确认自己的用户名在哪些平台被人占用，手动一个个网站去试都很费时，Sherlock 把这件事变成一条命令。用法很直接，sherlock user123 查单个，sherlock user1 user2 user3 批量查，结果默认按用户名存成单独的 txt 文件。安装推荐 pipx install sherlock-project，也可以直接跑 Docker 镜像，或用 dnf 装包；README 特别提示第三方维护的 ParrotOS 和 Ubuntu 24.04 包目前是坏的，这两个系统的用户应改用 uv、pipx、pip 或 Docker。

- ✨ 按用户名批量查询 400+ 社交网络，支持一次传入多个用户名
- ✨ 结果自动按用户名导出为独立文本文件，另支持 CSV、XLSX、JSON 输出
- ✨ --site 参数可把探测范围限定在指定站点，可重复指定多个
- ✨ 支持 socks5 等代理，并可自定义请求超时时间（默认 60 秒）
- ✨ --print-all 显示未命中的站点，--print-found 只输出命中项，--nsfw 纳入 NSFW 站点检查
- ✨ --browse 用默认浏览器打开所有结果，--json 可加载本地或在线 JSON 站点清单，--local 强制使用本地 data.json
- 👥 适合谁：适合做 OSINT 信息收集、安全研究与渗透测试的人，以及想排查自己用户名占用情况的开发者。

`Python` · Fork 11,947 · 🔗 [官网](https://sherlockproject.xyz)

### 9. [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) — ⭐ 17,291（今日 +1,955）

> 开源版 Grok Bot 替代品：一群跑在你自己机器上的 AI 机器人聊天应用

OpenMausBot 是一个 Electron 桌面聊天应用，界面像 Telegram，但侧边栏里每个联系人都是真实 agent——底层跑的是你本机已装好的 Claude、Codex 或 Grok CLI。它针对的问题很直接：单个助手塞进一个对话框并不是 agent 该有的形态，而 Grok Bot、Meta Muse、OpenAI dots、Cue 这类闭源产品把模型、电脑和你的数据都留在厂商那一侧。OpenMausBot 把同一套「AI 即通讯应用」的想法重做成开源、本地优先：一个跑在 127.0.0.1 的小型 harness 服务管理所有 agent 进程，转录、密钥、事件都存在 ~/.openmausbot，复用你已有的登录和订阅，不需要新账号、没有中间代理。

- ✨ 通讯录式的多 bot 聊天：每个 bot 是独立 agent，有自己的性格、对话记忆、指定模型、专属云电脑和已连接的应用
- ✨ 自带 agent：直接驱动本机 claude、codex、grok CLI，沿用现有登录与订阅；在 Settings → Engines 可把引擎指向自定义 CLI 二进制或包装脚本
- ✨ 本地优先架构：127.0.0.1 上的 harness 服务统一托管 agent 进程，转录、密钥与事件全部落在 ~/.openmausbot，不上云
- ✨ 给 agent 一双手：每个 bot 可用云端 Linux 桌面、隔离的 Local VM，或在平台安全边界已认证的情况下直接操作你自己的电脑
- ✨ 500+ 应用接入（Composio），让 bot 不止能聊，还能实际调用外部服务干活
- ✨ 主机控制需显式 opt-in：macOS 与 Ubuntu Xorg 可用，Ubuntu Wayland 因 issue #345 暂时禁用
- 👥 适合谁：想自托管个人 AI agent、并复用现有模型订阅的开发者与高级用户

`TypeScript` · Fork 2,439 · 🔗 [官网](https://www.openmausbot.com/)

### 10. [astral-sh/ruff](https://github.com/astral-sh/ruff) — ⭐ 51,027（今日 +350）

> Rust 编写的超快 Python linter 与格式化工具，一个工具替代 Flake8、Black、isort 等一整套。

Ruff 是 Astral 公司开发的 Python 代码检查与格式化工具，用 Rust 实现，比 Flake8、Black 等现有工具快 10 到 100 倍。它要解决的核心问题是：Python 项目过去需要同时安装 Flake8 及其大量插件、Black、isort、pydocstyle、pyupgrade、autoflake 等一堆工具，配置分散、速度慢；Ruff 把这些功能收进同一个接口，用一条命令跑完 lint 和 format，并通过 pip 安装、读取 pyproject.toml 配置。它还支持自动修复（如删除未使用的 import）、内置缓存跳过未改动文件，并在行为上与 Flake8、isort、Black 保持可直接替换的一致性，迁移时基本不用改代码风格。

- ✨ 速度比 Flake8、Black 等快 10-100 倍，在 CPython 代码库上可直观对比
- ✨ 内置 900 多条规则，原生重写了 flake8-bugbear 等流行插件
- ✨ 同时提供 linter 和 formatter，可替代 Flake8、Black、isort、pydocstyle、pyupgrade、autoflake
- ✨ 支持自动修复常见问题，例如自动移除未使用的 import
- ✨ 内置缓存，避免重复分析未改动的文件
- ✨ 官方提供 VS Code 等编辑器集成，支持 Python 3.15 与 pyproject.toml 配置
- 👥 适合谁：所有写 Python 的开发者，尤其是想统一并加速 lint 和格式化流程的团队与大型 monorepo 项目。

`Rust` · Fork 2,633 · 🔗 [官网](https://docs.astral.sh/ruff)

## 📋 完整榜单

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | 给 AI 智能体用的浏览器自动化 CLI，一条命令执行一步操作 | `Rust` | 47,010 | +190 |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | 把编码 Agent 变成安全审计员的多阶段审计技能，输出可机器校验的漏洞结论 | `JavaScript` | 66,032 | +2,085 |
| 3 | [google/skills](https://github.com/google/skills) | Google 官方 Agent Skills 合集，一条 npx 命令即可安装到 AI 编… | `Python` | 23,523 | +443 |
| 4 | [mattpocock/skills](https://github.com/mattpocock/skills) | 从 Matt Pocock 日常使用的 .agents 目录整理的、小巧可组合的 AI 编… | `Shell` | 317,925 | +1,100 |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | Anthropic 官方开源的 Claude Agent Skills 示例、规范与模板仓… | `Python` | 188,933 | +390 |
| 6 | [meta/astryx](https://github.com/meta/astryx) | Meta 开源的设计系统，150+ 可访问组件，主题完全可定制，并支持 AI 助手使用。 | `TypeScript` | 14,750 | +96 |
| 7 | [prometheus/prometheus](https://github.com/prometheus/prometheus) | CNCF 旗下的系统与服务监控系统，内置时序数据库和告警能力。 | `Go` | 67,487 | +322 |
| 8 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 一条命令在 400+ 社交网络上按用户名追踪账号的开源工具。 | `Python` | 101,068 | +1,766 |
| 9 | [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | 开源版 Grok Bot 替代品：一群跑在你自己机器上的 AI 机器人聊天应用 | `TypeScript` | 17,291 | +1,955 |
| 10 | [astral-sh/ruff](https://github.com/astral-sh/ruff) | Rust 编写的超快 Python linter 与格式化工具，一个工具替代 Flake8… | `Rust` | 51,027 | +350 |
| 11 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | 以工具类优先方式快速构建自定义界面的 CSS 框架，写类名即写样式。 | `TypeScript` | 98,568 | +122 |
| 12 | [mbillow/localthings](https://github.com/mbillow/localthings) | 在局域网内直连三星家电，不用云账号，把设备接入 Home Assistant 的集成。 | `Python` | 1,096 | +186 |
| 13 | [zed-industries/zed](https://github.com/zed-industries/zed) | 来自 Atom 与 Tree-sitter 作者的高性能、支持多人协作的代码编辑器 | `Rust` | 94,349 | +1,114 |
| 14 | [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) | 给编码 Agent 用的上下文压缩插件，让单个会话连跑一个月、省下约 5 倍 token。 | `TypeScript` | 4,721 | +191 |
| 15 | [dsx-ai-factory/nvke](https://github.com/dsx-ai-factory/nvke) | 在自有 NVIDIA GPU 裸金属上自建托管 Kubernetes 服务的开源管理平面 | `Go` | 615 | +123 |

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
