from services import show_inventory, add_product, calculate_statistics, search_product, update_product, delate_product, inventory
from files import save_csv, upload_csv

# Block to view the menu and execute the available options
while True:
    print("\n * * * * MENU * * * * \n1. Display inventory \n2. Add products \n3. Calculate statistics \n4. Search product \n5. Update product \n6. Delate product \n7. Save cvs \n8. Upload csv \n9. Log out")
    opcion = input("\nEnter an option: ")
    if opcion == "1":
        show_inventory(inventory)
    elif opcion == "2":
        name = input("\nName: ").capitalize() # Ask for the product name
        # Block to validate errors
        while True:
            try:
                quantity = int(input("Quantity: "))
                price = float(input("Price: ")) # Ask for the product price
                if quantity < 0 or price < 0: # Conditional to evaluate if the price is negative
                    print("The data entered must be positive.\n")
                    continue
                break
            except:
                print("Error value\n")
        add_product(name, quantity, price)
    elif opcion == "3":
        calculate_statistics(inventory)
    elif opcion == "4":
        product = input("\nProduct to search: ").capitalize()
        search = search_product(product, inventory)
        if search == None:
            print("\nProduct not found")
        else:
            print(search)
    elif opcion == "5":
        name = input("\nName: ").capitalize() # Ask for the product name
        search = search_product(name, inventory)
        if search == None:
            print("This product cannot be updated because it is not in stock.")
        else:
            # Block to validate errors
            while True:
                try:
                    new_quantity = int(input("Quantity: "))
                    new_price = float(input("Price: ")) # Ask for the product price
                    if new_quantity < 0 or new_price < 0: # Conditional to evaluate if the price is negative
                        print("The data entered must be positive.\n")
                        continue
                    break
                except:
                    print("Error value\n")
            update_product(name, new_quantity, new_price, inventory)
    elif opcion == "6":
        name = input("\nName: ").capitalize() # Ask for the product name
        delate_product(name, inventory)
    elif opcion == "7":
        file = "inventory.csv"
        save_csv(inventory, file)
    elif opcion == "8":
        new_inventory = []
        new_inventory = upload_csv("inventory.csv", inventory)
        print(new_inventory)
    elif opcion == "9":
        print("Exiting the system...")
        break
    else:
        print("Enter a valid option")

# This code allows the user to view stored products, add new items with data validation (price and quantity),
# and calculate statistics such as the total inventory value and the number of registered products.
# It also features an interactive menu that facilitates navigation between the different options,
# making the system easy to use and understand.