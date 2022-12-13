
from tkinter import *

window = Tk()
window.title("tkinter")
window.configure(background="#2FC9E0") # background yerine bg yazılabilir
#window.geometry("400x400+600+400")
window.iconbitmap("images\image.ico")
window.attributes("-alpha", 0.5) # transparanlık
window.attributes("-topmost", True) # daima üstte görünür
window.resizable(height=False, width=False) # yükseklik ve genişlik değiştirilemez
#window.minsize(width=400, height=400) # minimum boyut
#window.maxsize(width=400, height=400) # maksimum boyut
window.attributes("-fullscreen", True) # tam ekran
window.bind("<Escape>", lambda event: window.attributes('-fullscreen', False)) # escape tuşu ile tam ekrandan çıkılabilir
window.bind("<F11>", lambda event: window.attributes('-fullscreen', True)) # f11 tuşu ile tam ekrana geçilebilir
window.mainloop()