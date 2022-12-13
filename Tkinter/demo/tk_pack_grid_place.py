
from cProfile import label
from tkinter import *

window = Tk()
window.geometry("400x400")
lbl1 = Label(window, text="Kullanıcı Adı")
lbl2 = Label(window, text="Kullanıcı Adı")
lbl3 = Label(window, text="Kullanıcı Adı")

# lbl1.pack()
# lbl2.pack()
# lbl3.pack()

# lbl1.grid(column=0, row=0)
# lbl2.grid(column=1, row=0)
# lbl3.grid(column=2, row=0)

# lbl1.grid(column=0, row=0)
# lbl2.grid(column=0, row=1)
# lbl3.grid(column=0, row=2)

lbl1.place(x=10, y=10)
lbl2.place(x=10, y=50)
lbl3.place(x=10, y=100)


window.mainloop()