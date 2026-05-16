---
name: test-writer
description: Write or improve focused automated tests for existing code changes, bug fixes, edge cases, regressions, and behavior validation. Use when the user asks for tests, coverage, missing cases, failing tests, or stronger validation in the project's current stack.
---

# Test Writer

Write clear, maintainable tests that prove important behavior without bloating the suite.

Use this skill to add new tests, improve weak tests, or create regression coverage after a bug fix. Optimize for confidence, readability, and project fit over raw test count.

## Use When

- The user asks to write, add, improve, or review tests.
- A code change needs regression coverage before closeout.
- A bug report includes a reproducible behavior that should stay fixed.
- Existing tests cover the happy path but miss important boundaries, errors, or integration points.

## Contract

- Test observable behavior, not private implementation details.
- Follow the project's existing test framework, style, naming, fixtures, and file layout.
- Prefer small, explicit tests with one main reason to fail.
- Cover meaningful behavior first: happy path, important edge cases, failure paths, and regressions.
- Prefer deterministic tests; control time, randomness, network, wallets, databases, and external services at their boundary.
- Do not chase 100% coverage when it adds brittle, duplicate, or low-value tests.
- Do not add new test libraries, mocking frameworks, snapshots, or broad fixtures unless clearly necessary.
- Keep production code changes minimal and only make them when required to make behavior testable.
- Never weaken, delete, or skip existing tests just to make the suite pass unless the user explicitly asks and the reason is documented.

## Workflow

1. Identify the behavior under test, the risk being reduced, and the expected outcome.
2. Inspect the smallest relevant set of files: changed code, nearby tests, fixtures, helpers, and package/test config.
3. Determine the test layer that gives the most confidence with the least complexity:
   - unit tests for pure logic, validation, calculations, and small utilities
   - integration tests for module boundaries, API routes, storage, contracts, or component interactions
   - end-to-end tests only for critical user flows that cannot be trusted through lower-level tests
4. Reuse existing test patterns before inventing new structure.
5. Add the fewest tests that cover the meaningful cases.
6. Make test data realistic but minimal; avoid giant fixtures unless they already exist.
7. Use mocks and stubs only at true boundaries such as network, filesystem, time, randomness, wallets, chains, databases, or external services.
8. Run the most focused relevant test command first.
9. If focused tests pass, run the broader affected suite when practical.
10. Fix failures by reading the failing code path, not by loosening assertions.

## Stack Notes

Use the project's existing framework first. Apply only the notes relevant to the current repo.

- TypeScript/JavaScript: follow existing Jest, Vitest, Testing Library, Playwright, or framework-specific patterns. Await async behavior explicitly, prefer user-visible assertions for UI, and mock only real boundaries.
- Foundry/Solidity: follow existing Forge helpers and fixtures. Cover permissions, reverts, events, balances, accounting, upgrade/migration assumptions, and edge values. Use cheatcodes such as `expectRevert`, `expectEmit`, `prank`, `warp`, `roll`, or `deal` when they express the behavior clearly.
- Swift: follow existing XCTest or Swift Testing patterns. Test public behavior, async paths, error cases, and platform boundaries with deterministic clocks, dependencies, and fixtures where possible.

## References

- Read `references/testing-patterns.md` only when useful examples would improve test structure, assertions, or framework fit. Treat snippets as patterns, not templates to copy blindly.

## Test Selection

Prioritize tests in this order:

1. Regression test for the exact reported bug or changed behavior.
2. Normal successful behavior users or callers rely on.
3. Boundary values and invalid inputs that are likely in real use.
4. Error handling for important failures.
5. Integration behavior across project-specific seams.

Skip or defer tests that are mostly implementation trivia, duplicate another assertion, require excessive mocking, or would make future refactors unnecessarily painful.

## Assertion Guidelines

- Assert specific outputs, state changes, emitted events, rendered text, return values, thrown errors, or external calls at the boundary.
- Avoid assertions that only prove a mock was wired internally unless that call is the behavior contract.
- Prefer clear literals and named constants over clever helper logic inside tests.
- Keep snapshots small and intentional; do not add large snapshots for dynamic UI or noisy objects.
- Include one regression comment only when the reason for the case would otherwise be unclear.

## Coverage Heuristic

Aim for useful confidence, not maximum volume.

A good test set usually includes:

- one representative happy path
- one or two high-risk edge cases
- one failure path when errors matter
- one regression case when fixing a bug

Add more only when branches represent distinct user-visible behavior or meaningful risk.

## Validation

Use the project's existing commands. Prefer the narrowest command that proves the new tests first, then broaden if needed.

Examples:

- `npm test -- <file-or-pattern>`
- `pnpm test <file-or-pattern>`
- `yarn test <file-or-pattern>`
- `npx jest <file>`
- `npx vitest run <file>`
- `forge test --match-test <name>`
- `forge test --match-contract <name>`
- `swift test --filter <name>`

If no test command is obvious, inspect package scripts, Makefiles, CI config, Foundry config, or existing README instructions before guessing.

## Output

Final response should include:

- Tests added or improved.
- Behavior covered.
- Files changed.
- Validation command and result.
- Any gaps, skipped validation, or follow-up tests worth adding later.
