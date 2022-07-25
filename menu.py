from tkinter import ttk, messagebox


class CustomMenu(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._root = args[0]
        self.grid(row=0, column=0, sticky="NSEW")
        self.columnconfigure(0, weight=1)

        self._xwin = 0
        self._ywin = 0

        self.close_button = ttk.Button(
            self,
            text='✕',
            width=3,
            command=self._root.on_closing
        )
        self.close_button.grid(row=0, column=2, sticky="E", padx=(0, 2), pady=2)

        self.maximize_button = ttk.Button(
            self,
            text='🗖',
            width=3,
            command=self.maximize_window
        )
        self.maximize_button.grid(row=0, column=1, sticky="E", padx=(0, 2), pady=2)

        self.minimize_button = ttk.Button(
            self,
            text='🗕',
            width=3,
            command=self.minimize_window,
        )
        self.minimize_button.grid(row=0, column=0, sticky="E", padx=(0, 2), pady=2)

        self._root.bind('<B1-Motion>', self.move_window)
        self._root.bind('<Button-1>', self.get_pos)

    def fake_callback(self, event):
        print(event.widget)

    def get_pos(self, event):
        if event.widget is self:
            self._xwin = event.x
            self._ywin = event.y

    def move_window(self, event):
        if event.widget is self:
            self._root.geometry(f'+{event.x_root-self._xwin}+{event.y_root-self._ywin}')

    def maximize_window(self, *args, **kwargs):
        print('maximize')

    def minimize_window(self, *args, **kwargs):
        print('minimize')
