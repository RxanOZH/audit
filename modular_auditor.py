print("===================")
print("smart inventory system")
print("===================")
inventory = 0 
failed_input =0 
delivery = 0

def get_valid_input(user_input):
    if user_input.isdigit():
        return int(user_input)
    elif user_input.lower() == "quit":
        return "quit"
    else:
        return None
    
def process_delovery( delivery):
    delivery += 1
    return delivery 

def calculate_tax(inventory):
    return inventory * 0.1

def generator_report(inventory, failed_input):
    print(f"Total inventory: {inventory}")
    print(f"Failed input attempts: {failed_input}")
    


    
while True:
    user_input = input("enter inventory quantity:")
    valid_input = get_valid_input(user_input)
    if valid_input is not None:
        if valid_input == "quit":
            generator_report(inventory, failed_input)
            break
        else:
            inventory += valid_input
            process_delovery(delivery)
            print(f"Tax amount {calculate_tax(inventory)}")
            if inventory > 500:
                print("Alert: Inventory overflow")
                break
    else:
        failed_input += 1
        print("Invalid input. Please enter a valid number.")
   