# 100 Days of Code: Python
# Day 28 Project: Pomodoro App

import tkinter
import math

# --- Constants ---
PINK = "#E2979C"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#F7F5DD"
FONT_NAME = "Courier"
WORK_MIN = 0.1  # 25 minutes in production
SHORT_BREAK_MIN = 0.04  # 5 minutes in production
LONG_BREAK_MIN = 0.07  # 20 minutes in production

# --- Global Variables ---
reps = 0
timer = ""


# --- Timer Reset ---
def timer_reset():
    """Reset the timer and all UI elements."""
    global reps
    if timer:
        window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer", fg=GREEN)
    label_checkmarks.config(text="")


# --- Timer Start ---
def timer_start():
    """Start the timer and determine the current session type."""
    global reps
    reps += 1

    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    if reps > 8:
        timer_reset()
        return

    if reps % 8 == 0:
        label_title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label_title.config(text="Work", fg=GREEN)
        count_down(work_sec)


# --- Countdown ---
def count_down(count):
    """Perform countdown and update UI every second."""
    minutes = count // 60
    seconds = count % 60
    time_str = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=time_str)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        # Add checkmark after completing a work session
        if reps % 2 == 0:
            checkmarks = "✔" * math.floor(reps / 2)
            label_checkmarks.config(text=checkmarks)


# --- UI Setup ---
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_title = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label_title.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="img/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = tkinter.Button(text="Start", command=timer_start)
button_start.grid(column=0, row=2)

button_reset = tkinter.Button(text="Reset", command=timer_reset)
button_reset.grid(column=2, row=2)

label_checkmarks = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "normal"))
label_checkmarks.grid(column=1, row=3)

window.mainloop()
