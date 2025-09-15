# 100 Days of Code: Python
# Day 8 Project: Caesar Cipher

import string
from art import CAESAR_CIPHER

CHARACTER_SET = list(string.ascii_letters + string.digits + string.punctuation)
CHARACTER_SET_LENGTH = len(CHARACTER_SET)
run = "yes"


def encode(char, shift_number):
    return CHARACTER_SET[(CHARACTER_SET.index(char) + shift_number) % CHARACTER_SET_LENGTH]


def decode(char, shift_number):
    return CHARACTER_SET[(CHARACTER_SET.index(char) - shift_number) % CHARACTER_SET_LENGTH]


print(f"{CAESAR_CIPHER}")

while run == "yes":
    result = ""
    action = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").strip().lower()
    if action not in ['encode', 'decode']:
        print(f"You entered '{action}. This is a wrong input. Please try again.")
        continue

    message = input("Type your message:\n").strip()
    if len(message) == 0:
        print("Your message is empty. Please try again.")
        continue

    shift_number = int(input("Type the shift number:\n").strip())

    for char in message:
        if char in CHARACTER_SET:
            result += encode(char, shift_number) if action == "encode" else decode(char, shift_number)
        else:
            result += char

    print(f"The {action}d result is: {result}")

    run = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
