# Repository Expectations

This repository is the canonical source for Codex/Claude-style agent skills.

## Skill Locations

- Put production skills under `.agents/skills/<skill-name>`.
- Keep templates under `templates/`; templates are not meant to be loaded by Codex.
- Do not place placeholder or draft skills under `.agents/skills` unless they are valid and intentionally discoverable.

## Skill Shape

- Every skill directory must contain `SKILL.md`.
- `SKILL.md` frontmatter must include only `name` and `description`.
- The `name` must match the parent folder and use lowercase letters, digits, and hyphens.
- The `description` is the trigger surface; include what the skill does, when to use it, and important boundaries.
- Keep `SKILL.md` concise and procedural. Put larger details in `references/`.
- Use `scripts/` for deterministic repeatable work.
- Use `assets/` for templates, media, boilerplate, and output resources.
- Use `agents/openai.yaml` for OpenAI UI metadata, dependencies, and invocation policy.
- Do not add README, install guide, changelog, or other extra docs inside an individual skill folder.

## Validation

- Run `python3 tools/validate_skills.py` after adding or changing skills.
- For script-backed skills, run representative scripts with realistic inputs before considering the skill ready.
- Prefer small, focused commits that add or revise one skill at a time.
