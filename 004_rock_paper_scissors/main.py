# 100 Days of Code: Python
# Day 4 Project: Rock Paper Scissors

from random import randint
from art import rock, paper, scissors

print_art = [rock, paper, scissors]

print("Welcome to the Rock Paper Scissors game!")
users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n").strip())

if users_choice not in [0,1,2]:
    print("Invalid choice!")
else:
    computers_choice = randint(0,2)

    print("You chose:\n")
    print_art[users_choice]()
    print("Computer chose:\n")
    print_art[computers_choice]()

    # Results matrix for Rock-Paper-Scissors
    # Rows = user choice
    # Columns = computer choice
    # Values: 0 = draw, 1 = user wins, 2 = computer wins
    results = [
        [0, 2, 1],
        [1, 0, 2],
        [2, 1, 0]
    ]

    evaluation = results[users_choice][computers_choice]

    messages = ["It's a draw!", "You win!", "Computer wins!"]
    print(messages[evaluation])
