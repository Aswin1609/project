from admin import admin
from customer import customer


# LOGIN DETAILS
class super_market(admin,customer):
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
        elif email in self.customer_details and self.customer_details[email][1]==password:
            print()
            print("---Customer Logged In Successfully---")
            print("----------------------------")
            print("Welcome",self.customer_details[email][0])
            self.customer_operations(email)
        elif email in self.customer_details and self.customer_details[email][1]!=password:
            print("----------------------------")
            print("Invalid password pls provied valid password")
            self.start()
        else:
            print("----------------------------")
            print("Email not found please sign up first")
            self.start()

    def start(self):
        print("---Welcome to Zoho Super Market---")
        print()
        print("---------------------------")
        email=input("Enter your email id: ")
        password=input("Enter password: ")
        print("---------------------------")
        self.login(email,password)

libary_object=super_market()
libary_object.start()