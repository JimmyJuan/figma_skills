# Model-first rule ledger

This ledger governs the first rule package, `linear-user-journey`.

| Predicate that reads prose | Decision owner | Structured result | Deterministic boundary | Required evaluation |
| --- | --- | --- | --- | --- |
| Does the request concern a linear user journey? | Model semantics, guided by the skill description and the journey contract | `applies: true | false` plus a short rationale | File keys, node IDs and node types are validated exactly | Direct request; implicit journey work; unrelated Figma work |
| Is a requested screen change global or journey-specific? | Model semantics; ask the user when material ambiguity remains | `scope: main_component | instance_override | journey_annotation | migration` | Only an authorized scope can reach a write; exact target IDs are required | Global change; local-only change; explicit negation; ambiguous wording |
| Do two occurrences represent the same conceptual screen? | Model proposes evidence-backed mapping; a human approves migration mappings | Stable `screen_id` with listed occurrence IDs | Figma `INSTANCE.mainComponent.id` proves an established relationship; names never do | Same name/different meaning; different name/same meaning; variant vs separate screen |
| Is a branch condition, actor goal or journey outcome semantically equivalent? | Model semantics with cited journey evidence | Explanation and proposed canonical term | IDs and manifest enums are schema-checked only after the semantic decision | Paraphrases; negation; changed actor; changed outcome |
| Is the person whose account is being configured an internal team member? | Model semantics from explicit task context; ask when ambiguity would affect an external action | `membership: internal | external | uncertain` plus rationale | The preferred email is an exact value loaded from `docs/team-account-policy.md`; credentials and effect authorization remain separate | Explicit internal member; explicit external collaborator; ambiguous affiliation; explicit alternate email |
| Is a Figma write safe to continue after concurrent edits? | Figma Freshness Gate state machine | `fresh | stale | hard_conflict` and `continue | rebase | block` | Exact-node hashes, authorization and write allowlists are deterministic | Fresh read; concurrent child addition; unreadable target |
| Does the user authorize an external effect? | Model interprets the request; ambiguous material effects require confirmation | `authorized_effect: none | comment | design_write | git_push` | Tools enforce exact file/repository targets; no force push | Rules-only request; Figma write request; normal push; destructive/expanded action |

No production router may decide these open-ended predicates with keywords, regular expressions, token distance, string containment or sentence-specific branches. Closed identifiers, schemas, enums, authorization, freshness states and exact component relationships remain deterministic.

## Contrast cases

1. “把所有旅程里的首页安全区统一加高。” → propose `main_component`; require a stable screen/component identity before writing.
2. “只把 J02 里的首页按钮改绿，不要影响其他旅程。” → `instance_override`; preserve the main component and other instances.
3. “J01 和 J02 都有一个叫首页的画面，所以它们肯定是同一页面。” → reject name-only identity; compare purpose, state and structure, then request approval for a mapping.
4. “一个叫首页，一个叫附近，但其实都是同一个地图入口状态。” → allow a same-screen proposal based on semantics, not labels; request mapping approval.
5. “先把规则写进仓库，不要改 Figma。” → `authorized_effect: git_push`; `design_write` is forbidden.
6. “在 Figma 里加入规则入口。” → `design_write` only to the exact authorized file/node after a fresh gate.
7. “把线性旅程做得更完整。” → material scope is ambiguous; inspect evidence and ask before synchronizing or restructuring screens.
8. “给我们团队新建一个 Notion 账号，邮箱你选。” → propose the preferred team email, but create the account only if the request and available tools authorize that external effect.
9. “邀请外部设计顾问加入这个 Figma 文件。” → do not impose the internal-team email preference; use the collaborator identity supplied by the user or ask for it.
10. “团队账号这次使用 finance@example.com。” → use the explicitly selected email for this task; do not override it with the default preference.

## Postflight evidence required

- Inspect all changed executable files for new lexical heuristics and classify each occurrence.
- Validate the skill package and closed manifest schema.
- Run repeated live-model contrast trials without revealing expected answers to the evaluator.
- Run the final Figma freshness gate and record every remote effect.

## Postflight — 2026-08-11

### Executable lexical audit

The only executable regular expressions are in `scripts/validate_manifest.py`:

- `JOURNEY_ID`, `OCCURRENCE_ID`, `SCREEN_ID`, `NODE_ID` and `TRANSITION_ID` validate closed identifier grammars.
- `fullmatch` is applied only to those identifiers.
- Set membership checks validate closed enums, allowed object fields and exact referential IDs.
- The words `contains unsupported fields` appear only in structural error messages.

Classification: all occurrences are deterministic mechanism checks. No executable code reads free-form user/model prose or performs an open-ended semantic decision through lexical matching.

### Mechanism checks

- Skill package validator: passed.
- Example manifest: accepted.
- Malformed exact Figma node ID: rejected.
- JSON schema and example JSON parsing: passed.
- Repository whitespace check: passed.

### Live-model contrast trials

Three independent, read-only evaluator runs received realistic requests without expected answers:

- Two repeated trials classified “change the home safe area in every journey” as `main_component` intent and paused because exact shared identity/component evidence was absent.
- The local-only, explicitly negated J02 request classified as `instance_override` and preserved all other journeys.
- A connector-label request classified as `journey_annotation`, while surfacing the ambiguity between a journey connector and copy inside a product screen.
- Two repeated trials refused to merge same-named map/feed Frames and classified the requested durable conversion as `migration` requiring separate identities or further evidence.
- Different names with equivalent purpose/state/data/navigation produced a provisional same-screen proposal for analysis only, not an unauthorized write.
- A GitHub-only request with an explicit Figma negation preserved the separation between repository and design-write effects.

The repeated contrast cases were consistent. High-risk identity mappings still require exact-node evidence and human approval before migration, as required by the rule.

### Figma gate

- Canonical observation target `mMpVLl0gLxTt9O4zdhFb7e / 767:555`: `fresh`; no write.
- Rule-pointer target `QRfUTveQ0ZymfDy2wLC34N / 361:2`: rebased to the latest 12-partition canvas, then received the authorized rule-pointer write.
- Final state: `fresh`; all 12 existing partition hashes were unchanged. The only new partition is `645:2`.

## Postflight — 2026-08-12 team account preference

### Lexical audit

- The new policy contains no executable router or prose-reading code.
- The exact email is deterministic configuration data, not a membership classifier.
- Team membership and task-specific exceptions remain model-semantic decisions grounded in context. Names, domains, keywords and string matching are explicitly excluded as proof of membership.

### Contrast evaluation contract

- Internal member with no selected email: propose the documented default without inferring permission to create or connect an account.
- Explicit external collaborator: do not apply the internal default.
- Explicit alternate email: the current instruction overrides the default.
- Ambiguous affiliation with ownership, access or billing impact: return `uncertain` and ask before the external effect.

### Live-model contrast trials

Two repeated, read-only live-model trials loaded the repository instructions without the expected classifications:

- An internal-team account with no selected email consistently proposed `dywfjyie2489@163.com` and did not infer authorization to register it.
- An explicit external consultant or supplier did not receive the internal default; a supplied external email was preserved, and a missing one caused a request for it.
- An explicit alternate email for an internal account consistently overrode the default.
- Uncertain affiliation combined with ownership, access, account creation or billing caused a pause for clarification rather than forced classification or an external effect.

The repeated contrast cases were consistent. No executable mechanism changed, and no lexical membership classifier was introduced.
