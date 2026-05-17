# Global Agent Instructions

Use these rules in every repository. Repo-local `AGENTS.md` files may add or override rules for that project.

## Core

- Inspect relevant files before changing code.
- Prefer existing project conventions over new abstractions.
- Keep changes scoped to the user's request.
- Do not overwrite unrelated user or agent changes.
- Do not add secrets, credentials, local machine paths, or private account details.
- Use concise Markdown. Avoid tables unless explicitly requested.
- When instructions conflict, follow the more specific repo or directory instruction.

## Workflow

- State what context you are gathering before substantial edits.
- Read repo docs, package scripts, build config, and nearby code before choosing commands.
- Use the repo's package manager, formatter, test runner, and runtime.
- Do not swap frameworks, package managers, runtimes, or major dependencies without approval.
- Add focused tests for bug fixes and behavior changes when practical.
- Update docs or changelogs for user-visible behavior changes when the repo expects it.
- Keep inline comments brief and only for tricky, bug-prone, or non-obvious logic.
- Report validation run, skipped validation, and remaining risks at closeout.

## Skills

- Use available skills when they match the task.
- Use `git-commits` for commit creation, commit review, staging, and message selection.
- Use `code-review` for review requests, pre-commit checks, PR reviews, and bug-risk reviews.
- Use `test-writer` for adding or improving automated tests.
- Use `frontend-design` for UI creation, redesign, polish, layout, styling, and frontend implementation.

## Git

- If the current directory is in a Git repo, work in that checkout.
- Check `git status` and relevant diffs before staging or committing.
- Treat unrecognized changes as user or other-agent work; do not revert them.
- Stage only files or hunks that belong to the same coherent change.
- Use Conventional Commits when committing.
- Push only when the user explicitly asks.
- Do not amend, rebase, reset, clean, delete files, or rewrite history unless explicitly requested.
- Branch changes require user consent unless the user directly asks for that workflow.
- End in the checkout and branch the user expects.

## Review

- For code reviews, findings come first and summaries come second.
- Prioritize correctness, regressions, security-sensitive behavior, data loss, race conditions, error handling, and missing tests.
- Verify findings against the real code path before reporting them.
- Prefer no finding over weak or speculative findings.
- Include concrete file and line references when possible.

## Safety

- Never print or broadly enumerate secrets.
- Do not run broad secret/env dumps such as `env`, `set`, or `export -p`.
- Query only exact secret names when needed, and redact values.
- Use destructive shell, Git, or filesystem operations only after explicit user approval.
- For public GitHub text containing code, shell, user text, env vars, or backticks, prefer a temp file and body-file style command instead of fragile inline quoting.
