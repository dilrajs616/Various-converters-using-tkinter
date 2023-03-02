from tkinter import *
from tkinter import ttk

root = Tk()

img = PhotoImage(file="images\doge-small-size.gif")
Label(root, image=img).grid(row=0, column =1)

def metricChanged():
    Label = ttk.Label(root, textvariable=measureSystem).grid(row=1, column=1, sticky = (E))

measureSystem = StringVar()
check = ttk.Checkbutton(root, text='Use Metric', 
	    command=metricChanged, variable=measureSystem,
	    onvalue='metric', offvalue='imperial')
check.grid(row=1, column=1, sticky = (W))

ttk.Label(root, text="Choose the base").grid(row=2, column=1, sticky = W)

baseNumber = StringVar()
ttk.Radiobutton(root, text=2, variable=baseNumber, value='2')
ttk.Radiobutton(root, text=8, variable=baseNumber, value='8')
ttk.Radiobutton(root, text=16, variable=baseNumber, value='16')

def display():
    print("This function is invoked")


combo = ttk.Combobox(root, textvariable=baseNumber, values=('2', '8', '16'), state="readonly")
combo.grid(row=2, column=2, sticky=E)
combo.bind("<<ComboBoxSelected>>", display)

for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

    
root.mainloop()