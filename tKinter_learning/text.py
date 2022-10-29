# This line imports everything from the module.
from tkinter import *

window = Tk()

# This line sets the title of the GUI Application
window.title("NotePad")

# This is the implementation of a button that can close a window.
button = Button(window, text="Close", command=window.destroy, foreground = "white",  background="red", font=("Times", 20, "bold"))

# This line creates a textbox in the window.
text = Text(
    font = ("Times", 20, "italic"), # This line is manipulates the font and text of the textbox
    )

entry = Entry(foreground="black", background="white", width='40')

entry.pack()
button.pack()
text.pack()

# This line inserts some text in the widget after rendering it on the screen.
entry.insert(0,"What's your name?")

window.mainloop()