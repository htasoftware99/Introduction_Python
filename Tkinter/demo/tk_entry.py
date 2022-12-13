from tkinter import *
from tkinter import font

window = Tk()

window.geometry("400x400")

Entry(window, font=("Arial 14 bold"), bg="blue", fg="white",
cursor="spider", relief=FLAT).pack()

Entry(window, show="*").pack()
Entry(window, selectbackground="yellow", selectforeground="green", selectborderwidth=4).pack()

svar = StringVar(window, value="Merhaba")
ent1 = Entry(window, textvariable=svar)
ent1.pack()


def clicked_button():
    print(ent1.get())
Button(window, text = "Click me!", command=lambda: print(svar.get())).pack()
window.mainloop()