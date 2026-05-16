---
name: git-commits
description: Create small, coherent Git commits with Conventional Commit messages. Use when the user asks Codex to commit changes, write or review commit messages, split staged work, choose commit types, or keep repository history clean.
---

# Git Commits

Use this skill to make commits that are easy to review, revert, and understand later.

## Contract

- Treat one commit as one coherent change, not a line-count target.
- Review the working tree before committing.
- Stage only files or hunks that belong to the same change.
- Do not include unrelated, generated, secret, credential, or local-only files.
- Run relevant checks when available and practical.
- Do not push, amend, rebase, reset, clean, or delete files unless the user explicitly asks.

## Message Format

Use Conventional Commits:

```text
type: short description
type(scope): short description
```

Keep the subject concise, imperative, lowercase after the type, and specific to the change.

Examples:

```text
feat: add initial CLI support
fix: handle missing config file
refactor(parser): simplify command validation
docs: add commit conventions
ci: add GitHub Actions checks
```

## Commit Types

| Type | Use for |
| --- | --- |
| `feat` | New user-facing capability or meaningful functionality |
| `fix` | Correcting broken behavior |
| `refactor` | Internal code structure changes without behavior changes |
| `style` | Formatting-only changes with no logic or behavior change |
| `docs` | README, Markdown docs, code comments, or examples |
| `test` | Adding or updating tests |
| `chore` | Maintenance that does not affect product behavior |
| `ci` | GitHub Actions or other automation pipeline changes |
| `build` | Build system, packaging, bundling, exports, or compile configuration |
| `perf` | Performance improvements |
| `revert` | Undoing a previous commit |

Use `chore` sparingly; do not hide real features, fixes, tests, or docs under it.

## Workflow

1. Run `git status` and inspect relevant diffs.
2. Decide the single coherent change to commit.
3. Stage only related files or hunks with `git add <file>` or `git add -p`.
4. Confirm the staged patch with `git diff --cached`.
5. Run focused checks if the repo provides them and the change warrants it.
6. Commit with a clear Conventional Commit message.
7. Report the commit hash, message, files included, and any checks run or skipped.

## Readiness Check

A commit is ready when:

- It completes one coherent change.
- The repo still builds, runs, or has relevant checks accounted for.
- The change can be explained in one sentence.
- The commit could be reverted without removing unrelated work.

Avoid messages like `wip`, `updates`, `fix stuff`, `misc changes`, and `big cleanup`.
