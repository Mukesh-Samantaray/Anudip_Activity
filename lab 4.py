# Lab4: List Operations

# 1. Add and remove student names from a list
students = []
students.append("Alice")
students.append("Bob")
students.append("Charlie")
print("Students List after adding:", students)

students.remove("Bob")
print("Students List after removing 'Bob':", students)

# 2. Create a list of even numbers from 1 to 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("\nEven numbers from 1 to 20:", even_numbers)

# 3. Find the average of marks from a list
marks = [85, 90, 78, 92, 88]
average = sum(marks) / len(marks)
print("\nAverage marks:", average)

# 4. Check if a product is available in a shopping cart
shopping_cart = ["milk", "bread", "eggs", "butter"]
product = input("\nEnter a product to search in cart: ")
if product.lower() in [item.lower() for item in shopping_cart]:
    print("→ Product is available in the cart.")
else:
    print("→ Product not found in the cart.")

# 5. Count how many times a name appears in a list
name_list = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob"]
name_to_check = input("\nEnter name to count: ")
count = name_list.count(name_to_check)
print(f"→ {name_to_check} appears {count} time(s) in the list.")

# 6. Split a list into two parts based on given length
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
split_length = 3
part1 = original_list[:split_length]
part2 = original_list[split_length:]
print("\nOriginal list:", original_list)
print("Splitted into two parts:")
print("→ First part:", part1)
print("→ Second part:", part2)
