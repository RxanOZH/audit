import json
import os
"""
_____________________________________
Product                              |   <-- Class Name
_____________________________________|
- __product_id: String               |    
- __name: String                     |   <-- Attributes
- __price: float                     |
- __stock: int                       |
_____________________________________|            |
+ update_stock(quantity : int): void |   <-- Methods
+ display(): void        |
+ to_dict(): dict                    |
_____________________________________|
"""

class Product:
    def __init__(self, product_id, product_name, product_price, product_inventory):
        self.__product_id = product_id
        self.__name = product_name
        self.__price = product_price
        self.__stock = product_inventory

    def display(self):
        print(f"ID: {self.__product_id}|Name: {self.__name}|Price: {self.__price}|Stocks: {self.__stock}")

    def update_stock(self, new_stock):
        self.__stock = new_stock

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }
"""
_____________________________________
Inventory                            |   <-- Class Name
_____________________________________|   
- __products: list[Products]         |   <-- Attributes
_____________________________________|
+ display_all()                      |
+ add_product(product)               |   <-- Methods
+ search_product(product_id: str)    |
+ to_list(): list[dict]              |
_____________________________________|
"""

class Inventory:
    def __init__(self):
        self.__products = []

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return
        
        for product in self.__products:
            product.display()

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.__product_id == product_id:
                return product
        return None
    def to_list(self):
        return [product.to_dict() for product in self.__products]

def save_inventory(inventory):
    with open("new_inventory.json", "w") as file:
        json.dump(inventory.to_list(), file, indent=4)

def main():
    user_input = 0
    product_id = 0
    product_name = ""
    product_price = 0.0
    product_inventory = 0
    inventory = Inventory()
    if os.path.exists("new_inventory.json"):
        try:
            with open("new_inventory.json", "r") as file:
                data = json.load(file)
                for items in data:
                    inventory.add_product(Product(items["id"], items["name"], items["price"], items["stock"]))
        except (FileNotFoundError, json.JSONDecodeError):
            # This catches BOTH a missing file and a completely empty/corrupted file
            print("Inventory file is empty or missing. Starting with an empty inventory.")

    print ("====================================================")
    print ("|           Inventory Management System            |")
    print ("====================================================\n")
    print ("------Menu------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Quit the program")
    print ("----------------\n\n")

    while user_input != 6:
        user_input = int(input("Enter your choice (1-6): "))

        if user_input == 1:
            print("\nCurrent Inventory:")
            inventory.display_all()
            pass

        if user_input == 2:
            print("\nAdd New Product")
            product_id = input("Enter product ID: ")
            product_name = input("Enter product name: ")
            product_price = float(input("Enter product price: "))
            product_inventory = int(input("Enter product stock: "))

            new_product = Product(product_id, product_name, product_price, product_inventory)
            inventory.add_product(new_product)
            print("\nProduct added successfully!")
            pass

        if user_input == 3:
            print("\nUpdate Stock")
            search_id = input("Enter the product ID to search: ")
            product = inventory.search_product(search_id)

            if product is None:
                print("Product not found.")
            else:
                print("\nProduct found:")
                product.display()
                new_stock = int(input("Enter the new stock quantity: "))
                product.update_stock(new_stock)
                print("\nStock updated successfully!")
        if user_input == 4:
            print("\nSearch Product")
            search_id = input("Enter the product ID to search: ")
            product = inventory.search_product(search_id)

            if product is None:
                print("Product not found.")
            else:
                print("\nProduct found:")
                product.display()
        if user_input == 5:
            print("\nSaving Inventory")
            save_inventory(inventory)
        if user_input == 6:
            print("\nSaving Inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
   

main() 
