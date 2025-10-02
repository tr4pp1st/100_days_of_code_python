# 100 Days of Code: Python
# Day 20 Project: Snake Game - Part 1

# Hint:
# Part 1 - Create a snake body, move and control the snake.
# Part 2 (Day 21) - Detect collision with food, wall, tail, and create scoreboard.

import time
from turtle import Screen
from snake import Snake

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
}

# --- Setup ---
screen = Screen()
screen.setup(width=CONFIG["screen_width"], height=CONFIG["screen_height"])
screen.bgcolor(CONFIG["screen_background"])
screen.title(CONFIG["screen_title"])
screen.tracer(0)

snake = Snake(CONFIG)

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

# --- Exit ---
screen.exitonclick()
