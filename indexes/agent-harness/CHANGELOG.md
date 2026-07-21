# Changelog — agent-harness 索引

按时间倒序记录批量变更。单篇微调也可记一行。

## 2026-07-21（入库）

- 监控拉取 `inbox/2026-07-21.json`：**29** 篇新候选（arxiv + semanticscholar + dblp；dblp 一关键词 500）
- 分档入库 **25** 篇（跳过 4 篇检索噪声：MHD 模拟器 / 视频异常检测 / KV cache / 类增量学习）
  - A：`2607.18235` 无普适最优发现 harness；`2607.17598` 渐进披露受控研究；`2605.14271` HarnessAudit 轨迹安全审计（均含核心介绍）
  - B：16 篇（HarnessX / Code as Agent Harness 综述 / W4S / VRR-Stop / TRIM / FlashRT / GPU kernel harness / SR-Agent / Adaptive Adversaries / CodeSlop autoresearch / 人格纠偏等）
  - C：6 篇（reranker / 智能电网教程 / 6G / SGA / NLKGQ / 行为仿真）
- 主索引现为 **106** 篇（A12 / B71 / C23）
- 重建站点内容

## 2026-07-16（入库）

- 监控拉取 `inbox/2026-07-16.json`：**19** 篇新候选（arxiv 为主；Semantic Scholar 429 跳过）
- 分档入库 **16** 篇（跳过 3 篇检索噪声：Rashba / 工业线束 / 足迹生物识别）
  - A：`2607.14004` Do Agent Optimizers Compound?；`2607.13683` Self-Evolving Agent Harnesses（含核心介绍）
  - B：10 篇（verifier cascade / AgentCompass / TRACE / STOCKTAKE / MemCon / Safety Sentry / MyAG / PhysClaw / agentic coding 采用 / AI 渗透测）
  - C：4 篇（Lean Shor / upskilling / DVM-HALL / Analogical Deep Research）
- 主索引现为 **81** 篇（A9 / B55 / C17）
- 重建站点内容

## 2026-07-14（入库）

- 从 `watchlist` 分档入库 **15** 篇（跳过 1 本图书噪声）
  - A：`2605.27922` Harness-Bench（含核心介绍）
  - B：14 篇（演化/定义/评测/技能/安全治理等）
  - C：`2605.15218` CAX-Agent（专域）
- 主索引现为 **65** 篇（A7 / B45 / C13）
- 重建站点内容

## 2026-07-14

- 接入与 Paper Trends 同源的论文监控：`scripts/monitor_papers.py`
  - 数据源：arxiv / semanticscholar / dblp（crossref、pubmed 可开关）
  - 产出：`watchlist.json` + `inbox/YYYY-MM-DD.json`（不自动分档入库）
  - Actions：`.github/workflows/monitor-papers.yml` 每日定时拉取

## 2026-07-13（站点）

- 新增学习站 `site/`（交互对齐 onlyclaws harness 教程）
- 新增知识点文稿 `curriculum/` + 构建脚本 `scripts/build_site.py`
- 论文按 `tags` / `knowledge_ids` 自动挂到对应章节
- GitHub Actions：`deploy-pages.yml` 推送 `main` 后自动构建并发布 Pages

## 2026-07-13（晚）

- 扩展 A 档技术详解：`papers/a/2607.06906.md`（The Harness Effect）
  - 补充 token 经济学公式、两区 prompt / compaction / offload 等六族机制、实验设计与 harness leverage 结果表

## 2026-07-13

- **创建索引库** `indexes/agent-harness/`
- 来源：Paper Trends 检索关键词 `agent harness` 当前结果页
- 入库时间统一为 `2026-07-13T17:32:31+08:00`
- 收录 **50** 篇：A **6** / B **32** / C **12**
- A 档已写核心介绍：
  - `2607.06906` The Harness Effect
  - `2607.08938` Better Harnesses, Smaller Models
  - `2607.04528` Measuring Harness-Induced Belief Divergence
  - `2607.02577` Benchmarking the Benchmarks
  - `2607.08028` From Prompts to Contracts
  - `2607.08124` TTHE
- 评级依据：摘要级审阅（非全文同行评审）
