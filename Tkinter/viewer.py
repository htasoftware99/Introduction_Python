from logging import root
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")
root.iconbitmap("D:\Introduction_Python\Tkinter\images\image.ico")


my_img1 = ImageTk.PhotoImage(Image.open("images\images.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images\images.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images\images.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images\images.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward():
    return

def back():
    return

button_back = Button(root, text="<<", command=lambda: change_image(-1))
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: change_image(1))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()