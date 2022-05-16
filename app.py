import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# constants
BD_WIDTH = 3


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
            self.mainframe, borderwidth=BD_WIDTH, relief="groove")
        slider1_frame.grid(column=0, row=1)

        slider2_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="groove")
        slider2_frame.grid(column=1, row=1)

        slider3_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="groove")
        slider3_frame.grid(column=2, row=1)

        slider4_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="groove")
        slider4_frame.grid(column=3, row=1)

        slider5_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="groove")
        slider5_frame.grid(column=4, row=1)

        slider6_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="groove")
        slider6_frame.grid(column=5, row=1)

        options_frame = ttk.Frame(
            self.mainframe, borderwidth=BD_WIDTH, relief="groove")
        options_frame.grid(column=1, row=2, columnspan=5, sticky=NSEW)

        # test labels
        knob_label = ttk.Label(knob_frame, text="knobs")
        knob_label.grid(column=0, row=0)

        buttons_label = ttk.Label(buttons_frame, text="buttons")
        buttons_label.grid(column=0, row=0)

        self.slider_value = 0
        slider1 = ttk.Scale(slider1_frame, orient='vertical',
                            length=300, from_=12, to=-60, command=self.slider_moved)
        slider1.grid(column=0, row=0, rowspan=5)

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
        self.com_select = ttk.Combobox(
            options_frame, textvariable=self.com_port)
        self.com_select.grid(column=0, row=0)

        connect_button = ttk.Button(
            options_frame, text="Connect", command=self.on_connect)
        connect_button.grid(column=1, row=0)

        # resizing
        self.mainframe.columnconfigure(0, weight=1, minsize=150)
        self.mainframe.columnconfigure(1, weight=1, minsize=150)
        self.mainframe.columnconfigure(2, weight=1, minsize=150)
        self.mainframe.columnconfigure(3, weight=1, minsize=150)
        self.mainframe.columnconfigure(4, weight=1, minsize=150)
        self.mainframe.columnconfigure(5, weight=1, minsize=150)
        self.mainframe.rowconfigure(0, weight=1, minsize=100)
        self.mainframe.rowconfigure(1, weight=1, minsize=100)
        self.mainframe.rowconfigure(2, weight=1, minsize=100)

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

    def add_port(self, ports):
        """
        Set port drop down options 
        :param ports: list of COM ports
        :type ports: String List
        """
        self.com_select['value'] = ports

    @property
    def is_running(self):
        """
        Returns true if user has requested to close application.
        Returns false if otherwise

        :return: application state
        :rtype: Bool
        """
        return self.__is_running

    def slider_moved(self, val):
        print(val)
        # print(self.slider_value)
