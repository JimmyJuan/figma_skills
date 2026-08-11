# Linear user journey contract

## Definition

A linear user journey is a human-scannable, ordered account of how one actor moves from a trigger to a meaningful outcome through product screens, actions and system responses.

“Linear” describes the primary reading direction, not the absence of product complexity. Branches, failures, waits, alternate entries, loops and cross-role handoffs remain explicit, but they do not obscure the main story.

## Board anatomy

Each journey is a Figma Section named:

```text
Jxx｜Actor / role｜Goal or outcome
```

A Section contains:

1. **Journey information** — journey ID, actor, trigger, goal/outcome, assumptions and key principles.
2. **Start badge** — the explicit entry to the story.
3. **Main trunk** — screen occurrences arranged left to right in temporal order.
4. **Transitions** — arrows or connectors labeled with the user's action, system event or elapsed time.
5. **Branches** — decision and state alternatives arranged in labeled rows below the trunk.
6. **Alternate entries and cross-role flows** — separate labeled subflows that show where another actor or channel enters.
7. **Rule cards** — product constraints, fallback behavior and semantic explanations that are not themselves screens.
8. **End badge/outcome** — explicit success, failure or terminal state.
9. **Prototype reactions** — interactive links when the board is intended to be traversable.

## Identity and naming

Journey identity and screen identity are different dimensions.

- `journey_id`: `J01`, `J05-A`, `J02-V2`.
- `occurrence_id`: `J01-S01`, `J01-B01`, `J02-V2-R01`.
- `screen_id`: stable product concept such as `home-default` or `lost-pet-publish-form`.

Occurrence prefixes:

- `S` — screen on the primary trunk.
- `B` — branch or state-specific screen.
- `R` — supporting/cross-role stream.

An occurrence ID answers “where does this appear in this journey?” A screen ID answers “which reusable product screen is this?” Never put an occurrence-specific ID into the canonical component name.

## Layout rules

- Keep the main trunk left to right on one visual row when practical.
- Put branch rows below their decision point and label both the condition and the rejoin/terminal outcome.
- Align screen tops and use consistent horizontal spacing within a row.
- Keep journey information at the left edge so a reader understands the actor and goal before entering the flow.
- Distinguish actions, system events, decisions and elapsed-time transitions through labels, not color alone.
- Keep annotations and connectors outside screen Instances so a screen can update without swallowing journey-specific markup.

## Completion criteria

A journey is complete enough to hand off when a reader can answer:

- Who is acting, and what triggered the journey?
- What outcome defines success?
- What is the primary screen sequence?
- Which transitions are user actions versus system events?
- Where can the flow branch, wait, fail, loop or receive an alternate entry?
- Which screen occurrences share a canonical screen identity?
- Which visible differences are variants/overrides, and which represent different product screens?
