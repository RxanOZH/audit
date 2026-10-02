import json 

user_input = 0
product_id = 0
product_name = ""
product_price = 0.0
product_Inventory = 0
Dictionary1 = {}





while user_input != "6":
    print("1. Add a new order")
    print("2. View all orders")
    print("3. Search for an order by order number")
    print("4. Update an order by order number")
    print("5. Delete an order by order number")
    print("6. Quit the program")

    user_input = input("Enter your choice (1-6): ")

    if user_input == "1":
        # Add a new order
        print("Current Inventory:")
        pass
    elif user_input == "2":
        # View all orders
        print("Add New Product Order:")
        product_id = input("Enter product ID: ")
        product_name = input("Enter product name: ")
        product_price = input("Enter product price: ")
        product_Inventory = input("Enter product inventory: ")
        list1.append({"product_id": product_id, "product_name": product_name, "product_price": product_price, "product_Inventory": product_Inventory})
        with open("inventory.json","w") as file:
            json.dump(list1,file)
        pass
    elif user_input == "3":
        list1[0][""]
        pass
    elif user_input == "4":
        # Update an order by order number
        pass
    elif user_input == "5":
        # Delete an order by order number
        pass
    elif user_input == "6":
        print("Exiting the program.")
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
    
    
