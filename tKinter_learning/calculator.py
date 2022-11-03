from tkinter import *

expression = ""

def show(x):
    global expression
    expression = expression + str(x)
    variable.set(expression)

def evaluate():
        global expression
        variable.set(eval(expression))
        expression = ""

def makeBtn(x):
        myFont = ("Mono", 10, "bold")
        return Button(
        window,
        fg = 'black',
        bg = 'yellow',
        text = f"{x}",
        command = lambda: show(x),
        width = 9,
        height = 3, 
        font= myFont,
        )

def cleared():
        global expression
        expression = expression[0:(len(expression) - 1)]
        variable.set(expression)

def erase():
        global expression
        expression = ''
        variable.set('')

window = Tk()


# With the configure method, we can easily change the attributes of the window, or any widget for that matter.
window.configure(bg = "lightgreen")

window.resizable(0,0)

window.title("Calculator")

variable = StringVar()

entry = Entry(textvariable = variable, font=("MONO", 10, "bold"))

entry.grid(columnspan=4, ipady=10,ipadx=50)

one = makeBtn(1)

one.grid(row=2, column=0)

two = makeBtn(2)
two.grid(row=2, column=1)

three = makeBtn(3)
three.grid(row=2, column=2)

four = makeBtn(4)
four.grid(row=3, column=0)

five = makeBtn(5)
five.grid(row=3, column=1)

six = makeBtn(6)
six.grid(row=3, column=2)

seven = makeBtn(7)
seven.grid(row=4, column=0)

eight = makeBtn(8)
eight.grid(row=4, column=1)

nine = makeBtn(9)
nine.grid(row=4, column=2)

plus = makeBtn("+")
plus.grid(row=5, column=0)

subtract = makeBtn("-")
subtract.grid(row=5, column=1)

asterisk = makeBtn("*")
asterisk.grid(row=5, column=2)

slash = makeBtn("/")
slash.grid(row=6, column=0)

period = makeBtn(".")
period.grid(row=6, column=1)

zero = makeBtn(0)
zero.grid(row=6, column=2)

equal = Button(
        window,
        fg = 'black',
        bg = 'yellow',
        text = "=",
        command = lambda: evaluate(),
        width = 9,
        height = 3, 
        font= ("MONO", 10, "bold"),
        )
equal.grid(row=7, column=0)

AC = Button(
        window, 
        fg = 'white',
        bg = 'orange',
        text = "AC",
        command = lambda: cleared(),
        width = 9,
        height = 3, 
        font= ("MONO", 10, "bold"),
        )
AC.grid(row = 7, column= 1)

clear = Button(
        window,
        fg = 'white',
        bg = 'red',
        text = "Clear",
        command = lambda: erase(),
        width = 9,
        height = 3, 
        font= ("MONO", 10, "bold"),
)

clear.grid(row = 7, column = 2)

window.mainloop()