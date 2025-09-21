# 100 Days of Code: Python
# Day 15 Project: Coffee Machine Project

import os
from data import COFFEE_CONTENTS_AND_PRICES, COFFEE_MACHINE_RESOURCES


COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}


# --- Input / Choice Handling ---
def check_choice() -> str:
    while True:
        choice_ = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if choice_ not in ('espresso', 'latte', 'cappuccino', 'off', 'report'):
            print(f"Incorrect input. Allowed are 'espresso', 'latte' or 'cappuccino'. Your input was '{choice_}'.")
            continue
        else:
            return choice_


def get_valid_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# --- Coffee Recipes / Resources ---
def get_coffee_recipe(name: str) -> dict:
    """
    for coffee_ in COFFEE_CONTENTS_AND_PRICES:
        if coffee_["name"] == name:
            return coffee_
    return {}
    """
    return next((c for c in COFFEE_CONTENTS_AND_PRICES if c["name"] == name), {})


def is_resource_sufficient(recipe_: dict, resources_: dict) -> bool:
    enough_resources_ = True
    for item in ("water", "milk", "coffee"):
        if resources_[item] < recipe_[item]:
            print(f"Sorry but there is not enough {item}.")
            enough_resources_ = False
    return enough_resources_


# --- Money Handling ---
def insert_coins() -> float:
    print("Please insert coins.")
    total = 0
    for coin, value in COIN_VALUES.items():
        total += get_valid_int(f"How many {coin}: ") * value
    return total


def is_money_sufficient(needed_money_: float, inserted_money_: float) -> bool:
    if inserted_money_ >= needed_money_:
        if inserted_money_ > needed_money_:
            print(f"Here is ${inserted_money_ - needed_money_:.2f} in change.")
        return True
    return False


# --- Utility ---
def print_report(resources: dict, money: float):
    print(
        f"\nThe current resource values:"
        f"\nWater:  {resources['water']}ml"
        f"\nMilk:   {resources['milk']}ml"
        f"\nCoffee: {resources['coffee']}g"
        f"\nMoney:  ${money:.2f}\n"
    )


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    coffee_machine_resources = COFFEE_MACHINE_RESOURCES.copy()
    coffee_machine_money = 0
    coffee_machine_status = 'on'
    clear_screen()

    while coffee_machine_status == 'on':
        choice = check_choice()
        coffee_recipe = get_coffee_recipe(choice)
        if choice in ('espresso', 'latte', 'cappuccino'):
            enough_resources = is_resource_sufficient(coffee_recipe, coffee_machine_resources)
            if enough_resources:
                inserted_money = insert_coins()
                enough_money = is_money_sufficient(coffee_recipe["money"], inserted_money)
                if enough_money:
                    coffee_machine_money += coffee_recipe["money"]
                    coffee_machine_resources["water"] -= coffee_recipe["water"]
                    coffee_machine_resources["milk"] -= coffee_recipe["milk"]
                    coffee_machine_resources["coffee"] -= coffee_recipe["coffee"]
                    print(f"Here is your {choice} ☕ Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
        elif choice == 'off':
            coffee_machine_status = 'off'
            break
        elif choice == 'report':
            print_report(coffee_machine_resources, coffee_machine_money)
