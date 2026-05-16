# Agent Skills

Canonical repository for instructions, skills, and helpers for my codex and claude-style agents.

## Structure
Mostly focused for Codex. If/when I switch back over to claude I may have to take another look.

```ts
.
├── .agents/
│   └── skills/
│       └── <skill-name>/
│           ├── SKILL.md //the big enchilada 
│           ├── agents/
│           │   └── openai.yaml //optional: metadata
│           ├── scripts/ //optional: execution code
│           ├── references/ //optional: documentation
│           └── assets/ //optional: appearance and dependancies
├── templates/ //for reference & copy/paste
│   └── skill/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       ├── assets/
│       ├── references/
│       │   └── example.md
│       └── scripts/
├── docs/ // explanation and authoring guidance for Codex
│   └── skill-authoring.md
├── tools/ //to maintain the agent-skills repo itself
│   └── validate_skills.py
├── AGENTS.md
└── README.md
```

## Create a Skill

1. Copy `templates/skill` to `.agents/skills/<skill-name>`.
2. Rename the frontmatter `name` to match the folder exactly.
3. Rewrite `description` with clear trigger words and boundaries.
4. Keep core workflow instructions in `SKILL.md`.
5. Move long, conditional, or domain-specific detail into `references/`.
6. Add deterministic repeatable code to `scripts/`.
7. Put reusable output files, templates, images, or boilerplate in `assets/`.
8. Update `agents/openai.yaml` for UI metadata and invocation policy.
9. Run `python3 tools/validate_skills.py`.

For local experimentation outside this repo, Codex can also read user skills
from `$HOME/.agents/skills`; this repo keeps the canonical source in version
control.

## References

- [Agent Skills - Codex](https://developers.openai.com/codex/skills)
- [Custom instructions with AGENTS.md - Codex](https://developers.openai.com/codex/guides/agents-md)
- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [OpenAI skill-creator reference](https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md)