import tkinter as tk

def topla():
    num1 = float(number1.get())
    num2 = float(number2.get())
    result['text'] = str(num1 + num2)

def cikar():
    num1 = float(number1.get())
    num2 = float(number2.get())
    result['text'] = str(num1 - num2)

def carp():
    num1 = float(number1.get())
    num2 = float(number2.get())
    result['text'] = str(num1 * num2)

def bol():
    num1 = float(number1.get())
    num2 = float(number2.get())
    result['text'] = str(num1 / num2)

window = tk.Tk()
window.title("Button Entry")
window.geometry("300x300")

number1 = tk.Entry(width=10)
number1.place(x=20, y=20)

number2 = tk.Entry(width=10)
number2.place(x=100, y=20)

result = tk.Label(text="Sonuç", font="Verdana 18 bold", bg="gray", fg="white")
result.place(x=180, y=20)

btntopla = tk.Button(text="+", font="Verdana 15 bold", bg="gray", fg="white", command=topla)
btntopla.place(x=20, y=70)

btncikar = tk.Button(text="-", font="Verdana 15 bold", bg="gray", fg="white", command=cikar)
btncikar.place(x=80, y=70)

btncarp = tk.Button(text="x", font="Verdana 15 bold", bg="gray", fg="white", command=carp)
btncarp.place(x=140, y=70)

btnbol = tk.Button(text="/", font="Verdana 15 bold", bg="gray", fg="white", command=bol)
btnbol.place(x=200, y=70)
window.mainloop()