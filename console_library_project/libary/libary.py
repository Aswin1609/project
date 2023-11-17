from admin import admin
from member import member
# LOGIN DETAILS
class libary(admin,member):
    def __init__(self) -> None:
        pass

#LOGIN CREDENTIALS
    def login(self,email,password):
        if email in self.admin_details and self.admin_details[email][1]==password:
            print()
            print("---Admin Logged In Successfully---")
            print()
            print("Welcome Admin", self.admin_details[email][0])
            print()
            self.admin_operations()
        elif email in self.member_details and self.member_details[email][1]==password:
            print("----------------------------")
            print("Welcome",self.member_details[email][0])
            self.member_operations(email)
        elif email in self.member_details and self.member_details[email][1]!=password:
            print("----------------------------")
            print("Invalid password pls provied valid password")
            self.start()
        else:
            print("----------------------------")
            print("Email not found please sign up first")
            self.start()

    def start(self):
        print("---Welcome to Login page---")
        print()
        print("---------------------------")
        email=input("Enter your email id: ")
        password=input("Enter password: ")
        print("---------------------------")
        self.login(email,password)

libary_object=libary()
libary_object.start()