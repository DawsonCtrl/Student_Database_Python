import register_student
import sqlite3

connection = sqlite3.connect("studentsDB.db")
cursor = connection.cursor()


def search_student_by_id():
    id_to_search = input("\nEnter the student ID to search: ").lower()

    # Check if the ID exists in the student_registration dictionary
    if id_to_search in register_student.student_registration:
        student = register_student.student_registration[id_to_search]
        print("%20s%20s%30s%25s" % ("Student Name", "Student ID", "Email", "Program Enrolled"))
        name = student['name']
        email = student['email']
        program_enrolled = student['program enrolled']
        print("%20s%20s%30s%25s" % (name, id_to_search, email, program_enrolled))
        cursor.execute("SELECT * FROM students WHERE student_id = %s", id_to_search)
    else:
        print("Student with the given ID does not exist.\n")
