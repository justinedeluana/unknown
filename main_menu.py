from student import StudentInfo
from add_student import AddStudent
from search_student import SearchStudent
from print_allstudent import PrintAllStudent
from new_account import NewAccount
import os


class MainMenu:
    def __init__(self):
        self.add_student_obj = AddStudent()
        self.students = self.read_students_from_file()
        self.add_student_obj.allstudents.extend(self.students)
        self.username = f"Justine"
        self.email = f"2023-2-00815"
        self.age = f"20"

    def read_students_from_file(self):
        """Read students from the file."""
        try:
            file_path = "students.txt"

            # Create the file if it doesn't exist
            if not os.path.exists(file_path):
                open(file_path, 'w').close()

            with open(file_path, "r") as f:
                students = []
                for line in f:
                    name, age, id_no, email, phone = line.strip().split(",")
                    student = StudentInfo(name, int(age), id_no, email, phone)
                    students.append(student)
                return students

        except FileNotFoundError:
            print("Error: File not found. Creating a new file.")
            return []
        except ValueError as ve:
            print(f"Error parsing student data: {str(ve)}")
            return []
        except Exception as e:
            print(f"Error: {str(e)}")
            return []

    def display_menu(self):
        print(f"\nWelcome, {self.username}")
        print("Please choose from the following options:")
        print("1. View your information")
        print("2. View other student's information")
        print("3. Register a New Student")
        print("4. Print all students in the list")
        print("5. Exit")

    def handle_choice(self, choice):
        if choice == '1':
            self.view_student_info()
        elif choice == '2':
            self.view_other_student_info()
        elif choice == '3':
            self.register_new_student()
        elif choice == '4':
            self.print_all_students()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            return False
        else:
            print("Invalid choice. Please select a valid option.")
        return True

    def view_student_info(self):
        print("\n=== Student Information ===")
        print(f"Student Name: {self.username}")
        print("=========================")

    def view_other_student_info(self):
        keyword = input("Enter Student ID to view information: ").strip()
        if not keyword:
            print("Student ID cannot be empty.")
            return
        result = SearchStudent.search_student(self.add_student_obj.allstudents, keyword)
        print(result)

    def register_new_student(self):
        while True:
            print("\n=== Register New Student ===")
            new_account = NewAccount()
            student = new_account.create_new_account()
            if student:
                self.add_student_obj.add_student(student)
                self.add_student_obj.write_students_to_file()

            another = input("Do you want to add another student? (Y or N): ").strip().upper()
            if another == 'Y':
                continue
            elif another == 'N':
                print("Exiting student registration.")
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

    def print_all_students(self):
        printer = PrintAllStudent(self.add_student_obj.allstudents)
        printer.print_all_students()

    def run(self):
        running = True
        while running:
            self.display_menu()
            choice = input("\nYour choice: ").strip()
            running = self.handle_choice(choice)
