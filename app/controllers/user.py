from database.db import connect_db

def borrow_book(user_id, book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT quantity FROM books WHERE id = ?", (book_id,)
    )
    book = cursor.fetchone()

    if book and book['quantity'] > 0:
        cursor.execute(
            "UPDATE books SET quantity = quantity - 1 WHERE id = ?",
            (book_id,)
        )
        cursor.execute(
            "INSERT INTO borrow_requests (user_id, book_id, start_date, end_date, status) VALUES (?, ?, DATE('now'), DATE('now', '+7 days'), 'pending')",
            (user_id, book_id),
        )
        conn.commit()
        conn.close()
        return {"message": "Borrow request submitted successfully."}
    else:
        conn.close()
        return {"message": "Book not available."}
