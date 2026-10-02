import json 

user_input = 0
product_id = 0
product_name = ""
product_price = 0.0
product_Inventory = 0
dict1 = []

def load_inventory():
    with open ("inventory.json", "r") as file:
        return json.load(file)

dict1 = load_inventory()

print("1. Display All Products")
print("2. Add Product")
print("3. Update Stock")
print("4. Search Product")
print("5. Save Inventory")
print("6. Quit the program")


while user_input != "6":
    user_input = input("Enter your choice (1-6): ")

    if user_input == "1":
        load_inventory()
        print("\nCurrent Inventory:")
        print("-------------------------------------------------------")
        for item in dict1:
            print(f"ID: {item['product_id']}, Name: {item['product_name']}, Price: {item['product_price']}, Inventory: {item['product_Inventory']}")
        print("-------------------------------------------------------")
        pass

    elif user_input == "2":
        # View all orders
        print("\nAdd New Product")
        product_id = input("Enter product ID: ")
        product_name = input("Enter product name: ")
        product_price = input("Enter product price: ")
        product_Inventory = input("Enter product inventory: ")
        dict1.append({"product_id": product_id, "product_name": product_name, "product_price": product_price, "product_Inventory": product_Inventory})
        #with open("inventory.json","w") as file:
            #json.dump(dict1,file)
        pass
    elif user_input == "3":
        print("\nUpdate Stock")
        search_id = input("Enter the product ID to search:")
        for item in dict1:
            if item["product_id"] == search_id:
                print("\nProduct found:")
                print(f"Name: {item['product_name']}\n Current Stock : {item['product_Inventory']}\n")
                new_inv = input("Enter the new stock quantity:")
                item["product_Inventory"] = new_inv
                print("\nStock updated successfully!")     
            else:
                print("Product not found.")
        pass
    elif user_input == "4":
        # Search for a product by ID
        print("\nSearch Product")
        search_id = input("Enter the product ID to search:\n")
        for item in dict1:
            if item["product_id"] == search_id:
                print("Product found")
                print("-------------------------------------------------------")
                print(f"ID: {item['product_id']}\nName: {item['product_name']}\nPrice: {item['product_price']}\nInventory: {item['product_Inventory']}")
                print("-------------------------------------------------------")
        else:
            print("Product not found.")
    elif user_input == "5":
        print("\nSaving inventory.......")
        print("Inventory saved successfully saved to inventory.json")
        with open("inventory.json", "w") as file:
            json.dump(dict1, file)
        pass
    elif user_input == "6":
        print("\nSaving Inventory before exit...")
        with open("inventory.json", "w") as file:
            json.dump(dict1, file)
        print("\nThank you for using the Inventory Management System!\n Program terminated")
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
    
    
