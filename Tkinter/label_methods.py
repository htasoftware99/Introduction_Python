import tkinter as tk

window = tk.Tk()

window.title("My First GUI")
window.geometry("300x300")

label1 = tk.Label(text="Etiket1", font="Verdana 22 bold", bg="yellow", fg="red")
label1.pack(side="left")

label2 = tk.Label(text="Etiket2", font="Verdana 22 bold", bg="red", fg="yellow")
label2.pack(side="right")

label3 = tk.Label(text="Etiket3", font="Verdana 22 bold", bg="blue", fg="green")
label3.pack(fill="x")

label4 = tk.Label(text="Etiket4", font="Verdana 22 bold", bg="purple", fg="yellow")
label4.pack(expand= "yes")

window.mainloop()

window2 = tk.Tk()
window2.title("2. window")
label5 = tk.Label(text="Etiket5", font="Verdana 22 bold", bg="yellow", fg="red")
label5.grid(row=0, column=0)

window2.mainloop()

window3 = tk.Tk()
window3.title("3. window")
window3.geometry("300x300")
label6 = tk.Label(text="Etiket6", font="Verdana 22 bold", bg="yellow", fg="red")
label6.place(x=20, y=20)
window3.mainloop()