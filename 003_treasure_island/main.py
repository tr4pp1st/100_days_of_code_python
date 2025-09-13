# 100 Days of Code: Python
# Day 3 Project: Treasure Island

def game_over(reason):
    if reason.strip() != "":
        print(reason)
    print("Game Over")


# https://ascii.co.uk/art/treasureisland
print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \\/ _` / __| | | | '__/ _ \\ / __| |/ _` | '_ \\ / _` |
| |_| | |  __/ (_| \\__ \\ |_| | | |  __/ \\__ \\ | (_| | | | | (_| |
 \\__|_|  \\___|\\__,_|___/\\__,_|_|  \\___|_|___/_|\\__,_|_| |_|\\__,_|
 ''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

print("You are at a cross road. Where do you want to go?")
choice1 = input("Type \"left\" or \"right\":\n").lower()

if choice1 != "left":
    game_over("Fall into a hole.")
else:
    print("You come to a lake. Do you want to wait for the boat or swim?")
    choice2 = input("Type \"wait\" or \"swim\":\n").lower()
    if choice2 != "wait":
        game_over("Attacked by trout.")
    else:
        print("You come to a house with three doors. Which door do you want to go into?")
        choice3 = input("Type \"red\", \"blue\" or \"yellow\":\n").lower()
        if choice3 == "red":
            game_over("Burned by fire.")
        elif choice3 == "blue":
            game_over("Eaten by beasts.")
        elif choice3 != "yellow":
            game_over("")
        else:
            print("You Win!")

