from database.db import connect_db

def add_book(title, author, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)",
        (title, author, quantity),
    )
    conn.commit()
    conn.close()
    return {"message": "Book added successfully."}
