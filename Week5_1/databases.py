import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            Name INTEGER PRIMARY KEY AUTOINCREMENT,
            Cousre TEXT NOT NULL,
            Class TEXT NOT NULL UNIQUE,
            Lecturer TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
