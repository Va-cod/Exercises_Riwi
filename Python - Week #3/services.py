# Dictionary list to store each product
inventory = [{"Name": "Notebook", "Price": 2000., "Quantity": 10},
             {"Name": "Eraser", "Price": 2000., "Quantity": 20},
             {"Name": "Marker", "Price": 2000., "Quantity": 20}
            ]

# Function to display inventory
def show_inventory(lista):
    print("\n* * * * * INVENTORY * * * * *")
    if not lista:
        print("Empty inventory")
    else:
        for product in lista:
            print(f"Name: {product['Name']}, Price: {product['Price']}, Quantity: {product['Quantity']}")

# Function to add products
def add_product(name, quantity, price):
    product = {"Name": name, "Price": price, "Quantity": quantity} # Dictionary with product data
    inventory.append(product) # Dictionary added to list
    print("Product added to inventory")

# Function to calculate statistics
def calculate_statistics(lista):
    total_inventory = 0
    expensive_product = 0.
    greater_quantity = 0

    print("\n * * * STATISTICS * * *")
    for product in lista:
        total = product['Price'] * product['Quantity'] # Variable that stores the total cost for each product
        total_inventory += total # Variable that stores the total cost of inventory
        print(f"{product['Name']} ---> ${total}")
        if product['Price'] > expensive_product:
            expensive_product = product['Price']
            expensive = f"{product['Name']} - Price: {product['Price']}"
        elif product['Price'] == expensive_product:
            expensive += f"\n{product['Name']} - Price: {product['Price']}"
        if product['Quantity'] > greater_quantity:
            greater_quantity = product['Quantity']
            greater = f"{product['Name']} - Quantity: {product['Quantity']}\n"
        elif product['Quantity'] == greater_quantity:
            greater += f"{product['Name']} - Quantity: {product['Quantity']}"
    total_products = len(inventory)
    print("-------------------------")
    print(f"Most expensive product:\n{expensive}")
    print("-------------------------")
    print(f"Total products: {total_products}")
    print("-------------------------")
    print(f"Total inventory: {total_inventory}")
    print("-------------------------")
    print(f"Product with the largest stock:\n{greater}")


# Funtion to search products
def search_product(product, lista):
    for products in lista:
        if product == products["Name"]:
            return f"\nName: {products['Name']}, Price: {products['Price']}, Quantity: {products['Quantity']}"
    return None

# Function to update product information
def update_product(name, price, quantity, lista):
    for products in lista:
        if name == products["Name"]:
            products.update({"Name": name, "Price": price, "Quantity": quantity})
            print("\nProduct updated")
            break

# Function to delete a product
def delate_product(name, lista):
    search = search_product(name, lista)
    if search == None:
            print("This product cannot be delated because it is not in stock.")
    else:
        for products in lista:
            if name == products["Name"]:
                lista.remove(products)
                print("Removed product")
                break