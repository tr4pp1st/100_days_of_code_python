# 100 Days of Code: Python
# Day 29 Project: Password Manager

# This is a small example project from Day 29 of 100 Days of Code.
# It is meant as a learning exercise and can be expanded with additional features.
# Important notes for production use have been added at relevant places in the code.

import tkinter
from tkinter import PhotoImage
from file_manager import FileManager
from entry import Entry
from password_generator import PasswordGenerator

CONFIG = {
    # NOTE: In production, this value should come from an environment variable instead of being hardcoded.
    "user_mail_standard_value": "testuser@testmail.com"
}


def create_label(text: str, grid_column: int, grid_row: int) -> tkinter.Label:
    """Create a tkinter Label, set the text and grid position."""
    label = tkinter.Label(text=text)
    label.grid(column=grid_column, row = grid_row)
    return label


def create_entry(width: int, grid_column: int, grid_row: int) -> tkinter.Entry:
    entry = tkinter.Entry(width=width)
    entry.grid(column=grid_column, row=grid_row)
    return entry


def create_button(text: str, width: int, grid_column: int, grid_row: int, command) -> tkinter.Button:
    button = tkinter.Button(text=text, width=width, command=command)
    button.grid(column=grid_column, row=grid_row)
    return button


def add_new_entry():
    new_entry = Entry(entry_website.get(), entry_user.get(), entry_password.get())
    FileManager().save_new_entry(new_entry)
    clean_up_entry_widgets()


def generate_password():
    entry_password.delete(0, tkinter.END)
    password = PasswordGenerator().generate_password()
    entry_password.insert(0, password)


def clean_up_entry_widgets():
    entry_website.delete(0, tkinter.END)
    entry_password.delete(0, tkinter.END)
    entry_website.focus()


# --- UI Setup ---
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = PhotoImage(file="img/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

create_label("Website", 0, 1)
entry_website = create_entry(50, 1, 1)
entry_website.focus()

create_label("Email/Username", 0, 2)
entry_user = create_entry(50, 1, 2)
entry_user.insert(0, CONFIG.get("user_mail_standard_value", ""))

create_label("Password", 0, 3)

frame_password = tkinter.Frame(window)
frame_password.grid(column=1, row=3, sticky="ew")

frame_password.columnconfigure(0, weight=1)
frame_password.columnconfigure(1, weight=1)
frame_password.columnconfigure(2, weight=1)

entry_password = tkinter.Entry(frame_password, width=25)
entry_password.grid(column=0, row=0, sticky="w", padx=(0, 10))

label_spacer = tkinter.Label(frame_password, text="")
label_spacer.grid(column=1, row=0)

button_password = tkinter.Button(frame_password, text="Generate Password", command=generate_password)
button_password.grid(column=2, row=0, sticky="e")

button_add = create_button("Add", 42, 1, 4, command=add_new_entry)

window.mainloop()
