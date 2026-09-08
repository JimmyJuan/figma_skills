# figma_skills

团队共享的 Figma 工作规则库。它把「我们是怎样使用 Figma 的」写成对人和 AI 都可读、可版本化、可评审的规范。

团队已决定用一个 Notion workspace 作为正式知识源。在 Notion 的精确数据库 URL 和首条已验证的 Published 规则尚未记录前，本仓库仍是现有规则包的执行来源。完成切换后，本仓库作为可版本化、对 AI 友好的技能镜像；Obsidian 和 Figma 只保存入口、版本和内容 hash，不维护独立全量副本。

## 规则索引

| 规则 | 版本 | 用途 | 入口 |
| --- | --- | --- | --- |
| 设计源与 RC 基线 | 1.0.0 | 优先 RC；任务保持选定批次，用户明确指定才换版；非 RC 提醒后可继续 | [`rules/design-source/SKILL.md`](rules/design-source/SKILL.md) |
| 线性用户旅程 | 0.1.1 | 建立可扫描的角色旅程，并让重复页面通过 Component / Instance 安全同步 | [`rules/linear-user-journey/SKILL.md`](rules/linear-user-journey/SKILL.md) |

## 如何使用

### 团队成员

先读规则入口，再按其中的命名、布局、同步和迁移协议操作。对已有画布做组件化迁移前，必须先确认「哪些画面属于同一个概念页面」的映射。

### Codex / Claude Code 等代码代理

把本仓库加入工作区，或把相关 `SKILL.md` 安装为技能。代理应根据任务语义选择规则；不应依靠关键词或正则表达式猜测意图。

### 网页版 ChatGPT

在 ChatGPT 中连接 GitHub 后提供本仓库链接，或把对应的 `SKILL.md` 和它引用的 `references/` 文件上传到 Project。可直接这样发起任务：

> 请先读取 `figma_skills/rules/linear-user-journey/SKILL.md` 及它要求的 references，再分析或修改这份 Figma 用户旅程。

普通聊天不会自动读取任意 GitHub 仓库；需要 GitHub 连接、Project 文件或在对话中提供链接。Figma 也没有跨所有文件生效的账号级 AI 指令，因此每个相关 Figma 文件应放一个轻量规则入口，指向本仓库的固定规则路径。

## 团队协作账号

为团队注册或连接 Notion、Figma 等协作服务前，先读取 [`docs/team-account-policy.md`](docs/team-account-policy.md)。它记录默认邮箱、外部协作者例外、授权边界和凭据安全要求。

## 设计原则

- 语义判断交给模型并保留理由；身份、权限、节点关系、状态机和写入范围使用确定性约束。
- Figma 中同一个概念页面只维护一个主组件；旅程中的每次出现使用 Instance。
- 主组件修改用于全局同步；Instance override / variant 用于旅程特有状态；旅程注释和连接线放在实例外。
- Multi-edit 只能作为一次性迁移辅助，不是持久同步机制。
- 任何 Figma 写入都要先确认精确目标、授权范围与 freshness 状态。

## 贡献新规则

1. 在 `rules/<rule-id>/` 创建独立技能目录。
2. 在 `SKILL.md` 写清触发范围、工作流、权限边界和验证方式。
3. 把长篇规范、示例和评测放进 `references/`，脚本只验证确定性结构。
4. 更新本页索引，运行技能与脚本验证，再提交评审。
