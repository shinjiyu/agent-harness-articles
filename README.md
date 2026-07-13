# agent-harness-articles

**Agent Harness 知识库**：教程知识点 + 持续更新的论文索引（分档 A/B/C、入库时间、A 档核心介绍）。

站点交互参考 [Harness Engineering 教程](https://onlyclaws.world/harness/)，论文按标签挂到对应知识点章节，并由 GitHub Actions 自动发布 Pages。

## 快速入口

| 用途 | 路径 |
|------|------|
| 学习站（构建产物） | [`site/`](site/) |
| 知识点文稿 | [`curriculum/`](curriculum/) |
| 论文索引 | [`indexes/agent-harness/`](indexes/agent-harness/) |
| 构建脚本 | [`scripts/build_site.py`](scripts/build_site.py) |

## 本地预览

```bash
python scripts/build_site.py
# 用任意静态服务器打开 site/，例如：
python -m http.server 8080 --directory site
```

浏览器打开 `http://localhost:8080`。

## 每日更新流程

1. 用 `_add_paper.py` 或直接改 `indexes/agent-harness/index.json` 入库（填 `indexed_at`、`tier`、`tags`）
2. A 档补充 `papers/a/<arxiv_id>.md`
3. 需要强制挂章时加 `knowledge_ids: ["token-economics"]`（章节 id 见 `curriculum/catalog.json`）
4. `python scripts/build_site.py`
5. 提交并推送 `main` → Actions 部署 GitHub Pages

首次启用 Pages：仓库 **Settings → Pages → Source = GitHub Actions**。

## 分档说明

| 档 | 含义 |
|----|------|
| **A** | 主张清晰，有受控对照或评测审计；含核心介绍 |
| **B** | 有实证，但样本/外推/复现有软肋 |
| **C** | 愿景、平台、技术报告或与主线关联偏弱 |

评级基于摘要级审阅，非全文同行评审。
