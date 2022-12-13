
from tkinter import *

window = Tk()

window.geometry("400x300")

sval = StringVar(value=20)
Spinbox(window, from_=18, to=30, increment=5, cursor="pirate",
bd=5, justify=CENTER, state="disabled", textvariable=sval).pack()

window.mainloop()