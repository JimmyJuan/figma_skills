---
name: design-source
description: Select and retain a Figma design source for implementation, comparison, or handoff. Prefer a released design RC, warn when using Working Space or an unclassified source, and preserve the task's accepted baseline across RC updates and resumed sessions.
---

# Figma design source

Version: `1.0.0`.

Designers work continuously in Working Space and periodically publish a frozen batch as a design RC. Development follows the batch selected for its task. A task implementing RC1 continues on RC1 when RC2 appears; only an explicit user instruction switches that task to RC2. A design RC is distinct from a software release candidate or Production promotion.

## Select the source

1. Recover this task's existing source selection before choosing anything new. On resume or handoff, use its accepted version/hash and evidence reference, not the newest checkpoint from another task that happens to share a node ID.
2. For a new task, honor the source explicitly selected by the user. Otherwise prefer an applicable published RC. Resolve relevance from the task and design context; a name containing `RC` alone does not establish scope or completeness. If several candidates have materially different scope and context does not select one, ask which source to use.
3. If the selected source is Working Space or its RC status is unverified, tell the developer once that it is a changing or unclassified source and that RC is preferred. Continue with the selected source when the request already selects it; an explicit choice of the current design is sufficient. RC status alone is not a blocking gate and needs no additional approval ceremony.
4. Bind the task to the exact source and run the environment's Figma freshness gate before design-dependent implementation. A page link is an entry point: resolve the actual target frame/subtree inside that page. Verify copied indexes and links resolve to the selected RC's nodes rather than silently returning to Working Space.

The selection is complete when the task has an exact source, recoverable baseline evidence, and any non-RC warning has been given. Do not call an unverified source an RC or invent another project's RC link.

## Retain the accepted batch

The default task policy is `keep_baseline`, for both RC and an explicitly selected current Working Space snapshot. “Use the current design” selects its current state; it does not by itself request continuous tracking.

This rule supplies standing authority for that default: record `policy_authority: design-source-default` when no task-specific instruction overrides it. A stale observation on an existing accepted baseline does not reopen the policy question.

Record these facts in the task's existing handoff/evidence system, without introducing a separate lifecycle tracker:

- task identity and source selection authority;
- source kind (`rc`, `working_space`, or `unclassified`) and RC label when present;
- source URL, file key, entry page/section ID, and exact implementation target ID;
- accepted Figma version when available, complete snapshot reference, canonical SHA-256, and capture time;
- task policy and the checkpoint that accepted this baseline;
- non-RC warning when applicable.

Capture the geometry, text, layout, styles, resolved variables, component/instance properties, inherited values, and asset references required to reproduce the selected design; include visual evidence when fidelity matters. Preserve the old batch as an accessible version or complete stored snapshot before relying on a mutable RC location. Metadata, a page name, or a screenshot alone is not that complete baseline.

RC releases continue over time. Neither a new RC, a changed project default, a renamed page, nor a newer checkpoint from another task updates an existing task's selection. Do not impose a particular RC naming scheme or require the entire RC area to remain unchanged forever.

## Apply freshness to that selection

Keep the existing mechanical `fresh` / `stale` / `hard_conflict` gate and its audit logs. This rule selects the input and the response to change; it does not redefine a mismatch as fresh.

| Observation | Task response |
| --- | --- |
| Working Space or another RC changes outside the accepted target | Continue the selected batch; file-wide change alone does not cause rebase or revalidation. |
| RC2 is published while the task is on RC1 | Continue RC1 without a rebase question. |
| The selected live RC1 subtree changes in place | Record `stale` and `decision: keep_baseline`; use the recoverable accepted RC1 version/snapshot. Do not silently absorb the edited content. |
| The accepted source cannot be reproduced, or the gate has an authentication, exact-identity, or required-logging failure | Report the concrete `hard_conflict` under the existing gate. Never recover by guessing or switching to RC2. |
| The user explicitly switches this task to RC2 | Resolve its exact targets, record the instruction and source transition, capture and gate RC2, then rerun work and checks affected by the accepted diff. Preserve the old evidence. |

Only an explicit task instruction to continuously follow a named live target selects `follow_current`. An existing task with an explicitly selected policy retains it until the user changes it. A generic historical project default does not override the RC retention rule for new tasks under this policy. A new RC with different node IDs is not automatically the same live target.

Run the final gate against the task's accepted source. Report fidelity against the recorded version/hash and capture time, including live drift or unavailable evidence. Preserve the environment's requirements for reads and audit logging; no design write, comment, component migration, or library publication is authorized by source selection.

## Review scenarios

Validate the rule with realistic requests covering: RC1 with RC2 published; the user explicitly switching only one task to RC2; in-place changes to RC1; a resumed task whose node has a newer checkpoint from another task; an explicit Working Space request; an unclassified source; and an unavailable accepted snapshot. Keep source preference, user intent, mechanical evidence, and external-write authority separate.
