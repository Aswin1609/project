from customer import customer
from product import product

class admin(customer,product):
    admin_details={"admin@gmail.com":["Aswin","1234"]}
    def __init__(self,email,password):
        self.email=email
        self.password=password
        self.login(self.email,self.password)

#MANAGE CUSTOMER DETAILS
    def add_customer(self):
        print("1. Add new customer")
        print("2. Delete existing customer")
        print("3. View customer")
        print("4. Back to admin panel")
        n=input("Enter Operation: ")
        if n=="1":
            print()
            name = input("Enter the new customer name : ")
            email=input("Enter the new customer email id : ")
            password=input("Enter the new customer password : ")

            if email not in self.customer_details:
                self.customer_details[email]=[name,password]
                print()
                print ("Customer added successfully")

            elif email in self.customer_details:
                print()
                print("Customer Email already Exsist")
                print("---Details---")
                print("Name : ", self.customer_details[email][0])
                print("Email : ",email)
            self.add_customer()

        elif n=="2":
            email=input("Enter the exsiting customer email id to delete: ")
            if email in self.customer_details:
                del self.customer_details[email]
                print()
                print("Email id deleted sucessfully")
            else:
                print("Email not found in database")
            self.add_customer()

        elif n=="3":
            print()
            for key, value in self.customer_details.items():
                print("Email- ",key,"--",value)
            print()
            self.add_customer()

        elif n=="4":
            print()
            print("Admin Panel")
            print()
            self.admin_operations()

        else:
            print()
            print("Enter correct value")
            print()
            self.add_customer()

#MANAGE ADMIN DETAILS
    def add_admin(self):
        print("1. Add new admin")
        print("2. Delete existing admin")
        print("3. View Admin")
        print("4. Back to admin panel")
        n=input("Enter Operation: ")
        if n=="1":
            print()
            name = input("Enter the new admin name : ")
            email=input("Enter the new admin email id : ")
            password=input("Enter the new admin password : ")

            if email not in self.admin_details:
                self.admin_details[email]=[name,password]
                print()
                print ("Admin added successfully")
                self.add_admin()

            elif email in self.admin_details:
                print()
                print("Admin Email already Exsist")
                print("---Details---")
                print("Name : ", self.admin_details[email][0])
                print("Email : ",email)
                print()
                self.add_admin()

        elif n=="2":
            email=input("Enter the admin email id to delete: ")
            if email in self.admin_details:
                del self.admin_details[email]
                print()
                print("Email id deleted sucessfully")
                self.add_admin()
            else:
                print()
                print("Email not found in database")
                self.add_admin()

        elif n=="3":
            print()
            for key, value in self.admin_details.items():
                print("Email- ",key,"--",value)
            print()
            self.add_admin()
    
        elif n=="4":
            print()
            print("Admin Panel")
            print()
            self.admin_operations()
        
        else:
            print()
            print("Enter correct value")
            print()
            self.add_admin()
        

#MANAGE BOOKS
    def manage_product(self):
        print("1. Add Product")
        print("2. Delete Product")
        print("3. View avabile Product")
        print("4. Back to Admin panel")
        n=input("Enter operation: ")
        if n=="1":
            print()
            name=input("Enter book Title: ")
            count=int(input("Enter book count: "))
            if name not in self.product:
                self.product[name]=count
                print()
                print(name,"Product added sucessfully")
            else:
                print()
                print(name,"Product already exist")
            self.manage_product()
        elif n=="2":
            print()
            name=input("Enter book Title: ")
            if name in self.product:
                del self.product[name]
                print()
                print(name,"Product deleted sucessfully")
            else:
                print()
                print("Product not found")
            self.manage_product()
            
        elif n=="3":
            print()
            print(sorted(self.product.items(), key=lambda x: x[1], reverse=True))
            print()
            self.manage_product()
        
        elif n=="4":
            print()
            print("Admin Panel")
            print()
            self.admin_operations()
        else:
            print()
            print("Enter correct value")
            print()
            self.manage_product()


#ADMIN OPERATIONS
    def admin_operations(self):
        print("1. Add and manage customer details")
        print("2. Add and manage admin details")
        print("3. Add and manage product")
        print("4. Logout")
        n=input("Enter operations : ")
        if n=="1":
            print()
            self.add_customer()
        elif n=="2":
            print()
            self.add_admin()
        elif n=="3":
            print()
            self.manage_product()
        elif n=="4":
            print()
            self.start()
        else:
            print()
            print("Enter correct value")
            print()
            self.admin_operations()