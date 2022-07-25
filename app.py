import tkinter as tk
from tkinter import messagebox, ttk

from menu import CustomMenu
from widgets import BusWidget, StripWidget, ControlWidget


class App(tk.Tk):
    def __init__(self, voicemeeter, name="app", custom_title=False):
        super().__init__()

        self.vm = voicemeeter

        # custom title bar
        if custom_title:
            self.overrideredirect(True)
            self.geometry('+200+200')

            self._menu = CustomMenu(self)
            self._menu.grid(row=0, column=0, sticky="NSEW")
        else:
            self.title(name)
            self.resizable(False, False)
            self.geometry('-70-120')

        # main frame
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(row=1, column=0, sticky="NSEW")

        # setup gui
        self.setup()
        self.update()

    def setup(self):
        self._strips = []

        self._strips.append(StripWidget(
            master=self.mainframe,
            index=0,
            vm=self.vm,
            text='strip 1',
            border=3
        ))
        self._strips[-1].grid(row=0, rowspan=2, column=0, padx=5, pady=5)


        self._strips.append(StripWidget(
            master=self.mainframe,
            index=3,
            vm=self.vm,
            text='strip 2',
            border=3
        ))
        self._strips[-1].grid(row=0, rowspan=2, column=1, padx=5, pady=5)


        self._strips.append(StripWidget(
            master=self.mainframe,
            index=4,
            vm=self.vm,
            text='strip 3',
            border=3
        ))
        self._strips[-1].grid(row=0, rowspan=2, column=2, padx=5, pady=5)


        self._strips.append(StripWidget(
            master=self.mainframe,
            index=6,
            vm=self.vm,
            text='strip 4',
            border=3
        ))
        self._strips[-1].grid(row=0, rowspan=2, column=3, padx=5, pady=5)




        self._busses = []

        self._busses.append(BusWidget(
            master=self.mainframe,
            index=0,
            vm=self.vm,
            text='bus 1',
            border=3
        ))
        self._busses[-1].grid(row=1, column=4, padx=5, pady=5, sticky='S')

        self._busses.append(BusWidget(
            master=self.mainframe,
            index=2,
            vm=self.vm,
            text='bus 3',
            border=3
        ))
        self._busses[-1].grid(row=1, column=5, padx=5, pady=5, sticky='S')



        self._controls = ControlWidget(master=self.mainframe, vm=self.vm, border=3, text='controls')
        self._controls.grid(row=0, column=4, columnspan=2, padx=5, pady=5, sticky='N')

        # self.resizable(True, True)
        # for column in range(self.grid_size()[0]):
        #     self.columnconfigure(column, minsize=50, weight=1)
        # for row in range(self.grid_size()[1]):
        #     self.rowconfigure(row, minsize=50, weight=1)

        # for column in range(self.mainframe.grid_size()[0]):
        #     self.mainframe.columnconfigure(column, minsize=50, weight=1)
        # for row in range(self.mainframe.grid_size()[1]):
        #     self.mainframe.rowconfigure(row, minsize=50, weight=1)

    def update(self):
        for strip in self._strips:
            strip.update()
        for bus in self._busses:
            bus.update()

        self.after(30, self.update)

    @property
    def root(self):
        return self

    def on_closing(self, *args, **kwargs):
        """program exit callback"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
