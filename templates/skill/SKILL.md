---
name: skill-template
description: Replace with a concise trigger description. Include what the skill does, when Codex should use it, and important boundaries.
---

# Skill Template

State the workflow Codex should follow. Use direct instructions and include only the context another Codex session needs to perform the task well.

## Workflow

1. Identify the user's concrete goal and relevant inputs.
2. Select the smallest useful path through this skill.
3. Read referenced files only when their conditions apply.
4. Use scripts for deterministic or repetitive work.
5. Validate the result before responding.

## References

- Read `references/example.md` only when the task needs detailed background, schemas, policies, or examples.

## Scripts

- Use `scripts/example.py` only after replacing it with real deterministic logic for this skill.

## Output

Summarize the result briefly, name any changed files, and call out validation that was run or skipped.
