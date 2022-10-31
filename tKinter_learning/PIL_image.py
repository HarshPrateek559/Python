from tkinter import *
from PIL import Image, ImageTk

window = Tk()

window.title("Image with PIL")

window.state("zoomed")

# To open a .jpg image, the Image module of the PIL library is used. To open an image with it, this is the way. The "open" function takes the name of the file as a string.
images = Image.open("D:\Software Development\Python\\tKinter_learning\Po.jpg")

# The resize function of the Image module changes the size of the image provided. To change the image, it has to be stored in a variable, here it is stored in it's original variable.
images = images.resize((640, 320))

# The ImageTk module of the PIL library modifies the image to be compatible with Tkinter. The PhotoImage function constructs an image that can be displayed on the window.
photo = ImageTk.PhotoImage(images)

# Images require a label to be displayed on the window. The Label widget can display an image with the image argument. This is the syntax:- Label(image = image_object_made_with_PhotoImage). This label when packed would show the image.
label = Label(image = photo)

label.pack()

window.mainloop()