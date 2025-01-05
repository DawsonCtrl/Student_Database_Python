student_registration = {}

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