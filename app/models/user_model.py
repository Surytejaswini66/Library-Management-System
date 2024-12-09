# user_model.py
from database.db import get_db
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
def create_user(email, password, role):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users (email, password, role) VALUES (?, ?, ?)", 
        (email, password, role)
    )
    db.commit()

def get_user_by_email(email):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    return cursor.fetchone()
