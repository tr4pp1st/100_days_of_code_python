import tkinter


# Simple function using *args
def add(*args):
    return sum(args)


print(add(2, 4, 5, 6, 7))


# Function demonstrating **kwargs usage
def calculate(n, **kwargs):
    # for (key, value) in kwargs.items():
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=5, multiply=2)


# --- GUI Playground ---

def button_clicked():
    print("button_clicked was triggered")
    label.config(text=input_.get())


window = tkinter.Tk()
window.title("Tk window title")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# --- Label ---
label = tkinter.Label(text="label start text", font=("Arial", 5, "bold"))
# label["text"] = "label text"
label.config(fg="green", padx=20, pady=20)
label.grid(column=0, row=0)
# label.pack(side="bottom")

# --- Buttons ---
button = tkinter.Button()
button.config(
    text="button start text",
    fg="blue",
    bg="red",
    command=button_clicked
)
button.grid(column=2, row=0)
# button.pack()

button2 = tkinter.Button()
button2.config(
    text="button2 start text",
    fg="yellow",
    bg="black",
    command=button_clicked
)
button2.grid(column=1, row=1)

# --- Entry ---
input_ = tkinter.Entry(width=25)
input_.grid(column=3, row=3)
# input.place(x=0, y=0)
print(input_.get())

# -- Textbox ---
textbox = tkinter.Text(width=30, height=5)
textbox.focus()
# textbox.insert(tkinter.END, "Example of multi-line text entry.")
textbox.insert("end", "Example of multi-line text entry.")
textbox.grid(column=0, row=4)
# Prints partial content.
print(textbox.get(1.0, 1.5))


# --- Spinbox ---
def spinbox_used():
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=0, row=5)


# --- Scale ---
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.grid(column=0, row=6)


# -- Checkbutton ---
def checkbutton_used():
    print(checked_state.get())


checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.grid(column=0, row=7)


# --- Radiobuttons ---
def radio_used():
    print(radio_state.get())


radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=0, row=8)
radiobutton2.grid(column=0, row=9)


# --- Listbox ---
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=0, row=10)

# --- Run App ---
window.mainloop()
