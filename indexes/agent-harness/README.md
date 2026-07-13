# agent harness 论文索引

- 主题关键词：`agent harness`
- 创建时间：`2026-07-13T17:32:31+08:00`
- 最近更新：`2026-07-13T17:32:31+08:00`
- 条目数：**50**（A 6 / B 32 / C 12）
- 评级依据：abstract-level review (titles/authors/abstracts); not full-text peer review

权威数据源是 [`index.json`](index.json)。更新约定见 [`SCHEMA.md`](SCHEMA.md)。变更历史见 [`CHANGELOG.md`](CHANGELOG.md)。

## 分档标准（摘要级）

| 档 | 含义 |
|----|------|
| **A** | 主张清晰，有受控对照或评测审计，可指导工程决策 |
| **B** | 有实证，但样本/外推/复现有明显软肋 |
| **C** | 愿景、平台、技术报告或与主线关联偏弱 |

## A 档（含核心介绍）

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

## B 档

| ArXiv | 标题 | 入库时间 | 理由 |
|-------|------|----------|------|
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

## C 档

| ArXiv | 标题 | 入库时间 | 理由 |
|-------|------|----------|------|
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

## 持续更新

1. 按 `arxiv_id` 查重。
2. 新文写入 `index.json`，填写 `indexed_at`（加入索引时间）与 `tier` / `tier_reason`。
3. A 档必须新增 `papers/a/<arxiv_id>.md` 核心介绍，并设置 `core_intro_path`。
4. 更新库级 `updated_at`，在 `CHANGELOG.md` 追加记录。
5. 运行 `python _regen_readme.py` 刷新本页。
