# Agent Harness 知识库

这是一套把 **Harness 工程知识点** 与 **持续更新的论文索引** 绑在一起的学习站。

它不教你训练更大模型，而教你驾驭模型——设计 Agent 运行的环境、约束、工具、记忆、评估与反馈闭环；并把每天入库的论文挂到对应知识点下，方便对照阅读。

## 什么是 Harness？

Harness 原意是「马具 / 挽具」。在 AI 里，它指围绕大模型搭建的完整运行支架：控制流、工具、记忆、护栏、评估、可观测、生命周期管理。

**模型是马，Harness 是让这匹马能在真实道路上稳定拉车的全套装备。**

> 模型是简单的部分，可靠性才是这份工作。
> *The model is the easy part. The reliability is the job.*

## 本站结构

- **左侧**：按模块排列的知识点章节
- **正文**：概念讲解 + 关键要点
- **相关论文**：由 `indexes/agent-harness/index.json` 按标签自动挂载；A 档可跳转核心介绍

## 你将串起来的能力

1. 成本与 Token 经济学：为什么编排层决定账单
2. 上下文与记忆：决定每次推理「让模型看见什么」
3. 编排与演化：适配、测试时演化、技能库
4. 合约与审计：从提示原型到可验证工件
5. 评估与偏差：把 harness 当作实验变量
6. 安全与权限：MCP、规格不足、权限助手
7. 具身与多模态：VLA / 长视频等相邻 harness

数据来源见仓库 [`indexes/agent-harness/`](https://github.com/shinjiyu/agent-harness-articles/tree/main/indexes/agent-harness)。教程交互参考了 [Harness Engineering 教程](https://onlyclaws.world/harness/)。
