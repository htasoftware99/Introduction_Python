
from tkinter import *

window = Tk()

window.geometry("400x300")
sval = StringVar()
optionList = ["ocak", "şubat", "mart", "nisan", "mayıs", "haziran", "temmuz", "ağustos", "eylül", "ekim", "kasım", "aralık"]
opt1 = OptionMenu(window, sval, *optionList)
opt1.config(font=("Courier", 20, "italic", "underline"))
opt1.pack()
window.mainloop()