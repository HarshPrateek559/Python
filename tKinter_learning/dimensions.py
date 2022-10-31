from tkinter import *
from tkinter.font import BOLD

window = Tk()

window.title("LearningPythonWithTKinter")

window['bg'] = "black"

# This line sets the default size of the tkinter window. syntax:- window.geometry("widthxheight")
window.geometry("800x600")

# This line sets the minimum size of the tkinter window. syntax:- window.minsize(width, height)
window.minsize(480, 360)

# This line sets the maximum size of the tkinter window. syntax:- window.maxsize(width, height)
# window.maxsize(1280, 720)

# The state function of window object when set to "zoomed" would open the tkinter window in fullscreen by default.
window.state("zoomed")

button = Button(
    text="Close", 
    width="5", 
    height="1", 
    foreground="white", 
    background="red", 
    font=("Times", 12, BOLD),
    command=window.destroy
    )


button.pack()
window.mainloop()