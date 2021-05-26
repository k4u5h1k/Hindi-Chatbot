from tkinter import *
from englisttohindi.englisttohindi import EngtoHindi

def eng_to_hindi():
    trans = EngtoHindi(str(e.get()))
    res = trans.convert
    result.set(res)   
    master.clipboard_clear()
    master.clipboard_append(res)
    master.update()
  
master = Tk(screenName="Converter")
master.configure(bg = 'light grey')
master.title("English to Hindi")
result = StringVar();
Label(master, text="Enter Text : " , bg = "light grey").grid(row = 0, sticky = W)
Label(master, text="Result :", bg = "light grey").grid(row = 3, sticky = W)
Label(master, text="", textvariable=result,bg = "light grey").grid(row = 3,
                                                                   column = 1, 
                                                                   sticky = W)
e = Entry(master, width = 100)
e.grid(row = 0, column = 1)
b = Button(master, text = "Show", command = eng_to_hindi, bg = "Blue")
b.grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5,)
mainloop()