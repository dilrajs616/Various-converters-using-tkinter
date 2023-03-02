from tkinter import * 
from tkinter import ttk

baseName = {2:'binary', 8:'octal', 16:'hexadecimal'}
convertedNumbers = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

class NumberConverter:
    def __init__(self, root) -> None:
        root.title("Decimal to Other Bases")
        
        mainframe = ttk.Frame(root, padding="3 3 12 12", borderwidth=2, relief=RAISED)
        mainframe.grid(row=0, column=0, sticky=(W,E,S,N))
        
        self.baseNumber = StringVar()
        baseInput = ttk.Label(mainframe, text = "Select base from 2, 8 or 16", borderwidth=5, relief="ridge")
        baseInput.grid(row=0, column=0, sticky=(W))
        baseNumber_enter = ttk.Entry(mainframe, width=15, textvariable=self.baseNumber)
        baseNumber_enter.grid(row=0, column=1, sticky=(E))
        
        
        self.decimalNumber = StringVar()
        decimalInput = ttk.Label(mainframe, text="Enter the decimal number \t\t")
        decimalInput.grid(row=1, column=0, sticky=(W))
        decimalNumber_enter = ttk.Entry(mainframe, width=15)
        decimalNumber_enter.grid(row=1, column=1, sticky=(E))
        
        self.outputNumber = StringVar()
        self.message = StringVar()
        outputText = ttk.Label(mainframe, textvariable = self.message, font="TkTextFont")
        outputText.grid(row=2, column=0, sticky=(W))
        output = ttk.Label(mainframe, textvariable=self.outputNumber, font="TkFixedFont")
        output.grid(row=2, column=1, sticky=(W))
        
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
            
        baseNumber_enter.focus()
        baseNumber_enter.bind("<KeyRelease>", self.getOutput)
        decimalNumber_enter.bind("<KeyRelease>", self.on_input_change)
            
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.rowconfigure(1, weight=1)
        mainframe.rowconfigure(2, weight=1)
        mainframe.columnconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=1)
        
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
                
    def on_input_change(self,event, *args):
        self.decimalNumber.set(event.widget.get())
        self.getOutput()
        

root = Tk()
NumberConverter(root)
root.mainloop()