class AddStudent:
    def __init__(self):
        self.allstudents = []

    def add_student(self, student):
        """Adds a new student to the list."""
        self.allstudents.append(student)
        print(f"Added student {student.get_name()} to the list.")

    def write_students_to_file(self):
        """Writes all students to a file."""
        try:
            with open("students.txt", "w") as f:
                for student in self.allstudents:
                    f.write(f"{student.get_name()},{student.get_age()},{student.get_id_no()},{student.get_email()},{student.get_phone()}\n")
            print("Student data successfully written to file.")
        except Exception as e:
            print(f"Error writing to file: {str(e)}")
