# agent harness 论文索引

- 主题关键词：`agent harness`
- 创建时间：`2026-07-13T17:32:31+08:00`
- 最近更新：`2026-07-21T17:18:19+08:00`
- 条目数：**106**（A 12 / B 71 / C 23）
- 评级依据：abstract-level review (titles/authors/abstracts); not full-text peer review

权威数据源是 [`index.json`](index.json)。更新约定见 [`SCHEMA.md`](SCHEMA.md)。变更历史见 [`CHANGELOG.md`](CHANGELOG.md)。

## 分档标准（摘要级）

| 档 | 含义 |
|----|------|
| **A** | 主张清晰，有受控对照或评测审计，可指导工程决策 |
| **B** | 有实证，但样本/外推/复现有明显软肋 |
| **C** | 愿景、平台、技术报告或与主线关联偏弱 |

## A 档（含核心介绍）

### [2607.18235](http://arxiv.org/abs/2607.18235) · Automated Discovery Has No Universally Superior Harness

- 分档：`A` — 30 个预算对齐 harness×12 模型-问题对、310 万 rollout 重复试验；无普适最优 harness，应作超参调。
- 入库时间：`2026-07-21T17:18:19+08:00`
- ArXiv 公布：`2026-07-20`
- [核心介绍](papers/a/2607.18235.md)

### [2607.17598](http://arxiv.org/abs/2607.17598) · Is Progressive Disclosure All You Need for Long-Context Agents?

- 分档：`A` — 3 harness×3 模型族受控研究 Agent Skills 渐进披露；增益取决于 harness，一层足够。
- 入库时间：`2026-07-21T17:18:19+08:00`
- ArXiv 公布：`2026-07-20`
- [核心介绍](papers/a/2607.17598.md)

### [2607.14004](http://arxiv.org/abs/2607.14004) · Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0

- 分档：`A` — 三方法×两阶段 continual 对照；回归控制决定 harness 优化增益能否复利。
- 入库时间：`2026-07-16T17:53:42+08:00`
- ArXiv 公布：`2026-07-15`
- [核心介绍](papers/a/2607.14004.md)

### [2607.13683](http://arxiv.org/abs/2607.13683) · Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity

- 分档：`A` — 提案与计分分离；密封测试上 +9–15.5pp，病理键归档抗过拟合。
- 入库时间：`2026-07-16T17:53:42+08:00`
- ArXiv 公布：`2026-07-15`
- [核心介绍](papers/a/2607.13683.md)

### [2607.08938](http://arxiv.org/abs/2607.08938) · Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated Harness Adaptation

- 分档：`A` — 故障轨迹驱动自动适配；多任务×多 SLM，成本–性能数字具体。
- 入库时间：`2026-07-13T17:32:31+08:00`
- ArXiv 公布：`2026-07-10`
- [核心介绍](papers/a/2607.08938.md)

### [2607.08028](http://arxiv.org/abs/2607.08028) · From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents

- 分档：`A` — 合约/模型替换/提示vs代码消融齐全的企业工程模式。
- 入库时间：`2026-07-13T17:32:31+08:00`
- ArXiv 公布：`2026-07-09`
- [核心介绍](papers/a/2607.08028.md)

### [2607.08124](http://arxiv.org/abs/2607.08124) · TTHE: Test-Time Harness Evolution

- 分档：`A` — 测试时仅用未标注轨迹演化 harness；不改权重、不要金标。
- 入库时间：`2026-07-13T17:32:31+08:00`
- ArXiv 公布：`2026-07-09`
- [核心介绍](papers/a/2607.08124.md)

### [2607.06906](http://arxiv.org/abs/2607.06906) · The Harness Effect: How Orchestration Design Sets the Token Economics of Enterprise Agentic AI

- 分档：`A` — 锁任务锁模型只换编排层；多模型成本/时延/token 对照清晰。
- 入库时间：`2026-07-13T17:32:31+08:00`
- ArXiv 公布：`2026-07-08`
- [核心介绍](papers/a/2607.06906.md)

