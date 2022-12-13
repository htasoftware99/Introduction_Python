
from tkinter import *

window = Tk()
window.geometry("300x300")
frame1 = Frame(window, height=100, width=100, bg="red",
               highlightthickness=5, highlightbackground="blue", cursor="spider",
               padx=10, pady=10)
frame1.pack()

lbl1 = Label(frame1, text="Label1")
lbl1.place(x=10, y=10)
window.mainloop()