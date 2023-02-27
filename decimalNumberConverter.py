from tkinter import * 
from tkinter import ttk

baseName = {2:'binary', 8:'octal', 16:'hexadecimal'}
convertedNumbers = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

class NumberConverter:
    def __init__(self, root) -> None:
        root.title("Decimal to Other Bases")
        
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(row=0, column=0, sticky=(W,E,S,N))
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        
        self.decimalNumber = StringVar()
        ttk.Label(mainframe, text="Enter the decimal number \t\t\t").grid(row=0, column=0, sticky=(W))
        decimalNumber_enter = ttk.Entry(mainframe, width=15, textvariable=self.decimalNumber)
        decimalNumber_enter.grid(row=0, column=1, sticky=(E))
        
        self.baseNumber = StringVar()
        ttk.Label(mainframe, text = "Select base from 2, 8 or 16").grid(row=1, column=0, sticky=(W))
        baseNumber_enter = ttk.Entry(mainframe, width=15, textvariable=self.baseNumber)
        baseNumber_enter.grid(row=1, column=1, sticky=(E))
        
        self.outputNumber = StringVar()
        self.message = StringVar()
        ttk.Label(mainframe, textvariable = self.message).grid(row=2, column=0, sticky=(W))
        ttk.Label(mainframe, textvariable=self.outputNumber).grid(row=2, column=1, sticky=(W))
        
        ttk.Button(mainframe, text="Convert", command=self.getOutput).grid(row=3, column=1, sticky=(E))
        
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
            
        decimalNumber_enter.focus()
        root.bind("<Return>", self.getOutput)
            
    def getOutput(self, *args):
        try:
            self.localBase = int(self.baseNumber.get())
            self.localDecimal = int(self.decimalNumber.get())
            if self.localBase == "" or self.localDecimal == "":
                raise ValueError    
            self.message.set(f"This is how many fucks I give in {baseName[self.localBase]}")
            self.outputNumber.set(self._getOutput())
                
        except KeyError:
            self.message.set("Choose a valid base")
            self.outputNumber.set("Invalid")
            
        except ValueError:
                self.message.set("Please fill all the entry fields")
                self.outputNumber.set("Invalid")
            
    def _getOutput(self, *args):
        temp = ""
        while self.localDecimal:
            remainder = int(self.localDecimal%self.localBase)
            temp += convertedNumbers[remainder]
            self.localDecimal = int(self.localDecimal/self.localBase)
        my_list = list(temp)
        my_list.reverse()   
        finalAnswer = ''.join(my_list)
        return finalAnswer 
        

root = Tk()
NumberConverter(root)
root.mainloop()