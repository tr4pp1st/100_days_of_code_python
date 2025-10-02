# 100 Days of Code: Python
# Day 12 Project: Number Guessing Game

from art import NUMBER_GUESSING_GAME_ASCII
import random
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def get_valid_guess(number_of_guesses_: int) -> int:
    while True:
        try:
            return int(input(f"You've {number_of_guesses_} guesses left - Make a guess: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number.")


def evaluate_guess(guess_: int, answer_: int) -> str:
    if guess_ == answer_:
        return "correct"
    elif guess_ < answer_:
        return "low"
    else:
        return "high"


def set_difficulty():
    levels = {"easy": EASY_LEVEL_TURNS, "hard": HARD_LEVEL_TURNS}
    while True:
        level = input("Choose a difficulty, type 'easy' or 'hard': ").strip().lower()
        if level in levels:
            return levels[level]
        print(f"Invalid input '{level}'. Allowed are 'easy' or 'hard'.")


def ask_play_again() -> bool:
    while True:
        choice = input("Play again? Type 'y' or 'n': ").strip().lower()
        if choice in ('y', 'n'):
            return choice == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def play_round():
    number_of_guesses = set_difficulty()
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    while number_of_guesses > 0:
        guess = get_valid_guess(number_of_guesses)
        number_of_guesses -= 1
        evaluation = evaluate_guess(guess, answer)
        if evaluation == 'correct':
            print(f"\nCongratulations! {guess} is the correct answer!\n")
            return
        elif evaluation == 'low':
            print(f"\n{guess} is too low.\n")
        else:
            print(f"\n{guess} is too high.\n")

    print(f"You lost the game. The right answer was: {answer}.\n")


def start_game():
    print("Welcome to the Number Guessing Game.")
    print(NUMBER_GUESSING_GAME_ASCII)

    while True:
        play_round()
        if not ask_play_again():
            break
        clear_screen()


if __name__ == "__main__":
    start_game()