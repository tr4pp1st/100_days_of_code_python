from turtle import Turtle


class Player(Turtle):
    """Represents the player character that moves upward to cross the road."""

    def __init__(self, config: dict):
        """Initialize the player at the starting position, facing upward."""
        super().__init__()
        self.config = config
        self.shape(self.config.get("player_shape", "turtle"))
        self.color(self.config.get("player_color", "aqua"))
        self.penup()
        self.setheading(self.config.get("player_heading", 90))
        self.move_distance = self.config.get("player_move_distance", 10)
        self.reset_position()

    def go_up(self):
        """Move the player upward by a fixed distance."""
        self.goto(self.xcor(), self.ycor() + self.move_distance)

    def reset_position(self):
        """Return the player to the starting position."""
        self.goto(self.config.get("player_start_position", (0, -180)))
