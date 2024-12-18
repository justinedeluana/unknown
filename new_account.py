from student import StudentInfo

class NewAccount:
    def __init__(self):
        pass

    def create_new_account(self):
        print("\n=== Create New Account ===")
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return None
        try:
            age_input = input("Enter student age: ").strip()
            age = int(age_input)
            if age <= 0:
                print("Age must be 6 or higher.")
                return None
        except ValueError:
            print("Invalid age. Please enter a number.")
            return None
        id_no = input("Enter student ID number: ").strip()
        if not id_no:
            print("Student ID cannot be empty.")
            return None
        email = input("Enter student email: ").strip()
        phone = input("Enter student phone number: ").strip()

        student = StudentInfo(name, age, id_no, email, phone)
        return student