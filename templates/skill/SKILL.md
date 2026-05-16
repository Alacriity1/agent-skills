---
name: skill-template
description: Replace with a concise trigger description. Include what the skill does, when Codex should use it, expected inputs, and important boundaries.
---

# Skill Template

Copy this file when creating a new Codex skill. Replace the placeholders with instructions for one specific, repeatable workflow.

A finished skill should tell Codex when to use it, what inputs matter, what steps to follow, how to validate the result, and what to report back. Keep the main `SKILL.md` concise; move long examples, schemas, policies, and edge cases into `references/`.

## Use When

- The task matches the frontmatter `description`.
- The workflow is specific enough to execute with the available repo context.
- This skill is the smallest useful tool for the job.

## Contract

- Stay focused on the skill's single job.
- Preserve existing project conventions unless this skill explicitly overrides them.
- Prefer direct instructions over scripts unless the logic is deterministic or repetitive.
- Read only the files needed for the current task.
- Make the smallest correct change; avoid broad rewrites unless requested.
- Validate the result before responding, or state why validation was skipped.

## Workflow

1. Identify the user's goal, inputs, constraints, and done condition.
2. Inspect the minimum relevant files before editing or running commands.
3. Choose the smallest path through the skill; skip sections that do not apply.
4. Read bundled references only when their conditions apply.
5. Use bundled scripts only when they provide deterministic value.
6. Make the change or produce the requested output.
7. Run the most focused validation available.
8. Summarize the result, changed files, and validation.

## References

- Use `references/` for detailed background, schemas, policies, examples, and edge cases that would bloat this file.
- Read reference files only when needed for the current task.

## Scripts

- Use `scripts/` for repetitive parsing, formatting, generation, validation, or external-tool orchestration.
- Do not add scripts for one-off logic that is clearer as direct instructions.

## Output

Final response should include:

- What was done.
- Files changed, if any.
- Validation run, or why it was skipped.
- Any remaining risks or assumptions.