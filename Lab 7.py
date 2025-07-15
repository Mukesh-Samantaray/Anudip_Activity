# 1. Calculate the mean of dictionary values
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
mean = sum(test_dict.values()) / len(test_dict)
print("1. Mean of dictionary values:", mean)  # Output: 6.2

# --------------------------------------------

# 2. Concatenate dictionaries into one
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
# Using the update method
merged_dict = dic1.copy()  # Create a copy to avoid modifying original
merged_dict.update(dic2)  # Update with second dictionary
merged_dict.update(dic3)  # Update with third dictionary    
print("\n2. Merged Dictionary using update method:", merged_dict)
# Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Using dictionary unpacking (Python 3.5+)
merged_dict = {**dic1, **dic2, **dic3}
print("\n2. Merged Dictionary:", merged_dict)
# Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# --------------------------------------------

# 3. Get keys, values, and items from a dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("\n3. Keys:", list(dict_num.keys()))
print("Values:", list(dict_num.values()))
print("Items:", list(dict_num.items()))
 # Output:
# Keys: [1, 2, 3, 4, 5, 6]
# Values: [10, 20, 30, 40, 50, 60]
# Items: [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60)]

#using . items() method
print("\n3. Using items() method:")
print("Keys:", [key for key, value in dict_num.items()])
print("Values:", [value for key, value in dict_num.items()])
print("Items:", [item for item in dict_num.items()])

# --------------------------------------------

# 4. Display all keys and their values (even if None)
input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

print("\n4. Key-Value pairs (including None values):")
for key, value in input_dict.items():
    print(f"{key} → {value}")

# --------------------------------------------

# 5. Simple Employee Management System

# Create employee records
employees = {
    "E001": {"name": "Krishna", "department": "HR", "salary": 50000},
    "E002": {"name": "Biswakarma", "department": "IT", "salary": 60000},
    "E003": {"name": "Kuber", "department": "Finance", "salary": 55000}
}

# Ask user for employee ID
emp_id = input("\n5. Enter Employee ID to fetch details: ").strip()

# Check if ID exists
if emp_id in employees:
    emp = employees[emp_id]
    print(f"Name: {emp['name']}")
    print(f"Department: {emp['department']}")
    print(f"Salary: ₹{emp['salary']}")
else:
    print("Employee not found!")
