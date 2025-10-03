import random
from turtle import Turtle


class Food(Turtle):
    """Represent the food object in the Snake game."""

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def get_food_position(self) -> tuple[int, int]:
        """Generate a random (x, y) position within the screen boundaries."""
        max_x = int(self.config["screen_width"] / 2 - 20)
        max_y = int(self.config["screen_height"] / 2 - 20)
        random_x = random.randint(max_x * -1, max_x)
        random_y = random.randint(max_y * -1, max_y)
        return random_x, random_y

    def refresh(self):
        """Move the food to a new random position."""
        self.goto(self.get_food_position())
