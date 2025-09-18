# 100 Days of Code: Python
# Day 11 Project: Blackjack Capstone Project

import random
from art import BLACKJACK


def get_card():
    # 10, J, Q, K, Ace and a total of 52 cards in the card deck.
    # Draws and removes card from the deck.
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # ein Deck
    random.shuffle(deck)
    card = deck.pop()
    return card


def calculate_closest_possible_sum_to_win(lst: list[int]):
    cards = lst.copy()
    sum_ = sum(cards)
    while sum_ > 21 and 11 in cards:
        ace_index = cards.index(11)
        cards[ace_index] = 1
        sum_ = sum(cards)
    return sum_


def calculate_and_show_computer_actions(lst_computer_cards: list[int], lst_player_cards: list[int]):
    sum_of_the_player = calculate_closest_possible_sum_to_win(lst_player_cards)
    sum_of_the_computer = calculate_closest_possible_sum_to_win(lst_computer_cards)
    # Another approach would be:
    # while sum_of_the_computer < sum_of_the_player <= 21 or sum_of_the_computer <= 10:
    # Blackjack casino rule: The dealer draws card up to 17.
    while sum_of_the_computer < 17:
        print("The computer takes a card:")
        lst_computer_cards.append(get_card())
        sum_of_the_computer = calculate_closest_possible_sum_to_win(lst_computer_cards)
        show_card_overview(lst_computer_cards, lst_player_cards)


def show_card_overview(lst_computer_cards: list[int], lst_player_cards: list[int]):
    print("\n--- The current card overview: ---")
    print(f"Your cards: {lst_player_cards} (Sum: {calculate_closest_possible_sum_to_win(lst_player_cards)})")

    print(f"Computer cards: {lst_computer_cards} (Sum: {calculate_closest_possible_sum_to_win(lst_computer_cards)})")
    print("\n")


def show_game_result(lst_computer_cards: list[int], lst_player_cards: list[int]):
    sum_of_the_player = calculate_closest_possible_sum_to_win(lst_player_cards)
    sum_of_the_computer = calculate_closest_possible_sum_to_win(lst_computer_cards)
    if sum_of_the_player > 21:
        print("Computer wins!")
    elif sum_of_the_computer > 21:
        print("You are the winner!")
    elif sum_of_the_player > sum_of_the_computer:
        print("You are the winner!")
    elif sum_of_the_player < sum_of_the_computer:
        print("Computer is the winner!")
    else:
        print("It's a draw!")


play_blackjack = True
print("Welcome to the Blackjack Capstone Project")
print(BLACKJACK)


while play_blackjack:
    choice_play_blackjack = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")).strip().lower()
    if choice_play_blackjack not in ('y', 'n'):
        print(f"The input was not correct. Allowed are 'y' or 'n', the input was '{choice_play_blackjack}'.")
        continue
    elif choice_play_blackjack == 'n':
        play_blackjack = False
        print("Have a nice day.")
    elif choice_play_blackjack == 'y':
        # print("...lets play a round of blackjack...")
        player_cards = [get_card(), get_card()]
        computer_cards = [get_card()]
        show_card_overview(computer_cards, player_cards)

        get_another_card = True
        while get_another_card:
            choice_get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
            if choice_get_another_card not in ('y', 'n'):
                print(f"The input was not correct. Allowed are 'y' or 'n', the input was '{choice_get_another_card}'.")
                continue
            elif choice_get_another_card == 'n':
                get_another_card = False
            elif choice_get_another_card == 'y':
                player_cards.append(get_card())
                if calculate_closest_possible_sum_to_win(player_cards) > 21:
                    get_another_card = False
                show_card_overview(computer_cards, player_cards)

        players_best_sum = calculate_closest_possible_sum_to_win(player_cards)
        print(f"Your best sum is: {players_best_sum}")
        if players_best_sum <= 21:
            calculate_and_show_computer_actions(computer_cards, player_cards)

        show_game_result(computer_cards, player_cards)
