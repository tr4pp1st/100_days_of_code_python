# 100 Days of Code: Python
# Day 26 Project: NATO Alphabet

import pandas

CONFIG = {
    "csv_file_path": "data/nato_phonetic_alphabet.csv"
}

# Load CSV into a DataFrame.
df = pandas.read_csv(CONFIG.get("csv_file_path"))

# Create a dictionary in the format: {"A": "Alfa", "B": "Bravo [...]}.
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Prompt the user to enter a word.
word = input("Enter a word: ")

# Use list comprehension to output a new list with the phonetic codes of the word.
# Example: Input: Mia -> Output: ['Mike', 'India', 'Alfa']
phonetic_list = [phonetic_dict[letter.upper()] for letter in word]
