from tkinter import Y


x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and z:
    print(3)
else:
    print(4)