import tkinter as tk
from tkinter.ttk import *

def SecimAl():
    print(combo.get())
window = tk.Tk()
window.title("Combobox Component")

combo = Combobox()
combo['values'] = ("Ankara", "İstanbul", "İzmir", "Antalya", "Bursa", "Konya", "Trabzon")
combo.current(0)
combo.place(x=20, y=20)

button = tk.Button(text="Seç", command= SecimAl)
button.place(x=20, y=60)
window.mainloop()