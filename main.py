from asyncio import sleep
from asyncio.windows_events import NULL
from re import I
from tkinter import *
from tkinter import messagebox

import serial
from numpy import pad
from voicemeeter import *
import voicemeeter
from voicemeeter.errors import VMRDriverError

# constants
KIND = 'potato'
BUTTON_SIZE = 5
BUTTON_NAMES = ["C", "+/-", "%", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "connect", "+", "0", ".", "=", "!="]
# BUTTON_NAMES = "123456789abcdefghijk"

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
    global root
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
               
    
    # my loop
    # root.after(10, task)
    global arduino
    arduino = serial.Serial(port="COM38", baudrate=115200, timeout=0)
    
    # root.after(10, lambda arduino=arduino: print_serial(arduino))
    root.after(10, print_serial)

    # gui loop
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    

def task():
    print("hey is this thing loopin'?", time.time())
    root.after(1000, task)


def print_serial():
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').rstrip()
        data = data.strip('<').strip('>').split(',')
        # print("data:", data)
    root.after(10, print_serial)
                

def any_click(name, ent):
    print(f'name: {name} ent: {ent}')


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        print("vmr logout: ", vmr.logout())
        print("arduino close: ", arduino.close())
        root.destroy()

    
if __name__ == "__main__":
    main()
