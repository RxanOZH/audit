print("===================")
print("smart inventory system")
print("===================")
inventory = 0 
failed_input =0 
delivery = 0
tax=0 

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
    tax = inventory * 0.1
    return tax

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
            if inventory > 500:
                print("Alert: Inventory overflow")
                break
            else:
                tax = 0
                inventory += valid_input
                process_delovery(delivery)
                tax = calculate_tax(valid_input)
                print(f"Tax amount {tax}") 
                
    else:
        failed_input += 1
        print("Invalid input. Please enter a valid number.")