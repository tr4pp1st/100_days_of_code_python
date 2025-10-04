from turtle import Turtle

# --- Paddle Configuration ---
PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
PADDLE_STRETCH_WID = 5.0
PADDLE_STRETCH_LEN = 1.0
MOVEMENT_STEP = 20
MOVEMENT_LIMIT_UP = 240
MOVEMENT_LIMIT_DOWN = -240


class Paddle(Turtle):
    """Represents a paddle in the Pong game that can move up and down."""

    def __init__(self, position: tuple[int, int]):
        """Initialize the paddle at the given (x, y) position."""
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=PADDLE_STRETCH_WID, stretch_len=PADDLE_STRETCH_LEN)
        self.penup()
        self.setposition(position)

    def go_up(self):
        """Move the paddle up within the upper screen boundary."""
        if self.ycor() != MOVEMENT_LIMIT_UP:
            self.goto((self.xcor(), self.ycor() + MOVEMENT_STEP))

    def go_down(self):
        """Move the paddle down within the lower screen boundary."""
        if self.ycor() != MOVEMENT_LIMIT_DOWN:
            self.goto((self.xcor(), self.ycor() - MOVEMENT_STEP))
