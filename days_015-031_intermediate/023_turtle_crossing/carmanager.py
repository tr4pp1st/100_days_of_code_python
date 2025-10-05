import random
from turtle import Turtle


class CarManager:
    """Manages all cars that appear and move across the screen."""

    def __init__(self, config: dict):
        """Initialize the car manager with an empty list of cars."""
        self.config = config
        self.cars: list[Turtle] = []
        self.move_speed = self.config.get("car_speed_start", 0.2)

    def create(self) -> None:
        """Randomly create a new car and add it to the car list."""
        if random.randint(0, 2) == 1:
            new_car = Turtle(self.config.get("car_shape", "square"))
            new_car.penup()
            new_car.color(random.choice(
                self.config.get(
                    "car_colors",
                    ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'cyan',
                     'magenta', 'lime', 'teal', 'navy', 'maroon', 'olive', 'gold', 'silver']
                )))
            new_car.shapesize(
                stretch_wid=self.config.get("car_stretch_wid", 1.0),
                stretch_len=self.config.get("car_stretch_len", 2.0)
            )
            new_car.setposition(
                x=self.config.get("car_start_position_x", 300,),
                y=random.randint(
                    self.config.get("car_start_position_y_min", -150),
                    self.config.get("car_start_position_y_max", 150)
                )
            )
            self.cars.append(new_car)

    def move(self) -> None:
        """Move all cars to the left."""
        for car in self.cars:
            car.goto(car.xcor() - self.config.get("car_move_distance", 10), car.ycor())

    def remove_off_screen(self) -> None:
        """Remove cars that are off-screen."""
        self.cars = [car for car in self.cars if car.xcor() > -350]

    def check_collides_with_player(self, player) -> bool:
        """Check if any car collides with the player."""
        for car in self.cars:
            if car.distance(player) < 25:
                return True
        return False

    def increase_speed(self) -> None:
        """Increase car movement speed for higher difficulty."""
        self.move_speed *= self.config.get("car_speed_increase_factor", 0.9)
