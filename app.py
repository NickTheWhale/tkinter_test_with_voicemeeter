import tkinter as tk
from tkinter import messagebox, ttk

import sv_ttk

from slider import BusWidget, StripWidget


class App(tk.Tk):
    def __init__(self, name="app"):
        super().__init__()
        sv_ttk.set_theme("dark")

        # custom title bar
        self.overrideredirect(True)
        self.geometry('+200+200')
        
        self.title_bar = ttk.Frame(self)
        self.title_bar.grid(row=0, column=0, sticky="NSEW")
        
        self.close_button = ttk.Button(self.title_bar, text='X', command=self.on_closing)
        self.close_button.grid(row=0, column=0, sticky="E")
        
        self._xwin = 0
        self._ywin = 0
        
        self.title_bar.bind('<B1-Motion>', self.move_window)
        self.title_bar.bind('<Button-1>', self.get_pos)
        
        # main frame
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(row=1, column=0, sticky="NSEW")
        self.resizable(False, False)

        # setup gui
        self.setup()

    def setup(self):
        self._strip1 = StripWidget(1, master=self.mainframe, name='strip1', border=1).grid(row=0, column=0, padx=5, pady=10)
        self._strip2 = StripWidget(2, master=self.mainframe, name='strip2', border=1).grid(row=0, column=1, padx=5, pady=10)
        self._strip3 = StripWidget(3, master=self.mainframe, name='strip3', border=1).grid(row=0, column=2, padx=5, pady=10)
        self._strip4 = StripWidget(4, master=self.mainframe, name='strip4', border=1).grid(row=0, column=3, padx=5, pady=10)
                
        self._bus1 = BusWidget(5, master=self.mainframe, name='bus1', border=1).grid(row=0, column=4, padx=5, pady=10, sticky="S")
        self._bus2 = BusWidget(6, master=self.mainframe, name='bus2', border=1).grid(row=0, column=5, padx=5, pady=10, sticky="S")

    def get_pos(self, event):
        self._xwin = event.x
        self._ywin = event.y

    def move_window(self, event):
        self.geometry(f'+{event.x_root-self._xwin}+{event.y_root-self._ywin}')
            
    def on_closing(self):
        """program exit callback"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
