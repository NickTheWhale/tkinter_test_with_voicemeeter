# Imports
from tkinter import *
from ctypes import windll
# Some WindowsOS styles, required for task bar integration
GWL_EXSTYLE = -20
WS_EX_APPWINDOW = 0x00040000
WS_EX_TOOLWINDOW = 0x00000080


def set_appwindow(mainWindow):
    # Honestly forgot what most of this stuff does. I think it's so that you can see
    # the program in the task bar while using overridedirect. Most of it is taken
    # from a post I found on stackoverflow.
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
    # re-assert the new window style
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())


def main():
    global mainWindow
    # Default window configuration
    mainWindow = Tk()
    mainWindow.geometry('800x400')
    mainWindow.resizable(width=False, height=False)
    mainWindow.overrideredirect(True)
    mainWindow.after(10, lambda: set_appwindow(mainWindow))

    def exitGUI():
        mainWindow.destroy()

    def minimizeGUI():
        mainWindow.state('withdrawn')
        mainWindow.overrideredirect(False)
        mainWindow.state('iconic')

    def frameMapped(event=None):
        mainWindow.overrideredirect(True)
        mainWindow.state("normal")
        mainWindow.iconbitmap("ANALOG.ico")
    exitButton = Button(mainWindow, text='', bg='#212121', fg='#35DAFF',
                        command=exitGUI)
    minimizeButton = Button(mainWindow, text='', bg="#212121", fg='#35DAFF',
                            command=minimizeGUI)
    exitButton.place(x=780, y=0)
    minimizeButton.place(x=759, y=0)
    mainWindow.bind("<Map>", frameMapped)  # This brings back the window
    mainWindow.mainloop()  # Window Loop


if __name__ == '__main__':
    main()
