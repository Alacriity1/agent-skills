# Repository Expectations

This repository is the canonical source for reusable Codex/Claude-style agent skills, templates, and maintenance tools.

Keep this file limited to repo-wide rules. Detailed workflows belong in skills, `docs/`, or `tools/`.

## Core Rules

- Put production skills under `.agents/skills/<skill-name>/`.
- Keep templates under `templates/`; templates are not meant to be loaded by Codex.
- Keep human authoring guidance under `docs/` and maintenance utilities under `tools/`.
- Do not place placeholder or draft skills under `.agents/skills/` unless they are valid and intentionally discoverable.
- Do not include secrets, private accounts, local credentials, personal machine paths, or one-off project details in reusable skills.

## Skill Shape

Each skill should follow this shape:

```text
.agents/skills/<skill-name>/
  SKILL.md
  references/   # optional longer guidance or supporting docs
  scripts/      # optional deterministic helpers for this skill
  assets/       # optional templates, boilerplate, media, or output resources
  agents/       # optional agent-specific metadata
```

Required:

- Every skill directory must contain `SKILL.md`.
- `SKILL.md` frontmatter must include only `name` and `description`.
- `name` must match the parent folder and use lowercase letters, digits, and hyphens.
- `description` is the trigger surface: keep it short, generic, action-oriented, and clear about when to use the skill.

## Authoring

- Keep `SKILL.md` concise and procedural.
- Put larger explanations, examples, background material, policies, and schemas in `references/`.
- Use skill-local `scripts/` only for deterministic repeatable work that directly supports that skill.
- Use `assets/` for templates, media, boilerplate, and output resources used by the skill.
- Use `agents/openai.yaml` only for OpenAI-specific UI metadata, dependencies, or invocation policy.
- Prefer one focused skill over a broad skill that handles unrelated workflows.
- Do not add README, install guide, changelog, or other extra docs inside individual skill folders.

## Validation

- For script-backed skills, run representative scripts with realistic inputs before considering the skill ready.
- Do not mark a skill production-ready if its scripts, references, or metadata are stale or broken.

## Git

- Use Conventional Commits; use the `git-commits` skill for commit creation, review, and message selection.
- Prefer small, reviewable commits that add or revise one concept at a time.
- Prefer one skill addition or one skill revision per commit.
- Check `git status` and review relevant diffs before committing.
- Do not push, amend, rebase, reset, clean, or delete files unless explicitly requested.
- If unrelated user or agent changes are present, do not overwrite them.

## Style

- Be concise without sacrificing clarity.
- Use plain Markdown and short bullets.
- Keep reusable instructions portable across agents, repos, and machines.
