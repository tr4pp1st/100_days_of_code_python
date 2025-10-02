# 100 Days of Code: Python
# Day 6 Project: Escaping the Maze

# https://reeborg.ca/index_en.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
