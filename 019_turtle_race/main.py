# 100 Days of Code: Python
# Day 19 Project: Turtle Race


import random
from turtle import Turtle, Screen

# --- Configuration ---
CONFIG = {
    "colors": ["red", "orange", "yellow", "green", "blue", "purple"],
    "y_positions": [-70, -40, -10, 20, 50, 80],
    "start_x": -230,
    "finish_x": 200,
    "screen_width": 500,
    "screen_height": 400,
}


def create_turtles(colors, positions, start_x):
    """Create and return turtles with different colors and starting y-positions."""
    racers = []
    for index, color in enumerate(colors):
        new_racer = Turtle(shape="turtle")
        new_racer.penup()
        new_racer.color(color)
        new_racer.goto(x=start_x, y=positions[index])
        racers.append(new_racer)
    return racers


def get_user_bet(valid_colors):
    """Ask user for a valid bet until correct input is given."""
    bet = ""
    while bet not in valid_colors:
        bet = screen.textinput(
            title="Make your bet",
            prompt=f"Which turtle will win the race?\nEnter a color ({', '.join(valid_colors)}): "
        )
        if not bet:
            return None
        bet = bet.lower()
    return bet


def run_race(racers, finish_x, users_bet):
    """Run the turtle race until one reaches the finish line."""
    while True:
        for racer in racers:
            racer.forward(random.randint(0, 10))

            if racer.xcor() > finish_x:
                color_of_the_winner = racer.pencolor()
                return color_of_the_winner == users_bet, color_of_the_winner


def announce_winner_on_screen(won_: bool, winning_color_: str):
    """Display the winner announcement on the turtle screen."""
    announcer = Turtle()
    announcer.hideturtle()
    announcer.penup()
    announcer.goto(0, 150)

    status = "You've won!" if won_ else "You've lost!"
    announcer.write(
        f"{status}\nThe {winning_color_} turtle is the winner!",
        align="center",
        font=("Arial", 16, "bold")
    )


# --- Setup Screen ---
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=CONFIG["screen_width"], height=CONFIG["screen_height"])

# --- Setup Turtles ---
all_turtles = create_turtles(CONFIG["colors"], CONFIG["y_positions"], CONFIG["start_x"])

# --- User Bet ---
user_bet = get_user_bet(CONFIG["colors"])

if user_bet:
    won, winning_color = run_race(all_turtles, CONFIG["finish_x"], user_bet)

    message = "You've won!" if won else "You've lost!"
    announce_winner_on_screen(won, winning_color)


screen.exitonclick()