### [2607.04528](http://arxiv.org/abs/2607.04528) · Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents

- 分档：`A` — 把 harness 当作评测实验变量；信念诊断框架清晰。
- 入库时间：`2026-07-13T17:32:31+08:00`
- ArXiv 公布：`2026-07-06`
- [核心介绍](papers/a/2607.04528.md)

### [2607.02577](http://arxiv.org/abs/2607.02577) · Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation

- 分档：`A` — 工具调用基准有效性审计；人评分歧与重复方差证据硬。
- 入库时间：`2026-07-13T17:32:31+08:00`
- ArXiv 公布：`2026-07-01`
- [核心介绍](papers/a/2607.02577.md)

### [2605.27922](http://arxiv.org/abs/2605.27922) · Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows

- 分档：`A` — 跨模型实测 harness 效应；与 Harness Effect 互补的评测基建。
- 入库时间：`2026-07-14T17:32:32+08:00`
- ArXiv 公布：`2026-05-27`
- [核心介绍](papers/a/2605.27922.md)

### [2605.14271](http://arxiv.org/abs/2605.14271) · Auditing Agent Harness Safety

- 分档：`A` — 轨迹级 harness 安全审计：210 任务×8 域×10 配置；完成率与安全执行错位、违规随轨迹长度累积。
- 入库时间：`2026-07-21T17:18:19+08:00`
- ArXiv 公布：`2026-05-14`
- [核心介绍](papers/a/2605.14271.md)

## B 档

