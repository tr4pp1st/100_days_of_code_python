# FileNotFound
"""
with open("a_file.txt") as file:
    file.read()
"""

# KeyError
"""
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]
"""

# IndexError
"""
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]
"""

# TypeError
"""
text = "abc"
print(text + 5)
"""

# try-except-else-finally
"""
file = None
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["non_existent_key"])
except FileNotFoundError:
    file = open("a_file.text", "w")
    file.write("something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
finally:
    if file:
        file.close()
        print("File was closed")
"""

# raise
"""
try:
    height = float(input("Height: "))
    weight = float(input("Weight: "))
    if height > 3:
        raise ValueError("Human height should not be over 3 meters.")
    bmi = weight / height ** 2
    print(bmi)
except ValueError as e:
    print(f"Error: {e}")
"""
