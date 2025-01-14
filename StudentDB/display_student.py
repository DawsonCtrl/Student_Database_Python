from flask import render_template, g, Flask
import sqlite3

app = Flask(__name__, template_folder='templates')  # Use relative path for templates folder

db_name = "studentsDB.db"


# Function to get a database connection for each request
def get_db_connection():
    if 'g.db_connection' not in g:
        g.db_connection = sqlite3.connect(db_name)
        g.db_connection.row_factory = sqlite3.Row  # This allows column names to be accessed like dict keys
    return g.db_connection


@app.teardown_appcontext
def close_db_connection(error=None):
    """Close the database connection at the end of the request."""
    db_connection = getattr(g, 'g.db_connection', None)
    if db_connection is not None:
        db_connection.close()


def disp_student():
    connection = get_db_connection()

    # Execute query to fetch all students
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    # Debugging: Print the students to check what is being fetched
    print("Fetched students:", students)

    return render_template('disp_student.html', student=students)