# Agent Skills

Canonical repository for instructions, skills, and helpers for my codex and claude-style agents.

## Structure
Mostly focused for Codex. If/when I switch back over to claude I may have to take another look.

- [Agent Skills - Codex](https://developers.openai.com/codex/skills)
- [Custom instructions with AGENTS.md - Codex](https://developers.openai.com/codex/guides/agents-md)
- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [OpenAI skill-creator reference](https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md)
```ts
.
├── .agents/
│   └── skills/
│       └── <skill-name>/
│           ├── SKILL.md //the big enchilada 
│           ├── agents/
│           │   └── openai.yaml // optional: metadata
│           ├── scripts/ //execution code
│           ├── references/ //optional: documentation
│           └── assets/ //optional: appearance and dependancies
├── templates/ //for reference
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
