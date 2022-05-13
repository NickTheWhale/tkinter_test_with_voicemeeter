from asyncio import sleep
from asyncio.windows_events import NULL
from re import I
from tkinter import *

from numpy import pad
from voicemeeter import *
import voicemeeter
from voicemeeter.errors import VMRDriverError

# constants
KIND = 'potato'
BUTTON_SIZE = 5
BUTTON_NAMES = ["C", "+/-", "%", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "0", ".", "=", "!="]

A = 0


def main():
    # login to voicemeeter
    global vmr
    vmr = voicemeeter.remote(KIND)
    try:
        vmr.login()
    except VMRDriverError:
        voicemeeter.launch(KIND)
    
    # create main gui window
    root = Tk()
    root.title("super duper calculator")
    
    # create display box
    display_box = Entry(root, width=BUTTON_SIZE*10)
    display_box.grid(row=0, column=0, columnspan=4)
    
    
    # create buttons
    button_list = []
    for name in BUTTON_NAMES:
        button_list.append(Button(root, text=name, width=BUTTON_SIZE*2, height=BUTTON_SIZE, 
                                  command=lambda name=name, display_box=display_box: any_click(name, display_box)))
    
    
    # layout buttons
    i = 0
    for _row in range(5):
        for _column in range(4):
            button_list[i].grid(row=_row+1, column=_column)
            i += 1
               
                        
    # main loop
    root.mainloop()
    

def any_click(name, ent):
    if name == "!=":
        ent.delete(0, END)
        ent.insert(0, "who the hell cares?")
    elif name == "C":
        ent.delete(0, END)
    elif name == "=":
        vmr.set(ent.get(), True)
    else:
        current = ent.get()
        ent.delete(0, END)
        ent.insert(0, str(current) + " " + str(name))
    
    
if __name__ == "__main__":
    main()
