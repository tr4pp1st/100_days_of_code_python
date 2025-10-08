# 100 Days of Code: Python
# Day 27 Project: Mile to Kilometer Converter

import tkinter
from tkinter import messagebox

MILES_TO_KM = 1.60934

CONFIG = {
    "window_title": "Miles to Km Converter",
    "window_min_width": 300,
    "window_min_height": 150,
    "window_padding_x": 20,
    "window_padding_y": 20,
    "window_background_color": "white",
    "label_font": ("Arial", 11, "normal"),
    "label_fg": "black",
    "label_bg": "white",
    "button_font": ("Arial", 11, "normal"),
    "button_fg": "black",
    "button_bg": "white",
}


def validate_miles_input() -> float:
    """
    Validate the input from the user.
    Returns the numeric value of miles as a float.
    Shows an error message if the input is invalid and returns 0.0 instead.
    """
    try:
        return float(input_miles.get().strip())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return 0.0


def convert_miles_to_km(miles: float):
    """ Convert miles to kilometers."""
    return miles * MILES_TO_KM


def update_label_result():
    """Update the result label with the calculated value."""
    miles = validate_miles_input()
    result = convert_miles_to_km(miles)
    label_km_result.config(text=f"{result:.2f}")


def create_label(text: str, column: int, row: int) -> tkinter.Label:
    """Create a label with standard styling and place it in the grid."""
    label = tkinter.Label(text=text)
    label.config(
        font=CONFIG.get("label_font"),
        fg=CONFIG.get("label_fg"),
        bg=CONFIG.get("label_bg")
    )
    label.grid(column=column, row=row)
    return label


def create_button(text: str, command, column: int, row: int, fg=None, bg=None) -> tkinter.Button:
    """Create a button with standard styling and place it in the grid."""
    button = tkinter.Button(text=text, command=command)
    button.config(
        font=CONFIG.get("button_font"),
        fg=fg if fg else CONFIG.get("button_fg"),
        bg=bg if bg else CONFIG.get("button_bg")
    )
    button.grid(column=column, row=row)
    return button


def exit_program():
    """Close the application window and terminate the program."""
    window.destroy()


# --- Window Setup ---

window = tkinter.Tk()
window.title(CONFIG.get("window_title"))
window.minsize(width=CONFIG.get("window_min_width"), height=CONFIG.get("window_min_height"))
window.config(
    bg=CONFIG.get("window_background_color"),
    padx=CONFIG.get("window_padding_x"),
    pady=CONFIG.get("window_padding_y")
)

# --- Widgets ---

input_miles = tkinter.Entry()
input_miles.focus()
input_miles.config(width=10)
input_miles.grid(column=1, row=0)

create_label(text="Miles", column=2, row=0)
create_label("is equal to", 0, 1)
create_label("Km", 2, 1)
label_km_result = create_label("0.00", 1, 1)

create_button("Calculate", update_label_result, 1, 2)

button_exit = create_button("Exit", exit_program, 3, 3)
button_exit.config(fg="black", bg="red", padx=10)

# --- Run Application ---
window.mainloop()
