# 1. Read content from "ABC.txt" line by line and display
def read_file_lines():
    try:
        with open("ABC.txt", "r") as file:
            print("1. File Content Line by Line:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: 'ABC.txt' not found.")

# 2. Count and display total number of words in "ABC.txt"
def count_words():
    try:
        with open("ABC.txt", "r") as file:
            text = file.read()
            words = text.split()
            print("\n2. Total number of words in 'ABC.txt':", len(words))
    except FileNotFoundError:
        print("Error: 'ABC.txt' not found.")

# 3. Count uppercase characters in "ABC.txt"
def count_uppercase():
    try:
        with open("ABC.txt", "r") as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
            print("\n3. Total uppercase letters in 'ABC.txt':", uppercase_count)
    except FileNotFoundError:
        print("Error: 'ABC.txt' not found.")

# 4. Display words less than 4 characters from "story.txt"
def display_words():
    try:
        with open("story.txt", "r") as file:
            print("\n4. Words less than 4 characters in 'story.txt':")
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) < 4:
                        print(word)
    except FileNotFoundError:
        print("Error: 'story.txt' not found.")


# Call all functions for testing
read_file_lines()
count_words()
count_uppercase()
display_words()
