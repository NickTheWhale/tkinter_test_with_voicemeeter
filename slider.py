import tkinter as tk
from tkinter import *
from tkinter import ttk

class Slider(tk.Tk):
    def __init__(self, name="slider"):
        super().__init__()
        
        self.__name = name