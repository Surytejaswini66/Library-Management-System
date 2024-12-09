import sqlite3

def create_db():
    # Connect to the SQLite database (or create it)
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()

    # Create the books table if it does not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        published_date TEXT,
        quantity INTEGER NOT NULL DEFAULT 1
    )
    ''')

    # Inserting data into the books table with quantity (value should not be NULL)
    cursor.execute('''
    INSERT INTO books (title, author, published_date, quantity)
    VALUES
        ('Book Title 1', 'Author 1', '2024-01-01', 5),
        ('Book Title 2', 'Author 2', '2024-02-01', 3)
    ''')

    connection.commit()
    connection.close()

# Run the function to create the DB and insert data
create_db()
