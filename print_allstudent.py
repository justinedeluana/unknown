from student import StudentInfo

class PrintAllStudent:
    def __init__(self, students):
        self.students = students

    def print_all_students(self):
        if not self.students:
            print("No students to display.")
        else:
            for student in self.students:
                print(student)
                print("-" * 20)

    def read_students_from_file(self):
        try:
            with open("students.txt", "r") as f:
                students = []
                for line in f:
                    name, age, id_no, email, phone = line.strip().split(",")
                    student = StudentInfo(name, int(age), id_no, email, phone)
                    students.append(student)
                return students
        except FileNotFoundError:
            print("Error: File not found.")
            return []
