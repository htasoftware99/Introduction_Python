from pickle import FRAME
from tkinter import *
root_ex=Tk()
frame_1 = Frame(root_ex)
frame_1.pack()

redbutton = Button(frame_1, text="Red", fg="red", bg = "yellow", relief=FLAT)
redbutton.pack(side=RIGHT)

greenbutton = Button(frame_1, text="Brown", fg="brown")
greenbutton.pack(side=LEFT)

bluebutton = Button(frame_1, text="Blue", fg="blue")
bluebutton.pack(side=RIGHT)

frame_2 = Frame(root_ex)
frame_2.pack()
blackbutton = Button(frame_2, text="Black", fg="black")
blackbutton.pack()
root_ex.mainloop()