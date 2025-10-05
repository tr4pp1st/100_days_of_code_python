# 100 Days of Code: Python
# Day 24 Project: Mail Merge

from pathlib import Path

PLACEHOLDER = "[name]"

""" Version during the course.
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
"""

""" Refactored version """
# Define paths.
base_dir = Path(__file__).parent
names_path = base_dir / "Input" / "Names" / "invited_names.txt"
letter_template_path = base_dir / "Input" / "Letters" / "starting_letter.txt"
output_dir = base_dir / "Output" / "ReadyToSend"

# Ensure output directory exits.
output_dir.mkdir(parents=True, exist_ok=True)

# Read names.
with names_path.open() as file:
    names = [name.strip() for name in file.readlines()]

# Read letter template.
template = letter_template_path.read_text()

# Generate personalized letters.
for name in names:
    personalized = template.replace(PLACEHOLDER, name)
    output_file = output_dir / f"letter_for_{name}.txt"
    output_file.write_text(personalized)
