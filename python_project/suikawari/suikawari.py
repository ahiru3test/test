import random
from tkinter import *
from tkinter import ttk

print(random.randrange(0,5))
#handler
def btn_clicked():
    print("Button Clicked")

def key_handler(e):
    print(e.keycode)

#window
app = Tk()
app.geometry("300x200")
app.title("test app")

#textbox
txt = Entry(app)
txt.place(x=20,y=20,width=150,height=30)
#txt.bind("<KeyPress>", key_handler)
app.bind("<KeyPress>", key_handler)

#main loop
app.mainloop()

