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

# 🔥 GitHub 每日 Trending · 2026-11-04

> 数据来源：[github.com/trending](https://github.com/trending?since=daily) · 每天 08:00（北京时间）自动推送 · 共 13 个仓库
> 🎨 [打开精美 HTML 报告](https://onclicklistener2048.github.io/github-trending-daily/)（推荐浏览器查看）

## 🏆 TOP 10（详细介绍）

### 1. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) — ⭐ 112,197（今日 +1,139）

> 给 AI 编程助手加上跨会话持久记忆，自动捕获、压缩并复用上下文

claude-mem 是一个为 AI 编程助手提供持久记忆的压缩系统。它在会话过程中自动记录 Agent 的工具调用和操作观察，再用 AI 压缩成语义摘要保存下来；当新会话开始时，它会把相关的历史上下文注入回去。这样一来，即使会话结束、终端关掉或重新连接，助手依然记得这个项目里做过什么、改过哪里、为什么这么改，不用你每次从头复述背景。安装只需一条 npx 命令，并按你使用的 IDE 选择对应接入方式。

- ✨ 自动捕获会话中的工具使用与操作观察，不依赖手动记笔记
- ✨ 用 AI 将原始记录压缩成语义摘要，长期留存而非堆积日志
- ✨ 新会话开始时自动注入相关上下文，接续上次的工作进度
- ✨ 内置 MCP 搜索工具，可主动检索历史记忆
- ✨ 多 Agent 兼容：Claude Code、Codex、Gemini、Copilot、OpenCode 等
- ✨ 通过 npx 按 IDE 一键安装，并提供配置项与故障排查文档
- 👥 适合谁：长期用 AI 编程助手推进同一项目的开发者，尤其是受够了每次会话都要重新交代背景的人

`TypeScript` · Fork 9,759 · 🔗 [官网](https://claude-mem.ai)

### 2. [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) — ⭐ 13,391（今日 +3,791）

> 让 AI Agent 通过系统无障碍树看见并操作桌面应用，不依赖截图和像素匹配

agent-desktop 是 Vercel Labs 出的命令行工具，给 AI Agent 补上「操作桌面」的能力。它不做截图识别，而是直接读取 macOS、Windows、Linux 上应用的无障碍树，返回一份带 ref 的 JSON，Agent 对准 ref 点击或输入，再重新读一次 UI 验证结果，如此循环。项目本身不含任何模型，闭环逻辑跑在你自己的 Agent 里，以 CLI 和 C 库两种形式提供。安装只需 npm i -g agent-desktop；在 macOS 上运行 permissions --guide 可以一步步引导完成辅助功能授权，随后 snapshot --app Finder -i 即可拿到可交互元素列表。它还提供 MCP 模式和内置技能文档，方便直接接入现有 Agent 框架。

- ✨ 用无障碍树快照把桌面 UI 转成带 ref 的 JSON，Agent 可精确点击或输入到具体元素
- ✨ ref 绑定快照 id，UI 变化时返回 STALE_REF 或 AMBIGUOUS_TARGET，强制重新观察再操作
- ✨ 默认无头操作，不移动鼠标也不抢焦点，需要真实输入时加 --headed
- ✨ 所有命令输出统一的 JSON 信封，含错误码、退出码和 retry 处置建议
- ✨ 内置 skills get desktop / platform 技能文档，指导 Agent 掌握循环、重试规则与平台差异
- ✨ agent-desktop mcp 将所有命令以 MCP 工具形式通过 stdio 暴露，可直接挂到 MCP 客户端
- 👥 适合谁：想把桌面应用操作能力接入自有 Agent 的开发者，尤其是做 computer use 类产品的团队

`Rust` · Fork 923 · 🔗 [官网](https://agent-browser.dev/desktop)

### 3. [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) — ⭐ 10,648（今日 +438）

> Rust 写的 Git worktree 管理 CLI，专为并行跑 AI agent 的工作流设计

Worktrunk 是一个 Git worktree 管理命令行工具。Git 原生 worktree 能让每个 AI agent 拥有独立工作目录、互不干扰，但用起来很别扭——新建一个 worktree 就得把分支名敲三遍，还要手动 cd 进去。Worktrunk 让 worktree 像分支一样好用：用分支名寻址，路径按可配置模板自动生成。日常就是三条命令：wt switch 切换、wt remove 清理、wt list 看状态；wt switch -c -x claude 一条命令就能建好 worktree 并直接拉起 agent。

- ✨ 三个核心命令覆盖日常操作：wt switch 切换或新建 worktree，wt remove 删除 worktree 并清理分支，wt list 带状态列出所有 worktree
- ✨ 以分支名作为 worktree 的寻址方式，路径由可配置模板自动推算；命令既接受分支名，也接受 worktree 路径
- ✨ wt switch -c -x claude 一步完成“创建 worktree + 切进去 + 启动 AI agent”，取代 git worktree add、cd、启动三步
- ✨ Hooks 支持在创建、pre-* 等生命周期节点自动执行命令，把本地工作流固化下来
- ✨ copy-on-write 构建缓存，让多个并行 worktree 共享构建产物，避免每个目录重复编译
- ✨ 面对方便同时管理多个并行改动的需求，提供一系列 quality-of-life 功能，减少手工整理 worktree 的成本
- 👥 适合谁：同时并行跑多个 AI 编码 agent、需要给每个任务隔离工作目录的开发者

`Rust` · Fork 388 · 🔗 [官网](https://worktrunk.dev)

### 4. [JustVugg/colibri](https://github.com/JustVugg/colibri) — ⭐ 47,404（今日 +802）

> 纯 C 编写的分层推理引擎，让普通电脑跑起千亿参数 MoE 大模型

colibri 是一个用纯 C 写的推理引擎，专门用来在你自己已有的硬件上运行超大规模的开源 MoE 模型。它利用 MoE 模型每次推理只激活少量专家的特点，把热专家放在 GPU、温专家放在内存、冷专家放在 NVMe 上按需流式读取；这样一来，744B 的 GLM-5.2 在 int4 量化下只需约 9.9 GB 常驻内存即可启动。它提供一键安装脚本，自动检测内存、磁盘和显卡，推荐能装下的模型，编译或下载引擎，支持断点续传下载模型，随后启动 Web 面板，并暴露 OpenAI 与 Anthropic 兼容接口。

- ✨ 分层专家调度：热专家驻留 GPU（CUDA/Vulkan）、温专家放 RAM、冷专家从 NVMe 流式读取，按 token 需要加载
- ✨ 十三个引擎覆盖多类模型：GLM-5.2/5.3、Kimi K3、DeepSeek V4 Flash、Qwen3.6、OLMoE 等十个语言模型，Qwen-Image-2.1 图像模型，以及 Laya、GLiNER2.5-Decide 决策模型
- ✨ 直接读取社区已发布的 GGUF 文件，无需转换即可运行
- ✨ 一键安装：START-HERE.bat 或 start-here.sh 自动探测硬件、推荐放得下的模型、按需为 CPU/Vulkan/CUDA 编译，缺依赖时打印安装命令
- ✨ 模型下载支持进度显示与断点续传，中断后重跑可接着下载
- ✨ 启动后开箱即用的 Web 控制台，并提供 OpenAI 兼容的 /v1 与 Anthropic 兼容的接口地址供其他应用接入
- 👥 适合谁：想在消费级电脑或单卡工作站上本地跑大 MoE 模型的开发者与自建服务爱好者

`C` · Fork 5,475 · 🔗 [官网](https://justvugg.github.io/colibri)

### 5. [mattpocock/skills](https://github.com/mattpocock/skills) — ⭐ 311,787（今日 +1,164）

> 一套可直接安装的 AI 编程代理技能集，让代理按真实工程流程工作，告别随性式编码。

这是 Matt Pocock 从自己 .agents 目录里整理出的日常代理技能集，用来解决 AI 编码代理的几个常见问题：没理解需求就动手、输出啰嗦、缺少项目术语共识、过程失控。它不同于 GSD、BMAD、Spec-Kit 这类想接管整个流程的方案，每个技能都小而可改、可组合，支持任意模型。安装很简单：Claude Code、Codex、Copilot、Gemini CLI 各有一条命令，其他代理用 npx skills 安装；装好后每个仓库跑一次 /setup-matt-pocock-skills，选好 issue 跟踪方式、分诊标签和文档存放位置就能用。

- ✨ /grill-me 与 /grill-with-docs：在动手前让代理反过来追问你，把需求问清楚再开始写代码
- ✨ 共享语言文档：为项目建立术语表，让代理读懂行话、少说废话
- ✨ /triage 配合你自定义的标签，对工单进行分诊
- ✨ 安装后一次配置 issue 跟踪（GitHub、GitLab、本地文件或自定义），统一工作流
- ✨ 技能可自由修改、组合，不绑定特定模型
- ✨ 多代理安装支持：Claude Code、Codex、GitHub Copilot、Gemini CLI 及其他代理，可自动更新或手动更新
- 👥 适合谁：适合用 AI 代理写真实项目、希望保留流程控制权的开发者，尤其是嫌重型流程框架太黑盒的人。

`Shell` · Fork 26,200 · 🔗 [官网](https://aihero.dev/skills)

### 6. [p-e-w/heretic](https://github.com/p-e-w/heretic) — ⭐ 38,996（今日 +701）

> 无需训练即可改造本地大模型，去掉拒答、减少废话和谄媚。

Heretic 是一个让普通开发者在自己的显卡上直接改造语言模型的工具。过去这类修改（例如去除审查）通常只有算力充足的大公司才能做，而 Heretic 不做昂贵的训练，而是利用一组数学方法，根据对比示例提示和对应的评分器来引导模型行为。安装后执行一条命令（如 heretic Qwen/Qwen3-4B-Instruct-2507）即可运行，默认行为是去除模型的拒绝回答倾向；在 RTX 3090 上处理 Qwen3-4B 大约需要 30-40 分钟，完成后可以选择保存模型、上传到 Hugging Face、直接对话测试或运行基准评测。

- ✨ 去除审查、抑制拒答（默认行为）
- ✨ 通过配置文件切换目标：减少废话、减少幽默、降低谄媚、调整情绪倾向
- ✨ 支持通过插件自定义 scorer，控制优化目标
- ✨ 支持多数稠密模型、多种 MoE 架构、多模态与混合模型
- ✨ 支持 bitsandbytes 4-bit 动态量化，降低显存占用
- ✨ 运行前自动测试硬件以确定最优批大小，完成后可保存、上传、对话测试或跑基准
- 👥 适合谁：想在本地改造开源大模型行为、但缺乏大规模训练算力的开发者与爱好者。

`Python` · Fork 4,401 · 🔗 [官网](https://heretic-project.org)

### 7. [spotify/portal-ai-plugins](https://github.com/spotify/portal-ai-plugins) — ⭐ 3,096（今日 +91）

> 把 Spotify Portal 的软件目录与运维工作流接入 AI 编码助手

这是 Spotify 官方推出的插件，将 Portal CLI 封装成一组能在 AI 编码助手里直接使用的工作流：配置认证、运行只读体检、用自然语言搜索软件目录与技术文档、生成服务简报（负责人、健康度、事故、文档），以及发现并安全调用 Portal 动作。它还支持创建、运行、诊断 Fleetshift 任务，并在任务完成后开 PR。安装后，在 Claude Code、Codex、Cursor 或 pi 里运行一次 setup 即可开始使用，底层通过 npx @spotify/portal-cli 调用上游命令。

- ✨ 一键为当前编码助手环境配置 Portal CLI 认证
- ✨ doctor 只读体检，检查插件、CLI、认证与动作是否就绪
- ✨ 用自然语言搜索软件目录和技术文档
- ✨ 生成包含归属、健康度、事故与文档的服务简报
- ✨ 发现并安全调用 Portal 动作，带内置帮助、dry-run 与确认保护
- ✨ Fleetshift 全流程：创建 shift（含 dry-run 预览）、触发与限时监控、只读进度检查、失败任务日志诊断、确认后为完成目标开 PR、按需停止运行
- 👥 适合谁：Spotify 内部开发者，尤其是要在编码助手里查服务归属、健康度、事故和文档的人

`TypeScript` · Fork 240

### 8. [floci-io/floci](https://github.com/floci-io/floci) — ⭐ 29,044（今日 +482）

> 一个免费开源的本地 AWS 模拟器，用一条 Docker 命令替代真实云环境。

Floci 是面向开发、测试和 CI 的本地 AWS 模拟器，在 http://localhost:4566 上提供真实 AWS 形态的服务，无需云账号、无需认证令牌、没有付费功能限制。现有的 AWS SDK、CLI、Terraform、CDK、OpenTofu 和测试套件只要把端点指向本地，就能照常工作。启动方式也很简单：运行 floci start，或 docker compose up，用 eval $(floci env) 导出环境变量，然后正常执行 aws s3 mb、aws dynamodb create-table 等命令。它还是 LocalStack 的直接替代品，换掉镜像名即可继续使用，对想把云依赖从日常开发和流水线中剥离出来的团队来说相当省事。

- ✨ 在 localhost:4566 上提供 AWS 形态的服务，支持任意已发布区域和全部分区
- ✨ 不要求云账号、认证令牌或付费授权，凭据随便填非空值即可使用
- ✨ 与现有 AWS SDK、CLI、Terraform、CDK、OpenTofu 和测试套件直接对接，几乎不改代码
- ✨ 作为 LocalStack 的 drop-in 替代，只需替换镜像名即可迁移
- ✨ 内置 Web 控制台（/_floci/ui），以 sidecar 方式按需启动，用于查看本地模拟器中的资源
- ✨ 提供官方 CLI（floci start / floci env），并为 Linux、macOS、Windows 提供免 Docker 的独立二进制 floci-aws
- 👥 适合谁：需要在本地或 CI 中运行 AWS 服务的后端开发者、测试工程师和平台团队。

`Java` · Fork 3,230 · 🔗 [官网](https://floci.io/floci/)

### 9. [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) — ⭐ 16,784（今日 +228）

> 基于 Playwright 与 AI 的闲鱼多任务监控系统，带 Web 管理后台，帮你从海量商品中筛出值得买的那个。

这是一个把“盯闲鱼”这件事自动化的工具。你不再需要反复刷新搜索页、肉眼看描述判断成色和性价比——它按你设定的关键词、价格区间、发布时间、包邮条件和省市区，用 Playwright 持续抓取新上架商品，再交给支持图片输入的多模态模型，按你写的选购标准判断值不值得买，命中就通过 ntfy.sh、企业微信、Bark、Telegram 或 Webhook 推到手机上。整个流程跑在一个 Web 后台里：任务管理、闲鱼账号登录态导入、AI 判断标准编辑、运行日志、结果浏览都能点着操作，还支持 Cron 定时、多任务并发、多账号与代理轮换。Docker 一键起，默认 http://127.0.0.1:8000，最少只需填三个 AI 相关环境变量。

- ✨ 多任务并发监控，每个任务可独立配置关键词、价格范围、筛选条件与 AI Prompt
- ✨ AI 驱动：用自然语言描述需求即可后台异步生成判断标准，多模态模型结合商品图与详情做深度分析
- ✨ 高级筛选支持包邮、新发布时间范围、省/市/区三级区域选择
- ✨ 即时通知覆盖 ntfy.sh、企业微信、Bark、Telegram、Webhook 等渠道
- ✨ 多账号管理与代理池轮换，配合失败重试、黑名单 TTL 和任务失败自动暂停保护
- ✨ 完整 Web 管理界面：任务、账号、结果、日志、Prompt 编辑集中在一个后台，数据存 SQLite 并支持旧数据自动导入
- 👥 适合谁：想在闲鱼蹲低价好物、又不想手动刷新的个人买家，以及需要长期监控特定品类的小团队。

`Python` · Fork 2,877

### 10. [anomalyco/hex](https://github.com/anomalyco/hex) — ⭐ 4,755（今日 +410）

> 按住快捷键说话、松开就自动粘贴到当前应用的本地语音听写工具，支持 Mac、Windows 和 Linux。

Hex 是一款跨平台的本地语音听写工具，解决的是「打字慢、又不想把语音上传到云端」这个问题。用法很简单：按住快捷键开口说话，说完松手，Hex 会在这台设备上完成转写，并把文字直接粘贴进你当时正在使用的任何应用里，不需要切换窗口或复制粘贴。首次运行时会下载一个语音模型，之后所有处理都在本地完成，音频和文字都不会离开你的电脑。它提供 macOS（Apple silicon）、Windows x64/ARM64、Linux x86_64/ARM64 的安装包，也支持 Homebrew、AUR、Nix 和一条 Linux 安装脚本，此外还分稳定版与自动更新的 dev 通道。

- ✨ 按住快捷键说话、松手即粘贴，全程不用切换应用
- ✨ 完全本地转写，首次下载模型后音频和文字都不离开设备
- ✨ 支持 macOS（Apple silicon）、Windows x64/ARM64、Linux x86_64/ARM64
- ✨ 提供 Homebrew、AUR、Nix、Linux 安装脚本等多种安装方式
- ✨ 稳定版与 dev 双通道，dev 版本可自动从 dev 频道更新
- ✨ 侧边栏底部有 Labs，收纳实验性功能
- 👥 适合谁：适合经常需要大量输入文字、又在意隐私不想把语音传上云的 Mac、Windows、Linux 用户，比如写作者和开发者。

`Rust` · Fork 265 · 🔗 [官网](https://anoma.ly/hex)

## 📋 完整榜单

| # | 仓库 | 一句话定位 | 语言 | ⭐ | 今日 |
| --- | --- | --- | --- | --- | --- |
| 1 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 给 AI 编程助手加上跨会话持久记忆，自动捕获、压缩并复用上下文 | `TypeScript` | 112,197 | +1,139 |
| 2 | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | 让 AI Agent 通过系统无障碍树看见并操作桌面应用，不依赖截图和像素匹配 | `Rust` | 13,391 | +3,791 |
| 3 | [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | Rust 写的 Git worktree 管理 CLI，专为并行跑 AI agent 的工… | `Rust` | 10,648 | +438 |
| 4 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 纯 C 编写的分层推理引擎，让普通电脑跑起千亿参数 MoE 大模型 | `C` | 47,404 | +802 |
| 5 | [mattpocock/skills](https://github.com/mattpocock/skills) | 一套可直接安装的 AI 编程代理技能集，让代理按真实工程流程工作，告别随性式编码。 | `Shell` | 311,787 | +1,164 |
| 6 | [p-e-w/heretic](https://github.com/p-e-w/heretic) | 无需训练即可改造本地大模型，去掉拒答、减少废话和谄媚。 | `Python` | 38,996 | +701 |
| 7 | [spotify/portal-ai-plugins](https://github.com/spotify/portal-ai-plugins) | 把 Spotify Portal 的软件目录与运维工作流接入 AI 编码助手 | `TypeScript` | 3,096 | +91 |
| 8 | [floci-io/floci](https://github.com/floci-io/floci) | 一个免费开源的本地 AWS 模拟器，用一条 Docker 命令替代真实云环境。 | `Java` | 29,044 | +482 |
| 9 | [Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor) | 基于 Playwright 与 AI 的闲鱼多任务监控系统，带 Web 管理后台，帮你从海… | `Python` | 16,784 | +228 |
| 10 | [anomalyco/hex](https://github.com/anomalyco/hex) | 按住快捷键说话、松开就自动粘贴到当前应用的本地语音听写工具，支持 Mac、Windows … | `Rust` | 4,755 | +410 |
| 11 | [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 一站式 Python 爬虫框架：从单次请求到大规模并发爬取全都覆盖。 | `Python` | 95,300 | +1,658 |
| 12 | [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos) | 首个开源的金融 K 线基础模型，在 45 家以上全球交易所数据上预训练，可直接用于量化预测… | `Python` | 46,622 | +503 |
| 13 | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 把单个 Claude Code 会话变成 49 个 AI agent 组成的有层级的游戏工… | `Shell` | 34,906 | +1,182 |

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
