from tkinter import *
from bot import *

c = Bot()

window = Tk()
message = Text(window)
message.pack()
#message.title("Bot")
uinput = StringVar()
input_field = Entry(window, text=uinput)
input_field.pack(side=BOTTOM, fill=X)


def Enter_pressed(event):
    #input_get = input_field.get()
    #print(input_get)
    query = input_field.get()
    print(query)
    message.insert(INSERT, '%s\n' % query)
    
    response = c.reply(query)
    uinput.set(response)

    # label = Label(window, text=input_get)
    # label.pack()
    return "break"

frame = Frame(window, width=300, height=300)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()
