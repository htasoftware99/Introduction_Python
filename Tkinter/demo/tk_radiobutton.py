
from tkinter import *

window = Tk()

window.geometry("400x400")

ivar = IntVar()
rbtn1 = Radiobutton(window, text="Seçim 1", padx=20, variable=ivar, value=1).pack()
rbtn2 = Radiobutton(window, text="Seçim 2", padx=20, variable=ivar, value=2).pack()

window.mainloop()