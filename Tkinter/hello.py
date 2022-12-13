from tkinter import * 
root = Tk()
root.title("Hello World")

# Create a label widget
myLabel = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Hasan")
myLabel3 = Label(root, text="")

# Pack the label widget
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=1, column=1)

root.mainloop()