import tkinter as tk
from tkinter import messagebox, ttk

import sv_ttk

from slider import BusWidget, StripWidget
from menu import CustomMenu

class App(tk.Tk):
    def __init__(self, name="app"):
        super().__init__()
        sv_ttk.set_theme("dark")

        # custom title bar
        self.overrideredirect(True)
        self.geometry('+200+200')

        self._menu = CustomMenu(self)      
        self._menu.grid(row=0, column=0, sticky="NSEW")
        
        self.bind('<B1-Motion>', self.move_window)
        self.bind('<Button-1>', self.get_pos)
        
        
        # main frame
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(row=1, column=0, sticky="NSEW")
        self.resizable(False, False)

        # setup gui
        self.setup()

    def setup(self):
        self._strip1 = StripWidget(1, master=self.mainframe, name='strip1', border=1)
        self._strip1.grid(row=0, column=0, padx=5, pady=5)

        self._strip2 = StripWidget(2, master=self.mainframe, name='strip2', border=1)
        self._strip2.grid(row=0, column=1, padx=5, pady=5)

        self._strip3 = StripWidget(3, master=self.mainframe, name='strip3', border=1)
        self._strip3.grid(row=0, column=2, padx=5, pady=5)

        self._strip4 = StripWidget(4, master=self.mainframe, name='strip4', border=1)
        self._strip4.grid(row=0, column=3, padx=5, pady=5)

        self._bus1 = BusWidget(5, master=self.mainframe, name='bus1', border=1)
        self._bus1.grid(row=0, column=4, padx=5, pady=5, sticky="S")
        
        self._bus2 = BusWidget(6, master=self.mainframe, name='bus2', border=1)
        self._bus2.grid(row=0, column=5, padx=5, pady=5, sticky="S")
        
    @property
    def root(self):
        return self

    def get_pos(self, *args, **kwargs):
        if args[0].widget is self._menu:
            self._xwin = args[0].x
            self._ywin = args[0].y

    def move_window(self, *args, **kwargs):
        if args[0].widget is self._menu:            
            self.geometry(f'+{args[0].x_root-self._xwin}+{args[0].y_root-self._ywin}')

    def on_closing(self, *args, **kwargs):
        """program exit callback"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

    def maximize_window(self, *args, **kwargs):
        print('maximize')
        
    def minimize_window(self, *args, **kwargs):
        print('minimize')