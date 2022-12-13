
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x300")

def clicked_button():
    #messagebox.showinfo("Bilgi", "Information")
    #messagebox.showwarning("Uyarı", "Warning")
    #messagebox.askquestion("Soru", "Eminmisin")
    #messagebox.askokcancel("Soru", "Do you want to quit?")
    #messagebox.askretrycancel("Hata", "Hata oluştu")
    #messagebox.askyesno("Soru", "Eminmisin")
    messagebox.askyesnocancel("Soru", "Eminmisin")
Button(window, text="Click me", command=clicked_button).pack()
window.mainloop()