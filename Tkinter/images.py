from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Images")
root.iconbitmap("D:\Introduction_Python\Tkinter\image.ico")

my_image = ImageTk.PhotoImage(Image.open("D:\Introduction_Python\Tkinter\bg.png"))
my_label = Label(image=my_image)
my_label.pack()

button_quit = Button(root, text="Quit", command=root.quit)
button_quit.pack()
root.mainloop()