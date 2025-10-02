from turtle import Turtle


class Snake:
    def __init__(self, config):
        """Initialize the Snake with a starting body and head segment."""
        self.config = config
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake body from the starting positions."""
        for position in self.config["starting_positions"]:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a segment to the snake at the given (x, y) position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        """Move the snake forward by shifting each segment to the position of the previous one."""
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(new_x, new_y)
        self.head.forward(self.config["move_distance"])

    def up(self):
        """Change direction: move up if not currently moving down."""
        if self.head.heading() != self.config["down"]:
            self.head.setheading(self.config["up"])

    def down(self):
        """Change direction: move down if not currently moving up."""
        if self.head.heading() != self.config["up"]:
            self.head.setheading(self.config["down"])

    def left(self):
        """Change direction: move left if not currently moving right."""
        if self.head.heading() != self.config["right"]:
            self.head.setheading(self.config["left"])

    def right(self):
        """Change direction: move right if not currently moving left."""
        if self.head.heading() != self.config["left"]:
            self.head.setheading(self.config["right"])
