import register_student
def display_all_students():
    if not register_student.student_registration:
        print("There is no students registered currently.")
    else:
        print("%20s%20s%30s%25s" % ("Student Name", "Student ID", "Email", "Program Enrolled"))
        for student_id, details in register_student.student_registration.items():
            name = details['name']
            email = details['email']
            program_enrolled = details['program enrolled']
            print("%20s%20s%30s%25s" % (name, student_id, email, program_enrolled))