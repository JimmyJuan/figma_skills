# Screen synchronization contract

## Durable mechanism

Figma synchronizes a reusable screen through a Component and its Instances. Editing independent Frames, even when they look identical or have the same name, does not establish future synchronization.

Use these layers:

| Layer | Owns | How it changes |
| --- | --- | --- |
| Canonical screen Component | Shared structure, shared visual system, shared default content | Edit once for a global screen change |
| Variant / component property | Supported product states and intentional configurable differences | Select a state/property on an Instance |
| Instance override | Journey-specific value allowed by the contract | Edit only the exact occurrence |
| Journey annotation | Actions, decisions, elapsed time, notes, start/end and connectors | Edit outside the Instance |

## Migration from copied Frames

### 1. Inventory

Record every candidate occurrence with exact Figma node ID, journey ID, current name, dimensions, key state and prototype reactions.

### 2. Semantic mapping

The model proposes groups of occurrences that appear to represent the same product screen. It explains evidence and conflicts. A human approves the first migration mapping.

Names are hints, not proof:

- Same name, different state or navigation role may require separate screens or a variant.
- Different names may still represent one screen if purpose, structure, data and navigation role are equivalent.

### 3. Canonicalize

For each approved `screen_id`:

1. Choose or create the canonical Component.
2. Define supported variants/properties.
3. Replace each mapped Frame with an Instance at the same coordinates.
4. Restore approved occurrence-specific values as overrides.
5. Reconnect reactions and keep journey annotations outside the Instance.
6. Record the resulting `mainComponent.id` and instance IDs.

### 4. Verify

- A controlled main-component change reaches all expected Instances.
- A journey-only override does not alter other occurrences.
- Prototype reactions, visible states and connector targets remain correct.
- No mapped occurrence is detached.
- Unmapped or disputed Frames remain untouched and are reported.

## Edit decision examples

“Increase the safe area on the home screen everywhere” is a canonical Component change once screen identity is proven.

“Only J02 shows the first-visit banner” is an Instance state/variant change if the canonical Component supports that state.

“Change the arrow label from submit to confirm” is a journey annotation change, not a screen change.

“Make all frames named Home identical” is not safe enough to execute. Resolve conceptual identity first.

## Figma-level rule pointer

Because Figma does not provide an account-wide AI instruction field, add a small visible contract frame or Section to each relevant file and attach machine-readable shared plugin data when the tooling supports it. The pointer should contain:

- rule ID and version;
- canonical GitHub path;
- the Component/Instance synchronization rule;
- the global-versus-local scope rule;
- the prohibition on name-only batch edits;
- the local freshness and authorization requirements.

Keep the full specification in GitHub so file-level pointers cannot become competing sources of truth.
