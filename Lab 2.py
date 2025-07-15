# 1. Division function
def div(a, b):
    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero!")

div(10, 2)

# 2. Square function
def square(n):
    print("Square:", n ** 2)

square(5)

# 3. Max and Min of 5 random numbers
import random
nums = [random.randint(1, 100) for _ in range(5)]
print("Numbers:", nums)
print("Maximum:", max(nums))
print("Minimum:", min(nums))

# 4. Accept name and convert to lowercase
name = input("Enter your name: ")
print("Lowercase name:", name.lower())

# 5. Lambda for number sign
check_sign = lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Zero'
for n in [5, -3, 0]:
    print(f"{n}: {check_sign(n)}")
