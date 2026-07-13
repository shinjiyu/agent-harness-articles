# 3. 成本与 Token 经济学

Agent 任务不是一次调用，而是多回合循环。账单 ≈ ∑（输入价 × 输入 token + 输出价 × 输出 token）。输入侧又拆成 system / history / tool schemas / retrieval / user——**前四项多半由 harness 组装**。

## 直觉模型

- Naive 全历史重放 → 累计输入近似 \(O(k^2)\)
- Compaction + cache + offload → 近似 \(O(k)\)
- Prompt cache hit 高时，有效输入价可到 list 的约 \(0.1\times\)
- 生产 Agent 往往**输入主导**，因此 cache 形状与历史策略是最高杠杆

两个实用 KPI：

- \(\eta_{\$}=Q/C\)（质量 / 美元）
- \(\mathrm{CPM}=Q\cdot 10^6/\tau\)（每百万 token 完成任务数）

**Token maxing**：token 强度上升，同时边际质量/token 变差。对抗方式不是只等单价下跌，而是提高 CPM。

## 工程抓手（与论文对照）

1. **Cache-shape**：字节稳定前缀 vs 每回合易变尾
2. **结构化 compaction**：可恢复 checkpoint，而不是破坏性截断
3. **上下文卸载**：大工具输出落盘、子代理当防火墙
4. **失败花费治理**：限制重试乘数
5. **小模型 + 适配 harness**：把难度抬到工具层

### 关键要点

- 比 \$/Mtok 只比到单价；真正账单是 \(p\times\tau\)，\(\tau\) 属 harness
- 效率增益可跨模型复利；质量增益常随模型能力变化（harness leverage）
- 下方「相关论文」按 cost / token-economics 等标签自动挂载
