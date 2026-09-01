import sqlite3

def get_user_profile(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    cursor.execute(query)
    return cursor.fetchall()
