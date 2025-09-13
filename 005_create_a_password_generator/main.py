# 100 Days of Code: Python
# Day 5 Project: Create a Password Generator

import random
from allowed_character_set import letters, digits, symbols

print("Welcome to the Password Generator!")
count_of_letters = int(input("How many letters would you like in your password?\n").strip())
count_of_digits = int(input("How many digits would you like?\n").strip())
count_of_symbols = int(input("How many symbols would you like?\n").strip())

password_list = []

for _ in range(count_of_letters):
    password_list.append(random.choice(letters))
for _ in range(count_of_digits):
    password_list.append(random.choice(digits))
for _ in range(count_of_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = "".join(password_list)

print(f"Your password is: {password}")
