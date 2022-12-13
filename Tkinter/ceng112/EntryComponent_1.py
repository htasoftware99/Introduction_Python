from tkinter import *

master = Tk()

master.geometry("250x250")
frame_1 = Frame(master)
frame_1.pack()
lbl1 = Label(frame_1, text="First Name")
lbl1.pack(side=LEFT)
e1 = Entry(frame_1)
e1.pack(side=LEFT)

frame_2 = Frame(master)
frame_2.pack()
lbl2 = Label(frame_2, text="Last Name")
lbl2.pack(side=LEFT)
e2 = Entry(frame_2)
e2.pack(side=LEFT)

master.mainloop()
