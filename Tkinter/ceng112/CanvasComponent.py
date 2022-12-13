from tkinter import *

class PaintBox(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("PaintBox")
        self.master.geometry("300x300")

        self.message = Label(self, text="Drag the mouse to draw")
        self.message.pack(side=BOTTOM)

        self.mycanvas = Canvas(self)
        self.mycanvas.pack(expand=YES, fill=BOTH)

        self.mycanvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 2)
        x2, y2 = (event.x + 1), (event.y + 2)
        self.mycancas.create_oval(x1, y1, x2, y2, fill="black")

    def main():
        PaintBox().mainloop()
    
    if __name__ == "__main__":
        main()