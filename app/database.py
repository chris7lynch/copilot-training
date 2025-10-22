"""
Database module with intentionally vulnerable SQL endpoints for security training.

This module contains deliberately insecure code for educational purposes.
DO NOT use these patterns in production code.
"""
import sqlite3
from typing import List, Dict, Any

from fastapi import APIRouter, HTTPException

# Initialize router for database-related endpoints
router = APIRouter(prefix="/api", tags=["database"])

# Initialize simple in-memory database for training purposes
def init_db():
    """Create a simple database with sample user data for vulnerability training."""
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    """)
    
    # Insert sample data
    sample_users = [
        (1, "admin", "admin@company.com", "admin"),
        (2, "alice", "alice@company.com", "user"),
        (3, "bob", "bob@company.com", "user"),
        (4, "charlie", "charlie@company.com", "manager"),
    ]
    
    cursor.executemany("INSERT INTO users (id, username, email, role) VALUES (?, ?, ?, ?)", sample_users)
    conn.commit()
    return conn

# Global database connection for demo purposes
db_conn = init_db()


@router.get("/users/{username}")
async def get_user_by_username(username: str) -> Dict[str, Any]:
    """
    VULNERABLE ENDPOINT - Contains SQL injection vulnerability for training purposes.
    
    This endpoint demonstrates a common security flaw where user input is directly
    concatenated into SQL queries without proper sanitization or parameterization.
    
    Try: /api/users/admin' OR '1'='1
    This will return all users instead of just the requested username.
    
    Exercise: Use GitHub Copilot to identify and fix this vulnerability.
    """
    cursor = db_conn.cursor()
    
    # VULNERABILITY: Direct string concatenation allows SQL injection
    query = f"SELECT id, username, email, role FROM users WHERE username = '{username}'"
    
    try:
        cursor.execute(query)
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
            
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/users")
async def list_all_users() -> List[Dict[str, Any]]:
    """List all users - for comparison with the vulnerable endpoint above."""
    cursor = db_conn.cursor()
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