import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("study_sage.sqlite")
cursor = conn.cursor()

# Create 'chat' table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS chat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
"""
)

# Create 'sources' table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS sources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        source_text TEXT,
        chat_id INTEGER,
        FOREIGN KEY (chat_id) REFERENCES chat(id)
    )
"""
)

# Create 'checklist' table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS checklist (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        completed BOOLEAN DEFAULT FALSE,
        chat_id INTEGER,
        FOREIGN KEY (chat_id) REFERENCES chat(id)
    )
"""
)

# Create 'chat_response' table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS chat_response (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT,
        response_text TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        chat_id INTEGER,
        FOREIGN KEY (chat_id) REFERENCES chat(id)
    )
"""
)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Tables created successfully.")
