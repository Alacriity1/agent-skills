---
name: frontend-design
description: Create or improve production-quality frontend UI for pages, components, app flows, and new interface templates. Use when the user asks for visual design, layout, styling, polish, responsive UI, or non-generic frontend implementation.
---

# Frontend Design

Use this skill to create new frontend interfaces or improve existing ones with working code, clear visual direction, strong usability, and implementation that fits the project context.

## Use When

- The task involves UI, layout, styling, frontend polish, components, pages, app flows, or interface templates.
- The user wants a new frontend created from scratch or an existing frontend made more refined, distinctive, or production-ready.
- The requested output can be implemented within the current project’s frontend stack, or the user is starting from an empty/minimal frontend file.
- The user asks for design direction, visual structure, or a non-generic implementation rather than only functional logic.

## Contract

- For existing projects, preserve framework, component, styling, and naming conventions as applicable.
- Inspect the relevant files before changing UI.
- For empty or minimal files, establish a clear structure, visual system, and responsive baseline without over-engineering.
- Prefer localized changes over broad rewrites.
- Reuse existing components, tokens, utilities, and patterns where available; otherwise define lightweight local conventions.
- Do not add dependencies, fonts, animation libraries, or asset pipelines unless clearly justified.
- Make the interface usable, responsive, accessible, and functional.
- Avoid generic AI-looking UI unless the user explicitly asks for a conventional style.
- Validate with the most focused available command.

## Workflow

1. Identify whether the task is new UI creation, redesign, or targeted polish.
2. Identify the user’s goal, target screen/component, audience, constraints, and done condition.
3. Inspect the current frontend stack, relevant files, existing components, styling approach, and design conventions when present.
4. Choose a clear design direction appropriate to the product context.
5. For new UIs, establish the page/component structure, responsive layout, visual system, and interaction model.
6. For existing UIs, improve layout, hierarchy, typography, spacing, color, states, and motion without unnecessary rewrites.
7. Implement working code with the smallest reasonable change set for the task scope.
8. Check responsive behavior, accessibility basics, and interaction states.
9. Run focused validation such as typecheck, lint, tests, or build.
10. Report what changed, where, validation results, and any assumptions.

## Design Principles

- Choose an intentional aesthetic direction before coding.
- Make the UI feel designed for this specific product or concept, not copied from a generic SaaS template.
- Use strong visual hierarchy: clear primary actions, readable content, and obvious grouping.
- Use typography, spacing, color, borders, shadows, and motion consistently.
- Prefer a few memorable design choices over many decorative effects.
- Match complexity to the product: expressive interfaces can be bold; utility interfaces should be restrained and precise.
- Respect accessibility, contrast, keyboard navigation, focus states, and reduced-motion preferences.

Remember: You are capable of extraordinary creative work. Don't hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.

## Avoid

- Generic purple/blue gradient SaaS layouts unless contextually appropriate.
- Random glassmorphism, glow effects, oversized cards, or decorative noise without purpose.
- Unnecessary dependencies or one-off abstractions.
- Replacing the app’s design system without being asked, or inventing a heavy design system for a small standalone template.
- Breaking existing state, data flow, routing, or responsiveness for visual polish.

## Output

Final response should include:

- What was changed.
- Files changed.
- Validation run, or why validation was skipped.
- Any remaining assumptions or follow-up design risks.