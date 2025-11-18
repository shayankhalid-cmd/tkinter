from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("Getting started with widgets")
lbl1 = Label(root,text="enter a value")
lbl2 = Label(root,text="enter b value")
a_entry = Entry(root)
b_entry = Entry(root)
def display():
    a = int(a_entry.get())
    b = int(b_entry.get())
    product = a * b
    message = "\n the product of a and b is:"
    textbox.insert(END,message)
    textbox.insert(END,product)
textbox = Text(bg = "#BEBEBE", fg = "black")
btn = Button(text="calculate product",command=display)
lbl1.pack()
a_entry.pack()
lbl2.pack()
b_entry.pack()
btn.pack()
textbox.pack()
root.mainloop()