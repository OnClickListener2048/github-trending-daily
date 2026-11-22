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

# 🔥 GitHub 每日 Trending · 2026-11-22

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 10 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 今日精选（详细介绍）

### 1. [obra/superpowers](https://github.com/obra/superpowers) — ⭐ 323,884（今日 +883）

> 为编码代理准备的一套完整软件开发方法论，让 AI 先问清需求再动手写代码

Superpowers 是一套构建在可组合技能之上的软件开发方法论，安装后会自动作用于你的编码代理。它不会立刻写代码，而是先退后一步问你真正想解决什么问题，把需求梳理成规格，并分块展示给你确认。设计通过后，它会生成一份实施计划，细到没有项目背景、不重视测试的初级工程师也能照着执行，并强调真正的红绿 TDD、YAGNI 和 DRY。你确认开始后，它进入子代理驱动开发流程：逐项推进任务，检查并评审每个子代理的产出，常常能自主按计划工作数小时而不偏离。技能会自动触发，你不需要额外操作。

- ✨ 技能自动触发：代理在对话开始就加载 using-superpowers 技能，无需手动调用
- ✨ 先澄清需求再编码：通过对话梳理出规格说明，并切成足够短、能真正读完的片段给你确认
- ✨ 可执行的实施计划：细化到初级工程师能照做，同时强调红绿 TDD、YAGNI 与 DRY
- ✨ 子代理驱动开发：每个工程任务交给子代理执行，主代理检查评审后继续推进
- ✨ 长时间自主工作：可连续数小时按既定计划推进而不跑偏
- ✨ 广泛的 harness 覆盖：Claude Code、Codex App/CLI、Cursor、Gemini CLI、GitHub Copilot CLI、Devin CLI、Factory Droid、Grok Build CLI、Kimi Code、OpenCode、Qwen Code 等均有对应安装方式
- 👥 适合谁：希望让 AI 编码代理按严谨工程流程交付、而不只是补全代码的个人开发者与团队

`Shell` · Fork 28,728

### 2. [jingyaogong/minimind](https://github.com/jingyaogong/minimind) — ⭐ 68,278（今日 +488）

> 从零训练64M参数小语言模型，2小时3块钱，完整覆盖LLM全流程的开源教程项目。

MiniMind 是一个从零手写大语言模型全流程的开源项目：用约3元GPU租用成本、单卡3090跑2小时，就能训练出64M参数的迷你语言模型。它要解决的是主流框架把训练封装得太黑箱、付费课程又讲不透的问题——核心算法全部用PyTorch原生实现，不依赖transformers/trl/peft的高层抽象，让你真正读懂每一行代码。项目还提供Tokenizer训练、全阶段开源数据、OpenAI兼容API服务端和Streamlit聊天界面，可直接上手复现和二次开发。

- ✨ 完整的MiniMind-LLM结构代码（Dense与MoE），主线对齐Qwen3/Qwen3-MoE生态
- ✨ 覆盖Pretrain、SFT、LoRA、RLHF-DPO、RLAIF（PPO/GRPO/CISPO）、Tool Use、Agentic RL、自适应思考与模型蒸馏全流程
- ✨ 提供从收集、蒸馏、清洗到去重的高质量全阶段开源数据集，含工具调用与思考标记的Tokenizer训练代码
- ✨ 关键训练算法从零原生实现，同时兼容transformers/trl/peft、llama.cpp/vllm/ollama与Llama-Factory
- ✨ 支持单机单卡及多卡DDP/DeepSpeed训练、断点续训、wandb/swanlab可视化，并可在C-Eval等第三方评测集上测评
- ✨ 附带兼容OpenAI协议的极简服务端与Streamlit聊天WebUI，支持reasoning_content、tool_calls与open_thinking，可接入FastGPT、Open-WebUI
- 👥 适合谁：想深入理解大模型原理、亲手从零训练模型的学生、开发者与AI教学者。

