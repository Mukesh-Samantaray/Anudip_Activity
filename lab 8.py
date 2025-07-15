# -------------------------
# Problem 1: Validate marks
print("\nProblem 1: Marks Input Validation")
try:
    marks = []
    for i in range(5):
        mark = int(input(f"Enter mark {i+1}: "))
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100.")
        marks.append(mark)
    print("Marks entered successfully:", marks)
except ValueError as ve:
    print("Error:", ve)

# -------------------------
# Problem 2: Validate email format
print("\nProblem 2: Email Format Check")
try:
    email = input("Enter your email: ")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format")
    print("Email accepted:", email)
except ValueError as ve:
    print("Error:", ve)

# -------------------------
# Problem 3: Login attempts
print("\nProblem 3: Login Attempts")
correct_username = "admin"
correct_password = "1234"

attempts = 0
while attempts < 3:
    username = input("Username: ")
    password = input("Password: ")
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Invalid credentials.")
        attempts += 1
        if attempts == 3:
            try:
                raise PermissionError("Too many failed login attempts.")
            except PermissionError as pe:
                print("Error:", pe)

# -------------------------
# Problem 4: Password strength check
print("\nProblem 4: Password Strength Check")
try:
    password = input("Enter password: ")
    if len(password) < 8:
        raise ValueError("Weak password")
    print("Password accepted.")
except ValueError as ve:
    print("Error:", ve)

# -------------------------
# Problem 5: Custom NegativeNumberError
print("\nProblem 5: Custom NegativeNumberError")

# Define custom exception
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative number entered.")
    print("You entered:", num)
except NegativeNumberError as nne:
    print("Error:", nne)
except ValueError:
    print("Error: Please enter a valid integer.")
