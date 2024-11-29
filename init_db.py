import sqlite3

def create_db():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Create the tasks table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('Pending', 'Completed'))
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Database and table initialized successfully!")

if __name__ == '__main__':
    create_db()
