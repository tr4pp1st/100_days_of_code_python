# 100 Days of Code: Python
# Day 23 Project: Turtle Crossing Capstone Project

import time
from turtle import Screen
from player import Player
from carmanager import CarManager
from scoreboard import Scoreboard

CONFIG = {
    "screen_width": 600,
    "screen_height": 400,
    "screen_bg_color": "white",
    "screen_title": "Turtle Crossing",
    "top_edge_y": 180,
    "player_shape": "turtle",
    "player_color": "aqua",
    "player_start_position": (0, -180),
    "player_heading": 90,
    "player_move_distance": 10,
    "car_shape": "square",
    "car_stretch_wid": 1.0,
    "car_stretch_len": 2.0,
    "car_colors": [
        'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'cyan',
        'magenta', 'lime', 'teal', 'navy', 'maroon', 'olive', 'gold', 'silver'
    ],
    "car_start_position_x": 300,
    "car_start_position_y_min": -150,
    "car_start_position_y_max": 150,
    "car_move_distance": 10,
    "car_speed_start": 0.2,
    "car_speed_increase_factor": 0.9,
    "sb_start_position": (-280, 170),
    "sb_start_level": 1,
    "sb_color": "black",
    "sb_font": ("Arial", 10, "bold"),
    "sb_align": "left",
    "sb_game_over_position": (0, 0),
    "sb_game_over_align": "center"
}

# --- Setup Screen ---
screen = Screen()
screen.bgcolor(CONFIG.get("screen_bg_color", "black"))
screen.setup(
    width=CONFIG.get("screen_width", 600),
    height=CONFIG.get("screen_height", 400)
)
screen.title(CONFIG.get("screen_title", "Turtle Crossing"))
screen.tracer(0)

# --- Setup Game Objects ---
player = Player(CONFIG)
car_manager = CarManager(CONFIG)
scoreboard = Scoreboard(CONFIG)

# -- Event Listeners ---
screen.listen()
screen.onkey(player.go_up, key="Up")


# --- Game Loop ---
game_running = True
while game_running:
    time.sleep(car_manager.move_speed)
    screen.update()

    # Move cars and create new ones randomly.
    car_manager.create()
    car_manager.move()
    car_manager.remove_off_screen()

    # Detect collision with any car.
    if car_manager.check_collides_with_player(player):
        game_running = False
        scoreboard.game_over()

    # Detect if player reached the top edge.
    if player.ycor() >= CONFIG.get("top_edge_y", 180):
        scoreboard.increase_level()
        player.reset_position()
        car_manager.increase_speed()

# --- Exit ---
screen.exitonclick()
