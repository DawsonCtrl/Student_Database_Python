import display_student
import register_student
import remove_student
import student_email
import student_id
import sqlite3
import os

db_name = "studentDB.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()


def db_check():
    if os.path.exists(db_name):
        print(f"Database '{db_name}' exists. Ready to perform operations.")
        main_menu()
    else:
        print(f"Database '{db_name}' does not exist. Creating the database and setting up tables.")
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE if NOT EXISTS student_information (student_id VARCHAR(255) PRIMARY KEY, name VARCHAR(255) NOT NULL, 
        email VARCHAR(255) UNIQUE NOT NULL, program_enrolled VARCHAR(255))''')
        connection.commit()
        connection.close()
        print("Database created successfully")
        main_menu()


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
            display_student.display_all_students()
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db_check()
