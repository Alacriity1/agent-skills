# Skill Authoring

Use this checklist when adding or revising skills in this repo.

## Required

- The skill folder lives at `.agents/skills/<skill-name>`.
- The folder name and `SKILL.md` frontmatter `name` match exactly.
- The name uses lowercase letters, digits, and hyphens only.
- `SKILL.md` has YAML frontmatter followed by Markdown instructions.
- `description` starts with the highest-signal use case and trigger words.

## Recommended

- Add `agents/openai.yaml` for display metadata and invocation policy.
- Keep `SKILL.md` below 500 lines.
- Link every reference file from `SKILL.md` with a note about when to read it.
- Put only one level of files under `references/` unless a real workflow needs deeper structure.
- Include a table of contents in reference files longer than 100 lines.

## Resource Rules

- Use `scripts/` for fragile or repetitive operations where deterministic behavior matters.
- Use `references/` for policies, schemas, examples, API notes, and detailed domain knowledge.
- Use `assets/` for output templates, images, document boilerplate, or other files the agent should reuse.
- Avoid duplicating the same guidance in both `SKILL.md` and `references/`.

## Review Questions

- Would Codex know when to use this skill from the description alone?
- Is the skill narrow enough to be reliable?
- Are scripts actually tested?
- Are large details discoverable without loading them into every task?
- Is anything inside the skill useful only to humans rather than the agent? If so, keep it in repo docs, not inside the skill.
