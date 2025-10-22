# Copilot Usage Playbook

This repository exists to help new developers practice effective prompting, review, and iteration habits with GitHub Copilot.

## Project Context for Agent Mode

This is a **FastAPI training application** with the following structure:
- **Backend**: FastAPI app in `app/main.py` with vulnerable endpoints for security training
- **Frontend**: HTML templates in `app/templates/`, CSS/JS in `app/static/`
- **Environment**: Python virtual environment (`.venv/`) with dependencies in `requirements.txt`
- **Security Lab**: Intentional SQL injection vulnerability in `vulnerabilities/sql_injection/`

### Running the Application
```bash
# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# OR
.\.venv\Scripts\activate   # Windows

# Start the FastAPI server
uvicorn app.main:app --reload

# Access at: http://127.0.0.1:8000
```

### Key Endpoints
- `/` - Main training homepage
- `/vulnerable/users/{username}` - SQL injection vulnerable endpoint
- `/vulnerable/users` - Safe user listing endpoint

## Prompting Basics

- **Lead with context**: Mention the file, function, and desired outcome. Example: "In `app/main.py`, add an endpoint that returns JSON with workshop metadata."
- **State constraints**: Call out performance, style, or testing expectations so Copilot can respect them.
- **Request validation**: Ask Copilot to include tests or explain potential regressions so you always double-check suggestions.

## Agent Mode Guidelines

When working in agent mode on this project:

### Environment Setup
- **Always check** if virtual environment is activated before installing packages
- **Use `pip install -r requirements.txt`** for dependencies, not individual installs
- **Restart the server** after backend changes: `uvicorn app.main:app --reload`

### File Modifications
- **FastAPI routes**: Add new endpoints to `app/main.py` or create modules in `app/`
- **Frontend changes**: Modify `app/templates/index.html` for structure, `app/static/style.css` for styling
- **Security examples**: Work within `vulnerabilities/` folder structure for educational content

### Testing Changes
- **Backend**: Test endpoints by visiting URLs or using curl/httpie
- **Frontend**: Check `http://127.0.0.1:8000` for visual changes
- **Security**: Use the provided SQL injection test URLs to verify vulnerability fixes

### Code Quality
- **Follow FastAPI patterns**: Use proper type hints, async/await, dependency injection
- **Maintain security focus**: When fixing vulnerabilities, use parameterized queries and input validation
- **Keep educational value**: Preserve learning objectives when modifying training content

## Review Workflow

1. Generate code with inline completions or chat.
2. Inspect diffs just like a teammate's pull request. Reject suggestions that you cannot explain.
3. Test changes by running the application and accessing relevant URLs.
4. Run or extend automated tests before committing.



## Safety Guardrails

- Never accept code you do not understand—ask Copilot to clarify in comments or chat.
- Do not paste sensitive credentials or proprietary snippets into prompts.
- **Preserve educational vulnerabilities**: Don't accidentally fix training examples unless that's the goal.
- Document substantial AI-assisted changes in commit messages to maintain transparency.
- **Test security fixes**: Always verify that vulnerability patches actually prevent exploitation.
