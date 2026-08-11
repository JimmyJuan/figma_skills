# Canonical Figma observation — 2026-08-11

Reference: [爪际·爱心守护站 — 爪际用户旅程-线性版本1](https://www.figma.com/design/mMpVLl0gLxTt9O4zdhFb7e/爪际·爱心守护站?node-id=767-555)

Exact target: `{fileKey: mMpVLl0gLxTt9O4zdhFb7e, nodeId: 767:555}`.

Freshness snapshot:

- state: `fresh`
- snapshot schema: `figma-partition-merkle-v1`
- SHA-256: `8857d2469d3775dac5e1b1821cc229a2e217c67394ba46c18ea7d8b739eefa37`
- normalized nodes: `27,195`
- top-level partitions: `27`
- prototype reactions: `289`
- Instances: `1`

## What the canvas demonstrates

- The page is an indexed family of role-and-outcome journeys, not one unbroken mega-flow.
- Each `Jxx` Section starts with journey context, then presents a left-to-right screen trunk.
- Branch and timed/state alternatives sit in rows below the trunk and connect back to decisions or outcomes.
- Actions are written on connectors; rule cards explain exceptional behavior.
- Some journeys include alternate entries, decision nodes and cross-role supporting streams.
- Repeated screens are common across journeys, but almost all are independent Frames. The canvas therefore demonstrates the journey grammar while also exposing the maintainability problem this rule solves.

## Representative exact nodes

- `773:2712` — J01, owner publishes and follows a lost-pet journey through reunion/thanks.
- `773:4040` — J02, finder submits a useful clue.
- `773:5429` — J03, owner reviews and accepts/rejects clues, including alternate entry and exception paths.
- `777:3` — J14, multiple message scenarios stacked in rows.
- `1231:4` — J02-V2, AI recognition with a decision split and a cross-role supporting stream.

The observation is evidence for this rule, not a template to copy blindly. New projects may use different visual tokens while preserving the semantic contract.
