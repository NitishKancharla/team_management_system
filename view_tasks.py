import sqlite3

def view_tasks():
    conn = sqlite3.connect('init_db.db')  # Replace with your DB file name
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    print("ID | Title         | Description     | Due Date   | Status")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<3} | {row[1]:<13} | {row[2]:<15} | {row[3]:<10} | {row[4]}")

    conn.close()

if __name__ == "__main__":
    view_tasks()
