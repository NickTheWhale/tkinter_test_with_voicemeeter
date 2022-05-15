import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self, name="myApp"):
        super().__init__()
        # private variables
        self.__is_running = True

        # create main gui window
        self.title(name)
        mainframe = ttk.Frame(self, padding="1 1 1 1")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # frames
        slider1_frame = ttk.Frame(mainframe, borderwidth=10, relief="flat")
        slider1_frame.grid(column=0, row=0)

        slider2_frame = ttk.Frame(mainframe, borderwidth=10, relief="raised")
        slider2_frame.grid(column=1, row=1)

        slider3_frame = ttk.Frame(mainframe, borderwidth=10, relief="sunken")
        slider3_frame.grid(column=2, row=2)

        slider4_frame = ttk.Frame(mainframe, borderwidth=10, relief="solid")
        slider4_frame.grid(column=3, row=3)

        slider5_frame = ttk.Frame(mainframe, borderwidth=10, relief="ridge")
        slider5_frame.grid(column=4, row=4)

        slider6_frame = ttk.Frame(mainframe, borderwidth=10, relief="groove")
        slider6_frame.grid(column=5, row=5)

        # buttons
        button1 = ttk.Button(slider1_frame, text="button 1")
        button1.grid(column=0, row=0)

        button2 = ttk.Button(slider2_frame, text="button 2")
        button2.grid(column=0, row=0)

        button3 = ttk.Button(slider3_frame, text="button 3")
        button3.grid(column=0, row=0)

        button4 = ttk.Button(slider4_frame, text="button 4")
        button4.grid(column=0, row=0)

        button5 = ttk.Button(slider5_frame, text="button 5")
        button5.grid(column=0, row=0)

        button6 = ttk.Button(slider6_frame, text="button 6")
        button6.grid(column=0, row=0)

    def on_closing(self):
        """
        Called on application exit. Prompts user if they want to quit
        and sets "is_running" flag to false
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.__is_running = False
            self.destroy()

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
