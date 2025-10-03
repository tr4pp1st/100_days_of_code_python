# 100 Days of Code: Python
# Day 21 Project: Snake Game - Part 2

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# --- Configuration ---
CONFIG = {
    "starting_positions": [(0, 0), (-20, 0), (-40, 0)],
    "screen_width": 600,
    "screen_height": 600,
    "screen_background": "black",
    "screen_title": "Snake Game",
    "move_distance": 20,
    "right": 0,
    "up": 90,
    "left": 180,
    "down": 270,
    "speed": 0.1,
    "scoreboard_alignment": "center",
    "scoreboard_font": ("Arial", 24, "normal"),
    "scoreboard_color": "white",
    "scoreboard_offset": 35,
    "game_over_text": "GAME OVER",
    "wall_margin": 10
}

# --- Setup ---
screen = Screen()
screen.setup(width=CONFIG["screen_width"], height=CONFIG["screen_height"])
screen.bgcolor(CONFIG["screen_background"])
screen.title(CONFIG["screen_title"])
screen.tracer(0)

snake = Snake(CONFIG)
food = Food(CONFIG)
scoreboard = Scoreboard(CONFIG)

# --- Event Listeners: Control the snake with arrow keys ---
screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")

# --- Game Loop ---
game_running = True
while game_running:
    screen.update()
    time.sleep(CONFIG["speed"])
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if (snake.head.xcor() > (CONFIG["screen_width"] / 2 - CONFIG["wall_margin"])
            or snake.head.xcor() < (CONFIG["screen_width"] / 2 - CONFIG["wall_margin"]) * -1
            or snake.head.ycor() > (CONFIG["screen_height"] / 2 - CONFIG["wall_margin"])
            or snake.head.ycor() < (CONFIG["screen_height"] / 2 - CONFIG["wall_margin"]) * -1):
        game_running = False
        scoreboard.game_over()

    # Detect collision with tail. Ignore the head by slicing from index 1.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_running = False
            scoreboard.game_over()


# --- Exit ---
screen.exitonclick()
