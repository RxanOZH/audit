print("===================")
print("smart inventory system")
print("===================")
order_number =1001
list1 = []
new_list = []

def get_valid_input(user_input):
    if user_input.isdigit(): 
        return int(user_input)
    elif user_input.lower() == "quit":
        return "quit"
    else:
        return None

def get_product_name(user_input):
    if user_input.lower() == "quit":
        return "quit"
    elif user_input.isdigit():
        print("Invalid input. Please enter a valid product name.")
    elif user_input == "":
       return None 
    else:
        return user_input
    
def save_inventory(list1):
    with open("inventory.txt", "a") as file:
        file.write(f"{list1}" + "\n")
    

    
while True:
    list1.clear()
    user_input = input("enter product name:")
    user_input=get_product_name(user_input)
    if user_input == "quit":
        print("this program quit")
        break
    else:
        product_name = user_input
        user_input = input("enter Quantity:")
        user_input = get_valid_input(user_input)
        if user_input is not None:
            if user_input == "quit":
             print("this program quit")
             break
            else:
                product_quantity = user_input
                list1.append([order_number,product_name,product_quantity])
                save_inventory(list1)
                order_number +=1
                
        else:
            print("invalid input.PLease enter valid number")
                
        

    
    

        


    

    
 