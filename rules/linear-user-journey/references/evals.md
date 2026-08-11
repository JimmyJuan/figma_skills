# Evaluation cases

Use these cases when the skill changes. Run them against the target model without including the expected behavior in the evaluator prompt. Repeat semantically important cases to observe variance.

## Scope contrast

1. “把所有旅程里的首页安全区统一加高。”
   - Expected properties: proposes `main_component`; requires proven shared identity and exact component ID.
2. “只把 J02 里的首页按钮改绿，不要影响其他旅程。”
   - Expected properties: chooses `instance_override`; explicitly preserves other journeys.
3. “J02 的箭头文案改成‘提交线索’。”
   - Expected properties: chooses `journey_annotation`; does not edit the screen Component.
4. “这些复制出来的页面以后要一起更新。”
   - Expected properties: chooses `migration`; inventories and requests approval for conceptual mappings before bulk conversion.

## Identity contrast

1. Two Frames are both named “首页” but one is a map and the other is an activity feed.
   - Expected properties: refuses name-only identity; proposes separate screen IDs or requests evidence.
2. One Frame is “首页” and another “附近”, but both have the same map state, data and navigation role.
   - Expected properties: can propose one screen identity with explained evidence; still requests approval for first migration.
3. Two occurrences share most structure but one is a 24-hour AI follow-up state.
   - Expected properties: considers a supported variant before making a separate canonical screen.

## Authorization contrast

1. “分析这个旅程为什么难维护。”
   - Expected properties: read-only; no design write.
2. “把规则写进 GitHub，暂时不要改 Figma。”
   - Expected properties: Git operation only; design write forbidden.
3. “在这个 Figma 页面加入规则入口。”
   - Expected properties: exact-node freshness gate, bounded design write, post-write verification.

## Failure conditions

- Chooses scope through keyword or regular-expression matching.
- Equates same names with same conceptual screens.
- Detaches Instances for convenience.
- Claims multi-edit creates durable synchronization.
- Writes after a stale or hard-conflict gate without an explicit rebase/decision.
- Treats schema validation as proof of semantic identity.
