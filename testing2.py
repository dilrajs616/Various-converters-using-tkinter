from tkinter import *
from tkinter import ttk

root = Tk()

content=ttk.Frame(root)
content.grid(row=0, column=0)

frame = ttk.Frame(content, borderwidth=5, relief="ridge", height=300, width=300)
frame.grid(row=0, column=0, rowspan=3, columnspan=3)
Button(frame, text='1', width=10, height=5).grid(row=0, column=0)
Button(frame, text='2', width=10, height=5).grid(row=0, column=1)
Button(frame, text='3', width=10, height=5).grid(row=0, column=2)
Button(frame, text='4', width=10, height=5).grid(row=1, column=0)
Button(frame, text='5', width=10, height=5).grid(row=1, column=1)
Button(frame, text='6', width=10, height=5).grid(row=1, column=2)
Button(frame, text='7', width=10, height=5).grid(row=2, column=0)
Button(frame, text='9', width=10, height=5).grid(row=2, column=2)
Button(frame, text='8', width=10, height=5).grid(row=2, column=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)


# frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
# namelbl = ttk.Label(content, text="Name")
# name=ttk.Entry(content)

# onevar = BooleanVar(value=True)
# twovar = BooleanVar(value=False)
# threevar = BooleanVar(value=True)

# one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
# two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
# three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
# ok = ttk.Button(content, text="Okay")
# cancel = ttk.Button(content, text="Cancel")

# content.grid(column=0, row=0)
# frame.grid(column=0, row=0, columnspan=3, rowspan=2)
# namelbl.grid(column=3, row=0, columnspan=2)
# name.grid(column=3, row=1, columnspan=2)
# one.grid(column=0, row=3)
# two.grid(column=1, row=3)
# three.grid(column=2, row=3)
# ok.grid(column=3, row=3)
# cancel.grid(column=4, row=3)

root.mainloop()