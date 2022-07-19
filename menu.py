from tkinter import ttk


class CustomMenu(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._root = args[0]
        self.grid(row=0, column=0, sticky="NSEW")
        self.columnconfigure(0, weight=1)

        self.close_button = ttk.Button(
            self,
            text='✕',
            width=3,
            command=self._root.on_closing
        )
        self.close_button.grid(row=0, column=2, sticky="E", padx=(0,2), pady=2)

        self.maximize_button = ttk.Button(
            self,
            text='🗖',
            width=3,
            command=self._root.maximize_window
        )
        self.maximize_button.grid(row=0, column=1, sticky="E", padx=(0,2), pady=2)

        self.minimize_button = ttk.Button(
            self,
            text='🗕',
            width=3,
            command=self._root.minimize_window,
        )
        self.minimize_button.grid(row=0, column=0, sticky="E", padx=(0,2), pady=2)

        self._xwin = 0
        self._ywin = 0

