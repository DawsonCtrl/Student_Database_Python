import register_student, display_student, student_email, student_id, remove_student


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
    main_menu()