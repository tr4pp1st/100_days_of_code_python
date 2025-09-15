# 100 Days of Code: Python
# Day 7 Project: Hangman

import random
from hangman_art import HANGMAN_ASCII_PICTURES

word_list = ["elephant", "bear", "dinosaur", "duck", "hippopotamus"]

chosen_word = str(random.choice(word_list))

placeholder = ""
already_guessed = set()
failed_attempts = 0
max_fails = len(HANGMAN_ASCII_PICTURES)

print("_" * len(chosen_word))

while failed_attempts < max_fails:
    guess = input("Guess a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in already_guessed:
        print("You already guessed that letter.")
        continue

    already_guessed.add(guess)

    # placeholder = ""
    # for letter in chosen_word:
    #    if letter in already_guessed:
    #        placeholder += letter
    #    else:
    #        placeholder += "_"

    placeholder = "".join([letter if letter in already_guessed else "_" for letter in chosen_word])
    print(placeholder)

    if guess not in chosen_word:
        print(HANGMAN_ASCII_PICTURES[failed_attempts])
        failed_attempts += 1

    if "_" not in placeholder:
        print("You won!")
        break
else:
    print("You lost!")
