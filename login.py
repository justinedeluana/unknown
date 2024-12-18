class Login:
    def __init__(self):
        self.username = "2023-2-00815"
        
    def authenticate(self):
        print("=== Login ===")
        attempts = 3  
        while attempts > 0:
            username_input = input("Student ID: ").strip()

            if username_input == self.username:
                print("Login successful!")
                return True
            else:
                attempts -= 1
                print(f"Login failed! You have {attempts} attempts left.")

        print("Too many failed attempts. Exiting.")
        return False