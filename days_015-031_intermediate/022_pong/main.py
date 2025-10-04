# 100 Days of Code: Python
# Day 22 Project: Pong

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# --- Configuration ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BG_COLOR = "black"
SCREEN_TITLE = "Pong"
PADDLE_RIGHT_START_POSITION = (360, 0)
PADDLE_LEFT_START_POSITION = (-360, 0)
PADDLE_COLLISION_RANGE = 50
PADDLE_X_BOUNDARY = 330
BALL_WALL_OFFSET = 20

# --- Setup Screen ---
screen = Screen()
screen.bgcolor(SCREEN_BG_COLOR)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title(SCREEN_TITLE)
screen.tracer(0)

# --- Game Objects ---
paddle_right = Paddle(PADDLE_RIGHT_START_POSITION)
paddle_left = Paddle(PADDLE_LEFT_START_POSITION)
ball = Ball()
scoreboard = Scoreboard()

# --- Event Listeners ---
screen.listen()
screen.onkey(paddle_right.go_up, key="Up")
screen.onkey(paddle_right.go_down, key="Down")
screen.onkey(paddle_left.go_up, key="w")
screen.onkey(paddle_left.go_down, key="s")

# --- Game Loop ---
game_running = True
while game_running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the top/bottom wall and bounce the ball.
    if ball.ycor() > (SCREEN_HEIGHT / 2) - BALL_WALL_OFFSET or \
       ball.ycor() < (SCREEN_HEIGHT / 2 * -1) + BALL_WALL_OFFSET:
        ball.bounce_y()

    # Detect collision with the paddles.
    if (ball.distance(paddle_right) < PADDLE_COLLISION_RANGE and ball.xcor() > PADDLE_X_BOUNDARY) or \
       (ball.distance(paddle_left) < PADDLE_COLLISION_RANGE and ball.xcor() < -PADDLE_X_BOUNDARY):
        ball.bounce_x()

    # Detect when paddle_right misses.
    if ball.xcor() > SCREEN_WIDTH / 2:
        scoreboard.add_point("left")
        ball.reset_position()

    # Detect when paddle_left misses.
    if ball.xcor() < SCREEN_WIDTH / 2 * -1:
        scoreboard.add_point("right")
        ball.reset_position()

# --- Exit ---
screen.exitonclick()
