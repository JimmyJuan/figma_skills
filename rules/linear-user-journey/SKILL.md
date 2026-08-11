---
name: linear-user-journey
description: "Build, read, audit, revise or migrate Figma linear user journeys: ordered screen-by-screen flows for a role and outcome, including branches, alternate entries, prototype transitions and repeated screens that should synchronize through Components and Instances. Use when work concerns journey maps, repeated occurrences of the same conceptual screen, cross-journey screen updates, or converting copied Frames into maintainable component-backed journeys. Do not use for an unrelated single-screen mockup or a code-only navigation flow with no Figma journey artifact."
---

# Linear User Journey

Use this rule to keep a journey easy to scan as a story and safe to maintain as a system. “Linear” means the primary reading order is explicit; it does not forbid branches, loops, alternate entries or cross-role supporting flows.

Version: `0.1.0`.

## Required gates

- If the task reads, compares, comments on or writes Figma, run the environment's Figma freshness checkpoint against the exact file key and node ID before using target evidence. Repeat it before an authorized write and before completion.
- Load the available Figma editing guidance before using a Figma write tool.
- Treat analysis, comments, design writes and Git pushes as different effects. Do not infer a design write from a request to document or explain a rule.
- For free-form prose that affects scope, screen identity, routing or external effects, follow the repository's model-first rule ledger. Never replace semantic judgment with lexical matching.

## Load the relevant references

- Always read [journey-contract.md](references/journey-contract.md) when creating or restructuring a journey.
- Read [synchronization-contract.md](references/synchronization-contract.md) for repeated screens, global/local edits or copied-Frame migration.
- Read [figma-observation-2026-08-11.md](references/figma-observation-2026-08-11.md) when evidence from the canonical example matters.
- Read [evals.md](references/evals.md) when changing this skill or its semantics.

## Classify the operation semantically

Produce this structured intent before an edit:

```yaml
scope: main_component | instance_override | journey_annotation | migration
target_screen_id: <stable conceptual screen ID or null>
target_journey_id: <Jxx variant or null>
target_instance_ids: [<exact Figma node IDs>]
authorized_effect: none | comment | design_write
rationale: <semantic reason grounded in the request and canvas>
```

Choose the scope by meaning:

| Scope | Use when | Effect |
| --- | --- | --- |
| `main_component` | The shared screen itself should change everywhere | Edit the canonical component, then verify every instance |
| `instance_override` | One journey occurrence intentionally differs in copy, state or a supported property | Edit only that instance property/variant |
| `journey_annotation` | The change describes the journey rather than the product screen | Edit connectors, badges, rule cards or journey metadata outside the instance |
| `migration` | Independent Frames need a durable shared identity | Create an approved mapping, componentize and replace occurrences |

Explicit negation and locality matter. A request such as “only this journey; do not affect the others” is not a global edit. If the intended scope could materially change other journeys and remains ambiguous after inspection, pause for the user.

## Establish screen identity

Do not treat matching names, visual similarity or spatial proximity as identity.

1. Propose a stable `screen_id` from purpose, user-visible state, data contract and navigation role.
2. List every candidate occurrence with exact Figma node ID, journey ID and evidence.
3. Explain conflicts: same label with different meaning, different labels with the same meaning, or structural divergence that needs a variant/new screen.
4. Obtain human approval before the first bulk migration mapping.
5. After migration, use `INSTANCE.mainComponent.id` as the deterministic proof of shared identity.

For multi-screen migrations, capture the mapping in a manifest that follows [linear-journey-manifest.schema.json](references/linear-journey-manifest.schema.json). Validate its shape with `python3 scripts/validate_manifest.py <manifest.json>`. Validation proves format, not semantic correctness.

## Build or revise the journey

1. Preserve one Section per actor-and-outcome journey.
2. Keep the happy-path trunk left to right, from explicit start to explicit outcome.
3. Place branches and time/state alternatives in labeled rows below the trunk. Show rejoin points or terminal outcomes.
4. Use screen occurrences as Instances of canonical screen Components. Keep journey occurrence IDs on instance names or annotations, not in the main component name.
5. Keep connectors, action/event labels, alternate entries, system events, rule cards and start/end badges outside screen Instances.
6. Add prototype reactions when the journey is meant to be traversable; visual arrows alone do not prove interaction.
7. Preserve existing coordinates, reactions, overrides and occurrence IDs during migration unless the approved change requires otherwise.

## Synchronize safely

- Edit the main Component for a global screen change.
- Use component properties or variants for intentional state differences.
- Use instance overrides only for journey-specific values allowed by the component contract.
- Never detach an Instance merely to make an edit easier. If the occurrence has a genuinely different product meaning, propose a new canonical screen or variant and record the rationale.
- Use Figma multi-edit only as a one-time migration aid. It does not create a durable relationship between Frames.
- Do not batch-edit “all similarly named frames.” Resolve conceptual identity first, then operate on exact approved IDs.

## Verify and hand off

After any design write:

1. Re-read the exact changed node and the affected main component/instances.
2. Confirm instance-to-component IDs, override scope, preserved reactions and branch labels.
3. Compare a screenshot at a useful scale when layout or visual meaning changed.
4. Run the final freshness checkpoint and record the remote effect.
5. Report what synchronized globally, what stayed local, every unresolved mapping and the exact node IDs changed.

## Non-goals

- This rule does not make Figma Frames synchronize automatically.
- It does not grant permission to publish a library, overwrite a component or edit another file.
- It does not claim that a visually linear board represents branch-free product logic.
- It does not let a manifest or schema validator decide whether two screens mean the same thing.
