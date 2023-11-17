from product import product
from datetime import datetime

class customer(product):
    customer_details={"aswin@gmail.com":["Aswin","12345"]}
    cart={}
    order_details={}
    def customer_operations(self,email):
        print()
        print("1. Purchase Product")
        print("2. Edit purchase list")
        print("3. View Avaible Products")
        print("4. View cart")
        print("5. Order")
        print("6. Purchase History")
        print("7. Logout")
        n=input("Enter Operation: ")
        if n=="1":
            print()
            print(self.product)
            while(True):
                print()
                product=input("Enter product name to purchase: ")
                quantity=int(input("Enter Quantity: "))
                if product in self.cart:
                    self.cart[product]+=quantity
                elif product not in self.cart:
                    self.cart[product]=quantity
                self.product[product]=self.product[product]-quantity
                print()
                ans=input("Do you want to continue? (yes/no): ")
                if ans=="no":
                    break
                elif ans=="yes":
                    continue
                else:
                    print("pls enter yes or no")
                    continue
            self.customer_operations(email)
            
        elif n=="2":
            print()
            print(self.cart)
            print()
            product_name=input("Enter product to removw from cart: ")
            quantity=int(input("Enter Quantity to remove: "))
            if product_name not in self.cart:
                print("Enter correct product name")
            
            elif product_name in self.cart:
                del self.cart[product_name]
                self.product[product_name]=self.product[product_name]+quantity
                print("Product removed from cart sucessfully")
            self.customer_operations(email)

        elif n=="3":
            print()
            print(self.product)
            self.customer_operations(email)

        elif n=="4":
            print()
            print("Your cart: ",self.cart)
            self.customer_operations(email)

        elif n=="5":
            print()
            print(self.cart)
            print()
            print("1. Check out")
            print("2. Continue Shopping")
            n=int(input("Check out or continue purchase: "))
            if n=="1":
                now=datetime.now()
                dt_string=now.strftime("%d/%m/%Y %H:%M:%S")
                self.order_details[dt_string]=(self.cart)
                print("Thank for Shoping")
                print()
            elif n=="2":
                self.customer_operations(email)
            self.customer_operations(email)

        elif n=="6":
            print()
            print(self.order_details)
            print()
            self.customer_operations(email)
        elif n=="7":
            print()
            self.start()
        else:
            print()
            print("Enter correct operation")
            self.customer_operations(email)