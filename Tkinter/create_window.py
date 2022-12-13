from cProfile import label
import tkinter as tk
window = tk.Tk()
# <Design and Script>
window.title("My First GUI")  # title proje için isim veriyoruz
window.geometry("400x400+0+0") # geometry metodu proje için boyutlandırma yapar (0+0) ise ekranının hangi konumunda açılacağını belirler

label = tk.Label(text="Hello World", font="Verdana 22 bold") # label metodu ile label oluşturduk
label.pack() # pack metodu ile labelın ekrana yerleştirilmesi için kullanılır
# </Design and Script>
window.mainloop() # mainloop metodu projenin çalışmasını sağlar. Yani ana formun çalışmasını sağlar.



# componentleri oluşturmak için kullanılan metodlar
# pack() komponentleri paketliyor yani ekrana yerleştiriyor
# grid() komponentleri grid ile yerleştiriyor
# place() x,y koordinatlarına göre yerleştiriyor
