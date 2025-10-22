# GitHub Copilot Training Lab Guide

Welcome to the GitHub Copilot Training Lab! This hands-on workshop will teach you how to effectively use GitHub Copilot through three progressive exercises that build from basic chat commands to advanced prompt engineering.

## 🎯 Learning Objectives

By the end of this lab, you will:
- Use Copilot Chat to identify and fix security vulnerabilities
- Execute existing prompt files to make large-scale changes
- Create and run your own custom prompt files
- Understand best practices for prompting AI coding assistants

## � Setup Instructions

### Prerequisites
- VS Code installed
- GitHub Copilot extension enabled in VS Code
- Python 3.8+ installed
- Git (to clone this repository)

### Step 1: Environment Setup
1. **Clone or download this repository**:
   ```bash
   git clone https://github.com/chris7lynch/copilot-training.git
   cd copilot-training
   ```

2. **Create a virtual environment**:
   - Open VS Code in the project folder
   - Open the Command Palette:
     - **Windows/Linux**: `Ctrl+Shift+P`
     - **Mac**: `⇧⌘P` (Shift+Command+P)
   - Run `Python: Create Environment...` → `Venv` → select your Python interpreter
   - **Alternative (if VS Code doesn't prompt)**: In the integrated terminal, run:
     ```bash
     # Windows
     py -m venv .venv
     .\.venv\Scripts\activate
     
     # macOS/Linux
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Start the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Verify setup**:
   - Open `http://127.0.0.1:8000` in your browser
   - You should see the Copilot Training Demo homepage

---

## Lab 1: Security Vulnerability Fix (Basic Chat Usage)

**Focus**: Learning to use Copilot Chat for code analysis and fixes

### Objective
Use GitHub Copilot Chat to identify and fix a SQL injection vulnerability, demonstrating how AI can help with security code reviews.

**📖 Background Reading**: For detailed information about SQL injection vulnerabilities, see `vulnerabilities/sql_injection/SQL_Injection_Lab.md`

### Step 1: Explore the Vulnerability
1. Open your browser and test these URLs:
   - Normal: `http://127.0.0.1:8000/vulnerable/users/admin`
   - Malicious: `http://127.0.0.1:8000/vulnerable/users/admin%27%20OR%20%271%27%3D%271`
   - Compare: `http://127.0.0.1:8000/vulnerable/users` (see all users)

2. **Understanding the Attack**: The malicious URL contains `admin' OR '1'='1` (URL-encoded above). This manipulates the SQL query from:
   ```sql
   SELECT * FROM users WHERE username = 'admin'
   ```
   Into:
   ```sql
   SELECT * FROM users WHERE username = 'admin' OR '1'='1'
   ```
   Since `'1'='1'` is always true, the query returns all users instead of just "admin", bypassing the intended access control.

3. Notice how the malicious URL returns all users instead of just "admin"

### Step 2: Use Copilot to Identify the Issue
1. Open `vulnerabilities/sql_injection/vulnerable_routes.py`
2. Find the `get_user_by_username_vulnerable()` function
3. Select the function and open Copilot Chat:
   - **Windows/Linux**: `Ctrl+Shift+I` or `Ctrl+I`
   - **Mac**: `⌃⇧I` (Control+Shift+I) or `⌘I` (Command+I)
4. Ask Copilot:
   ```
   Review the get_user_by_username_vulnerable function for security vulnerabilities. What's wrong with this SQL query construction?
   ```

### Step 3: Generate the Fix
1. Select the entire vulnerable function
2. In Copilot Chat, use this command:
   ```
   Fix this function to prevent SQL injection by using parameterized queries. Keep the same route and behavior, only fix the security issues. Add input validation (check for empty/null usernames and reasonable length limits). Use secure error handling that doesn't expose database details to users.
   ```
3. Review the suggested changes and apply them

### Step 4: Verify the Fix
1. Save the file and restart the server if needed
2. Test the malicious URL again: `http://127.0.0.1:8000/vulnerable/users/admin%27%20OR%20%271%27%3D%271`
3. **Success looks like**: The endpoint now returns a http error or validation error instead of exposing all users

### 🎓 Key Takeaways
- Copilot can identify common security vulnerabilities
- Specific, detailed prompts yield better results
- Always verify and understand AI-generated fixes
- Parameterized queries prevent SQL injection

**📖 Detailed Guide**: See `vulnerabilities/sql_injection/SQL_Injection_Lab.md` for complete documentation.

---

## Lab 2: Dark Mode Transformation (Prompt File Execution)

**Focus**: Using structured prompt files for complex changes

### Objective
Execute a pre-built prompt file to transform the entire application to dark mode, demonstrating how prompt files can orchestrate large-scale changes.

### Step 1: Examine the Current UI
1. Open `http://127.0.0.1:8000` in your browser
2. Note the current light theme styling
3. Take a screenshot or mental note for comparison

### Step 2: Review the Prompt File
1. Open `.github/prompts/dark-mode.prompt.md`
2. Review the YAML front matter:
   - `mode: agent`
   - `model: Claude Sonnet 4`
   - `description: Enhance the FastAPI training app with an accessible dark theme`
3. Read through the mission and objectives

### Step 3: Execute the Prompt File
1. With `dark-mode.prompt.md` open in VS Code
2. Open the Command Palette:
   - **Windows/Linux**: `Ctrl+Shift+P`
   - **Mac**: `⇧⌘P` (Shift+Command+P)
3. Run the command: "Run Prompt"
4. Wait for Copilot to analyze and modify the files
5. Review the changes in:
   - `app/static/style.css`
   - `app/templates/index.html` (if modified)
   - `app/static/script.js` (if modified)

### Step 4: See the Results
1. Refresh `http://127.0.0.1:8000`
2. **Success looks like**: The website now has a dark theme with good contrast and readable text
3. Test interactive elements (buttons, hover states)
4. Verify accessibility (keyboard navigation, contrast)

### 🎓 Key Takeaways
- Prompt files enable complex, multi-file changes
- YAML front matter provides structure and constraints
- Agent mode allows autonomous file modification
- Good prompts include specific objectives and constraints

---

## Lab 3: Custom Prompt File Creation (Advanced)

**Focus**: Creating original prompt files for custom requirements

### Objective
Design, create, and execute your own prompt file to implement a novel feature or improvement to the training application.

### Step 1: Brainstorm Your Enhancement
Use Copilot Chat to generate ideas:
```
I have a FastAPI training application with HTML/CSS/JS frontend. Suggest 5 creative enhancements I could implement to improve the user experience or add useful features. Consider accessibility, interactivity, and educational value.
```

**Example Ideas** (choose one or create your own):
- Add a responsive navigation menu with smooth animations
- Implement a code snippet showcase with copy-to-clipboard functionality
- Create an interactive tutorial overlay with guided tooltips
- Add a feedback form with local storage persistence
- Build a progress tracker for completed lab exercises
- Implement keyboard shortcuts for common actions
- Add a theme switcher (light/dark/auto)
- Create animated loading states and micro-interactions

### Step 2: Plan Your Implementation
1. Choose your enhancement idea
2. Ask Copilot to help plan the implementation:
   ```
   Help me plan the implementation of [YOUR IDEA]. Break this down into:
   1. Required file changes
   2. New functionality needed
   3. Potential challenges
   4. Testing approach
   5. Success criteria
   ```

### Step 3: Create Your Prompt File
1. Create a new file: `.github/prompts/[your-feature-name].prompt.md`
2. Use this template structure:

```markdown
---
mode: agent
model: Claude Sonnet 4
description: [One sentence describing your enhancement]
---
## Mission

[Detailed description of what you want to accomplish]

## Objectives

- [Specific goal 1]
- [Specific goal 2]
- [Specific goal 3]

## Constraints

- [Important limitation 1]
- [Important limitation 2]
- [Important limitation 3]

## Deliverables

- [Expected output 1]
- [Expected output 2]
- [Expected output 3]
```

### Step 4: Refine Your Prompt
Ask Copilot to review your prompt file:
```
Review this prompt file for clarity, completeness, and feasibility. Suggest improvements to make it more effective for an AI agent to execute.
```

### Step 5: Execute and Iterate
1. Run your prompt file using "Run Prompt" command
2. Review the generated changes
3. **Success looks like**: Your chosen feature is implemented and works as expected
4. Test the implementation thoroughly
5. If needed, refine your prompt and run again

### Step 6: Document Your Work
1. Update the main README.md with a brief description of your new feature
2. Add your prompt file to the `.github/prompts/` collection
3. **Success looks like**: Your feature works reliably and is properly documented
4. Test the feature thoroughly and note any issues

### 🎓 Key Takeaways
- Effective prompts balance specificity with creative freedom
- Iterative refinement often improves results
- Clear constraints prevent scope creep
- Good documentation makes prompts reusable

---

## 🏆 Workshop Completion

Congratulations! You've completed the GitHub Copilot Training Lab. You should now understand:

### ✅ Skills Mastered
- **Chat Commands**: Using Copilot for targeted code analysis and fixes
- **Prompt Execution**: Running structured prompt files for complex changes
- **Prompt Creation**: Designing custom prompts for novel requirements
- **Best Practices**: Effective prompting strategies and verification techniques

### 🚀 Next Steps
1. **Explore More**: Try the other prompt files in `.github/prompts/`
2. **Create More**: Build additional prompt files for your specific needs
3. **Share Knowledge**: Document your learnings in `.github/copilot-instructions.md`
4. **Apply Skills**: Use these techniques in your real development projects

### 📚 Additional Resources
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- Project-specific guides in the `vulnerabilities/` folder

---

## 🛟 Troubleshooting

### Setup Issues

**Virtual environment not activating?**
- **VS Code**: Check the Python interpreter in the bottom status bar - it should show `.venv`
- **Terminal**: You should see `(.venv)` at the start of your command prompt
- **Fix**: Try `source .venv/bin/activate` (macOS/Linux) or `.\.venv\Scripts\activate` (Windows)

**Dependencies won't install?**
- Ensure you're in the virtual environment (see above)
- Try: `pip install --upgrade pip` first
- Check Python version: `python --version` (should be 3.8+)

**FastAPI won't start?**
- Ensure you're in the project root directory
- Check that all dependencies installed: `pip list | grep fastapi`
- Try: `python -m uvicorn app.main:app --reload`

**Can't access the website?**
- Verify the server is running (look for "Uvicorn running on http://127.0.0.1:8000")
- Try accessing `http://localhost:8000` instead
- Check firewall settings

### Copilot Issues

**Copilot Chat not responding?**
- Check your GitHub Copilot subscription status
- Reload VS Code window:
  - **Windows/Linux**: `Ctrl+Shift+P` → "Developer: Reload Window"
  - **Mac**: `⇧⌘P` (Shift+Command+P) → "Developer: Reload Window"
- Verify internet connection
- Sign out and back into GitHub in VS Code

**Prompt files not executing?**
- Ensure proper YAML front matter format (three dashes before and after)
- Check for syntax errors in the markdown
- Try with a simpler prompt first
- Verify the file has `.prompt.md` extension

**Changes not taking effect?**
- Save all files before testing:
  - **Windows/Linux**: `Ctrl+S`
  - **Mac**: `⌘S` (Command+S)
- Restart the FastAPI server:
  - **Windows/Linux/Mac**: `Ctrl+C` in terminal, then re-run `uvicorn`
- Clear browser cache for CSS/JS changes:
  - **Windows/Linux**: `Ctrl+F5` or `Ctrl+Shift+R`
  - **Mac**: `⌘⇧R` (Command+Shift+R)
- Check browser developer console for errors

### Getting Help

**Need help with ideas for Lab 3?**
- Review existing prompts in `.github/prompts/` for inspiration
- Ask Copilot Chat: "Suggest 5 improvements for a FastAPI training app"
- Check the project issues or discussions for community ideas

**Still stuck?**
- Review the detailed guides in `vulnerabilities/sql_injection/` and `README.md`
- Check that all prerequisites are properly installed
- Ensure GitHub Copilot extension is active and authenticated