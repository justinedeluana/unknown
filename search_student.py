class SearchStudent:
    @staticmethod
    def search_student(student_list, keyword):
        for student in student_list:
            if student.get_id_no() == keyword:
                return f"Student Found!\n{student}"
        return "Student Not Found..."