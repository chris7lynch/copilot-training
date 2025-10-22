# Copilot Training Demo

This repo hosts a minimal FastAPI web app coupled with light CSS and JavaScript. It is designed to help new teammates learn how to get the most out of GitHub Copilot while iterating on Python services and front-end tweaks.

## Prerequisites for Training

**Technical Background**: Participants should have basic familiarity with:
- Command line/terminal usage
- VS Code interface and Command Palette
- Python virtual environments (basic concept)
- Git clone and basic repository navigation
- Web development concepts (HTML, CSS, JavaScript basics)

**Required Software**:
- VS Code with GitHub Copilot extension
- Python 3.8+ installed
- Git for repository cloning
- Active GitHub Copilot subscription

**Security Concepts**: The lab includes a SQL injection vulnerability exercise. While the lab provides links to detailed explanations, instructors should be prepared to explain:
- What SQL injection attacks are
- Why parameterized queries prevent them
- Basic security principles in web development

## Project Layout

- `app/main.py` – FastAPI application entry point
- `app/templates/index.html` – Landing page template rendered by FastAPI
- `app/static/` – Lightweight CSS and JavaScript assets
- `vulnerabilities/` – Training modules with intentional security flaws for Copilot remediation practice
- `.github/copilot-instructions.md` – Team-specific guidance for using Copilot
- `.github/prompts/` – Ready-to-use prompt snippets for workshops

## Working in VS Code

1. **Create a virtual environment**
   - Open the command palette:
     - **Windows/Linux**: `Ctrl+Shift+P`
     - **Mac**: `⇧⌘P` (Shift+Command+P)
   - Run `Python: Create Environment...` → `Venv` → select your interpreter.
   - Alternatively, run `py -m venv .venv` in the integrated terminal.
   - When prompted, allow VS Code to activate the environment. You can confirm the environment by checking the Python interpreter shown in the status bar.
   - If VS Code does not prompt for activation, manually run `.\.venv\Scripts\activate` (PowerShell: `.\.venv\Scripts\Activate.ps1`).
   

2. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Run the FastAPI app locally**
   ```bash
   uvicorn app.main:app --reload
   ```
   Visit http://127.0.0.1:8000 in your browser.

4. **Leverage GitHub Copilot**
   - Use inline comments to steer Copilot toward the tests or features you want to explore.
   - Ask Copilot Chat to document endpoints, propose refactors, or scaffold new workshop exercises.

5. **Working with Prompt Files**
   - Create prompt files in `.github/prompts/` with the `.prompt.md` extension for structured agent workflows.
   - Use YAML front matter to define `mode: agent`, `model`, and `description` fields.
   - Execute prompt files by opening them in VS Code and using the "Run Prompt" command from the command palette:
     - **Windows/Linux**: `Ctrl+Shift+P`
     - **Mac**: `⇧⌘P` (Shift+Command+P)
   - Example: Open `.github/prompts/dark-mode.prompt.md` and run it to automatically apply dark theme styling to the app.

## Security Training Module

The `vulnerabilities/sql_injection/` folder contains a hands-on SQL injection training lab:

**🚨 Vulnerable Endpoint**: `/vulnerable/users/{username}`
- Demonstrates string concatenation in SQL queries
- Contains sample user data with sensitive information
- Shows real exploitation techniques

**🔍 Testing the Vulnerability**:
1. Normal request: `http://127.0.0.1:8000/vulnerable/users/admin`
2. Basic injection: `http://127.0.0.1:8000/vulnerable/users/admin%27%20OR%20%271%27%3D%271`
3. Data extraction: `http://127.0.0.1:8000/vulnerable/users/admin%27%20UNION%20SELECT%20id%2C%20username%2C%20secret_data%2C%20role%20FROM%20users--`

**🤖 Copilot Fix Command**:
Open `vulnerabilities/sql_injection/vulnerable_routes.py` and use this prompt in Copilot Chat:
```
Fix this function to prevent SQL injection by using parameterized queries. Keep the same route and behavior, only fix the security issues. Add input validation (check for empty/null usernames and reasonable length limits). Use secure error handling that doesn't expose database details to users.
```

**📚 Learning Resources**:
- Complete lab guide in `vulnerabilities/sql_injection/SQL_Injection_Lab.md`


## Next Steps

- Expand the prompt library under `.github/prompts/` with scenarios relevant to your team.
- Add pytest-based exercises to practice test-driven development with Copilot.
- Deploy the app to your preferred hosting solution (e.g., Azure App Service or Fly.io) for remote workshops.
