# agent-harness 索引 Schema

持续更新时请遵守本约定，保证 `index.json` 可机器读取、可合并。

## 文件布局

```
indexes/agent-harness/
  index.json              # 主索引（唯一权威数据源）
  README.md               # 人类可读总览（可由 index 同步）
  CHANGELOG.md            # 每次批量变更记录
  SCHEMA.md               # 本约定
  papers/
    a/<arxiv_id>.md       # A 档核心介绍（必填）
    b/<arxiv_id>.md       # B 档可选补充笔记
    c/<arxiv_id>.md       # C 档可选补充笔记
```

## `index.json` 字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `topic` | string | 主题名 |
| `schema_version` | number | 当前为 `1` |
| `created_at` | string | 库创建时间 ISO-8601 |
| `updated_at` | string | 最近一次更新时间 ISO-8601 |
| `papers[]` | array | 论文条目 |

### `papers[]` 条目

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `arxiv_id` | string | 是 | 不含版本号，如 `2607.06906` |
| `arxiv_version` | string | 否 | 入库时版本，如 `v1` |
| `title` | string | 是 | 英文标题 |
| `authors` | string[] | 否 | 作者列表 |
| `published` | string | 否 | ArXiv 公布日期 `YYYY-MM-DD` |
| `url` | string | 是 | 论文链接 |
| `source` | string | 否 | 默认 `arxiv` |
| `tier` | `"A"\|"B"\|"C"` | 是 | 分档结果 |
| `tier_reason` | string | 是 | 一句话分档理由 |
| `indexed_at` | string | 是 | **加入本索引的时间** ISO-8601 |
| `updated_at` | string | 否 | 条目修订时间（改档/改正文时更新） |
| `tags` | string[] | 否 | 主题标签 |
| `core_intro_path` | string | A 必填 | 相对路径，如 `papers/a/2607.06906.md` |
| `notes` | string | 否 | 短备注 |
| `knowledge_ids` | string[] | 否 | 强制挂到站点章节 id（见 `curriculum/catalog.json`）；不填则按 `tags` 自动匹配 |

## 更新流程

1. 查重：按 `arxiv_id` 是否已在 `papers` 中。
2. 新文：写入条目，`indexed_at` / 库级 `updated_at` 设为当前时间；A 档同步新建 `papers/a/<id>.md`。
3. 改档：更新 `tier`、`tier_reason`、条目 `updated_at`；若升为 A，补核心介绍。
4. 在 `CHANGELOG.md` 追加一条：日期、新增/改档数量、摘要。

## 分档标准（摘要级）

- **A**：主张清晰，有受控对照或评测审计，可指导工程决策。
- **B**：有实证但样本/外推/复现有明显软肋。
- **C**：愿景、平台、技术报告或与主线关联偏弱；作地图用。
