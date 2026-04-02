# Agent Skills 集合

[English](./README.md)

这是一个可复用的 Agent Skills 仓库，用来沉淀和分享面向 Codex 及兼容 Agent Skills 运行时的工作流技能。

本仓库按 skill 集合的方式组织。每个 skill 位于 `skills/<skill-name>/` 目录下，通常会包含：

- `SKILL.md`：给 Codex 使用的技能说明
- `README.md`：给 GitHub 读者使用的文档
- `scripts/`：可执行辅助脚本
- `references/`：参考资料
- `assets/`：模板和资源文件
- `agents/openai.yaml`：可选的 UI 元数据

## 前置要求

- 已安装 Node.js 环境
- 能够运行 `npx bun` 命令

## 安装方式

使用 `skills` CLI 从这个仓库安装 skill。

### 快速安装（推荐）

安装整个仓库：

```bash
npx skills add chunge16/chunge-skills
```

安装仓库中的指定 skill：

```bash
npx skills add chunge16/chunge-skills --skill git-activity-report
```

安装前先查看本仓库包含哪些 skill：

```bash
npx skills add chunge16/chunge-skills --list
```

如果你想安装到全局而不是当前项目：

```bash
npx skills add chunge16/chunge-skills --skill git-activity-report --global
```

### 仓库结构

```text
chunge-skills/
├── README.md
├── README.zh.md
├── LICENSE
└── skills/
    └── git-activity-report/
        ├── README.md
        ├── SKILL.md
        ├── LICENSE.txt
        ├── agents/
        │   └── openai.yaml
        ├── scripts/
        │   └── generate_report.py
        └── references/
            └── periods.md
```

## 可用 Skills

本仓库按实际工作流场景来组织 skill。

### 报告生成类

用于把仓库活动整理成结构化工程报告的 skill。

#### `git-activity-report`

基于 git commit 历史生成日报、周报和月报，既支持单仓库，也支持按项目根目录聚合多个仓库。

典型场景：

- 工程日报
- 周报与月报汇总
- 多仓库开发活动归总
- 按作者筛选贡献记录

快速使用示例：

```text
使用 $git-activity-report 生成今天的日报
使用 $git-activity-report 生成本周周报
使用 $git-activity-report 汇总 /path/to/projects 下的所有仓库
使用 $git-activity-report 为 /path/to/repo 生成月报
使用 $git-activity-report 通过 --author "alice" 生成周报
使用 $git-activity-report 通过 --since 2026-04-01 --until 2026-04-01T18:00:00 生成昨天的日报
使用 $git-activity-report 通过 --format json 导出月报
```

相关文档：

- [git-activity-report README](./skills/git-activity-report/README.md)
- [git-activity-report SKILL.md](./skills/git-activity-report/SKILL.md)

## 说明

- 每个 skill 的安装、配置、示例和输出样例，建议维护在该 skill 自己的 `README.md` 中。
- `SKILL.md` 主要面向 Codex 的触发和运行时指导，不是面向 GitHub 读者的长文档。

## 贡献方式

新增一个 skill 时，建议按下面的步骤组织：

1. 在 `skills/` 下创建新目录
2. 添加 `SKILL.md`
3. 添加面向用户的 `README.md`
4. 需要时补充 `agents/openai.yaml`
5. 只有在确实需要时才加入 `scripts/`、`references/` 或 `assets/`
6. 在 skill 目录中加入 `LICENSE.txt`
7. 在本 README 的 `可用 Skills` 中补充该 skill 的说明

## License

仓库级许可证见 [LICENSE](./LICENSE)。

每个 skill 也可以有自己单独的许可证，例如 [skills/git-activity-report/LICENSE.txt](./skills/git-activity-report/LICENSE.txt)。
