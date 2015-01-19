def hello():
    print('hello there')

from tkinter import *
root = Tk()
btn = Button(root, text="click me", command=hello)
btn.pack()

root.mainloop() # need this in visual studio -- IDLE does it for you automatically