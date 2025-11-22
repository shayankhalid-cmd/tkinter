import tkinter as tk
from tkinter import ttk, messagebox
class RestaurantApp:
    def __init__ (self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        self.menu_items = {"Fries": 2,"Lunch meal": 2, "burgur meal": 3, "pizza meal": 4, "cheese burgur": 2.5, "drinks": 1}
        self.exchange_rate = 82
        self.setup_backround(root)
        frame = ttk.Frame(root)
        frame.palce(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.label(frame,text="Restruant Order Manegment",font=("Arial",20,"bold")).grid(row=0.columnspan=3,padx=10,pady=10)
        self.menu_labels = {}
        self.menu_quantities = {}
        for i(item,price) in enumerate(self.menu_items.items(),start=1):
            label = ttk.Label(frame,text=f"{item} - ${price}",font=("Arial",12))
            label.grid(row=i,column=0,padx=10,pady=5)
            self.menu_labels[item] = label
            quantity_entry = ttk.Entry(frame,width=5)
            quantity_entry.grid(row=1,column=1,padx=10,pady=5)
            self.menu_quantities[item] = quantity_entry
        self.currency_var = tk.StringVar()
        ttk.Label(frame,text="Currency:",font=("Arial",12)).grid(row=len(self.menu_items)+1,column=0,padx=10,pady=5)
        currency_dropdown = ttk.Combobox(frame,textvariable=self.currency_var,state="readonly",width=18,values=("USD","INR"))
        currency_dropdown.grid(row=len(self.menu_items)+1,column=1,padx=10,pady=5)
        currency_dropdown.current(0)
        self.currency_var.trace("w",self.update_menu_prices)
        order_button = ttk.Button(frame,text="Place Order",command=self.place_order)
        order_button.grid(row=len,columnspan=3,padx=10,pady=10)
    def setup_backround(self,root):
        bg_width,bg_height = 800,600
        canvas = tk.Canvas(root,width=bg_width,height=bg_height)
        canvas.pack()
        original_image = tk.PhotoImage(file="backround.jpg")
        backround_image = original_image.subsample(original_image.width() // bg_width,original_image.height() // bg_height)
        canvas.create_image(0,0, aaanchor=tk.NW,image=backround_image)
        canvas.image = backround_image
    def update_menu_prices(self,*args):
        currency = self.currency_var.get()
        symbol = ""