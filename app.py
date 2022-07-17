import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import serial
from serial import SerialException

# constants
BD_WIDTH = 3


class App(tk.Tk):
    def __init__(self, name="app"):
        super().__init__()
        # private variables
        self.__is_running = True

        # create main gui window
        self.title(name)
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(row=0, column=0, sticky="NSEW")
        self.resizable(False, False)
        
        # build gui
        self.build()

    def build(self):
        pass

        # resizing
        # self.mainframe.columnconfigure(0, weight=1, minsize=150)
        # self.mainframe.columnconfigure(1, weight=1, minsize=150)
        # self.mainframe.columnconfigure(2, weight=1, minsize=150)
        # self.mainframe.columnconfigure(3, weight=1, minsize=150)
        # self.mainframe.columnconfigure(4, weight=1, minsize=150)
        # self.mainframe.columnconfigure(5, weight=1, minsize=150)
        # self.mainframe.rowconfigure(0, weight=1, minsize=100)
        # self.mainframe.rowconfigure(1, weight=1, minsize=100)
        # self.mainframe.rowconfigure(2, weight=1, minsize=30)

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
        a_port = self.com_port.get()
        a_baud = self.com_baud.get()
        if a_baud == ' ':
            a_baud = "9600"
        print(
            f'Connecting to {self.com_port.get()} at {self.com_baud.get()} baud')
        try:
            arduino = serial.Serial(port=a_port, baudrate=a_baud, timeout=0)
            connected = True
            print("Success")
        except SerialException as e:
            print(e)
            connected = False
        return connected
        

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
