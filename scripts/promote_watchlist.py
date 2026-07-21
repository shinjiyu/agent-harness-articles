#!/usr/bin/env python3
"""Promote watchlist candidates into index.json with abstract-level tiers."""

from __future__ import annotations

import html
import json
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_DIR = ROOT / "indexes" / "agent-harness"
INDEX_PATH = INDEX_DIR / "index.json"
WATCHLIST_PATH = INDEX_DIR / "watchlist.json"
TZ = timezone(timedelta(hours=8))
UA = "agent-harness-articles/0.1 (promote-watchlist)"
ATOM = "{http://www.w3.org/2005/Atom}"


def now_iso() -> str:
    return datetime.now(TZ).replace(microsecond=0).isoformat()


def arxiv_id_from_url(url: str) -> str:
    m = re.search(r"arXiv\.(\d{4}\.\d{4,5})", url or "", re.I)
    if m:
        return m.group(1)
    m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", url or "", re.I)
    return m.group(1) if m else ""


def clean_authors(authors: list[str]) -> list[str]:
    out = []
    for a in authors:
        a = re.sub(r"\s+\d{4}$", "", a.strip())  # drop dblp numbering suffix like "0001"
        a = re.sub(r"\s+\d{4}\b", "", a)
        a = html.unescape(a)
        if a:
            out.append(a)
    return out


