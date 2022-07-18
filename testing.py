#from tkinter import *  # PEP8: `import *` is not preferred
import tkinter as tk

# --- classes ---

# empty

# --- functions ---

def get_pos(event):
    global xwin
    global ywin

    xwin = event.x
    ywin = event.y

def move_window(event):
    root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')

def change_on_hovering(event):
    close_button['bg'] = 'red'

def return_to_normal_state(event):
    close_button['bg'] = back_ground

# --- main ---

# set background color of title bar
back_ground = "#2c2c2c"
# set background of window
content_color = "#ffffff"

# ---

root = tk.Tk()
# turns off title bar, geometry
root.overrideredirect(True)

# set new geometry
root.geometry('400x100+200+200')

# make a frame for the title bar
title_bar = tk.Frame(root, bg=back_ground, relief='raised', bd=1, 
                     highlightcolor=back_ground, 
                     highlightthickness=0)

# put a close button on the title bar
close_button = tk.Button(title_bar, text='x', bg=back_ground, padx=5, pady=2, 
                         bd=0, font="bold", fg='white',
                         activebackground="red",
                         activeforeground="white", 
                         highlightthickness=0, 
                         command=root.destroy)
                         
# window title
title_window = "Title Name"
title_name = tk.Label(title_bar, text=title_window, bg=back_ground, fg="white")

# a canvas for the main area of the window
window = tk.Canvas(root, bg="white", highlightthickness=0)

# pack the widgets
title_bar.pack(expand=True, fill='x')
title_name.pack(side='left')
close_button.pack(side='right')
window.pack(expand=True, fill='both')

# bind title bar motion to the move window function
title_bar.bind("<B1-Motion>", move_window)
title_bar.bind("<Button-1>", get_pos)
close_button.bind('<Enter>', change_on_hovering)
close_button.bind('<Leave>', return_to_normal_state)

root.mainloop()