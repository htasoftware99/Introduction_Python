from tkinter import *

class LabelDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Label Demo")
        self.Label1 = Label(self, text="Label with text")
        self.Label1.pack()

        self.Label2 = Label(self, text="Label with text and a bitmap")
        self.Label2.pack(side=LEFT)

        self.label3 = Label(self, bitmap="warning")
        self.label3.pack(side=LEFT)

   
LabelDemo().mainloop()