def fetch_arxiv_meta(arxiv_id: str) -> dict:
    url = (
        "https://export.arxiv.org/api/query?"
        + f"id_list={arxiv_id}&max_results=1"
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
            break
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 3:
                time.sleep(10 * (attempt + 1))
                continue
            raise
    root = ET.fromstring(raw)
    entry = root.find(f"{ATOM}entry")
    if entry is None:
        return {}
    title = re.sub(r"\s+", " ", (entry.findtext(f"{ATOM}title") or "").strip())
    abstract = re.sub(r"\s+", " ", (entry.findtext(f"{ATOM}summary") or "").strip())
    published = (entry.findtext(f"{ATOM}published") or "")[:10]
    authors = [
        (a.findtext(f"{ATOM}name") or "").strip()
        for a in entry.findall(f"{ATOM}author")
    ]
    id_url = entry.findtext(f"{ATOM}id") or ""
    ver = re.search(r"(v\d+)$", id_url)
    return {
        "title": title,
        "abstract": abstract,
        "published": published,
        "authors": [a for a in authors if a],
        "arxiv_version": ver.group(1) if ver else "v1",
    }


# Manual abstract-level ratings (title + known role in literature).
RATINGS: dict[str, dict] = {
    "2605.27922": {
        "tier": "A",
        "tier_reason": "跨模型实测 harness 效应；与 Harness Effect 互补的评测基建。",
        "tags": ["evaluation", "benchmark", "methodology", "orchestration"],
        "notes": "Harness-Bench：模型–harness 配置是能力单位",
        "knowledge_ids": ["evaluation"],
    },
    "2606.15874": {
        "tier": "B",
        "tier_reason": "LLM-as-Code 架构主张清晰；实证偏案例，外推待核。",
        "tags": ["orchestration", "control", "architecture"],
        "notes": "控制流归程序，LLM 只作自适应组件",
    },
    "2606.12882": {
        "tier": "B",
        "tier_reason": "可学习双向 harness 控制器；工程贡献明确，域覆盖待核。",
        "tags": ["control", "adaptation", "orchestration"],
        "notes": "HarnessBridge：冻结执行器上的可学习控制层",
    },
    "2606.10106": {
        "tier": "B",
        "tier_reason": "给出 harness 必要充分条件的概念框架；偏定义文。",
        "tags": ["orchestration", "methodology"],
        "notes": "What makes a harness a harness",
    },
    "2604.25850": {
        "tier": "B",
        "tier_reason": "可观测驱动的编码 harness 自动演化；自演化路线实证。",
        "tags": ["self-evolution", "observability", "code-agent", "orchestration"],
        "notes": "Agentic Harness Engineering",
    },
    "2605.30621": {
        "tier": "B",
        "tier_reason": "区分「能更新 harness」与「更新带来收益」；对自演化叙事有纠偏。",
        "tags": ["self-evolution", "evaluation", "methodology"],
        "notes": "Harness Updating ≠ Harness Benefit",
    },
    "2604.07236": {
        "tier": "B",
        "tier_reason": "度量 harness 承担多少重活 vs LLM 残差角色；测量设计清楚。",
        "tags": ["evaluation", "orchestration", "planning"],
        "notes": "规划代理中 harness 的重活占比",
    },
    "2605.15184": {
        "tier": "B",
        "tier_reason": "讨论 harness 如何重塑 agentic search；偏经验/系统设计。",
        "tags": ["orchestration", "search"],
        "notes": "Is Grep All You Need?",
    },
    "2601.15322": {
        "tier": "B",
        "tier_reason": "金融工具调用代理的可重放/确定性保真 harness。",
        "tags": ["audit", "validation", "enterprise", "tool-calling"],
        "notes": "Replayable Financial Agents",
    },
    "2602.22480": {
        "tier": "B",
        "tier_reason": "用代理优化代理的评估 harness（VeRO）；评测基建。",
        "tags": ["evaluation", "benchmark"],
        "notes": "VeRO evaluation harness",
    },
    "2606.11686": {
        "tier": "B",
        "tier_reason": "对确定性脚手架做无 LLM 回归锁定测试；工程评测味道浓。",
        "tags": ["evaluation", "testing", "enterprise"],
        "notes": "Layer-Isolated Evaluation",
    },
    "2606.08348": {
        "tier": "B",
        "tier_reason": "后验引导的技能演化；自演化+harness 交叉。",
        "tags": ["self-evolution", "skill", "bayesian"],
        "notes": "Bayesian-Agent skill evolution",
    },
    "2606.20631": {
        "tier": "B",
        "tier_reason": "技能中介 LLM 代理的架构模式与参考架构；综述/模式文。",
        "tags": ["skill", "architecture", "orchestration"],
        "notes": "Agent Skills reference architecture",
    },
    "2606.21856": {
        "tier": "B",
        "tier_reason": "多用户 LLM 代理的安全治理 harness；领域专用。",
        "tags": ["security", "governance", "multi-agent", "permissions"],
        "notes": "Harness-MU",
    },
    "2605.15218": {
        "tier": "C",
        "tier_reason": "APDL/CAE 专域轻量 harness；与通用 harness 主线关联弱。",
        "tags": ["domain", "code-agent"],
        "notes": "CAX-Agent APDL",
    },
    # --- 2026-07-16 inbox ---
    "2607.14004": {
        "tier": "A",
        "tier_reason": "三方法×两阶段 continual 对照；回归控制决定 harness 优化增益能否复利。",
        "tags": ["self-evolution", "orchestration", "evaluation", "methodology"],
        "notes": "agent 优化器增益能否复利：回归控制是关键",
        "knowledge_ids": ["orchestration-evolution", "evaluation"],
    },
    "2607.13683": {
        "tier": "A",
        "tier_reason": "提案与计分分离；密封测试上 +9–15.5pp，病理键归档抗过拟合。",
        "tags": ["self-evolution", "orchestration", "adaptation"],
        "notes": "门控语义质量多样性驱动的自演化 harness",
        "knowledge_ids": ["orchestration-evolution"],
    },
    "2607.13918": {
        "tier": "B",
        "tier_reason": "部分相关 verifier cascade 理论清晰；实证偏合成，工程外推待核。",
        "tags": ["evaluation", "reliability", "methodology"],
        "notes": "LLM harness 中串行验证门的相关性与盲区天花板",
    },
    "2607.13705": {
        "tier": "B",
        "tier_reason": "Benchmark/Harness/Environment 解耦的评测基建；覆盖广但非因果实验。",
        "tags": ["evaluation", "benchmark", "orchestration"],
        "notes": "AgentCompass 统一 agent 评测基础设施",
        "knowledge_ids": ["evaluation"],
    },
    "2607.13988": {
        "tier": "B",
        "tier_reason": "回合级信用分配显著提升长程工具使用；属 agentic RL，非 harness 编排主线。",
        "tags": ["rl", "tool-calling", "long-horizon"],
        "notes": "TRACE：工具边界上的 TD 信用估计",
    },
    "2607.13618": {
        "tier": "B",
        "tier_reason": "公平 oracle 拆开「感知 vs 行动」缺口；供应链专域，样本模型有限。",
        "tags": ["evaluation", "benchmark", "methodology"],
        "notes": "STOCKTAKE：测量 LLM agent 的 knowing-doing gap",
    },
    "2607.13591": {
        "tier": "B",
        "tier_reason": "把记忆当可控过程并用轻量策略学习；多基准增益明确，属记忆层非全 harness。",
        "tags": ["memory", "context", "adaptation"],
        "notes": "MemCon：自适应记忆检索/注入/巩固",
        "knowledge_ids": ["context-memory"],
    },
    "2607.13594": {
        "tier": "B",
        "tier_reason": "EXECUTE/ASK/REFUSE 三路路由比二元护栏更贴近部署；护栏模型评测，非完整 harness。",
        "tags": ["security", "permissions", "governance"],
        "notes": "Safety Sentry：上下文感知人机介入路由",
        "knowledge_ids": ["security-permissions"],
    },
    "2607.13474": {
        "tier": "B",
        "tier_reason": "组件/工作流/搜索三图抽象便于组合分析；框架文，实证偏代表性应用。",
        "tags": ["orchestration", "architecture", "multi-agent"],
        "notes": "MyAG：可组合 LLM agent 系统的图框架",
    },
    "2607.14047": {
        "tier": "B",
        "tier_reason": "纠正记忆跨轮复用降人工成本；具身数据采集设定，复现门槛高。",
        "tags": ["embodied", "memory", "human-in-the-loop"],
        "notes": "PhysClaw-0：语言纠正可复用的具身采集 harness",
        "knowledge_ids": ["embodied-multimodal"],
    },
    "2607.14037": {
        "tier": "B",
        "tier_reason": "大规模 GitHub agentic PR 采用实证；观测性早期快照，非方法贡献。",
        "tags": ["code-agent", "empirical", "human-agent"],
        "notes": "开源项目对 agentic coding 工具的早期采用",
    },
    "2607.14006": {
        "tier": "B",
        "tier_reason": "把 AI 渗透测从基础设施攻陷扩展到行为目标违背；框架/定义文。",
        "tags": ["security", "evaluation", "methodology"],
        "notes": "AI 系统渗透测：行为目标违背范式",
        "knowledge_ids": ["security-permissions"],
    },
    "2607.14082": {
        "tier": "C",
        "tier_reason": "Lean 中 agentic 形式化 Shor；与 LLM agent harness 主线关联弱。",
        "tags": ["formal-methods", "quantum"],
        "notes": "agentic 量子密码分析形式化",
    },
    "2607.14044": {
        "tier": "C",
        "tier_reason": "企业 upskilling 端到端框架；产品/培训叙事，非 harness 方法。",
        "tags": ["education", "enterprise"],
        "notes": "AI 加速专业再培训框架",
    },
    "2607.13998": {
        "tier": "C",
        "tier_reason": "自主商务忠诚度概念模型；愿景/理论，待三阶段实证。",
        "tags": ["commerce", "multi-agent", "theory"],
        "notes": "DVM-HALL / NHAS 忠诚度模型",
    },
    "2607.13602": {
        "tier": "C",
        "tier_reason": "历史类比 deep research；与 harness 编排主线相邻偏弱。",
        "tags": ["research-agent", "retrieval"],
        "notes": "Analogical Deep Research / CANA",
    },
    # --- 2026-07-21 inbox ---
    "2607.18235": {
        "tier": "A",
        "tier_reason": "30 个预算对齐 harness×12 模型-问题对、310 万 rollout 重复试验；无普适最优 harness，应作超参调。",
        "tags": ["evaluation", "orchestration", "methodology", "discovery"],
        "notes": "自动发现无普适最优 harness：harness 是超参数",
        "knowledge_ids": ["evaluation", "orchestration-evolution"],
    },
    "2607.17598": {
        "tier": "A",
        "tier_reason": "3 harness×3 模型族受控研究 Agent Skills 渐进披露；增益取决于 harness，一层足够。",
        "tags": ["context", "skill", "evaluation", "retrieval"],
        "notes": "渐进披露买的是上下文而非智能；强 harness 下近零增益",
        "knowledge_ids": ["context-memory", "evaluation"],
    },
    "2605.14271": {
        "tier": "A",
        "tier_reason": "轨迹级 harness 安全审计：210 任务×8 域×10 配置；完成率与安全执行错位、违规随轨迹长度累积。",
        "tags": ["security", "audit", "evaluation", "multi-agent"],
        "notes": "HarnessAudit：输出正确≠执行安全",
        "knowledge_ids": ["security-permissions", "evaluation"],
    },
    "2607.18171": {
        "tier": "B",
        "tier_reason": "chain-of-program 引导编码代理产出多 GPU 部署；数字亮但域限实时多模态服务。",
        "tags": ["orchestration", "code-agent", "systems"],
        "notes": "FlashRT：引导代理做实时多模态部署优化",
    },
    "2607.18161": {
        "tier": "B",
        "tier_reason": "定义 CodeSlop 并以轨迹最小化削减 17.9–32.9%；对代码库长期可维护性有工程价值。",
        "tags": ["code-agent", "trajectory", "quality"],
        "notes": "TRIM：最小化轨迹以减少 AI 代码冗余",
    },
    "2607.18064": {
        "tier": "B",
        "tier_reason": "生产任务上自然捕获 spec gaming（逐行背答案）；加 held-out 后消失。样本小但预注册。",
        "tags": ["evaluation", "code-agent", "empirical"],
        "notes": "autoresearch 中的 metric-maximizer 行为",
    },
    "2607.18063": {
        "tier": "B",
        "tier_reason": "自适应多轮攻击基准：15 轮 ASR 升至 5.4–14%；排名跨场景不一致。属安全评测基建。",
        "tags": ["security", "benchmark", "multi-agent"],
        "notes": "Adaptive Adversaries：适应性攻击者×无记忆防御者",
        "knowledge_ids": ["security-permissions"],
    },
    "2607.18039": {
        "tier": "B",
        "tier_reason": "客服代理三个可复用部署模式；真实部署但属经验文，无对照数字。",
        "tags": ["enterprise", "rag", "orchestration"],
        "notes": "Evidence-in-the-Loop：trace 驱动的客服代理优化",
    },
    "2607.17979": {
        "tier": "B",
        "tier_reason": "评测 harness 与优化控制器分离的内核生成系统；Agent-Assisted 胜 Full-Agent，域限竞赛。",
        "tags": ["code-agent", "evaluation", "systems"],
        "notes": "GPU kernel 生成的 harness 工程",
    },
    "2607.17900": {
        "tier": "B",
        "tier_reason": "把 harness 层思想搬到 TTS 表达控制；路由+合成双评测，领域专属。",
        "tags": ["domain", "control", "orchestration"],
        "notes": "Harness TTS：TTS 引擎外的表达控制层",
    },
    "2607.17719": {
        "tier": "B",
        "tier_reason": "工业推荐后排策略精炼 harness；快手一个月 A/B 在线部署，域专属。",
        "tags": ["enterprise", "self-evolution", "domain"],
        "notes": "SR-Agent：约束式策略精炼 harness + 可回滚门控",
    },
    "2607.17641": {
        "tier": "B",
        "tier_reason": "噪声 verify-repair 环的鲁棒停机理论+GSM8K 压力测试 +60.6pp；实证域窄。",
        "tags": ["reliability", "verification", "methodology"],
        "notes": "VRR-Stop：修复该停就停",
    },
    "2607.17420": {
        "tier": "B",
        "tier_reason": "预注册人格 prompt 对照：效应依模型而异；对 harness 提示层设计有纠偏价值。",
        "tags": ["prompting", "empirical", "evaluation"],
        "notes": "人格是模型依赖的行为策略偏置，非普适质量干预",
    },
    "2606.14249": {
        "tier": "B",
        "tier_reason": "可组合/可演化 harness foundry，5 基准平均 +14.5%；严谨性细节与开源待核。",
        "tags": ["orchestration", "self-evolution", "architecture"],
        "notes": "HarnessX：类型化 harness 原语 + trace 驱动演化",
    },
    "2605.21825": {
        "tier": "B",
        "tier_reason": "端到端 VIS 应用设计 harness，SciVis 竞赛验证；域专属。",
        "tags": ["domain", "orchestration", "skill"],
        "notes": "AI VIS co-scientist harness",
    },
    "2605.18747": {
        "tier": "B",
        "tier_reason": "「代码即 harness」三层统一视角综述；覆盖广，属综述非新实证。",
        "tags": ["survey", "code-agent", "orchestration"],
        "notes": "Code as Agent Harness 综述",
    },
    "2605.00663": {
        "tier": "B",
        "tier_reason": "验证门控技能编排改善 affordance 接地的精度-成本前沿；具身专域。",
        "tags": ["embodied", "verification", "orchestration"],
        "notes": "Affordance Agent Harness：Router+Verifier 闭环",
        "knowledge_ids": ["embodied-multimodal"],
    },
    "2603.20380": {
        "tier": "B",
        "tier_reason": "CAT 纯文本数据层管理多代理 harness；22 模型×115 任务评测，工具偏小众。",
        "tags": ["multi-agent", "context", "tooling"],
        "notes": "Herding CATs：ALARA 式上下文-代理-工具声明层",
    },
    "2504.04785": {
        "tier": "B",
        "tier_reason": "弱 meta-agent 经 RL 学会设计工作流驾驭强执行器；11 基准增益，2025 文补录。",
        "tags": ["orchestration", "rl", "workflow"],
        "notes": "W4S：weak-for-strong 工作流优化",
    },
    "2607.18152": {
        "tier": "C",
        "tier_reason": "listwise reranker 模型发布；agentic 检索组件，与 harness 主线关联弱。",
        "tags": ["retrieval", "model-release"],
        "notes": "jina-reranker-v3.5",
    },
    "2607.18147": {
        "tier": "C",
        "tier_reason": "智能电网 agentic 系统教程 + solver-grounded 原则；教程/领域文。",
        "tags": ["domain", "tutorial", "tool-calling"],
        "notes": "solver-grounded：数值必须出自可信工具",
    },
    "2607.18138": {
        "tier": "C",
        "tier_reason": "6G 网络承载 AI agent 通信的差距分析；愿景/标准化文。",
        "tags": ["networking", "vision"],
        "notes": "AI-native 6G 与 agent 通信",
    },
    "2607.18116": {
        "tier": "C",
        "tier_reason": "教育视频合成的几何验证插件；专域验证模块。",
        "tags": ["domain", "verification"],
        "notes": "SGA：Manim 动画几何验证",
    },
    "2607.18029": {
        "tier": "C",
        "tier_reason": "OWL 本体 + LLM 生成 SPARQL 的元数据查询 harness；专域框架。",
        "tags": ["domain", "retrieval"],
        "notes": "NLKGQ：自然语言查询知识图谱",
    },
    "2607.17437": {
        "tier": "C",
        "tier_reason": "经验接地提升 LLM 代理行为仿真真实度；仿真相邻域。",
        "tags": ["simulation", "empirical"],
        "notes": "灾害中断下的人类行为仿真接地",
    },
}


SKIP_TITLES = {
    "agentic artificial intelligence - harnessing ai agents to reinvent business, work, and life",
}

# 检索噪声（物理 Rashba / 工业线束 / 足迹生物识别 / MHD 模拟器 / 视频异常检测 / KV cache 服务 / 类增量学习）
SKIP_IDS = {
    "2607.14069",
    "2607.14021",
    "2607.13905",
    "2607.18176",
    "2607.18142",
    "2607.18141",
    "2607.17593",
}


def write_a_intro(arxiv_id: str, title: str, published: str, authors: list[str], abstract: str, rating: dict) -> str:
    path = INDEX_DIR / "papers" / "a" / f"{arxiv_id}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    abs_short = abstract[:1200] + ("…" if len(abstract) > 1200 else "")
    body = f"""# {title}

- ArXiv: [{arxiv_id}](http://arxiv.org/abs/{arxiv_id})
- Tier: **A**
- Indexed: {now_iso()}

## 核心介绍

{rating.get('notes') or title}

### 分档理由

{rating['tier_reason']}

### 摘要要点（机器摘录）

{abs_short if abs_short else '（暂无摘要，待补）'}

### 挂载知识点

{', '.join(rating.get('knowledge_ids') or rating.get('tags') or [])}

### 阅读时注意

本介绍为摘要级入库笔记；完整机制与实验以 PDF/HTML 为准。
"""
    path.write_text(body, encoding="utf-8")
    return f"papers/a/{arxiv_id}.md"


def main() -> None:
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    watch = json.loads(WATCHLIST_PATH.read_text(encoding="utf-8"))
    existing = {p["arxiv_id"] for p in index["papers"] if p.get("arxiv_id")}
    existing_titles = {p["title"].lower().strip() for p in index["papers"]}

    added = []
    skipped = []
    ts = now_iso()

    for c in watch.get("candidates", []):
        title = html.unescape(c.get("title") or "").strip()
        aid = c.get("arxiv_id") or arxiv_id_from_url(c.get("url") or "")

        if title.lower() in SKIP_TITLES or aid in SKIP_IDS:
            c["status"] = "skipped"
            c["skip_reason"] = "noise / weak harness sense"
            skipped.append(f"{aid} {title}" if aid else title)
            continue

        if not aid:
            c["status"] = "needs_manual"
            skipped.append(title)
            continue
        if aid in existing or title.lower() in existing_titles:
            c["status"] = "already_indexed"
            continue

        rating = RATINGS.get(aid)
        if not rating:
            c["status"] = "needs_manual"
            skipped.append(f"{aid} {title}")
            continue

        print(f"fetch {aid} ...")
        meta = {}
        try:
            meta = fetch_arxiv_meta(aid)
            time.sleep(3.5)
        except Exception as e:
            print(f"  arxiv fetch failed: {e}")

        authors = meta.get("authors") or clean_authors(c.get("authors") or [])
        published = meta.get("published") or (c.get("published") if "-" in str(c.get("published")) else "")
        if not published and c.get("published"):
            published = f"{c['published']}-01-01" if len(str(c["published"])) == 4 else str(c["published"])
        final_title = meta.get("title") or title
        abstract = meta.get("abstract") or c.get("abstract") or ""
        version = meta.get("arxiv_version") or "v1"

        entry = {
            "arxiv_id": aid,
            "arxiv_version": version,
            "title": final_title,
            "authors": authors[:12] if len(authors) > 12 else authors,
            "published": published,
            "url": f"http://arxiv.org/abs/{aid}",
            "source": "arxiv",
            "tier": rating["tier"],
            "tier_reason": rating["tier_reason"],
            "tags": rating.get("tags") or [],
            "notes": rating.get("notes") or "",
            "indexed_at": ts,
        }
        if rating.get("knowledge_ids"):
            entry["knowledge_ids"] = rating["knowledge_ids"]
        if rating["tier"] == "A":
            entry["core_intro_path"] = write_a_intro(
                aid, final_title, published, authors, abstract, rating
            )

        index["papers"].append(entry)
        existing.add(aid)
        existing_titles.add(final_title.lower())
        c["status"] = "promoted"
        c["arxiv_id"] = aid
        c["promoted_tier"] = rating["tier"]
        c["promoted_at"] = ts
        added.append((aid, rating["tier"], final_title))
        print(f"  + {rating['tier']} {aid} {final_title[:60]}")

    # reorder
    order = {"A": 0, "B": 1, "C": 2}
    by_tier = {"A": [], "B": [], "C": []}
    for p in index["papers"]:
        by_tier.setdefault(p["tier"], []).append(p)
    for t in by_tier:
        by_tier[t].sort(key=lambda x: x.get("published") or "", reverse=True)
    index["papers"] = by_tier.get("A", []) + by_tier.get("B", []) + by_tier.get("C", [])
    index["updated_at"] = ts
    index["tier_counts"] = {
        "A": len(by_tier.get("A", [])),
        "B": len(by_tier.get("B", [])),
        "C": len(by_tier.get("C", [])),
        "total": len(index["papers"]),
    }

    watch["updated_at"] = ts
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    WATCHLIST_PATH.write_text(json.dumps(watch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"\npromoted {len(added)} papers → index now {index['tier_counts']}")
    for aid, tier, title in added:
        print(f"  [{tier}] {aid} {title[:70]}")
    if skipped:
        print("skipped/needs_manual:")
        for s in skipped:
            print(" ", s[:80])


if __name__ == "__main__":
    main()
