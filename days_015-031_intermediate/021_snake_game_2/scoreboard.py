from turtle import Turtle


class Scoreboard(Turtle):
    """Display and update the game score and end-game message."""
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.score = 0
        self.color(self.config["scoreboard_color"])
        self.hideturtle()
        self.penup()
        self.goto(0, self.config["screen_height"] / 2 - self.config["scoreboard_offset"])
        self.update_scoreboard()

    def increase_score(self):
        """Increase score by 1 and update the scoreboard display."""
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear and redraw the current score."""
        self.clear()
        self.write(f"Score: {self.score}",
                   align=self.config["scoreboard_alignment"],
                   font=self.config["scoreboard_font"]
                   )

    def game_over(self):
        """Display the game over message using the configured settings."""
        self.goto(0, 0)
        self.write(self.config.get("game_over_text", "GAME OVER"),
                   align=self.config["scoreboard_alignment"],
                   font=self.config["scoreboard_font"]
                   )
