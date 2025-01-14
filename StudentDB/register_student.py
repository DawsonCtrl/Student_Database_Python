from flask import render_template, request, redirect, url_for
from main import app  # Import the app instance directly from the main app

# Set up a connection to the SQLite database (if not already done in main.py)
import sqlite3

connection = sqlite3.connect("studentsDB.db", check_same_thread=False)
cursor = connection.cursor()


# Define the route for adding a student
@app.route('/register_student', methods=['GET', 'POST'])
def register_student():
    if request.method == 'POST':
        student_id = request.form['student_id'].lower()
        name = request.form['name']
        email = request.form['email'].lower()
        program_enrolled = request.form['program_enrolled']

        # Validate email and student ID
        if email.endswith("@humber.ca"):
            # Check if student already exists in the database
            cursor.execute("SELECT * FROM students WHERE student_id = ? OR email = ?", (student_id, email))
            existing_student = cursor.fetchone()

            if existing_student:
                return render_template('reg_student.html', error="Student ID or email already registered.")

            # Add the student to the database
            cursor.execute("INSERT INTO students (student_id, name, email, program_enrolled) VALUES (?, ?, ?, ?)",
                           (student_id, name, email, program_enrolled))
            connection.commit()

            return redirect(url_for('index'))  # Redirect to home page after registration
        else:
            return render_template('reg_student.html', error="Email must be from '@humber.ca'.")

    return render_template('reg_student.html')  # Render the form for GET request
