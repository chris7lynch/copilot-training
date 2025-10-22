---
mode: agent
model: Claude Sonnet 4
description: Enhance the FastAPI training app with an accessible dark theme while staying within the current project structure.
---

## Mission
Transform the existing FastAPI demo app into a cohesive dark-mode experience while keeping readability and accessibility as top priorities. Work within the current project structure and avoid introducing new design systems.

## Repository Context
- `app/templates/index.html`
- `app/static/style.css`
- `app/static/script.js`

## Objectives
1. Update global colors, typography, and component styling for a dark UI in `style.css`.
2. Adjust HTML classes or structure in `index.html` only if necessary to support dark-mode styling (e.g., adding wrapper classes or ARIA attributes).
3. Ensure interactive elements meet WCAG AA contrast ratios and retain clear focus states.
4. Provide minimal JavaScript tweaks in `script.js` only if required for contrast or theming consistency.

## Constraints
- Stay within existing assets; do not pull in external CSS frameworks.
- Keep gradients and accent colors subtle; avoid neon on dark backgrounds.
- Preserve semantic HTML and current layout logic.
- Test against light-on-dark readability and hover/focus accessibility.

## Deliverables
- Updated files with inline comments only where non-obvious decisions were made.
- A brief summary explaining the design rationale and any accessibility considerations.
- A checklist of manual QA steps (e.g., keyboard navigation, color contrast verification).