# Task: Create a simple billing system using tuples

# Ask how many products the user wants to enter
num_products = int(input("Enter the number of products: "))

# Initialize an empty list to store product tuples
products = []

# Loop to input product details
for i in range(num_products):
    # Input product name, price and quantity
    name = input(f"Enter name of product {i+1}: ")
    price = float(input(f"Enter price of {name}: "))
    quantity = int(input(f"Enter quantity of {name}: "))
    
    # Create a tuple and add it to the products list
    product = (name, price, quantity)
    products.append(product)

# Display the bill
print("\n--- Detailed Bill ---")
print(f"{'Product':<15}{'Price':<10}{'Quantity':<10}{'Total':<10}")

# Initialize total bill amount
total_bill = 0

# Loop through products to calculate and display each product's total
for product in products:
    # Unpack tuple into individual variables
    name, price, quantity = product
    
    # Calculate total for current product
    total = price * quantity
    total_bill += total

    # Print product-wise billing info
    print(f"{name:<15}{price:<10.2f}{quantity:<10}{total:<10.2f}")

# Print final total
print("\nTotal Bill Amount:", total_bill)
print("Thank you for your purchase!")
# End of billing system