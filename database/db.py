import sqlite3

DB_PATH = "library.db"
def get_db():
    conn = sqlite3.connect('library.db')  # Connect to your SQLite database
    conn.row_factory = sqlite3.Row  # This will allow accessing columns by name
    return conn
def connect_db():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    with connect_db() as conn:
        with open("database/schema.sql", "r") as schema_file:
            conn.executescript(schema_file.read())
            conn.commit()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
