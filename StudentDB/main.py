"""Initialize dictionary"""
student_registration = {}

"""Function to add a student. Checks if the id and email exist, if not appends, if they do registration fails."""


def register_student():
    student_id = input("\nEnter student ID: ").lower()
    name = input("Enter student name: ")
    email = input("Enter student email: ").lower()
    program_enrolled = input("Enter program: ")

    if student_id not in student_registration and email.endswith("@humber.ca") and all(
            student['email'] != email for student in student_registration.values()):
        student_registration[student_id] = {'name': name, 'email': email, 'program enrolled': program_enrolled}
        print("Student registered successfully!\n")
    else:
        if student_id in student_registration and email in [student['email'] for student in
                                                            student_registration.values()]:
            print(f"Both the student ID: {student_id} and email: {email} are already registered. Registration failed.\n"
                  )
        elif student_id in student_registration:
            print(f"The student ID {student_id} is already registered. Registration failed.\n")
        elif email in [student['email'] for student in student_registration.values()]:
            print(f"The email: {email} is already registered. Registration failed.\n")
        elif not email.endswith("@humber.ca"):
            print(f"The email: {email} is not for the right institution. Registration failed.\n")


"""Function to display all information in the dictionary"""


def display_all_students():
    if not student_registration:
        print("There is no students registered currently.")
    else:
        print("%20s%20s%30s%25s" % ("Student Name", "Student ID", "Email", "Program Enrolled"))
        for student_id, details in student_registration.items():
            name = details['name']
            email = details['email']
            program_enrolled = details['program enrolled']
            print("%20s%20s%30s%25s" % (name, student_id, email, program_enrolled))


"""While loop for function choice"""
while True:
    print("\na) Type 'add' to register a student at the institution.")
    print("b) Type 'display' to display information of all registered students.")
    print("c) Type 'search_by_email' to search a student by email.")
    print("d) Type 'search_by_id' to search a student based on student ID.")
    print("e) Type 'withdraw' to withdraw a student from the registration list.")
    print("f) Type 'end' to end the application")

    choice = input("Enter your choice based on the options displayed: ").lower()

    if choice == 'add':
        register_student()
    elif choice == 'display':
        display_all_students()
    elif choice == 'search_by_email':
        search_student_by_email()
    elif choice == 'search_by_id':
        search_student_by_id()
    elif choice == 'withdraw':
        withdraw_student()
    elif choice == 'end':
        break
    else:
        print("Please enter a valid option.\n")
