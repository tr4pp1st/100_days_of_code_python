from turtle import Turtle


class Scoreboard(Turtle):
    """Display the current level and game over message for the Turtle Crossing game."""

    def __init__(self, config: dict):
        """Initialize the scoreboard at the starting position and show the initial level."""
        super().__init__()
        self.config = config
        self.hideturtle()
        self.penup()
        self.color(self.config.get("sb_color", "black"))
        self.level = self.config.get("sb_start_level", 1)
        self.setposition(self.config.get("sb_start_position", (-280, 170)))
        self.update_level()

    def update_level(self):
        """Clear the previous level and write the current level."""
        self.clear()
        self.write(
            f"Level: {self.level}",
            align=self.config.get("sb_align", "left"),
            font=self.config.get("sb_font", ("Arial", 10, "bold"))
        )

    def increase_level(self):
        """Increment the level by one and update the display."""
        self.level += 1
        self.update_level()

    def game_over(self):
        """Display the 'GAME OVER' message at the center of the screen."""
        self.setposition(self.config.get("sb_game_over_position", (0, 0)))
        self.write(
            "GAME OVER",
            align=self.config.get("sb_game_over_align", "center"),
            font=self.config.get("sb_font", ("Arial", 10, "bold"))
        )
