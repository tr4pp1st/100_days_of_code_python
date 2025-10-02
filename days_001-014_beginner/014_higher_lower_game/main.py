# 100 Days of Code: Python
# Day 14 Project: Higher Lower Game Project

import random
import os
from art import HIGHER_LOWER_ASCII
from game_data import DATA_FOLLOWER


def get_data_set(data_: list[dict]) -> dict:
    random.shuffle(data_)
    data_set_ = data_.pop()
    return data_set_


def get_data_set_string(data_set_: dict) -> str:
    return f'{data_set_.get("name")}, {data_set_.get("description")}, from {data_set_.get("country")}.'


def get_data_set_follower(data_set_: dict) -> int:
    return int(data_set_.get("follower_count"))


def is_answer_correct(data_set_a: dict, data_set_b: dict, answer: str) -> bool:
    a_followers = get_data_set_follower(data_set_a)
    b_followers = get_data_set_follower(data_set_b)
    return (a_followers > b_followers and answer == "A") or (b_followers > a_followers and answer == "B")


def ask_who_has_more_followers() -> str:
    is_input_correct = False
    choice_ = ""
    while not is_input_correct:
        choice_ = input("Who has more followers? Type 'A' or 'B':   ").strip().upper()
        if choice_ not in ('A', 'B'):
            print(f"The input was not correct. Allowed are 'A' or 'B', the input was '{choice_}'.")
        else:
            is_input_correct = True
    return choice_


def ask_play_again() -> bool:
    is_input_correct = False
    play_again_ = ""
    while not is_input_correct:
        play_again_ = input("Play again? Type 'y' or 'n':   ").strip().lower()
        if play_again_ not in ('y', 'n'):
            print(f"The input was not correct. Allowed are 'y' or 'n', the input was '{play_again_}'.")
        else:
            is_input_correct = True
    if play_again_ == 'y':
        return True
    return False


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


data = DATA_FOLLOWER.copy()
run = True
score = 0
print(HIGHER_LOWER_ASCII)

data_set_a = get_data_set(data)
data_set_b = get_data_set(data)

while run:
    print(f"Compare A: {get_data_set_string(data_set_a)}")
    print(f"Against B: {get_data_set_string(data_set_b)}")
    choice = ask_who_has_more_followers()
    evaluation = is_answer_correct(data_set_a, data_set_b, choice)

    clear_screen()
    print(HIGHER_LOWER_ASCII)

    if evaluation:
        score += 1
        print(f"You're right! Current score: {score}.")
        if choice == 'B':
            data_set_a = data_set_b
        if len(data) > 0:
            data_set_b = get_data_set(data)
        else:
            print("You've completed all the data sets. Congratulations!")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        play_again = ask_play_again()
        if play_again:
            data = DATA_FOLLOWER.copy()
            score = 0
            clear_screen()
            print(HIGHER_LOWER_ASCII)
            data_set_a = get_data_set(data)
            data_set_b = get_data_set(data)
        else:
            run = False
