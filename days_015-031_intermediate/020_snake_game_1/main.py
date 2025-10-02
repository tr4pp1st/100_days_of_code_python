# 100 Days of Code: Python
# Day 20 Project: Snake Game - Part 1


#148##############################################################################################


from turtle import Screen, Turtle

# --- Configuration ---
CONFIG = {
    "starting_positions": [(0, 0), (-20, 0), (-40, 0)],
    "screen_width": 600,
    "screen_height": 600,
    "screen_background": "black",
    "screen_title": "Snake Game"
}


def create_snake():
    """Create the Snake body at the start position."""
    for position in CONFIG["starting_positions"]:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.goto(position)


screen = Screen()
screen.setup(width=CONFIG["screen_width"], height=CONFIG["screen_height"])
screen.bgcolor(CONFIG["screen_background"])
screen.title(CONFIG["screen_title"])


create_snake()








screen.exitonclick()
