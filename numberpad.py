from tkinter import*
root = Tk()
root.title("Number pad")
root.geometry("250x300")
frame = Frame(master=root,height=200,width=360,bg="#0defff")
nums = [[9,8,7],[6,5,4],[3,2,1],["#","0","*","+","-","X"]]
for i in range(4):
    root.columnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=50)
    for j in range(0,3):
        frame=Frame(master=root,relief=RAISED,borderwidth=1)
        frame.grid(row=i,column=j)
        label= Label(master=frame,text=nums[i][j],bg="#F1E8E8")
        label.pack(padx=3,pady=3)
root.mainloop()