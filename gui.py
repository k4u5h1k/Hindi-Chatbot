from tkinter import *
from bot import chat

c = chat()

def chat_api():
    query = str(e.get())
    response = c.respond(query)
    result.set(response)
    

master = Tk()
master.configure(bg = 'light grey')
master.title("Bot")
result = StringVar();
Label(master, text="Enter Text : " , bg = "light grey").grid(row = 0, sticky = W)
Label(master, text="Result :", bg = "light grey").grid(row = 3, sticky = W)
Label(master, text="", textvariable=result,bg = "light grey").grid(row = 3,
                                                                   column = 1, 
                                                                   sticky = W)
e = Entry(master, width = 100)
e.grid(row = 0, column = 1)
b = Button(master, text = "Show", command = chat_api, bg = "Blue")
b.grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5,)
  
mainloop()