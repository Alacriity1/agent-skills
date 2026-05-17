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
├── global/
│   └── AGENTS.md // global Codex defaults
├── AGENTS.md
└── README.md
```

## Quick Setup

Codex uses two separate global locations:

1. Skills go in `$HOME/.agents/skills`.
2. Global instructions go in `$HOME/.codex/AGENTS.md`.

`AGENTS.md` does not load skills. Skills must be installed into the skills folder.

### 1. Set Up Global Skills

Recommended: point Codex's global skills folder at this repo's skills folder.

```bash
mkdir -p "$HOME/.agents"
ln -s "<path-to-this-repo>/.agents/skills" "$HOME/.agents/skills"
```

Alternative: copy this repo's skills into Codex's global skills folder.

```bash
mkdir -p "$HOME/.agents/skills"
cp -R "<path-to-this-repo>/.agents/skills/"* "$HOME/.agents/skills/"
```

Use one approach, not both. If `$HOME/.agents/skills` already exists and has skills you want to keep, copy selected skills instead of replacing the folder.

### 2. Set Up Global Instructions

Recommended: point Codex's global instructions file at this repo's `global/AGENTS.md`.

```bash
mkdir -p "$HOME/.codex"
ln -s "<path-to-this-repo>/global/AGENTS.md" "$HOME/.codex/AGENTS.md"
```

Alternative: copy this repo's instructions file into Codex's global instructions file.

```bash
mkdir -p "$HOME/.codex"
cp "<path-to-this-repo>/global/AGENTS.md" "$HOME/.codex/AGENTS.md"
```

These commands work in macOS, Linux, Git Bash, and WSL. In PowerShell, use `New-Item -ItemType SymbolicLink` instead of `ln -s`, or copy files with `Copy-Item`. On Windows Git Bash can be a bit funky, so it's probably best to just use PowerShell.

Instruction hierarchy:

1. Global: `$HOME/.codex/AGENTS.md`.
2. Repo root: `AGENTS.md`.
3. Nested directories from repo root to the current working directory.

More specific files override earlier guidance. Use this repo's root `AGENTS.md` for maintaining this repo; use `global/AGENTS.md` for portable defaults across all repos.

### 3. Set Up Downstream Repo Instructions

Downstream repos can use a pointer-style `AGENTS.md` so shared rules stay canonical here:

```text
READ <path-to-this-repo>/global/AGENTS.md BEFORE ANYTHING (skip if missing).
```

Put repo-specific rules below that pointer. Do not copy shared blocks into downstream repos.

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

For local experimentation outside this repo, copy selected skills into a target project's `.agents/skills/` folder.

## References

- [Agent Skills - Codex](https://developers.openai.com/codex/skills)
- [Custom instructions with AGENTS.md - Codex](https://developers.openai.com/codex/guides/agents-md)
- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [OpenAI skill-creator reference](https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md)
