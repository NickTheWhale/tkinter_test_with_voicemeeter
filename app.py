import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from numpy import var

# constants
BD_WIDTH = 5


class App(tk.Tk):
    def __init__(self, name="myApp"):
        super().__init__()
        # private variables
        self.__is_running = True

        # create main gui window
        self.title(name)
        self.mainframe = ttk.Frame(self, padding="1 1 1 1")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def initialize_widgets(self):
        # frames
        knob_frame = ttk.Frame(self.mainframe, borderwidth=BD_WIDTH, width=4)
        knob_frame.grid(column=0, row=0)

        buttons_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, width=2)
        buttons_frame.grid(column=4, row=0)

        slider1_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="flat")
        slider1_frame.grid(column=0, row=1)

        slider2_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="raised")
        slider2_frame.grid(column=1, row=1)

        slider3_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="sunken")
        slider3_frame.grid(column=2, row=1)

        slider4_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="solid")
        slider4_frame.grid(column=3, row=1)

        slider5_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="ridge")
        slider5_frame.grid(column=4, row=1)

        slider6_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="groove")
        slider6_frame.grid(column=5, row=1)

        options_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="groove")
        options_frame.grid(column=0, row=2, columnspan=5)

        # test labels
        knob_label = ttk.Label(knob_frame, text="knobs")
        knob_label.grid(column=0, row=0)

        buttons_label = ttk.Label(buttons_frame, text="buttons")
        buttons_label.grid(column=0, row=0)

        # buttons
        slid1 = tk.Button(slider1_frame, text="slider", height=20)
        slid1.grid(column=0, row=0, rowspan=5)

        self.A1checkvar = IntVar()

        A1 = ttk.Checkbutton(slider1_frame, text="A1",
                             variable=self.A1checkvar, command=self.onA1)
        A1.grid(column=1, row=0)

        A2 = ttk.Button(slider1_frame, text="A2")
        A2.grid(column=1, row=1)

        A3 = ttk.Button(slider1_frame, text="A3")
        A3.grid(column=1, row=2)

        B1 = ttk.Button(slider1_frame, text="B1")
        B1.grid(column=1, row=3)

        B2 = ttk.Button(slider1_frame, text="B2")
        B2.grid(column=1, row=4)

        slider2_label = ttk.Label(slider2_frame, text="slider2")
        slider2_label.grid(column=0, row=0)

        slider3_label = ttk.Label(slider3_frame, text="slider3")
        slider3_label.grid(column=0, row=0)

        slider4_label = ttk.Label(slider4_frame, text="slider4")
        slider4_label.grid(column=0, row=0)

        slider5_label = ttk.Label(slider5_frame, text="slider5")
        slider5_label.grid(column=0, row=0)

        slider6_label = ttk.Label(slider6_frame, text="slider6")
        slider6_label.grid(column=0, row=0)

        # port box
        self.com_port = StringVar()
        com_select = ttk.Combobox(options_frame, textvariable=self.com_port)
        com_select.grid(column=0, row=0)
        
        connect_button = ttk.Button(options_frame, text="Connect", command=self.on_connect)
        connect_button.grid(column=1, row=0)

    def onA1(self):
        print(
            f'value: {self.A1checkvar.get()} type: {type(self.A1checkvar.get())}')

    def on_closing(self):
        """
        Called on application exit. Prompts user if they want to quit
        and sets "is_running" flag to false
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.__is_running = False
            self.destroy()
            
    def on_connect(self):
        print(self.com_port.get())

    @property
    def is_running(self):
        """
        Returns true if user has requested to close application.
        Returns false if otherwise

        :return: application state
        :rtype: Bool
        """
        return self.__is_running

    def button1_callback(self):
        print("button 1")

    def button2_callback(self):
        print("button 2")
