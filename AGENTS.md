# AGENTS.md

## Rule routing

- Treat each folder under `rules/` as a self-contained agent skill. Read its `SKILL.md` completely before acting, then load only the referenced files required for the task.
- Use `rules/linear-user-journey/SKILL.md` when a task creates, reads, edits, audits or migrates a screen-by-screen journey, especially when screen occurrences repeat across journeys and must stay synchronized.
- Select rules by meaning and task context. Do not build keyword, regular-expression, containment, token-distance or sentence-specific routers for open-ended user text.

## Safety and evidence

- A request to document or analyze a rule does not authorize a Figma write. Require explicit design-write intent and exact file/node targets.
- Before every Figma-dependent action, after resuming, before a write and before completion, use the environment's Figma freshness checkpoint when one exists.
- For semantic routing or scope changes, maintain `docs/model-first-rule-ledger.md` and run its postflight checks.
- Validate exact node IDs, main-component relationships, schemas, authorization and effect scope deterministically.

## Repository conventions

- GitHub content is canonical. Obsidian and Figma should point here rather than copy full rules.
- Keep each rule portable: no private credentials, local-only secrets or unexplained machine paths.
- Put detailed guidance in `references/`; keep `SKILL.md` focused on decisions and workflow.
- Scripts may validate closed formats only. They must not pretend to understand free-form product or design semantics.
