import time
import tkinter as tk
from tkinter import ttk
import sv_ttk
import voicemeeterlib


NUM = 2

root = tk.Tk()
sv_ttk.set_theme('light')
with voicemeeterlib.api('potato') as vm:
    levels = []
    for i in range(NUM):
        levels.append(tk.DoubleVar())
        levels[-1].set(0)


    progresses = []
    for i in range(NUM):
        progresses.append(ttk.Progressbar(root,
                                        variable=levels[i],
                                        maximum=100,
                                        length=100,
                                        orient='vertical',
                                        mode='determinate'))
        progresses[-1].grid(row=0, column=i, padx=50)


    def set_levels(*args):
        global levels
        for level in levels:
            lvl = max(vm.strip[4].levels.prefader)

            lvl = 100 + lvl - 18  
            
            level.set(lvl)


            root.update_idletasks()
        root.after(50, set_levels)


    set_levels()


    root.mainloop()

