from operator import index
from tkinter import *

border_effects = {
    "flat": FLAT,
    "raised": RAISED,
    "sunken": SUNKEN,
    "groove": GROOVE,
    "ridge": RIDGE,
}

window = Tk()

for relief_name, index in border_effects.items():
    frame = Frame(window, relief=index, borderwidth=5)
    frame.pack(side=LEFT)
    label = Button(master=frame, text=relief_name)
    label.pack()

window.mainloop()