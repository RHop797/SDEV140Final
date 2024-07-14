import tkinter as tk
from tkinter import ttk

class Window:
    def __init__(self, master):
        self.master=master
        self.notebook = ttk.Notebook(self.master, width = 300, height = 200)

        self.frame1= ttk.Frame(self.notebook)
        self.frame2= ttk.Frame(self.notebook)
        self.frame3= ttk.Frame(self.notebook)

        self.label1= ttk.Label(self.frame1, text= "Schedule Delivery")
        self.label2= ttk.Label(self.frame2, text= "Cancel Delivery")
        self.label3= ttk.Label(self.frame3, text= "View Delivery Schedule")

        self.label1.pack(padx=10, pady=10)
        self.label2.pack(padx=10, pady=10)
        self.label3.pack(padx=10, pady=10)

        self.frame1.pack(padx = 5, pady = 5)
        self.frame2.pack(padx = 5, pady = 5)
        self.frame3.pack(padx = 5, pady = 5)

        self.notebook.add(self.frame1, text = "Schedule Delivery")
        self.notebook.add(self.frame2, text = "Cancel Delivery")
        self.notebook.add(self.frame3, text = "View Delivery Schedule")

root = tk.Tk()
window = Window(root)
root.mainloop()