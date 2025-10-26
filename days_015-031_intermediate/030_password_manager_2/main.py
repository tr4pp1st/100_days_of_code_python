# 100 Days of Code: Python
# Day 30 Project: Password Manager - Part 2


import tkinter
from tkinter import PhotoImage
from file_manager import FileManager
from entry import Entry
from password_generator import PasswordGenerator
from config import CONFIG
from tkinter import messagebox


def create_label(text: str, grid_column: int, grid_row: int) -> tkinter.Label:
    """Create a tkinter Label, set the text and grid position."""
    label = tkinter.Label(text=text)
    label.grid(column=grid_column, row=grid_row)
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


def search_password():
    website = entry_website.get().strip()
    user = entry_user.get().strip()
    if len(website) < CONFIG.get("website_len_min", 1) or len(user) < CONFIG.get("user_len_min", 1):
        messagebox.showinfo(title="Info", message="Please enter a valid website and user.")
    else:
        FileManager().search_password(website, user)


# --- UI Setup ---
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = PhotoImage(file="img/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

create_label("Website", 0, 1)

frame_website = tkinter.Frame(window)
frame_website.grid(column=1, row=1, sticky="ew")

frame_website.columnconfigure(0, weight=1)
frame_website.columnconfigure(1, weight=1)
frame_website.columnconfigure(2, weight=1)

entry_website = tkinter.Entry(frame_website, width=25)
entry_website.grid(column=0, row=0, sticky="we", padx=(0, 10))
entry_website.focus()

label_spacer_website = tkinter.Label(frame_website, text="")
label_spacer_website.grid(column=1, row=0)

button_search = tkinter.Button(frame_website, text="Search", width=18, command=search_password)
button_search.grid(column=2, row=0, sticky="e")

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
entry_password.grid(column=0, row=0, sticky="we", padx=(0, 10))

label_spacer = tkinter.Label(frame_password, text="")
label_spacer.grid(column=1, row=0)

button_password = tkinter.Button(frame_password, text="Generate Password", width=18, command=generate_password)
button_password.grid(column=2, row=0, sticky="e")

button_add = create_button("Add", 42, 1, 4, command=add_new_entry)

window.mainloop()
