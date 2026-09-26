print("===================")
print("smart inventory system")
print("===================")
inventory = 0 
failed_input =0 
delivery = 0 
order_number = 1
list1 = []
new_list = []

def get_valid_input(user_input):
    if user_input.isdigit(): 
        return int(user_input)
    elif user_input.lower() == "quit":
        return "quit"
    else:
        return None

def generator_report(inventory, failed_input):
    print(f"Total inventory: {inventory}")
    print(f"Failed input attempts: {failed_input}")
    
def save_invetory(user_input):
    with open("inventory.txt", "a") as file:
        file.write(f"{user_input}")
    



    
while True:
    
    user_input = input("enter product name:")
    if user_input.lower() == "quit":
        break
    else:
        list1.append(order_number)
        save_invetory(order_number)
        order_number += 1
        save_invetory(user_input)
        list1.append(user_input)
        user_input = input("enter inventory quantity:")
        user_input = get_valid_input(user_input)
        save_invetory(user_input)
        if user_input is not None:
            if user_input == "quit":
                break
            else:
                list1.append(user_input)


    print (list1)

    
 