`Python` · Fork 8,928 · 🔗 [官网](https://jingyaogong.github.io/minimind)

### 3. [cursor/plugins](https://github.com/cursor/plugins) — ⭐ 18,184（今日 +260）

> Cursor 官方插件仓库，把开发工作流和 SaaS 工具接入 AI 编辑器

这是 Cursor 官方维护的插件集合，每个插件都是仓库根目录下的独立文件夹，并带有自己的 .cursor-plugin/plugin.json 清单，可以单独安装和使用。它解决的核心问题是：AI 编程助手通常只了解本地代码，却无法访问 PR 评审、云任务编排、Google Workspace、Salesforce 等真实工作流，而 Cursor 把这些能力封装成了可复用的插件。使用方式很直接：在插件目录中找到需要的能力并启用它，再通过 agent 技能、命令或 CLI 在对话里调用。目前已覆盖教学、代码审查、并行云端 agent 编排、SDK 开发，以及一大批第三方 SaaS 集成。

- ✨ Thermos 深度分支审查：针对安全性和正确性进行审计，采用严苛的代码质量评分标准，并行调度多个子 agent，并可选用 merge-ready PR 流程
- ✨ Orchestrate 把大型任务拆分给并行的云端 agent，并包含 planner、worker、verifier 和结构化交接
- ✨ Cursor Team Kit 提供 CI、代码评审、发版、本地自动化和验证等团队内部工作流
- ✨ Create Plugin 用来搭建和校验新的 agent 插件；Teaching 提供技能映射、练习计划和学习复盘
- ✨ Continual Learning 把对话记录增量写入 AGENTS.md 长期记忆；Ralph Loop 实现自引用式迭代 AI 循环
- ✨ 大量第三方集成：GitHub、Playwright、Gmail、Google Drive、Calendar、Docs、Sheets、Slides、Salesforce、HubSpot、Zoom、Gong、Ashby 等，可直接操作真实业务数据
- 👥 适合谁：使用 Cursor 的开发者、需要把 AI agent 接入团队工作流和 SaaS 工具的工程团队

`TypeScript` · Fork 1,986

### 4. [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) — ⭐ 196,513（今日 +780）

> 给 AI 编程助手加上“最懒资深开发”的思维，让它少写代码但不少写安全。

Ponytail 是一个给 AI 编程 Agent 使用的技能包（skill），相当于把团队里那位扎马尾、话不多、五十行变一行的老工程师装进你的 Agent。它要解决的是 AI 编码助手常见的过度工程：为了一个日期选择器手搓 335 行日历，或者随手引入新依赖。Ponytail 让 Agent 先看仓库里已有什么、平台已自带什么，只写任务真正需要的那部分。它的原则不是“最少 token”，而是绝不砍掉校验、错误处理、安全与可访问性——代码小是因为必要，不是因为高尔夫式删减。README 给出的对照基准显示：代码量 -53%、耗时 -41%、成本 -26%、token -45%，同时 98% 的风险逻辑带测试（不用时为 68%），还附有 20 个 Agent 的兼容说明。

- ✨ 懒人式复用优先：先检查仓库现有组件和浏览器原生能力，10 行替代手搓的 335 行日期选择器
- ✨ 克制引入依赖：不为一件事装一个库，能拼装现有能力就不新增包
- ✨ 不牺牲正确性：校验、错误处理、安全、可访问性一律保留，只删冗余
- ✨ 自带测试倾向：基准中 98% 的风险逻辑附带测试，Agent 自写测试能拦住 66% 的注入 bug（对照组 46%）
- ✨ 可量化的收益：官方基准 39 个任务（含真实 FastAPI + React 仓库），代码 -53%、时间 -41%、成本 -26%、token -45%
- ✨ 安全任务全通过：SQL 注入、路径穿越、伪造 token、限流、畸形 CSV、缓存 6 类场景 30 次运行全数通过
- 👥 适合谁：日常用 AI Agent 写业务代码、受够了过度工程和多余依赖的开发者与团队。

`JavaScript` · Fork 11,077 · 🔗 [官网](https://ponytail.dev)

### 5. [driceroland/Search](https://github.com/driceroland/Search) — ⭐ 3,731（今日 +230）

> Office Commun 出品的 macOS 极简 WebKit 浏览器，约 10 MB，无工具栏、无账号、无同步。

Search 是一款把「浏览器」还原成工具的 macOS 浏览器，由一家整天泡在浏览器里的设计工作室开发——他们受够了那些把自己做成产品的浏览器。整个界面只有一栏标签页（左侧或顶部，可切换）和网页本身：没有工具栏、没有起始页、没有推荐侧栏、没有要登录的账号。它复用系统自带的 WebKit 引擎，所以安装包只有约 10 MB，启动几乎瞬时，不需要再下载维护一份 Chromium。使用方式极简：在唯一的输入框里敲地址就跳转、敲词就搜索，历史补全在本地完成，回车之前不向任何地方发送内容。支持 macOS 14 及以上，免费，也可用 Homebrew cask 安装。

- ✨ 单一输入框：地址与搜索合一，基于本地历史补全，按下回车前不发送任何输入
- ✨ 克制的标签页：常驻页面可固定并缩成图标或首字母，上次会话的标签恢复不占资源，⌘K 按名称检索所有打开的标签
- ✨ 分屏视图：把一个标签拖到页面上即可左右并排，拖动分隔线调整宽度，成对标签与宽度随空间一起恢复
- ✨ 永久隐藏元素：⇧⌘H 后点掉 Cookie 横幅、订阅弹层、相关推荐栏，下次访问时页面渲染前就已消失
- ✨ 网络层广告拦截：第三方追踪器与广告网络在请求阶段就被拦掉，默认开启，站点出错可按站关闭
- ✨ 阅读模式与画中画：⇧⌘R 剥离正文，⇧⌘P 把视频提为置顶小窗，浮于其他应用之上
- 👥 适合谁：适合追求速度与隐私、厌恶功能膨胀和账号体系的 Mac 用户，尤其是每天长时间在浏览器里工作的开发者与设计师。

`Swift` · Fork 387

### 6. [rtk-ai/rtk](https://github.com/rtk-ai/rtk) — ⭐ 87,441（今日 +125）

> 把常见开发命令的输出压缩 60-90% 的 CLI 代理，单个 Rust 二进制，装完即用。

RTK 是一个面向 AI 编程 Agent 的 token 成本削减工具。它安装在你的机器上，通过 hook 自动接管 git status、测试、diff、日志、构建等 100+ 条常见命令：Agent 发出命令时，实际执行的是 rtk 包装后的版本，原始输出在 Agent 读取前就被压缩成精简摘要，例如 40 行的 git status 变成 3 行总结。无需改配置、无需学习新命令，装完重启 Agent 即生效；每条命令开销低于 25ms。它同时提供 pipelines 机制，用一份 Agent 无关的配置文件做更进一步的优化，比如把重读取交给更便宜的模型、压缩 bash 之外的内容、在不破坏 prompt 缓存的前提下清理 API 流量。

- ✨ 开箱即用的输出压缩：100+ 条常用命令，单条开销低于 25ms，无需任何配置
- ✨ 透明接入 Agent：rtk init -g 注册 hook，重启后命令自动被包装，工作方式完全不变
- ✨ rtk gain 用量仪表盘：汇总统计、30 天 ASCII 图表、历史记录、按天明细与 JSON 导出
- ✨ rtk discover 找出被遗漏的节省机会，支持跨项目、按时间范围扫描
- ✨ Pipelines 进阶优化：一份 Agent 无关的配置文件，可从内置模板起步、安装社区分享的、或自己编写并分享
- ✨ 跨平台单二进制分发：Homebrew、winget、安装脚本均可，另有 RTK Pro 为团队提供统一网关、成本与合规管控
- 👥 适合谁：适合使用 Claude Code 等 AI 编程 Agent、希望降低 token 开销的开发者与团队。

`Rust` · Fork 5,612 · 🔗 [官网](https://www.rtk-ai.app)

### 7. [superdesigndev/treg](https://github.com/superdesigndev/treg) — ⭐ 8,721（今日 +121）

> 面向 agent 的工具版 OpenRouter：一个 token 调用数千个按次计费的第三方 API

treg 把 agent 真正干活需要的工具集中到一个网关后面：SEO 与反链、社交与趋势、人物与公司信息补全、广告、抓取、图像视频生成，覆盖数千个端点，按次计费、最低一分钱起，不用去各家注册账号。它替团队持有 Semrush、Moz、Crunchbase、Apollo 这类订阅，让你按调用付费，而不是按席位买月费。装好 CLI 后执行 treg login，用 treg catalog search 按「要做什么」找工具，treg call 直接调用，treg balance 看这一单花了多少。你还可以把团队自己的 API 账号、OAuth、厂商 CLI 或 SKILL.md 注册进来，用自己的 key 调用且不计费。

- ✨ 策展目录覆盖数千个端点：SEO 与反链、社交趋势、人物与公司信息补全、广告、爬取、图像视频生成，按次计价，最低一分钱起
- ✨ 无需向供应商注册：上游账号由 treg 持有，也支持无需 key 的公开路由；自有 key 永远优先于 treg 的 key，且这类调用从不计费
- ✨ 三类自带工具统一注册：endpoint（base_url + 多个凭证绑定，一次请求可同时注入 OAuth bearer 和 developer-token 头）、CLI（stripe、gh、vercel 等二进制）、skill/bundle（SKILL.md + secrets + tools）
- ✨ 代理只转发、不建模，并在服务端注入鉴权：上游 API 改动不会波及调用方，调用者永远拿不到密钥
- ✨ 换 base URL 即可迁移：把 https://api.dataforseo.com/v3 换成 https://treg.to/call/dataforseo，已有客户端就能跑对应目录工具，目录未列出的路径一律 404、不做转发
- ✨ strict_query 工具做严格参数校验：未声明、重复、超范围或类型不符的参数直接返回 400 catalog_parameter_invalid 并指明参数，且不计费
- 👥 适合谁：把 agent 用于真实业务的开发者与团队，尤其是做增长、SEO、数据补全类 agent，且需要共享凭证、可自托管的人

`Python` · Fork 859 · 🔗 [官网](https://treg.to)

### 8. [datazip-inc/olake-go](https://github.com/datazip-inc/olake-go) — ⭐ 2,224（今日 +93）

> 开源高性能数据入湖引擎，把数据库、Kafka 和 S3 的数据实时复制进 Apache Iceberg 或 Parquet。

OLake Go 是一个用 Go 编写的数据摄取引擎，解决的是「把业务数据搬进开放湖仓」这件事。它支持从 PostgreSQL、MySQL、MongoDB、Oracle、DB2、MSSQL 这类事务库，以及 Kafka、S3 读取数据，写入 Apache Iceberg 表或纯 Parquet 文件。相比传统方案，它不需要 Spark、Flink、Kafka、Debezium 这一整套重型组件，因此基础设施成本很低；用 Docker Compose 就能起一套带 Web UI 的服务，也可以用 CLI 操作。它提供全量加 CDC 增量同步、自动 schema 发现与演进、Exactly-once 投递，写入走 Arrow，官方公布的 Postgres 全量吞吐达 580K RPS。Iceberg 侧兼容 Glue、Hive、JDBC、REST 四类 Catalog，表维护交给配套的 olake-fusion 项目。

- ✨ 全量与 CDC 增量复制一体，支持自动 schema 发现和 schema 演进
- ✨ 官方基准：Postgres 全量 580K RPS、Oracle 526K RPS、MSSQL 345K RPS，CDC 场景下 Postgres/MySQL 均快于 Fivetran
- ✨ Exactly-once 语义保证，基于 Arrow 列式写入兼顾速度与准确性
- ✨ Iceberg 原生支持，可对接 Glue、Hive、JDBC、REST 四种 Catalog，也可直接落地纯 Parquet
- ✨ 覆盖 Postgres、MySQL、MongoDB、Oracle、DB2、MSSQL、Kafka、S3 八类数据源
- ✨ 提供 Web UI 与 CLI 两种使用方式，Docker Compose 一条命令即可部署，无需 Spark/Flink/Debezium
- 👥 适合谁：需要把业务库或流数据实时同步到 Iceberg 湖仓、又不想维护 Spark/Flink 重型栈的数据团队与平台工程师。

`Go` · Fork 325 · 🔗 [官网](https://olake.io/olake-go/)

### 9. [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) — ⭐ 119,092（今日 +92）

> 一份系统整理 macOS 优质软件的精选清单，按类别归纳，方便查找和使用。

awesome-mac 是一个面向 Mac 用户的软件精选合集，目标是把散落在各处的优质 macOS 应用集中起来，并按类别系统化整理，解决“想找某个功能的 Mac 软件却不知道用什么好”的问题。它不是代码库，而是一份持续维护的清单：你可以直接在目录里按分类浏览，比如效率工具、开发工具、设计、系统增强等，快速定位到具体应用。遇到合适的项目，按清单里的链接前往官网或商店获取即可。适合当作日常查阅的 Mac 软件选型参考。

- ✨ 按类别系统整理 macOS 软件，便于按用途快速查找
- ✨ 持续收录高质量 Mac 应用，形成可长期参考的清单
- ✨ 覆盖效率、开发、设计、系统工具等多个方向
- ✨ 每个条目提供应用名称与跳转链接，方便直接获取
- ✨ 以 Markdown 清单形式维护，阅读和检索成本低
- ✨ 由社区参与补充和更新，保持内容与时俱进
- 👥 适合谁：适合所有 Mac 用户，尤其是想按类别发掘优质应用、需要软件选型参考的开发者与效率爱好者。

`Swift` · Fork 10,494 · 🔗 [官网](https://git.io/macx)

### 10. [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) — ⭐ 75,434（今日 +89）

> 面向 AI 编码助手的规格驱动开发（SDD）框架，先定计划再写代码。

OpenSpec 是一套在终端里使用的规格驱动开发框架：用 /openspec-propose 让 AI 先把需求写成 proposal.md、specs、design.md 和 tasks.md，再由 AI 按清单逐条实现，做完归档并把规格沉淀下来。它要解决的是「AI 一上来就写代码、需求和实现两头跑偏」的问题——规格全是纯 Markdown，不需要学新语法，你审完计划再让它动手，个人项目和多人协作都能用，也支持直接在已有代码库上迭代。

- ✨ /openspec-explore：零风险的思考搭子，先读你的代码、比较几种方案、收敛范围，再决定要不要做
- ✨ /openspec-propose：一次产出 proposal.md（为什么做、改什么）、specs（需求与场景）、design.md（技术方案）和 tasks.md（实现清单）
- ✨ /openspec-apply-change：AI 按 tasks.md 逐条实现并打勾，做到哪一步一眼能看到
- ✨ /openspec-archive-change：完成后自动归档到 changes/archive/日期-名称，同时更新规格，留给下一个特性继续用
- ✨ 规格就是纯 Markdown：Requirement + Scenario 的 WHEN/THEN 写法，AI 负责写、你负责审，不需要学新语法
- ✨ Stores（beta）：把 openspec/ 放进独立仓库，让一次变更横跨 API、Web 和共享库；平台团队维护规格，产品团队只读引用，不用维护会走样的 wiki
- 👥 适合谁：使用 Claude Code、Cursor 等 AI 编码助手的开发者与技术团队，尤其是已有代码库、需要跨仓库协作的中大型团队。

`TypeScript` · Fork 5,154 · 🔗 [官网](https://openspec.dev/)


## 🧡 Product Hunt 今日榜

[Beat Watcher](https://www.producthunt.com/products/beat-watcher) · Product Hunt

> Beat Wat

[Smorza](https://www.producthunt.com/products/smorza) · Product Hunt

> Smorza 让每个 Mac 应用都能拥有独立音量和输出设备。

[AlterContacts](https://www.producthunt.com/products/alter-contacts-ai-client-relationships) · Product Hunt

> AlterContacts 是一款能

[Stitch Loop](https://www.producthunt.com/products/stitch-loop) · Product Hunt

> Stitch Loop 是 Google 的 AI 代理，能自动交付修复并持续监控指标。

[Publicit](https://www.producthunt.com/products/publicit) · Product Hunt

> Publicit 是面向营销人员和 AI 代理的全渠道广告基础设施。


## 🇨🇳 中文独立开发 · V2EX 分享创造

[创建了几个 muse 账户，有谁想玩吗](https://www.v2ex.com/t/1258889) · 💬 5 回复

> 开发者创建了几个 muse 账户，

[我做了 Kooyu：一个本地优先的 AI 助手，统一调度你手里所有的编程 CLI](https://www.v2ex.com/t/1258880) · 💬 4 回复

> 开发者打造了本地优先的 AI 助手 Kooyu，可统一调度各类编程 CLI。

[\[开源\] 微子中枢 v0.6.1：一键部署 + 远程控制，新增本地 Ollama 和 OpenCode](https://www.v2ex.com/t/1258878) · 💬 0 回复

> 开源项目微子中枢 v0.6.1 支持一键部署和远程控制，新增本地 Ollama 与 OpenCode。

[myco：可能是全网唯一能安全使用 Claude 的客户端，开放免费内测啦！](https://www.v2ex.com/t/1258876) · 💬 0 回复

> 独立开发者发布 myco 客户端，号称全网唯一能安全使用 Claude，现已开放免费内测。

[年初做的终端排障小工具推倒重做成了 aist：零配置融进 Shell、多机 SSH、带环境记忆，再来求各位老哥拍砖](https://www.v2ex.com/t/1258874) · 💬 0 回复

> 独立开发者将年初的终端排障小工具重做成 aist，支持零配置融入 Shell、多机 SSH 和环境记忆。

## 📋 完整榜单

> ℹ️ 同一仓库 3 天内不会重复出现，往期出现过的不会重复收录

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | 为编码代理准备的一套完整软件开发方法论，让 AI 先问清需求再动手写代码 | `Shell` | 323,884 | +883 |
| 2 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 从零训练64M参数小语言模型，2小时3块钱，完整覆盖LLM全流程的开源教程项目。 | `Python` | 68,278 | +488 |
| 3 | [cursor/plugins](https://github.com/cursor/plugins) | Cursor 官方插件仓库，把开发工作流和 SaaS 工具接入 AI 编辑器 | `TypeScript` | 18,184 | +260 |
| 4 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 给 AI 编程助手加上“最懒资深开发”的思维，让它少写代码但不少写安全。 | `JavaScript` | 196,513 | +780 |
| 5 | [driceroland/Search](https://github.com/driceroland/Search) | Office Commun 出品的 macOS 极简 WebKit 浏览器，约 10 MB… | `Swift` | 3,731 | +230 |
| 6 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | 把常见开发命令的输出压缩 60-90% 的 CLI 代理，单个 Rust 二进制，装完即用… | `Rust` | 87,441 | +125 |
| 7 | [superdesigndev/treg](https://github.com/superdesigndev/treg) | 面向 agent 的工具版 OpenRouter：一个 token 调用数千个按次计费的第… | `Python` | 8,721 | +121 |
| 8 | [datazip-inc/olake-go](https://github.com/datazip-inc/olake-go) | 开源高性能数据入湖引擎，把数据库、Kafka 和 S3 的数据实时复制进 Apache I… | `Go` | 2,224 | +93 |
| 9 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 一份系统整理 macOS 优质软件的精选清单，按类别归纳，方便查找和使用。 | `Swift` | 119,092 | +92 |
| 10 | [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 面向 AI 编码助手的规格驱动开发（SDD）框架，先定计划再写代码。 | `TypeScript` | 75,434 | +89 |

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
