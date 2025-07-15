# Lab 3: String Operations

# 1. Check if a string is palindrome
text = input("1. Enter a string to check palindrome: ")
if text == text[::-1]:
    print("→ It's a Palindrome")
else:
    print("→ Not a Palindrome")

# 2. Count number of vowels in the text
text_vowels = input("\n2. Enter a text to count vowels: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for ch in text_vowels if ch in vowels)
print(f"→ Number of vowels: {vowel_count}")

# 3. Replace all spaces with "-"
text_replace = input("\n3. Enter text to replace spaces with '-': ")
replaced_text = text_replace.replace(" ", "-")
print(f"→ Modified text: {replaced_text}")

# 4. Check if password is valid (at least 8 characters, one uppercase, one number)
password = input("\n4. Enter a password to validate: ")

has_upper = any(ch.isupper() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
length_ok = len(password) >= 8

if has_upper and has_digit and length_ok:
    print("→ Password is valid ✅")
else:
    print("→ Password is invalid ❌")
    if not length_ok:
        print("  - Should be at least 8 characters")
    if not has_upper:
        print("  - Should contain at least one uppercase letter")
    if not has_digit:
        print("  - Should contain at least one digit")
