# Dictionary list to store each product
inventory = [{"Name": "Notebook", "Price": 3500., "Quantity": 10},
             {"Name": "Eraser", "Price": 2000., "Quantity": 20},
            ]

# Function to display inventory
def show_inventory():
    print("\n* * * * * INVENTORY * * * * *")
    if not inventory:
        print("Empty inventory")
    else:  
      for product in inventory:
        print(f"Name: {product['Name']}, Price: {product['Price']}, Quantity: {product['Quantity']}")

# Function to add products
def add_product():
  name = input("\nName: ") # Ask for the product name
  
  # Data validation block
  while True:
    try:
      price = float(input("Price: ")) # Ask for the product price
      if price < 0: # Conditional to evaluate if the price is negative
        print("Price must be positive.\n")
        continue
      break
    except:
      print("Error value\n")

  # Data validation block
  while True:
    try:
      quantity = int(input("Quantity: ")) # Ask for the product quantity
      if quantity < 0: # Conditional to evaluate if the quantity is negative
        print("Quantity must be positive.\n")
        continue
      break
    except:
      print("Error value\n")
  
  product = {"Name": name, "Price": price, "Quantity": quantity} # Dictionary with product data
  inventory.append(product) # Dictionary added to list
  print("Product added to inventory") 
