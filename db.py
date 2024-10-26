import sqlite3


# Connect to SQLite database
def connect_db():
    return sqlite3.connect("study_sage.sqlite")


# CRUD Operations for 'chat' table
def create_chat(title):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat (title) VALUES (?)", (title,))
    chat_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return chat_id


def list_chats():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chat ORDER BY created_at DESC")
    chats = cursor.fetchall()
    conn.close()
    return chats


def read_chat(chat_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chat WHERE id = ?", (chat_id,))
    result = cursor.fetchone()
    conn.close()
    return result


def update_chat(chat_id, new_title):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE chat SET title = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
        (new_title, chat_id),
    )
    conn.commit()
    conn.close()


def delete_chat(chat_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chat WHERE id = ?", (chat_id,))
    conn.commit()
    conn.close()


def create_source(name, source_text, chat_id, source_type="document"):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sources (name, source_text, chat_id, type) VALUES (?, ?, ?, ?)",
        (name, source_text, chat_id, source_type),
    )
    conn.commit()
    conn.close()


def read_source(source_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sources WHERE id = ?", (source_id,))
    result = cursor.fetchone()
    conn.close()
    return result


def update_source(source_id, new_name, new_source_text):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE sources SET name = ?, source_text = ? WHERE id = ?",
        (new_name, new_source_text, source_id),
    )
    conn.commit()
    conn.close()


def list_sources(chat_id, source_type=None):
    conn = connect_db()
    cursor = conn.cursor()
    if source_type:
        cursor.execute(
            "SELECT * FROM sources WHERE chat_id = ? AND type = ?",
            (chat_id, source_type),
        )
    else:
        cursor.execute("SELECT * FROM sources WHERE chat_id = ?", (chat_id,))
    sources = cursor.fetchall()
    conn.close()
    return sources


def delete_source(source_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sources WHERE id = ?", (source_id,))
    conn.commit()
    conn.close()


# CRUD Operations for 'checklist' table
def create_checklist(name, completed, chat_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO checklist (name, completed, chat_id) VALUES (?, ?, ?)",
        (name, completed, chat_id),
    )
    conn.commit()
    conn.close()


def read_checklist(checklist_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM checklist WHERE id = ?", (checklist_id,))
    result = cursor.fetchone()
    conn.close()
    return result


def list_checklists(chat_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM checklist WHERE chat_id = ?", (chat_id,))
    checklists = cursor.fetchall()
    conn.close()
    return checklists


def update_checklist(checklist_id, new_name, new_completed):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE checklist SET name = ?, completed = ? WHERE id = ?",
        (new_name, new_completed, checklist_id),
    )
    conn.commit()
    conn.close()


def delete_checklist(checklist_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM checklist WHERE id = ?", (checklist_id,))
    conn.commit()
    conn.close()


# CRUD Operations for 'chat_response' table
def create_chat_response(response_text, chat_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat_response (response_text, chat_id) VALUES (?, ?)",
        (response_text, chat_id),
    )
    conn.commit()
    conn.close()


def read_chat_response(response_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chat_response WHERE id = ?", (response_id,))
    result = cursor.fetchone()
    conn.close()
    return result


def update_chat_response(response_id, new_response_text):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE chat_response SET response_text = ? WHERE id = ?",
        (new_response_text, response_id),
    )
    conn.commit()
    conn.close()


def list_chat_responses(chat_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chat_response WHERE chat_id = ?", (chat_id,))
    responses = cursor.fetchall()
    conn.close()
    return responses


def delete_chat_response(response_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chat_response WHERE id = ?", (response_id,))
    conn.commit()
    conn.close()


# CRUD Operations for 'messages' table
def create_message(chat_id, sender, content):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages (chat_id, sender, content) VALUES (?, ?, ?)",
        (chat_id, sender, content),
    )
    conn.commit()
    conn.close()


def get_messages(chat_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT sender, content FROM messages WHERE chat_id = ? ORDER BY timestamp ASC",
        (chat_id,),
    )
    messages = cursor.fetchall()
    conn.close()
    return messages


def delete_messages(chat_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM messages WHERE chat_id = ?", (chat_id,))
    conn.commit()
    conn.close()
