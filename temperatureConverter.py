from tkinter import *
from tkinter import ttk

class Temperature:
    def __init__(self, root) :
        root.title("Temperature Converter")
        
        mainframe = ttk.Frame(root, padding = "3 3 12 12")
        mainframe.grid(row=0, column=0, sticky = (W,E,S,N))
        root.rowconfigure(0, weight = 1)
        root.columnconfigure(0, weight = 1)
        
        self.farenheit = StringVar()
        ttk.Label(mainframe, text="degree farenheit").grid(row=0, column=3, sticky=(W,E))
        farenheit_enter = ttk.Entry(mainframe, width = 10, textvariable = self.farenheit)
        farenheit_enter.grid(row=0, column=2, sticky=(W,E))
        
        self.celcius = StringVar()
        ttk.Label(mainframe, text="is equivalent to ").grid(row=1, column=1, sticky=(W,E))
        ttk.Label(mainframe, textvariable = self.celcius).grid(row=1, column=2, sticky=(W,E))
        ttk.Label(mainframe, text = "degree celcuis").grid(row=1, column=3, sticky=(W,E))
        ttk.Button(mainframe, text="calculate", command=self.get_value).grid(row=2, column=3, sticky=(W,E))
        
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
            
        farenheit_enter.focus()
        
    def get_value(self,*args):
        localFarenheit = float(self.farenheit.get())
        self.celcius.set((localFarenheit-32)*(5/9))
        
        
root = Tk()
Temperature(root)
root.mainloop()