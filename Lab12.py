import csv
import json
import os
from classes.Inventory import Inventory
from classes.ProductFactor import ProductFactory
from classes.Supplier import Supplier


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")


def get_non_negative_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a number of 0 or greater.")
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row
            for row in reader:
                if not row:
                    continue
                try:
                    p_type, p_id, name, price_str, stock_str = row
                    price = float(price_str)
                    stock = int(stock_str)
                    product = ProductFactory.create(p_type, p_id, name, price, stock, supplier)
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as e:
                    print(f"Skipping invalid row {row}: {e}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")


def save_inventory(inventory: Inventory) -> None:
    with open("new_inventory.json", "w") as file:
        json.dump(inventory.to_list(), file, indent=4)


def main():
    supplier1 = Supplier("S001", "Supplier One", "supplier1@example.com")
    supplier2 = Supplier("S002", "Supplier Two", "supplier2@example.com")
    inventory = Inventory()

    if os.path.exists("new_inventory.json"):
        try:
            with open("new_inventory.json", "r") as file:
                data = json.load(file)
                for item in data:
                    p_type = item.get("type")
                    extra = item.get("weight") if p_type == "physical" else item.get("file_size", 1.0)
                    sup = supplier1 if p_type == "physical" else supplier2
                    product = ProductFactory.create(
                        p_type, item["id"], item["name"], item["price"], item["stock"], sup, extra
                    )
                    inventory.add_product(product)
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            print(f"Could not load JSON inventory ({e}). Starting fresh.")

    print("====================================================")
    print("|           Inventory Management System            |")
    print("====================================================\n")

    user_input = 0
    while user_input != 6:
        print("\n------Menu------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Quit the program")
        print("7. Load Products from CSV")
        print("----------------\n")

        try:
            user_input = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if user_input == 1:
            print("\nCurrent Inventory:")
            inventory.display_all()

        elif user_input == 2:
            print("\nAdd New Product")
            product_id = input("Enter product ID: ").strip()
            product_name = input("Enter product name: ").strip()
            product_price = get_positive_float("Enter product price: ")
            product_inventory = get_non_negative_int("Enter product stock: ")
            product_type = input("Enter product type (physical/digital): ").strip().lower()
            extra_info = get_positive_float("Enter weight in kg (physical) or file size in MB (digital): ")
            supplier = supplier1 if product_type == "physical" else supplier2

            try:
                new_product = ProductFactory.create(
                    product_type, product_id, product_name, product_price, product_inventory, supplier, extra_info
                )
                new_product.display_information()
                new_product.get_fulfillment_info()
                inventory.add_product(new_product)
                print("\nProduct added successfully!")
            except ValueError as e:
                print(f"Error creating product: {e}")

        elif user_input == 3:
            print("\nUpdate Stock")
            search_id = input("Enter the product ID to search: ").strip()
            product = inventory.search_product(search_id)

            if product is None:
                print("Product not found.")
            else:
                print("\nProduct found:")
                product.display()
                new_stock = get_non_negative_int("Enter the new stock quantity: ")
                product.update_stock(new_stock)
                print("\nStock updated successfully!")

        elif user_input == 4:
            print("\nSearch Product")
            search_id = input("Enter the product ID to search: ").strip()
            product = inventory.search_product(search_id)

            if product is None:
                print("Product not found.")
            else:
                print("\nProduct found:")
                product.display_information()

        elif user_input == 5:
            print("\nSaving Inventory")
            save_inventory(inventory)
            print("Inventory saved successfully.")

        elif user_input == 6:
            print("\nSaving Inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break

        elif user_input == 7:
            csv_path = input("Enter CSV filename (default: products.csv): ").strip() or "products.csv"
            load_products(csv_path, inventory, supplier1)

        else:
            print("Please select a valid option (1-7).")


if __name__ == "__main__":
    main()