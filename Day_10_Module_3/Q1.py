# wap  that has a class store which keeps a record 
# of code and price of each product display a menu of all products 
# to the user  and prompt them to enter the quantity of each item required and 
# finally geenrate a bill and display total amount
# class Store :
#     __itemcode=0
#     __price=0
#     def __init__(self):
#         print(" Welcome to the store ")
#         a=int(input("Select The Product:\n1 : Soap\n2 : Milk\n3 :Cloths\n4 : Free Product "))
#         if a==1:
#             __itemcode=1
#             __price=50
#         elif a==2:
#             __itemcode=2
#             __price=20
#         elif a==3:
#             __itemcode=3
#             __price=60
#         elif a==4:
#             __itemcode=4
#             __price=100
#         print(" Product : ")



# class Store:
#     __itemcode = 0
#     __price = 0
#     quantity = 0

#     def __init__(self):
#         print("Welcome to the store")
#         print("Select The Product:")
#         print("1: Soap\n2: Milk\n3: Cloths\n4: Free Product")
#         choice = int(input())
        
#         if choice == 1:
#             self.__itemcode = 1
#             self.__price = 50
#         elif choice == 2:
#             self.__itemcode = 2
#             self.__price = 20
#         elif choice == 3:
#             self.__itemcode = 3
#             self.__price = 60
#         elif choice == 4:
#             self.__itemcode = 4
#             self.__price = 100

#         self.quantity = int(input(f"Enter the quantity for Product {self.__itemcode}: "))

#     def generate_bill(self):
#         total_amount = self.__price * self.quantity
#         print("Product Code:", self.__itemcode)
#         print("Price per unit:", self.__price)
#         print("Quantity:", self.quantity)
#         print("Total Amount:", total_amount)


# if __name__ == "__main__":
#     store = Store()
#     store.generate_bill()









class Store:
    __itemCode = 0
    __price = 0
    __total = 0
    product = []
    quantity = []
    price = []

    def __init__(self):
        print("Welcome to ABC Store!")
        while True:
            a = int(input("Select a product:\n1.Soap\n2.Toothbrush\n3.Toothpaste\n4.Comb\n5.Book\n"))
            c = ("Soap", "Toothbrush", "Toothpaste", "Comb", "Book")
            
            if 1 <= a <= 5:
                self.__itemCode = a
                if a == 1:
                    self.__price = 50
                elif a == 2:
                    self.__price = 100
                elif a == 3:
                    self.__price = 200
                elif a == 4:
                    self.__price = 150
                elif a == 5:
                    self.__price = 500

                print("Product:", c[a - 1], "\nPrice:", self.__price)
                self.product.append(c[a - 1])
                self.price.append(self.__price)
                b = int(input("Enter the quantity: "))
                self.quantity.append(b)
                self.__total = self.__total + self.__price * b
                print("Total:", self.__total)
                d = input("Do you want to add more items? (y/n): ")
                if d.lower() == "n":
                    break
            else:
                print("Invalid option. Please select a valid product.")

        print("\t\tBill\n\nProduct\t\tPrice\t\tQuantity")
        for i in range(len(self.product)):
            print(self.product[i], "\t\t", self.price[i], "\t\t", self.quantity[i])
        print("Total:", self.__total)


obj = Store()
