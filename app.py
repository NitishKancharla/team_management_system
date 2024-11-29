from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    due_date = data.get('due_date')
    status = data.get('status', 'Pending')

    if not title or not description or not due_date:
        return jsonify({"error": "Missing fields"}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (title, description, due_date, status) VALUES (?, ?, ?, ?)', 
                 (title, description, due_date, status))
    conn.commit()
    conn.close()

    return jsonify({"message": "Task created successfully!"}), 201


@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return jsonify([dict(task) for task in tasks])

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    due_date = data.get('due_date')
    status = data.get('status')

    if not title or not description or not due_date:
        return jsonify({"error": "Missing fields"}), 400

    conn = get_db_connection()
    conn.execute('UPDATE tasks SET title = ?, description = ?, due_date = ?, status = ? WHERE id = ?',
                 (title, description, due_date, status, id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Task updated successfully!"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
