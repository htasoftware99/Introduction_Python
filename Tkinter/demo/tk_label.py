
from tkinter import *

window = Tk()
window.geometry("400x500")

label1 = Label(window, text="tkinter label", font=("times", 20, "bold"), fg="red", bg="yellow", cursor="spider", wraplength=200)
label1.pack()
label2 = Label(window, text="tkinter label", font="Arial 15 bold underline italic", fg="purple", bg="green", cursor="man", bitmap="error")
label2.pack()
photo = PhotoImage(file="images\img.jpg")
label3 = Label(window, text="Python Tkinter", font="Ariel 25", image=photo)
label3.pack()
window.mainloop()