| ArXiv | 标题 | 入库时间 | 理由 |
|-------|------|----------|------|
| [2607.18171](http://arxiv.org/abs/2607.18171) | FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications | `2026-07-21T17:18:19+08:00` | chain-of-program 引导编码代理产出多 GPU 部署；数字亮但域限实时多模态服务。 |
| [2607.18161](http://arxiv.org/abs/2607.18161) | TRIM: Reducing AI-Generated CodeSlop via Agent Trajectory Minimization | `2026-07-21T17:18:19+08:00` | 定义 CodeSlop 并以轨迹最小化削减 17.9–32.9%；对代码库长期可维护性有工程价值。 |
| [2607.18064](http://arxiv.org/abs/2607.18064) | Autoresearch with Coding Agents: Generalizers and Metric-Maximizers on Quran Recitation Data | `2026-07-21T17:18:19+08:00` | 生产任务上自然捕获 spec gaming（逐行背答案）；加 held-out 后消失。样本小但预注册。 |
| [2607.18063](http://arxiv.org/abs/2607.18063) | Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security | `2026-07-21T17:18:19+08:00` | 自适应多轮攻击基准：15 轮 ASR 升至 5.4–14%；排名跨场景不一致。属安全评测基建。 |
| [2607.18039](http://arxiv.org/abs/2607.18039) | Evidence-in-the-Loop: Trace-Driven Optimization for Customer-Service LLM Agents | `2026-07-21T17:18:19+08:00` | 客服代理三个可复用部署模式；真实部署但属经验文，无对照数字。 |
| [2607.17979](http://arxiv.org/abs/2607.17979) | Harness Engineering for LLM-Driven GPU Kernel Generation | `2026-07-21T17:18:19+08:00` | 评测 harness 与优化控制器分离的内核生成系统；Agent-Assisted 胜 Full-Agent，域限竞赛。 |
| [2607.17900](http://arxiv.org/abs/2607.17900) | Harness TTS: Towards Context-Aware Expressive Speech Synthesis with Harness Layer | `2026-07-21T17:18:19+08:00` | 把 harness 层思想搬到 TTS 表达控制；路由+合成双评测，领域专属。 |
| [2607.17719](http://arxiv.org/abs/2607.17719) | SR-Agent: An Experience-Driven Agentic Framework for Post-Ranking Strategies Refinement in E-Commerce Recommendation | `2026-07-21T17:18:19+08:00` | 工业推荐后排策略精炼 harness；快手一个月 A/B 在线部署，域专属。 |
| [2607.17641](http://arxiv.org/abs/2607.17641) | Verify, Repair, Repeat, or Stop? Robust Stopping for Noisy Verify-Repair Loops in LLM Agents | `2026-07-21T17:18:19+08:00` | 噪声 verify-repair 环的鲁棒停机理论+GSM8K 压力测试 +60.6pp；实证域窄。 |
| [2607.17420](http://arxiv.org/abs/2607.17420) | The Librarian Who Refused to Code: Model-Dependent Identity Enactment in LLM Code Generation | `2026-07-21T17:18:19+08:00` | 预注册人格 prompt 对照：效应依模型而异；对 harness 提示层设计有纠偏价值。 |
| [2607.14047](http://arxiv.org/abs/2607.14047) | PhysClaw-0: A Symbiotic Agentic System for Robot Autonomy via Language Corrections | `2026-07-16T17:53:42+08:00` | 纠正记忆跨轮复用降人工成本；具身数据采集设定，复现门槛高。 |
| [2607.14037](http://arxiv.org/abs/2607.14037) | Early Adoption of Agentic Coding Tools by GitHub Projects | `2026-07-16T17:53:42+08:00` | 大规模 GitHub agentic PR 采用实证；观测性早期快照，非方法贡献。 |
| [2607.14006](http://arxiv.org/abs/2607.14006) | Rethinking Penetration Testing for AI-Enabled Systems: From Resource Compromise to Behavioral Objective Violation | `2026-07-16T17:53:42+08:00` | 把 AI 渗透测从基础设施攻陷扩展到行为目标违背；框架/定义文。 |
| [2607.13988](http://arxiv.org/abs/2607.13988) | TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents | `2026-07-16T17:53:42+08:00` | 回合级信用分配显著提升长程工具使用；属 agentic RL，非 harness 编排主线。 |
| [2607.13918](http://arxiv.org/abs/2607.13918) | Partially Correlated Verifier Cascades in LLM Harnesses: Concave Log-Odds, Polynomial Reliability, and Blind-Spot Ceilings | `2026-07-16T17:53:42+08:00` | 部分相关 verifier cascade 理论清晰；实证偏合成，工程外推待核。 |
| [2607.13705](http://arxiv.org/abs/2607.13705) | AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities | `2026-07-16T17:53:42+08:00` | Benchmark/Harness/Environment 解耦的评测基建；覆盖广但非因果实验。 |
| [2607.13618](http://arxiv.org/abs/2607.13618) | STOCKTAKE: Measuring the Gap Between Perception and Action in LLM Agents with a Fair Oracle | `2026-07-16T17:53:42+08:00` | 公平 oracle 拆开「感知 vs 行动」缺口；供应链专域，样本模型有限。 |
| [2607.13594](http://arxiv.org/abs/2607.13594) | SAFETY SENTRY: Context-Aware Human Intervention via EXECUTE-ASK-REFUSE Routing | `2026-07-16T17:53:42+08:00` | EXECUTE/ASK/REFUSE 三路路由比二元护栏更贴近部署；护栏模型评测，非完整 harness。 |
| [2607.13591](http://arxiv.org/abs/2607.13591) | Memory as a Controlled Process: Learned Adaptive Memory Management for LLM Agents | `2026-07-16T17:53:42+08:00` | 把记忆当可控过程并用轻量策略学习；多基准增益明确，属记忆层非全 harness。 |
| [2607.13474](http://arxiv.org/abs/2607.13474) | MyAG: A Graph-Based Framework for Designing and Analyzing Composable LLM Agent Systems | `2026-07-16T17:53:42+08:00` | 组件/工作流/搜索三图抽象便于组合分析；框架文，实证偏代表性应用。 |
| [2607.08716](http://arxiv.org/abs/2607.08716) | Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents | `2026-07-13T17:32:31+08:00` | 消融较全、基准增益明确；记忆代理成本披露不足。 |
| [2607.09175](http://arxiv.org/abs/2607.09175) | Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift | `2026-07-13T17:32:31+08:00` | 多副本 pass³ 结果强，但域偏电信固定工具栈。 |
| [2607.09195](http://arxiv.org/abs/2607.09195) | Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents | `2026-07-13T17:32:31+08:00` | HEP 可审计假设循环概念清晰；实证域偏材料科学。 |
| [2607.08448](http://arxiv.org/abs/2607.08448) | Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents | `2026-07-13T17:32:31+08:00` | 涨幅大但具身扰动设定与复现门槛高。 |
| [2607.08497](http://arxiv.org/abs/2607.08497) | Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing | `2026-07-13T17:32:31+08:00` | CMA-Harness 与长对话检索数字亮；依赖自建数据与基准。 |
| [2607.06764](http://arxiv.org/abs/2607.06764) | Cost-Effective Agent Harnesses for Abstract Reasoning and Generalization on ARC-AGI-1 | `2026-07-13T17:32:31+08:00` | 预算约束下架构消融清楚；强绑定 ARC 设定。 |
| [2607.05369](http://arxiv.org/abs/2607.05369) | GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks | `2026-07-13T17:32:31+08:00` | 图即策略+仿真自精炼设计清楚；新基准外推待观察。 |
| [2607.05377](http://arxiv.org/abs/2607.05377) | Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation | `2026-07-13T17:32:31+08:00` | 双向对齐与技能原语工程扎实；具身复现成本高。 |
| [2607.05382](http://arxiv.org/abs/2607.05382) | Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Visual Generation | `2026-07-13T17:32:31+08:00` | 基准与共训练配方完整；与 harness 主线为相邻域。 |
| [2607.05743](http://arxiv.org/abs/2607.05743) | The Balkanization of Execution-Security Research for AI Coding Agents | `2026-07-13T17:32:31+08:00` | 系统化综述有价值；本身非新方法实证。 |
| [2607.05744](http://arxiv.org/abs/2607.05744) | Unicode TAG-Block Concealment of Tool-Metadata Payloads in the Model Context Protocol | `2026-07-13T17:32:31+08:00` | 机制分析+多实现一致 PoC；安全影响大但属漏洞披露型。 |
| [2607.06256](http://arxiv.org/abs/2607.06256) | Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition | `2026-07-13T17:32:31+08:00` | 诊断型贡献扎实；偏问题刻画而非完整解法。 |
| [2607.06341](http://arxiv.org/abs/2607.06341) | Harnessing Code Agents for Automatic Software Verification | `2026-07-13T17:32:31+08:00` | 全覆盖验证结果极强；高度依赖强模型与工具约束设计。 |
| [2607.04758](http://arxiv.org/abs/2607.04758) | AgenticPD: A Stage-Aware Agentic Framework for Physical Design QoR Optimization | `2026-07-13T17:32:31+08:00` | 阶段感知 harness 对 EDA 有意义；领域专属难横向比。 |
| [2607.05458](http://arxiv.org/abs/2607.05458) | Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning | `2026-07-13T17:32:31+08:00` | 形式化清晰且有消融；域偏窄、终局收益受离线缓冲限制。 |
| [2607.05462](http://arxiv.org/abs/2607.05462) | Evaluating calibrated refusal and safe usefulness in dual-use biology settings | `2026-07-13T17:32:31+08:00` | BioSecBench 有校准拒答价值；与 harness 优化主线相邻。 |
| [2607.03935](http://arxiv.org/abs/2607.03935) | Harness-Aware Self-Evolving: Co-Evolving Model Weights, Harness, and Task Solutions | `2026-07-13T17:32:31+08:00` | 权重–harness 共演化设定新；任务覆盖与稳定性需全文核实。 |
| [2607.03451](http://arxiv.org/abs/2607.03451) | SkillOpt-Lite: Better and Faster Agent Self-evolution via One Line of Vibe | `2026-07-13T17:32:31+08:00` | 最小技能优化管线与 HarnessOpt 外推有趣；任务选择可能偏友好。 |
| [2607.02436](http://arxiv.org/abs/2607.02436) | Reasoning effort, not tool access, buys first-try reliability in agentic code generation: an observational study | `2026-07-13T17:32:31+08:00` | 观测设计对「工具越多越好」有纠偏；非因果实验。 |
| [2607.02469](http://arxiv.org/abs/2607.02469) | TestEvo-Bench: An Executable and Live Benchmark for Test and Code Co-Evolution | `2026-07-13T17:32:31+08:00` | 可执行 live 基准建设扎实；属评测基建而非 harness 方法。 |
| [2607.02807](http://arxiv.org/abs/2607.02807) | SwarmResearch: Orchestrating Coding Agents for Open-Ended Discovery | `2026-07-13T17:32:31+08:00` | 编排器–子代理设计清楚；开放式优化难做硬对照。 |
| [2607.01510](http://arxiv.org/abs/2607.01510) | Janus: a Playground for User-Involved Agentic Permission Management | `2026-07-13T17:32:31+08:00` | 权限设计空间与评估框架有用；综合响应用户限制生态效度。 |
| [2607.01709](http://arxiv.org/abs/2607.01709) | COMFYCLAW: Self-Evolving Skill Harnesses for Image Generation Workflows | `2026-07-13T17:32:31+08:00` | 技能演化在视觉工作流上证据完整；领域专属。 |
| [2607.01916](http://arxiv.org/abs/2607.01916) | ContextSniper: AntTrail's Token-Efficient Code Memory for Repository-Level Program Repair | `2026-07-13T17:32:31+08:00` | token/成本降幅明确且解析率大致不变；宿主代理设定限定。 |
| [2607.02255](http://arxiv.org/abs/2607.02255) | AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents | `2026-07-13T17:32:31+08:00` | 有界记忆合约测试床有价值；关键对比样本小且非决定性。 |
| [2607.02294](http://arxiv.org/abs/2607.02294) | Coding Agents Are Guessing: Measuring Action-Boundary Violations in Underspecified DevOps Instructions | `2026-07-13T17:32:31+08:00` | UnderSpecBench 规格不足诊断有力；属安全评测基建。 |
| [2606.32007](http://arxiv.org/abs/2606.32007) | AxDafny: Agentic Verified Code Generation in Dafny | `2026-07-13T17:32:31+08:00` | 验证成功率提升明确；依赖验证器反馈循环与强模型。 |
| [2607.00269](http://arxiv.org/abs/2607.00269) | Mnemosyne: Agentic Transaction Processing for Validating and Repairing AI-generated Workflows | `2026-07-13T17:32:31+08:00` | ATP 准入模型与安全属性表述强；实时试点规模仍有限。 |
| [2607.00692](http://arxiv.org/abs/2607.00692) | Self-GC: Self-Governing Context for Long-Horizon LLM Agents | `2026-07-13T17:32:31+08:00` | 生产衍生套件与 token 节省有说服力；「无影响延续」指标需细读定义。 |
| [2607.00871](http://arxiv.org/abs/2607.00871) | Self-Evolving Agents with Anytime-Valid Certificates | `2026-07-13T17:32:31+08:00` | 门控证书机制诚实；摘要已承认单次 run/方差未确认。 |
| [2607.02588](http://arxiv.org/abs/2607.02588) | Homer: Understanding Long-form Videos with Hierarchical Memory and Agentic Reasoning | `2026-07-13T17:32:31+08:00` | 分层记忆+多 backbone 提升；属视频代理相邻域。 |
| [2607.02599](http://arxiv.org/abs/2607.02599) | AgentLTL: A Trace-Verification Framework for Measuring, Enforcing, and Training Procedural Compliance in Tool-Using LLM Agents | `2026-07-13T17:32:31+08:00` | FO-LTL 过程合规框架清晰；基准覆盖与外推待核。 |
| [2606.21856](http://arxiv.org/abs/2606.21856) | Harness-MU: A Safe, Governed, and Effective Harness for Multi-User LLM Agents | `2026-07-14T17:32:32+08:00` | 多用户 LLM 代理的安全治理 harness；领域专用。 |
| [2606.15874](http://arxiv.org/abs/2606.15874) | LLM-as-Code: Agentic Programming for Agent Harness | `2026-07-14T17:32:32+08:00` | LLM-as-Code 架构主张清晰；实证偏案例，外推待核。 |
| [2606.14249](http://arxiv.org/abs/2606.14249) | HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry | `2026-07-21T17:18:19+08:00` | 可组合/可演化 harness foundry，5 基准平均 +14.5%；严谨性细节与开源待核。 |
| [2606.12882](http://arxiv.org/abs/2606.12882) | HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness | `2026-07-14T17:32:32+08:00` | 可学习双向 harness 控制器；工程贡献明确，域覆盖待核。 |
| [2606.11686](http://arxiv.org/abs/2606.11686) | Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness | `2026-07-14T17:32:32+08:00` | 对确定性脚手架做无 LLM 回归锁定测试；工程评测味道浓。 |
| [2606.10106](http://arxiv.org/abs/2606.10106) | What makes a harness a harness: necessary and sufficient conditions for an agent harness | `2026-07-14T17:32:32+08:00` | 给出 harness 必要充分条件的概念框架；偏定义文。 |
| [2606.08348](http://arxiv.org/abs/2606.08348) | Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses | `2026-07-14T17:32:32+08:00` | 后验引导的技能演化；自演化+harness 交叉。 |
| [2606.20631](http://arxiv.org/abs/2606.20631) | Harnessing Agent Skills: Architectural Patterns and a Reference Architecture for Skill-Mediated LLM Agents | `2026-07-14T17:32:32+08:00` | 技能中介 LLM 代理的架构模式与参考架构；综述/模式文。 |
| [2605.30621](http://arxiv.org/abs/2605.30621) | Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents | `2026-07-14T17:32:32+08:00` | 区分「能更新 harness」与「更新带来收益」；对自演化叙事有纠偏。 |
| [2605.21825](http://arxiv.org/abs/2605.21825) | Toward AI VIS Co-Scientists: A General and End-to-End Agent Harness for Solving Complex Data Visualization Tasks | `2026-07-21T17:18:19+08:00` | 端到端 VIS 应用设计 harness，SciVis 竞赛验证；域专属。 |
| [2605.18747](http://arxiv.org/abs/2605.18747) | Code as Agent Harness | `2026-07-21T17:18:19+08:00` | 「代码即 harness」三层统一视角综述；覆盖广，属综述非新实证。 |
| [2605.15184](http://arxiv.org/abs/2605.15184) | Is Grep All You Need? How Agent Harnesses Reshape Agentic Search | `2026-07-14T17:32:32+08:00` | 讨论 harness 如何重塑 agentic search；偏经验/系统设计。 |
| [2605.00663](http://arxiv.org/abs/2605.00663) | Affordance Agent Harness: Verification-Gated Skill Orchestration | `2026-07-21T17:18:19+08:00` | 验证门控技能编排改善 affordance 接地的精度-成本前沿；具身专域。 |
| [2604.25850](http://arxiv.org/abs/2604.25850) | Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses | `2026-07-14T17:32:32+08:00` | 可观测驱动的编码 harness 自动演化；自演化路线实证。 |
| [2604.07236](http://arxiv.org/abs/2604.07236) | How Much Heavy Lifting Can an Agent Harness Do?: Measuring the LLM's Residual Role in a Planning Agent | `2026-07-14T17:32:32+08:00` | 度量 harness 承担多少重活 vs LLM 残差角色；测量设计清楚。 |
| [2603.20380](http://arxiv.org/abs/2603.20380) | Herding CATs: ALARA for Agent Harness Engineering in Portable Composable Multi-Agent Teams | `2026-07-21T17:18:19+08:00` | CAT 纯文本数据层管理多代理 harness；22 模型×115 任务评测，工具偏小众。 |
| [2602.22480](http://arxiv.org/abs/2602.22480) | VeRO: A Harness for Agents to Optimize Agents | `2026-07-14T17:32:32+08:00` | 用代理优化代理的评估 harness（VeRO）；评测基建。 |
| [2601.15322](http://arxiv.org/abs/2601.15322) | Replayable Financial Agents: A Determinism-Faithfulness Assurance Harness for Tool-Using LLM Agents | `2026-07-14T17:32:32+08:00` | 金融工具调用代理的可重放/确定性保真 harness。 |
| [2504.04785](http://arxiv.org/abs/2504.04785) | Weak-for-Strong: Training Weak Meta-Agent to Harness Strong Executors | `2026-07-21T17:18:19+08:00` | 弱 meta-agent 经 RL 学会设计工作流驾驭强执行器；11 基准增益，2025 文补录。 |

## C 档

| ArXiv | 标题 | 入库时间 | 理由 |
|-------|------|----------|------|
| [2607.18152](http://arxiv.org/abs/2607.18152) | jina-reranker-v3.5: An Efficient Listwise Reranker with Hybrid Attention and Self-Distillation | `2026-07-21T17:18:19+08:00` | listwise reranker 模型发布；agentic 检索组件，与 harness 主线关联弱。 |
| [2607.18147](http://arxiv.org/abs/2607.18147) | LLMs and Agentic AI Systems for Smart Grids: A Tutorial on Architectures and Applications | `2026-07-21T17:18:19+08:00` | 智能电网 agentic 系统教程 + solver-grounded 原则；教程/领域文。 |
| [2607.18138](http://arxiv.org/abs/2607.18138) | AI Agent Communications in AI-Native 6G Network: Status, Challenges and Opportunities | `2026-07-21T17:18:19+08:00` | 6G 网络承载 AI agent 通信的差距分析；愿景/标准化文。 |
| [2607.18116](http://arxiv.org/abs/2607.18116) | SGA: Plug&Play Geometric Verification for Educational Video Synthesis | `2026-07-21T17:18:19+08:00` | 教育视频合成的几何验证插件；专域验证模块。 |
| [2607.18029](http://arxiv.org/abs/2607.18029) | Natural Language Access to Domain-Specific Metadata: A Reusable Framework for LLM Query Generation | `2026-07-21T17:18:19+08:00` | OWL 本体 + LLM 生成 SPARQL 的元数据查询 harness；专域框架。 |
| [2607.17437](http://arxiv.org/abs/2607.17437) | Empirical Grounding Improves the Realism of LLM Agents Simulating Human Behavior During Disruptions | `2026-07-21T17:18:19+08:00` | 经验接地提升 LLM 代理行为仿真真实度；仿真相邻域。 |
| [2607.14082](http://arxiv.org/abs/2607.14082) | Building Shor's Algorithm in Lean: An Agentic Formalization of Quantum Attacks on RSA-2048 and P-256 | `2026-07-16T17:53:42+08:00` | Lean 中 agentic 形式化 Shor；与 LLM agent harness 主线关联弱。 |
| [2607.14044](http://arxiv.org/abs/2607.14044) | AI-accelerated End-to-End Framework for Rapid Professional Upskilling | `2026-07-16T17:53:42+08:00` | 企业 upskilling 端到端框架；产品/培训叙事，非 harness 方法。 |
| [2607.13998](http://arxiv.org/abs/2607.13998) | The Dynamic Verifiable Multi-Agent Human Agentic Loyalty Loop (DVM-HALL) Model and the Net Human-Agent Score (NHAS) in Autonomous Commerce | `2026-07-16T17:53:42+08:00` | 自主商务忠诚度概念模型；愿景/理论，待三阶段实证。 |
| [2607.13602](http://arxiv.org/abs/2607.13602) | Analogical Deep Research: Retrieving and Integrating Historical Analogies for Foresight Analysis | `2026-07-16T17:53:42+08:00` | 历史类比 deep research；与 harness 编排主线相邻偏弱。 |
| [2607.07859](http://arxiv.org/abs/2607.07859) | Feedback Manipulation Regularization: Enabling Offline Agent Alignment for Imitation Learning | `2026-07-13T17:32:31+08:00` | 经典 RL 对齐工作；与 LLM agent harness 主线关联弱（检索噪声）。 |
| [2607.07534](http://arxiv.org/abs/2607.07534) | Infinite Worlds with Versatile Interactions | `2026-07-13T17:32:31+08:00` | 世界模型产品报告气质；agent harness 非核心主张。 |
| [2607.04394](http://arxiv.org/abs/2607.04394) | MechMath Agent Team: LLM Driven Agents for Mathematical Research | `2026-07-13T17:32:31+08:00` | 三平面工具架构有启发；开放问题解决偏部署叙事。 |
| [2607.05471](http://arxiv.org/abs/2607.05471) | KAT-Coder-V2.5 Technical Report | `2026-07-13T17:32:31+08:00` | 编码代理技术报告；科学主张需相对产品叙事打折。 |
| [2607.04089](http://arxiv.org/abs/2607.04089) | PLACEMEM: Toward a Compute-Aware Memory Plane for Lifelong Agents | `2026-07-13T17:32:31+08:00` | 概念与原型路线图；摘要主动降低了已实现功能边界。 |
| [2607.03601](http://arxiv.org/abs/2607.03601) | ArchEval: Measuring AI Agents as Computer Architects | `2026-07-13T17:32:31+08:00` | 领域基准首发；工具支持层级设定有价值但属基建。 |
| [2607.03863](http://arxiv.org/abs/2607.03863) | Rethinking Scientific Discovery in the Agentic Era | `2026-07-13T17:32:31+08:00` | SCION Meta-Harness 愿景完整；完成度取决于后续采用。 |
| [2607.02440](http://arxiv.org/abs/2607.02440) | EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments | `2026-07-13T17:32:31+08:00` | 策略演化评测设定有用；排行榜型首发。 |
| [2607.03105](http://arxiv.org/abs/2607.03105) | ORBIT-Q: Dual-axis benchmarking of autonomous agents in scientific quantum programming | `2026-07-13T17:32:31+08:00` | 量子科学编程双轴基准；专域基建。 |
| [2607.01120](http://arxiv.org/abs/2607.01120) | Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents | `2026-07-13T17:32:31+08:00` | 系统愿景与支柱论述强；实例化偏路线图。 |
| [2607.01152](http://arxiv.org/abs/2607.01152) | AGC-Bench: Measuring Artificial General Creativity | `2026-07-13T17:32:31+08:00` | 创造力基准与 harness 主线弱相关；作地图收录。 |
| [2607.02598](http://arxiv.org/abs/2607.02598) | Evaluating Agentic Harness Systems for Autonomous Computational Pathology | `2026-07-13T17:32:31+08:00` | ACP-Bench 病理专域审计基准；端到端成熟度仍低。 |
| [2605.15218](http://arxiv.org/abs/2605.15218) | CAX-Agent: A Lightweight Agent Harness for Reliable APDL Automation | `2026-07-14T17:32:32+08:00` | APDL/CAE 专域轻量 harness；与通用 harness 主线关联弱。 |

## 持续更新

1. 按 `arxiv_id` 查重。
2. 新文写入 `index.json`，填写 `indexed_at`（加入索引时间）与 `tier` / `tier_reason`。
3. A 档必须新增 `papers/a/<arxiv_id>.md` 核心介绍，并设置 `core_intro_path`。
4. 更新库级 `updated_at`，在 `CHANGELOG.md` 追加记录。
5. 运行 `python _regen_readme.py` 刷新本页。
