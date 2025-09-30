# 100 Days of Code: Python
# Day 18 Project: The Hirst Painting Project

import colorgram
import turtle as turtle_module
import random


IMAGE_NAME = "damien_hirst_example_(self-created).jpg"
NUMBER_OF_DOTS = 100
DOTS_PER_ROW = 10
DOT_SIZE = 20
SPACING = 50


def extract_colors(image_path: str, num_colors: int = 10, tolerance: int = 240):
    """
    Extract a limited number of dominant RGB colors from an image,
    while ignoring the background (tolerance).
    """
    rgb_colors = []
    while len(rgb_colors) < num_colors:
        # Extract up to 100 colors from the image.
        # colorgram might return duplicates or too many background-like colors.
        raw_colors = colorgram.extract(image_path, 100)

        for color in raw_colors:
            r, g, b = color.rgb

            # Skip colors that are too close to the background (tolerance).
            if r > tolerance and g > tolerance and b > tolerance:
                continue

            rgb_colors.append((r, g, b))

    # rgb_colors might contain more colors than we need.
    # Using list slicing to cut the list down to the desired size.
    return rgb_colors[:num_colors]


# NOTE (Clean Code best practice):
# This function has many parameters (number_of_dots, dots_per_row, dot_size, spacing).
# In production code, it's often better to wrap these values into a configuration object
# or a dedicated class (e.g. DotGridConfig). That makes the function easier to extend
# and maintain.
# This is Day 18 of "100 Days of Code", the main goal is to practice Python.
def draw_dots(turtle, colors: list,
              number_of_dots: int = NUMBER_OF_DOTS,
              dots_per_row: int = DOTS_PER_ROW,
              dot_size: int = DOT_SIZE,
              spacing: int = SPACING
              ):
    """
    Draws a grid of colored dots using the provided turtle.

    Each dot is drawn with a random color from the given list.
    The turtle moves forward after each dot and jumps to the next line
    once a full row of dots is completed.

    Parameters:
        turtle: The turtle object used to draw the dots.
        colors (list): A list of RGB tuples to choose dot colors from.
        number_of_dots (int): Total number of dots to draw.
        dots_per_row (int): Number of dots in each row before moving to the next line.
        dot_size (int): The diameter of each dot in pixels.
        spacing (int): The distance between the centers of two consecutive dots.
    """
    for dot_count in range(1, number_of_dots + 1):
        turtle.dot(dot_size, random.choice(colors))
        turtle.forward(spacing)

        if dot_count % dots_per_row == 0:
            turtle.setheading(90)
            turtle.forward(spacing)
            turtle.setheading(180)
            turtle.forward(spacing * dots_per_row)
            turtle.setheading(0)


# Project part 1: Extract rgb values from an image.
# https://pypi.org/project/colorgram.py/
color_list = extract_colors(IMAGE_NAME, num_colors=20)

# Project part 2: Drawing the dots
# https://docs.python.org/3/library/turtle.html#turtle.dot

turtle_module.colormode(255)
painter = turtle_module.Turtle()

painter.speed("fastest")
painter.penup()
painter.hideturtle()
painter.setheading(225)
painter.forward(300)
painter.setheading(0)

draw_dots(painter, color_list)

screen = turtle_module.Screen()
screen.exitonclick()
