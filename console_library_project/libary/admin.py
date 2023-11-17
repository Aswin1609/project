from member import member
from book import book

class admin(member,book):
    admin_details={"admin@gmail.com":["Aswin","1234"]}
#MANAGE MEMBER DETAILS
    def add_member(self):
        print("1. Add new member")
        print("2. Delete existing member")
        print("3. View Members")
        print("4. Back to admin panel")
        n=input("Enter Operation: ")
        if n=="1":
            print()
            name = input("Enter the new members name : ")
            email=input("Enter the new members email id : ")
            password=input("Enter the new members password : ")

            if email not in self.member_details:
                self.member_details[email]=[name,password,1500]
                self.books_taken[email]=[]
                print()
                print ("Member added successfully")

            elif email in self.member_details:
                print()
                print("Member Email already Exsist")
                print("---Details---")
                print("Name : ", self.member_details[email][0])
                print("Email : ",email)
            self.add_member()

        elif n=="2":
            email=input("Enter the exsiting member email id to delete: ")
            if email in self.member_details:
                del self.member_details[email]
                print()
                print("Email id deleted sucessfully")
            else:
                print("Email not found in database")
            self.add_member()

        elif n=="3":
            print()
            for key, value in self.member_details.items():
                print("Email- ",key,"--",value)
            print()
            self.add_member()

        elif n=="4":
            print()
            print("Admin Panel")
            print()
            self.admin_operations()

        else:
            print()
            print("Enter correct value")
            print()
            self.add_member()

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
            if email in self.member_details:
                del self.member_details[email]
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
    def manage_books(self):
        print("1. Add Book")
        print("2. Delete Book")
        print("3. View avabile Book")
        print("4. View taken books")
        print("5. Back to Admin panel")
        n=input("Enter operation: ")
        if n=="1":
            print()
            title=input("Enter book Title: ")
            count=int(input("Enter book count: "))
            if title not in self.books:
                self.books[title]=count
                print()
                print(title,"Book added sucessfully")
                self.manage_books()
            elif title in self.books:
                print()
                self.books[title]+=count
                self.manage_books()
            else:
                print()
                print("Book not found")
                self.manage_books()
                
        elif n=="2":
            print()
            title=input("Enter book Title: ")
            if title in self.books:
                del self.books[title]
                print()
                print(title,"Book deleted sucessfully")
                self.manage_books()
            else:
                print()
                print("Book not found")
                self.manage_books()
        elif n=="3":
            print()
            print(sorted(self.books.items(), key=lambda x: x[1], reverse=True))
            print()
            self.manage_books()

        elif n=="4":
            print()
            print(self.books_taken)
            self.manage_books()
        
        elif n=="5":
            print()
            print("Admin Panel")
            print()
            self.admin_operations()
        else:
            print()
            print("Enter correct value")
            print()
            self.manage_books()


#ADMIN OPERATIONS
    def admin_operations(self):
        print("1. Add and manage member details")
        print("2. Add and manage admin details")
        print("3. Add and manage book details")
        print("4. Logout")
        n=input("Enter operations : ")
        if n=="1":
            print()
            self.add_member()
        elif n=="2":
            print()
            self.add_admin()
        elif n=="3":
            print()
            self.manage_books()
        elif n=="4":
            print()
            self.start()
        else:
            print()
            print("Enter correct value")
            print()
            self.admin_operations()