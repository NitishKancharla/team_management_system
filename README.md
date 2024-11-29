Task Management System
A simple Task Management System that allows users to manage tasks by creating, viewing, updating, and deleting them. The system is built using Python with SQLite as the database.

Features
Create a task with a title, description, due date, and status.
View all tasks stored in the database.
Update existing tasks.
Delete tasks from the database.
Status management (toggle between Pending and Completed).

Technologies Used
Backend: Python 3, SQLite3
Database: SQLite
Frontend: using HTML, CSS, and JavaScript.

project/
init_db.py        # Script to initialize the database and create tables
view_tasks.py     # Script to view all tasks in the database
database.db       # SQLite database file (created after running init_db.py)
README.md         # Documentation for the project

#Setup Instructions
Prerequisites
Python 3 installed on your system.
Basic understanding of Python and SQLite.

Steps to Run
Clone the Repository

bash
Copy code
git clone <repository_url>
cd project
Initialize the Database Run the init_db.py script to create the database and the tasks table:
python init_db.py
Add Tasks You can add tasks either by extending the project or by using SQLite tools like DB Browser for SQLite.

View Tasks Run the view_tasks.py script to view all tasks in the database:
bash
Copy code
python view_tasks.py
Update/Delete Tasks Extend the project by adding more features such as updating and deleting tasks programmatically.

Future Improvements
Add a RESTful API using Flask or FastAPI.
Build a frontend interface using HTML, CSS, and JavaScript or React.
Add filtering options (e.g., show only Pending or Completed tasks).
Include error handling for database queries.
Contributing
Contributions are welcome! Feel free to fork the repository and create a pull request for any enhancements or bug fixes.
