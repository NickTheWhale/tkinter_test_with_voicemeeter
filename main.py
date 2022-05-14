from asyncio import sleep
from asyncio.windows_events import NULL
from re import I
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import serial
from numpy import pad
from voicemeeter import *
import voicemeeter
from voicemeeter.errors import VMRDriverError

# constants
KIND = 'potato'


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
    root.title("Voicemeeter Utility")
    mainframe = ttk.Frame(root, padding="1 1 1 1")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    # frames
    frame1 = ttk.Frame(mainframe)
    frame1.grid(column=0, row=0)
    
    frame2 = ttk.Frame(mainframe)
    frame2.grid(column=1, row=1)

    # labels
    label1 = ttk.Label(mainframe, text="label1")
    label1.grid(column=0, row=0)
    
    label2 = ttk.Label(mainframe, text="label2")
    label2.grid(column=0, row=0)
    
    
    # serial loop
    global arduino
    arduino = serial.Serial(port="COM38", baudrate=115200, timeout=0)
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
        print("data:", data)
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
