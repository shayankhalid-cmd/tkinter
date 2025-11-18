from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
messagebox.showwarning("Window Name", "text to be displayed")
def msg():
    messagebox.showwarning("ALERT!!","VIRUS FOUND")
button = Button(root,text="Scan for virus",command=msg)
button.place(x=40,y=80)
root.mainloop()