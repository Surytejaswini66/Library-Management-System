# borrow_model.py
from database.db import get_db

def add_borrow_record(user_id, book_id, borrow_date, due_date):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO borrow_records (user_id, book_id, borrow_date, due_date) VALUES (?, ?, ?, ?)",
        (user_id, book_id, borrow_date, due_date)
    )
    db.commit()

def get_borrowed_books(user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM borrow_records WHERE user_id = ?", (user_id,))
    return cursor.fetchall()
