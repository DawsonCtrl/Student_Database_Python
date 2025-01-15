import display_student
import register_student
import remove_student
import student_email
import student_id
from flask import render_template, request, Flask, g
import sqlite3
import os
import threading

# Database configuration
db_name = "studentsDB.db"

# Flask app setup
app = Flask(__name__, template_folder='templates')  # Use relative path for templates folder


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


@app.route('/')  # This links the function to the home route
def index():
    return render_template('index.html')


@app.route('/reg_student', methods=['GET', 'POST'])
def reg_student():
    register_student.register_student()
    return render_template('reg_student.html')


@app.route('/disp_student.html', methods=['GET', 'POST'])
def disp_student():
    connection = get_db_connection()

    # Execute query to fetch all students
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    # If no students are found, handle it gracefully
    if not students:
        error_message = "No students found."
        return render_template('disp_student.html', student=students, error=error_message)

    return render_template('disp_student.html', student=students)


@app.route('/search_email.html', methods=['GET', 'POST'])
def search_email():
    connection = get_db_connection()

    if request.method == 'POST':
        # Get the email from the form
        email = request.form['email']

        # Execute query to fetch student with the provided email
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE email = ?", (email,))
        students = cursor.fetchone()  # Use fetchone since you're searching for a single student

        # If no student is found, handle gracefully
        if students:
            return render_template('disp_student.html', student=[students])  # Pass as list to keep template consistent
        else:
            return render_template('search_email.html', error="Student does not exist.")

    return render_template('search_email.html')


@app.route('/search_by_id.html', methods=['GET', 'POST'])
def search_by_id():
    connection = get_db_connection()

    if request.method == 'POST':
        # Get the email from the form
        student_id = request.form['student_id']

        # Execute query to fetch student with the provided email
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        students = cursor.fetchone()  # Use fetchone since you're searching for a single student

        # If no student is found, handle gracefully
        if students:
            return render_template('disp_student.html', student=[students])  # Pass as list to keep template consistent
        else:
            return render_template('search_by_id.html', error="Student does not exist.")

    return render_template('search_by_id.html')


@app.route('/withdraw.html', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        connection = get_db_connection()
        cursor = connection.cursor()
        student_id = request.form['student_id']

        # Execute a query to fetch the student details based on the provided student_id
        cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
        student = cursor.fetchone()

        if student:
            # If the student exists, delete them from the database
            cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
            connection.commit()  # Commit the transaction to apply the changes
            return render_template('withdraw.html', student=[student])
        else:
            # If no matching student is found, display an error message
            return render_template('withdraw.html', error="Student does not exist.")

    # Render the form for the GET method
    return render_template('withdraw.html')


# Run Flask app and perform database check
def run_flask_app():
    app.run(debug=True, use_reloader=False)  # Running Flask app in the background thread


def db_check():
    if not os.path.exists(db_name):
        print(f"Database '{db_name}' does not exist. Creating the database and setting up tables.")
        connection = get_db_connection()  # Get a fresh connection
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE if NOT EXISTS students (
                           student_id VARCHAR(255) PRIMARY KEY, 
                           name VARCHAR(255) NOT NULL, 
                           email VARCHAR(255) UNIQUE NOT NULL, 
                           program_enrolled VARCHAR(255))''')
        connection.commit()
        connection.close()
        print("Database created successfully")
        flask_thread = threading.Thread(target=run_flask_app, daemon=True)
        flask_thread.start()
        main_menu()  # Proceed to the main menu after DB setup
    else:
        print(f"Database '{db_name}' exists. Ready to perform operations.")
        flask_thread = threading.Thread(target=run_flask_app, daemon=True)
        flask_thread.start()
        main_menu()


# Main menu logic for non-web operations
def main_menu():
    while True:
        print("\na) Type 'add' to register a student at the institution.")
        print("b) Type 'display' to display information of all registered students.")
        print("c) Type 'search_by_email' to search a student by email.")
        print("d) Type 'search_by_id' to search a student based on student ID.")
        print("e) Type 'withdraw' to withdraw a student from the registration list.")
        print("f) Type 'end' to end the application")

        choice = input("Enter your choice based on the options displayed: ").lower()

        if choice == 'add':
            register_student.register_student()
        elif choice == 'display':
            display_student.disp_student()
        elif choice == 'search_by_email':
            student_email.search_student_by_email()
        elif choice == 'search_by_id':
            student_id.search_student_by_id()
        elif choice == 'withdraw':
            remove_student.withdraw_student()
        elif choice == 'end':
            break
        else:
            print("Please enter a valid option.\n")


if __name__ == '__main__':
    db_check()  # Ensure DB is checked and created if necessary
