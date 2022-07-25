from tkinter import ttk

import serial
import sv_ttk
import voicemeeterlib
from serial import SerialException

from app import App

# constants
VM_KIND = 'potato'


def main():
    with voicemeeterlib.api(VM_KIND) as vm:
        app = App(vm, 'Voicemeeter Remote', False)

        app.tk.call('source', 'azure.tcl')
        app.tk.call('set_theme', 'dark')

        app.protocol("WM_DELETE_WINDOW", app.on_closing)
        app.mainloop()


if __name__ == "__main__":
    main()
