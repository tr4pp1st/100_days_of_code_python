# 100 Days of Code: Python
# Day 9 Project: Blind Auction

from art import GAVEL_ART
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


bidders = {}

print("Welcome to the Blind Auction program.")
print(GAVEL_ART)

while True:
    name = input("What is your name:\n").strip()
    if len(name) == 0:
        print("Please enter a valid name.")
        continue

    try:
        bid_price = float(input("What is your bid:\n").strip())
        if bid_price <= 0:
            print("Bid must be positive number.")
            continue
    except ValueError:
        print("Please enter a valid number (no currency symbol).")
        continue

    bidders[name] = bid_price

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no':\n").strip()
    if more_bidders == 'no':
        break

    clear()

max_bid = max(bidders.values())
winners = [name for name, bid in bidders.items() if bid == max_bid]

if len(winners) == 1:
    print(f"The winner is {winners[0]} with a bid of ${max_bid:,.2f}")
else:
    print(f"It's a tie between {', '.join(winners)} with ${max_bid:,.2f} each")
