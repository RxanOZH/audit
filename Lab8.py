import json

class Product:
    def __init__(self, product_id, product_name, product_price, product_inventory):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_inventory = product_inventory

    def display(self):
        print(f"ID: {self.product_id}|Name: {self.product_name}|Price: {self.product_price}|Stocks: {self.product_inventory}")

    def update_stock(self, new_stock):
        self.product_inventory += new_stock

class Inventory:
    def __init__(self):
        self.products = []

    def display_all(self):
        if not self.products:
            print("Inventory is empty.")
            return
        
        for product in self.products:
            product.display()

    def add_product(self, product):
        self.products.append(product)

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

def main():
    user_input = 0
    product_id = 0
    product_name = ""
    product_price = 0.0
    product_inventory = 0
    inventory = Inventory()
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



while True:
    main() 




    


