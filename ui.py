from tkinter import *
from tkinter import messagebox
from login import Login
from main_menu import MainMenu
from student import StudentInfo
from add_student import *
from search_student import SearchStudent
from PIL import Image, ImageTk



class UI:
    def __init__(self):
        self.win = Tk()
        self.win.attributes('-alpha', 1)
        self.win.title("Student Management System")
        self.win.geometry("1024x768+450+150")
        self.main_menu = None
        self.login_screen()
        self.win.overrideredirect(False)

    def login_screen(self):
        for widget in self.win.winfo_children():
            widget.destroy()
        #frames
        left_frame = Frame(self.win, width=100, bg="#a47864")
        right_frame = Frame(self.win, bg="white")
        left_frame.pack(side="left", fill="x", expand=True)
        right_frame.pack(side="right", fill="x", expand=True)
        Label(left_frame, text="Login", font=("Arial", 36), bg="lightgray").pack(anchor="center", pady=300)
        right_inner_frame = Frame(right_frame)
        right_inner_frame.pack(expand=True, fill="x")
        Label(right_inner_frame, text="Enter Your Student ID", font=("Gothic Century", 32)).pack(pady=30, padx=10)
        self.student_id_entry = Entry(right_inner_frame, font=("Arial", 25), width=20, justify="center")
        self.student_id_entry.pack(pady=10, padx=5)
        Button(right_inner_frame,text="Login",font=("Arial", 14),command=self.authenticate,width=10,bg="#4CAF50",fg="white").pack(pady=10, anchor="c", padx=40)
        Button(right_inner_frame,text="Exit",font=("Arial", 14),command=self.win.quit,width=10,bg="#4CAF50",fg="white",).pack(pady=10, anchor="c", padx=40)

    def authenticate(self):
        login = Login()
        student_id = self.student_id_entry.get().strip()
        if not student_id:
            messagebox.showerror("Error", "Please enter your Student ID.")
            return
        if login.username == student_id:
            self.main_menu_screen()
        else:
            messagebox.showerror("Error", "Invalid Student ID.")


    def main_menu_screen(self):
        for widget in self.win.winfo_children():
            widget.destroy()
        self.main_menu = MainMenu()
        left_frame = Frame(self.win, width=500, bg="lightgray")
        right_frame = Frame(self.win, bg="darkgray")
        left_frame.pack(side="left", fill="both")
        right_frame.pack(side="right", expand=True, fill="both")
        Label(left_frame, text="Menu", font=("Arial", 16), bg="lightgray").pack(pady=10)
    
        buttons = [
            ("View Your Information", self.view_your_info),
            ("Search for a Student", self.view_other_students),
            ("Register a New Student", lambda: self.register_new_student(right_frame)),
            ("Print All Students", self.print_all_students),
            ("Exit", self.confirm_exit),
        ]

        for text, command in buttons:
            Button(left_frame, text=text, font=("Arial", 12), command=command, width=40).pack(pady=5)
            self.output_screen = right_frame
            self.update_output_screen("Welcome to the Main Menu! Please select an option from the left.")

    def confirm_exit(self):
        response = messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?")
        if response: 
            self.login_screen() 

    def update_output_screen(self, content):
        for widget in self.output_screen.winfo_children():
            widget.destroy()
        text_widget = Text(self.output_screen, wrap="word", font=("Arial", 12), bg="darkgrey", fg="black", padx=10, pady=10)
        text_widget.insert("1.0", content)  
        text_widget.tag_configure("left", justify="left")
        text_widget.tag_add("left", "1.0", "end")
        text_widget.configure(state="disabled")  
        text_widget.pack(expand=True, fill="both")


    def view_your_info(self):
        if hasattr(self.main_menu, 'username'):
            content = f"User Information\n\n{self.main_menu.username},\n{self.main_menu.email},\n{self.main_menu.age}"
        else:
            content = "No user information available."
        self.update_output_screen(content)

    def view_other_students(self):
        def search_student():
            keyword = search_entry.get().strip()
            if not keyword:
                messagebox.showerror("Error", "Please enter a Student ID.")
                return
            result = SearchStudent.search_student(self.main_menu.add_student_obj.allstudents, keyword)
            self.update_output_screen(f"Search Result\n{result}")
        for widget in self.output_screen.winfo_children():
            widget.destroy()
        Label(self.output_screen, text="Search for a Student", font=("Arial", 24)).pack(pady=10)
        Label(self.output_screen, text="Enter Student ID", font=("Arial", 16)).pack(pady=5)
        search_entry = Entry(self.output_screen, font=("Arial", 16), justify="center")
        search_entry.pack(pady=5)
        Button(self.output_screen, text="Search", font=("Arial", 16), command=search_student).pack(pady=10)

    def register_new_student(self, parent_frame):
        for widget in parent_frame.winfo_children():
            widget.destroy()
        Label(parent_frame, text="Register New Student", font=("Arial", 24)).pack(pady=10)
        Label(parent_frame, text="Name", font=("Arial", 16)).pack(pady=5)
        name_entry = Entry(parent_frame, font=("Arial", 16))
        name_entry.pack(pady=5)
        Label(parent_frame, text="Age", font=("Arial", 16)).pack(pady=5)
        age_entry = Entry(parent_frame, font=("Arial", 16))
        age_entry.pack(pady=5)
        Label(parent_frame, text="Student ID", font=("Arial", 16)).pack(pady=5)
        id_entry = Entry(parent_frame, font=("Arial", 14))
        id_entry.pack(pady=5)
        Label(parent_frame, text="Email", font=("Arial", 16)).pack(pady=5)
        email_entry = Entry(parent_frame, font=("Arial", 16))
        email_entry.pack(pady=5)

        Label(parent_frame, text="Phone", font=("Arial", 16)).pack(pady=5)
        phone_entry = Entry(parent_frame, font=("Arial", 16))
        phone_entry.pack(pady=5)

        def save_student():
            name = name_entry.get().strip()
            age = age_entry.get().strip()
            student_id = id_entry.get().strip()
            email = email_entry.get().strip()
            phone = phone_entry.get().strip()

            if not name or not age or not student_id:
                messagebox.showerror("Error", "Name, Age, and Student ID are required.")
                return

            try:
                for student in self.main_menu.add_student_obj.allstudents:
                    if student.get_id_no() == student_id:
                        messagebox.showerror("Error", "Student ID already exists.")
                        return

                age = int(age)
                new_student = StudentInfo(name, age, student_id, email, phone)
                self.main_menu.add_student_obj.add_student(new_student)
                self.main_menu.add_student_obj.write_students_to_file()
                messagebox.showinfo("Success", "Student registered successfully!")
                self.update_output_screen("Student registered successfully!")
            except ValueError:
                messagebox.showerror("Error", "Invalid age. Please enter a valid integer.")

        Button(parent_frame, text="Register", font=("Arial", 16), command=save_student).pack(pady=10)

    def print_all_students(self):
        students = "\n".join(str(student) for student in self.main_menu.add_student_obj.allstudents)
        self.update_output_screen(f"=======All Students=======\n\n{students}\n")

    def run(self):
        self.win.mainloop()