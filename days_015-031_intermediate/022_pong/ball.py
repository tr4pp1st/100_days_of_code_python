import random
from turtle import Turtle

# --- Ball Configuration ---
BALL_SHAPE = "circle"
BALL_COLOR = "yellow"
BALL_START_POSITION_X = 0
BALL_RANDOM_Y_OFFSET = 200
MOVE_SPEED_START = 0.1
SPEED_INCREASE_FACTOR = 0.9
MOVE_DISTANCE_X = 10
MOVE_DISTANCE_Y = 10


class Ball(Turtle):
    """Represents the moving ball in the Pong game."""

    def __init__(self):
        """Initialize the ball at the start position and set its initial speed and direction."""
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.x_move = MOVE_DISTANCE_X
        self.y_move = MOVE_DISTANCE_Y
        self.move_speed = MOVE_SPEED_START

    def move(self):
        """Move the ball one step along its current trajectory."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Invert the vertical direction when hitting the top or bottom wall."""
        self.y_move *= -1

    def bounce_x(self):
        """Invert the horizontal direction and increase the ball speed when hitting a paddle."""
        self.x_move *= -1
        self.move_speed *= SPEED_INCREASE_FACTOR

    def reset_position(self):
        """
        Reset the ball to the center (with random vertical offset), reverse direction,
        and reset speed after a missed hit.
        """
        random_y = random.randint(-BALL_RANDOM_Y_OFFSET, BALL_RANDOM_Y_OFFSET)
        self.setposition(BALL_START_POSITION_X, random_y)
        self.bounce_x()
        self.move_speed = MOVE_SPEED_START
