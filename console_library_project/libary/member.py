from book import book

class member(book):
    member_details={"aswin@gmail.com":["Aswin","12345",1500]}
    def member_operations(self,email):
        print()
        print("1. Take Book")
        print("2. Return Book")
        print("3. View Avaible books")
        print("4. View taken book")
        print("5. Logout")
        n=input("Enter Operation: ")
        if n=="1":
            print()
            print(self.books)
            print()
            book_count=int(input("Enter the name of the book you want to take: "))
            for i in range(book_count):
                book_name = input("Enter the book want to take: ")
                if book_name in self.books and self.member_details[email][2]>=500:
                    self.books_taken[email].append(book_name)
                    self.books[book_name]=self.books[book_name]-1
                    print("Book taken successfully!")
            self.member_operations(email)
            
        elif n=="2":
            print()
            print(self.books_taken[email])
            print()
            book_name=input("Enter book name to retrun")
            if book_name not in self.books_taken[email]:
                print("You have not borrowed this book.")
            
            elif book_name in self.books_taken[email]:
                self.books_taken[email].remove(book_name)
                self.books[book_name]=self.books[book_name]+1
                print("Book returned sucessfully")
            self.member_operations(email)

        elif n=="3":
            print()
            print(self.books)

        elif n=="4":
            print()
            print("Books taken: ",self.books_taken[email])
            self.member_operations(email)

        elif n=="5":
            print()
            self.start()
        else:
            print()
            print("Enter correct operation")