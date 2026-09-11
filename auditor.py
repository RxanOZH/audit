print("===================")
print("smart inventory system")
print("===================")
inventory = 0 
failed_input =0 


while True:
    user_input = input("enter inventory quantity:")
    if user_input.isdigit():
        user_int =int(user_input)
        inventory += user_int
        if inventory > 500:
            print("Alert: Inventory overflow")
            break
    
    elif user_input.lower() == "quit":
        print(f"Total inventory: {inventory}")
        print(f"Failed input attempts: {failed_input}")
        break

    else:
        failed_input += 1
        print("Invalid input. Please enter a valid number.")





                