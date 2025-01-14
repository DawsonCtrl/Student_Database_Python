import register_student
import sqlite3

connection = sqlite3.connect("studentsDB.db")
cursor = connection.cursor()


def withdraw_student():
    student_id = input("Enter the ID of the student you want to remove: ").lower()

    if student_id in register_student.student_registration:
        del register_student.student_registration[student_id]  # Remove the student
        cursor.execute("DELETE * FROM students WHERE student_id = %s", (student_id,))
        connection.commit()
        connection.close()
        print(f"Student with ID {student_id} has been removed.\n")
    else:
        print(f"Student with the ID {student_id} does not exist.\n")
