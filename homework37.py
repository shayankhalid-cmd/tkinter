from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("Inches to Centimeters Converter")
lbl1 = Label(root,text="enter the value of inches")
a_entry = Entry(root)
def display():
    a = int(a_entry.get())
    b = 2.54
    cm  = a * b
    message = "\n this is the amount of cm:"
    textbox.insert(END,message)
    textbox.insert(END,cm)
textbox = Text(bg = "#BEBEBE", fg = "black")
btn = Button(text="calculate",command=display)
lbl1.pack()
a_entry.pack()
btn.pack()
textbox.pack()
root.mainloop()