import tkinter as tk
from tkinter import ttk


class Slider(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gain = tk.DoubleVar()
        self._level = tk.DoubleVar()

        self._slider = ttk.Scale(
            master=self,
            from_=12.0,
            to=-60.0,
            orient="vertical",
            length=300,
            command=self.callback,
            variable=self._gain
        )

        self._gain_label = ttk.Label(master=self, text=str(self._gain.get()))

        self._slider.grid(row=0, column=0, padx=30, pady=20, sticky="NSEW")
        self._gain_label.grid(row=1, column=0)

    def callback(self, *args):
        self._gain_label['text'] = str(round(float(args[0]), 1))
        print(f'Slider moved: {round(self._gain.get())}')


class Dial(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._name = ''
        self._level = tk.DoubleVar()

        self._slider = ttk.Scale(
            master=self,
            from_=0.0,
            to=10.0,
            orient='horizontal',
            length=80,
            command=self.callback,
            variable=self._level
        )

        self._level_label = ttk.Label(master=self, text=str(self._level.get()))
        self._seperator = ttk.Separator(master=self, orient='horizontal')

        self._slider.grid(row=0, column=0, padx=10, pady=5, sticky="NSEW")
        self._level_label.grid(row=1, column=0)
        self._seperator.grid(row=2, column=0, pady=10, sticky="NSEW")

    def callback(self, *args):
        self._level_label['text'] = str(round(float(args[0]), 1))
        print(f'Slider moved: {round(self._level.get())}')


class Button(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'name' in kwargs:
            self._name = kwargs['name']
        else:
            self._name = 'button'

        self._button = ttk.Checkbutton(
            master=self,
            text=self._name,
            command=self.callback,
            style="Toggle.TButton"
        )
        self._button.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

    def callback(self, *args, **kwargs):
        print(f'Button pressed. args: {args} kwargs: {kwargs}')

    def set_text(self, text):
        self._button['text'] = text


class Progress(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._level = tk.DoubleVar()

        self._progress = ttk.Progressbar(
            master=self,
            maximum=100,
            orient="vertical",
            mode="determinate",
            length=298,
            variable=self._level
        )
        self._progress.grid(row=0, column=0, padx=5, pady=(0, 17), sticky="NSEW")

    @property
    def level(self):
        return self._level.get()

    @level.setter
    def level(self, level):
        self._level.set(level)


class StripWidget(ttk.Labelframe):
    def __init__(self, index, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._index = index

        if 'name' in kwargs:
            self._name = kwargs['name']
        else:
            self._name = 'strip'

        self.configure(text=self._name)

        self.dial_frame = ttk.Frame(self)
        self.dial_frame.grid(row=0, column=0)

        self.dial = Dial(self.dial_frame)
        self.dial.grid(row=0, column=0, sticky="NSEW")

        self.dial = Dial(self.dial_frame)
        self.dial.grid(row=0, column=1, sticky="NSEW")

        self.slider_frame = ttk.Frame(self)
        self.slider_frame.grid(row=1, column=0)
        
        self.progress = Progress(self.slider_frame)
        self.progress.grid(row=1, rowspan=5, column=0)

        self.slider = Slider(self.slider_frame)
        self.slider.grid(row=1, rowspan=5, column=1, sticky="NSEW")

        self.button1 = Button(self.slider_frame)
        self.button1.grid(row=1, column=2, sticky="NSEW")

        self.button2 = Button(self.slider_frame)
        self.button2.grid(row=2, column=2, sticky="NSEW")

        self.button3 = Button(self.slider_frame)
        self.button3.grid(row=3, column=2, sticky="NSEW")

        self.button4 = Button(self.slider_frame)
        self.button4.grid(row=4, column=2, sticky="NSEW")

        self.button5 = Button(self.slider_frame)
        self.button5.grid(row=5, column=2, sticky="NSEW")


class BusWidget(ttk.Labelframe):
    def __init__(self, index, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._index = index

        if 'name' in kwargs:
            self._name = kwargs['name']
        else:
            self._name = 'bus'

        self.configure(text=self._name)

        self.slider_frame = ttk.Frame(self)
        self.slider_frame.grid(row=1, column=0)
        
        self.progress = Progress(self.slider_frame)
        self.progress.grid(row=1, rowspan=5, column=0)

        self.slider = Slider(self.slider_frame)
        self.slider.grid(row=1, rowspan=5, column=1, sticky="NSEW")

        self.button = Button(self.slider_frame)
        self.button.grid(row=5, column=2, padx=(0,15), pady=(8,0))
