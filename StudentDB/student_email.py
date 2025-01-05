import register_student

def search_student_by_email():
    email_to_search = input("\nEnter the email to search: ").lower()
    for student_id, student in register_student.student_registration.items():
        if student['email'] == email_to_search:
            print("%20s%20s%30s%25s" % ("Student Name", "Student ID", "Email", "Program Enrolled"))
            name = student['name']
            email = student['email']
            program_enrolled = student['program enrolled']
            print("%20s%20s%30s%25s" % (name, student_id, email, program_enrolled))