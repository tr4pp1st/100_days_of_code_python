from turtle import Turtle

# --- Scoreboard Configuration ---
SCORE_COLOR = "white"
SCORE_FONT = ("Courier", 50, "normal")
SCORE_ALIGN = "center"
LEFT_SCORE_POSITION = (-100, 220)
RIGHT_SCORE_POSITION = (100, 220)


class Scoreboard(Turtle):
    """Display and update scores for left and right players in Pong."""

    def __init__(self):
        super().__init__()
        self.color(SCORE_COLOR)
        self.penup()
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Redraw the scores for both players."""
        self.clear()
        self.goto(LEFT_SCORE_POSITION)
        self.write(self.score_left, align=SCORE_ALIGN, font=SCORE_FONT)
        self.goto(RIGHT_SCORE_POSITION)
        self.write(self.score_right, align=SCORE_ALIGN, font=SCORE_FONT)

    def add_point(self, point_for: str):
        """Increase the score of the specified player ('left' or 'right')."""
        if point_for == "left":
            self.score_left += 1
        elif point_for == "right":
            self.score_right += 1
        self.update_scoreboard()
