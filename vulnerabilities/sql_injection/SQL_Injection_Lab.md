# SQL Injection Vulnerability Lab

## 🎯 Overview
This lab contains an intentionally vulnerable SQL injection endpoint to practice identifying and fixing security issues with GitHub Copilot.

**⚠️ WARNING**: This code is vulnerable by design for educational purposes only. Never use these patterns in production!

## � The Vulnerability

**Location**: `vulnerable_routes.py` - `get_user_by_username_vulnerable()` function

**Problem**: User input is directly concatenated into SQL queries:
```python
query = f"SELECT id, username, email, role FROM users WHERE username = '{username}'"
```

This allows attackers to inject malicious SQL code through the `username` parameter.

## 🔍 Testing the Exploit

Start the app with `uvicorn app.main:app --reload`, then test these URLs:

### 1. Normal Usage
```
http://127.0.0.1:8000/vulnerable/users/admin
```
Returns the admin user details.

### 2. Basic SQL Injection
```
http://127.0.0.1:8000/vulnerable/users/admin%27%20OR%20%271%27%3D%271
```
**Payload**: `admin' OR '1'='1`  
**Result**: Returns ALL users instead of just admin (bypasses authentication)

### 3. Data Extraction Attack
```
http://127.0.0.1:8000/vulnerable/users/admin%27%20UNION%20SELECT%20id%2C%20username%2C%20secret_data%2C%20role%20FROM%20users--
```
**Payload**: `admin' UNION SELECT id, username, secret_data, role FROM users--`  
**Result**: Exposes sensitive `secret_data` that should be hidden

## 🛠️ Fixing with GitHub Copilot

### Step 1: Identify the Issue
Open `vulnerable_routes.py` and ask Copilot:
```
Review the get_user_by_username_vulnerable function for security vulnerabilities. What's wrong with this SQL query construction?
```

### Step 2: Fix the Vulnerability In-Place
Select the vulnerable function and use this Copilot command:
```
Fix this function to prevent SQL injection by using parameterized queries. Keep the same route and behavior, only fix the security issues. Add input validation (check for empty/null usernames and reasonable length limits). Use secure error handling that doesn't expose database details to users.
```

### Step 3: Understand the Solution
Ask Copilot to explain the security improvements:
```
Explain why parameterized queries prevent SQL injection. What's the difference between string concatenation and using query parameters?
```

## ✅ Expected Secure Code

Copilot should transform the existing function to use parameterized queries (exact implementation may vary):
```python
@router.get("/users/{username}")
async def get_user_by_username_vulnerable(username: str):
    """Secure version using parameterized queries."""
    
    # Input validation (Copilot may implement differently)
    if not username or len(username.strip()) == 0:
        raise HTTPException(status_code=400, detail="Username required")
    
    if len(username) > 50:  # Reasonable length limit
        raise HTTPException(status_code=400, detail="Username too long")
    
    cursor = vulnerable_db.cursor()
    
    # ✅ SECURE: Parameterized query prevents injection
    query = "SELECT id, username, email, role FROM users WHERE username = ?"
    
    try:
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        
        if result:
            return {
                "id": result[0],
                "username": result[1], 
                "email": result[2],
                "role": result[3]
            }
        else:
            raise HTTPException(status_code=404, detail="User not found")
            
    except sqlite3.Error:
        # Don't expose database errors to users
        raise HTTPException(status_code=500, detail="Internal server error")
```

**Key improvements to look for in Copilot's solution:**
- Parameterized query with `?` placeholder
- Input validation before processing
- Generic error messages that don't reveal database structure

## 🔬 Verify the Fix

After applying the Copilot-generated fix, test the same endpoint:
```
http://127.0.0.1:8000/vulnerable/users/admin%27%20OR%20%271%27%3D%271
```
**Expected Result**: Should return a http error (not all users) - the exact message will depend on Copilot's implementation.

Use the `/vulnerable/users` endpoint to see what the complete user list looks like for comparison.

## 📚 Key Learning Points

1. **Never concatenate user input into SQL queries**
2. **Use parameterized queries (? placeholders)**
3. **Validate input before processing**
4. **Don't expose database errors to users**
5. **GitHub Copilot can identify and fix common security vulnerabilities**

## ✅ Success Criteria

You've completed the lab when:
- [ ] You understand why string concatenation is dangerous
- [ ] You can exploit the vulnerability with the provided payloads
- [ ] Copilot helps you identify the security issue
- [ ] You generate secure code using parameterized queries
- [ ] The fixed version blocks injection attempts