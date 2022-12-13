
from cProfile import label
from tkinter import *

from numpy import pad

window = Tk()
window.title("Üyelik Formu")
window.geometry("500x350+600+300")
window.resizable(height=False, width=False)
window.iconbitmap("images\icn.ico")
window.configure(background="#D7C6EE")

frame1 = Frame(window, bg="#D7C6EE")
frame1.grid(column=0, row=0)

frame2 = Frame(window, bg="#D7C6EE")
frame2.grid(column=1, row=0)

frame3 = Frame(window, bg="#D7C6EE")
frame3.grid(column=2, row=0)

frame4 = Frame(window, bg="#D7C6EE")
frame4.grid(column=2, row=1)

lbl1 = Label(frame1, text = "Adınız", font = "Arial 15 bold", bg="#D7C6EE", padx=5, pady=5)
lbl1.pack()

lbl2 = Label(frame1, text = "Soyadınız", font = "Arial 15 bold", bg="#D7C6EE", padx=5, pady=5)
lbl2.pack()

lbl3 = Label(frame1, text = "Yaşınız", font = "Arial 15 bold", bg="#D7C6EE", padx=5, pady=5)
lbl3.pack()

lbl4 = Label(frame1, text = "Doğum", font = "Arial 15 bold", bg="#D7C6EE", padx=5, pady=5)
lbl4.pack()

lbl5 = Label(frame1, text = "Cinsiyet", font = "Arial 15 bold", bg="#D7C6EE", padx=5, pady=5)
lbl5.pack()

Label(frame2, text = ":", font="Arial 15 bold", bg="#D7C6EE", padx=5, pady=5).pack()
Label(frame2, text = ":", font="Arial 15 bold", bg="#D7C6EE", padx=5, pady=5).pack()
Label(frame2, text = ":", font="Arial 15 bold", bg="#D7C6EE", padx=5, pady=5).pack()
Label(frame2, text = ":", font="Arial 15 bold", bg="#D7C6EE", padx=5, pady=5).pack()
Label(frame2, text = ":", font="Arial 15 bold", bg="#D7C6EE", padx=5, pady=5).pack()

Entry(frame3, font="Arial 15 bold", bg="#ECE8F0").pack(padx=5, pady=5)
Entry(frame3, font="Arial 15 bold", bg="#ECE8F0").pack(padx=5, pady=5)


Button(window, text="Kaydet", font=("Arial 13 bold"), bg = "green", width=12).place(x=100, y=300)
Button(window, text="Temizle", font=("Arial 13 bold"), bg = "yellow", width=12).place(x=260, y=300)

photo = PhotoImage(file="images\prof.png")
photoResized = photo.subsample(4, 4)
Button(window, text="Yükle", image=photoResized, compound=TOP).place(x=400, y=40)

Spinbox(frame3, from_=18, to = 60, font=("Arial 12 bold"), bg="#ECE8F0", justify="center", width=23).pack(padx=5, pady=5)

optionList = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
sval = StringVar(frame3)
opt = OptionMenu(frame3, sval , *optionList)
opt.config(width=30)
opt.pack(padx=5, pady=5)
window.mainloop()
