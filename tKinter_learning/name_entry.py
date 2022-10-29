# The tkinter module is used to make GUI with Python.
import tkinter as tk

# the Tk function of tkinter module is used to make the window object.
window = tk.Tk()

name = tk.Label(text="Name")
# This widget creates a little text input box for 
entry = tk.Entry()

input = entry.get()

print(input)

# Label is like a holder for text that is to be shown on the GUI window
greetings = tk.Label(
    text="Hello, Tkinter. This is an adaptation of GUI in Python", # this line defines the text which is to be shown.
    # fg="white", this line sets the color of the text
    # bg="black"  this line sets the background color of the text
    )

buttons = tk.Button(text="Click me")

# The pack function appends the widget to the window. These widgets would be rendered in the order they are packed on the screen.

greetings.pack()
name.pack()
entry.pack()
buttons.pack()

# the mainloop function keeps the window open. Without this function, the program would finish execution without giving it enough time to open the window.
window.mainloop()