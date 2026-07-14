# Changelog — agent-harness 索引

按时间倒序记录批量变更。单篇微调也可记一行。

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
