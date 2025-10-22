"""
SQL Injection Vulnerability Training Module

This module contains intentionally vulnerable code for educational purposes.
DO NOT use these patterns in production code.
"""
import sqlite3
from typing import List, Dict, Any

from fastapi import APIRouter, HTTPException

# Initialize router for vulnerable database endpoints
router = APIRouter(prefix="/vulnerable", tags=["sql-injection-training"])

# Initialize simple in-memory database for training purposes
def init_vulnerable_db():
    """Create a simple database with sample user data for vulnerability training."""
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            secret_data TEXT
        )
    """)
    
    # Insert sample data with some sensitive information
    sample_users = [
        (1, "admin", "admin@company.com", "admin", "admin_secret_key_12345"),
        (2, "alice", "alice@company.com", "user", "alice_personal_data"),
        (3, "bob", "bob@company.com", "user", "bob_financial_info"),
        (4, "charlie", "charlie@company.com", "manager", "charlie_hr_records"),
        (5, "eve", "eve@company.com", "user", "eve_private_notes"),
    ]
    
    cursor.executemany(
        "INSERT INTO users (id, username, email, role, secret_data) VALUES (?, ?, ?, ?, ?)", 
        sample_users
    )
    conn.commit()
    return conn

# Global database connection for demo purposes
vulnerable_db = init_vulnerable_db()


@router.get("/users/{username}")
async def get_user_by_username_vulnerable(username: str) -> Dict[str, Any]:
    """
    🚨 VULNERABLE ENDPOINT - Contains SQL injection vulnerability for training purposes.
    
    This endpoint demonstrates a common security flaw where user input is directly
    concatenated into SQL queries without proper sanitization or parameterization.
    
    EXERCISE: Use GitHub Copilot to identify and fix this vulnerability in-place.
    Goal: Fix the security issues while keeping the same route and functionality.
    
    Test with these payloads:
    - Normal: admin
    - Basic injection: admin' OR '1'='1  
    - Data extraction: admin' UNION SELECT id, username, secret_data, role FROM users--
    """
    cursor = vulnerable_db.cursor()
    
    # 🚨 VULNERABILITY: Direct string concatenation allows SQL injection
    query = f"SELECT id, username, email, role FROM users WHERE username = '{username}'"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        if results:
            # Return first result (or all results if injection succeeds)
            if len(results) == 1:
                result = results[0]
                return {
                    "id": result[0],
                    "username": result[1], 
                    "email": result[2],
                    "role": result[3]
                }
            else:
                # Multiple results indicate successful injection
                return {
                    "warning": "Multiple users found - possible SQL injection detected!",
                    "results": [
                        {
                            "id": row[0],
                            "username": row[1], 
                            "email": row[2],
                            "role": row[3]
                        }
                        for row in results
                    ]
                }
        else:
            raise HTTPException(status_code=404, detail="User not found")
            
    except sqlite3.Error as e:
        # Expose database errors (another security issue)
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/users")
async def list_all_users_safe() -> List[Dict[str, Any]]:
    """List all users - properly implemented for comparison and verification."""
    cursor = vulnerable_db.cursor()
    cursor.execute("SELECT id, username, email, role FROM users")
    results = cursor.fetchall()
    
    return [
        {
            "id": row[0],
            "username": row[1],
            "email": row[2], 
            "role": row[3]
        }
        for row in results
    ]