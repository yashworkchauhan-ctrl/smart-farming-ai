import sqlite3

def connect_db():
    return sqlite3.connect("smart_farming.db")


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        result TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_log(log_type, result):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO logs (type, result) VALUES (?, ?)", (log_type, result))

    conn.commit()
    conn.close()


def get_counts():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM logs WHERE type='crop'")
    crop = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE type='disease'")
    disease = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE type='weather'")
    weather = cursor.fetchone()[0]

    conn.close()

    return crop, disease, weather