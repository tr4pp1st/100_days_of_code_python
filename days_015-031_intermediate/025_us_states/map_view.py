import turtle


class MapView:
    """Handles the visual part of the U.S. States game using the turtle module."""

    def __init__(self, image_path: str):
        self.screen = turtle.Screen()
        self.screen.title("U.S. States Game")
        self.screen.addshape(image_path)
        turtle.shape(image_path)

    def prompt_for_state(self, correct_count: int):
        """Ask user to name a state via input dialog."""
        return self.screen.textinput(
            title=f"{correct_count}/50 States Correct",
            prompt="What's another state's name?"
        )

    def mark_state(self, state_name: str, x: int, y: int):
        """Write the guessed state name on the map."""
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(x, y)
        marker.write(
            state_name,
            align="center",
            font=("Arial", 8, "normal")
        )

    def exit_on_click(self):
        """Exit the game when the map is clicked."""
        self.screen.exitonclick()
