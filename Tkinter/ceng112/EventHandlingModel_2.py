from tkinter import *

root = Tk()
root.title("Event Handling Model")

def motion(event):
    print("Mouse position: (%s %s)" % (event.x, event.y))
    return

my_message = "it is my life, it is now or never, I am gonna be forever"
msg = Message(root, text=my_message)
msg.config(bg="lightgreen", font=("times", 24, "italic"))
msg.pack()
msg.bind("<Motion>", motion)
root.mainloop()