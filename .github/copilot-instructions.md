# Copilot Usage Playbook

This repository exists to help new developers practice effective prompting, review, and iteration habits with GitHub Copilot.

## Prompting Basics

- **Lead with context**: Mention the file, function, and desired outcome. Example: "In `app/main.py`, add an endpoint that returns JSON with workshop metadata."
- **State constraints**: Call out performance, style, or testing expectations so Copilot can respect them.
- **Request validation**: Ask Copilot to include tests or explain potential regressions so you always double-check suggestions.

## Review Workflow

1. Generate code with inline completions or chat.
2. Inspect diffs just like a teammate's pull request. Reject suggestions that you cannot explain.
3. Run or extend automated tests before committing.

## Common Exercises

- Refactor the landing page content to match your team's onboarding journey.
- Introduce a new FastAPI route and have Copilot propose both implementation and pytest coverage.
- Improve `style.css` for accessibility, asking Copilot to justify each change.

## Safety Guardrails

- Never accept code you do not understand—ask Copilot to clarify in comments or chat.
- Do not paste sensitive credentials or proprietary snippets into prompts.
- Document substantial AI-assisted changes in commit messages to maintain transparency.
