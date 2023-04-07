import tkinter

from tkinter import ttk

window = tkinter.Tk()

window.state("zoomed")

window.title("Notepad")

# create a menu bar
menu_bar = tkinter.Menu(window)

# implement a cut button to cut the text
def cut():
    text.event_generate("<<Cut>>")

# implement a copy button to copy the text
def copy():
    text.event_generate("<<Copy>>")

# implement a paste button to paste the text
def paste():
    text.event_generate("<<Paste>>")
    
# implement a about button to show the about message
def about():
    tkinter.messagebox.showinfo("About", "This is a simple notepad")

window.config(menu=menu_bar)


# implement a save button to save the text
def save():
    with open("text.txt", "w") as f:
        f.write(text.get(1.0, tkinter.END))

# implement a clear button to clear the text
def clear():
    text.delete(1.0, tkinter.END)

# implement a open button to open the text
def open_file():
    with open("text.txt", "r") as f:
        text.delete(1.0, tkinter.END)
        text.insert(1.0, f.read())

# create a file menu
file_menu = tkinter.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Clear", command=clear)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# create a edit menu
edit_menu = tkinter.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# create a help menu
help_menu = tkinter.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# create a text area
text = tkinter.Text(window, font=("Arial", 12), wrap='word')
text.pack(fill=tkinter.BOTH, expand=True)

# make a tkinter button at the top of the window to save the text. have dimensions of 10x1
save_button = tkinter.Button(
    window,
    text = "Save",
    command = save,
    width = 10,
    height = 1
    )

# make a tkinter button at the top of the window to clear the text. have dimensions of 10x1
clear_button = tkinter.Button(
    window,
    text = "Clear",
    command = clear,
    width = 10,
    height = 1
    )

# make a tkinter button at the top of the window to open the text. have dimensions of 10x1
open_button = tkinter.Button(
    window,
    text = "Open",
    command = open_file,
    width = 10,
    height = 1
    )

window.mainloop()
