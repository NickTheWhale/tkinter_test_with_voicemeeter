import tkinter as tk
from tkinter import ttk


class Slider(ttk.Frame):
    def __init__(self, *args, **kwargs):
        self._vm = kwargs.pop('vm')
        super().__init__(*args, **kwargs)

        self._gain = tk.DoubleVar()

        self._max = 12
        self._start = 0
        self._min = -60

        self._slider = ttk.Scale(
            master=self,
            from_=self._max,
            to=self._min,
            orient="vertical",
            length=300,
            variable=self._gain
        )

        self._gain_label = ttk.Label(master=self, text=str(self._gain.get()))

        self._slider.grid(row=0, column=0, padx=30, pady=20, sticky="NSEW")
        self._gain_label.grid(row=1, column=0)

    def _update_label(self):
        self._gain_label['text'] = str(round(self._gain.get(), 1))

    @property
    def gain(self):
        return self._gain.get()

    @gain.setter
    def gain(self, gain):
        if gain > self._max:
            gain = self._max
        elif gain < self._min:
            gain = self._min

        self._gain.set(gain)
        self._update_label()


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
        self._progress.grid(row=0, column=0, sticky="NSEW")

    @property
    def level(self):
        return self._level.get()

    @level.setter
    def level(self, level):
        self._level.set(level)


class Dial(ttk.Frame):
    def __init__(self, *args, **kwargs):
        text = kwargs.pop('text')
        self._vm = kwargs.pop('vm')
        super().__init__(*args, **kwargs)

        self._text = tk.StringVar()
        self._text.set(text)
        self._gain = tk.DoubleVar()

        self._max = 10
        self._min = 0

        self._text_label = ttk.Label(master=self, text=self._text.get())

        self._slider = ttk.Scale(
            master=self,
            from_=0.0,
            to=10.0,
            orient='horizontal',
            length=80,
            variable=self._gain
        )

        self._gain_label = ttk.Label(master=self, text=str(self._gain.get()))
        self._seperator = ttk.Separator(master=self, orient='horizontal')

        self._text_label.grid(row=0, column=0)
        self._slider.grid(row=1, column=0, padx=10, pady=5, sticky="NSEW")
        self._gain_label.grid(row=2, column=0)
        self._seperator.grid(row=3, column=0, pady=10, sticky="NSEW")

    def _update_label(self):
        self._gain_label['text'] = str(round(self._gain.get(), 1))

    @property
    def gain(self):
        return self._gain.get()

    @gain.setter
    def gain(self, gain):
        if gain > self._max:
            gain = self._max
        elif gain < self._min:
            gain = self._min

        self._gain.set(gain)
        self._update_label()

    @property
    def text(self):
        return self._text.get()

    @text.setter
    def text(self, text):
        self._text.set(text)


class CheckButton(ttk.Frame):
    def __init__(self, *args, **kwargs):
        self._text = kwargs.pop('text')
        self._vm = kwargs.pop('vm')
        self._width = kwargs.pop('width', None)
        super().__init__(*args, **kwargs)

        self._button = ttk.Checkbutton(
            master=self,
            text=self._text,
            command=self.on_button,
            style="Toggle.TButton",
            width=self._width
        )
        self._button.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

    def on_button(self):
        print(f'{self._text} pressed')

    @property
    def text(self):
        return self._button['text']

    @text.setter
    def text(self, text):
        self._button['text'] = text


class Button(ttk.Frame):
    def __init__(self, *args, **kwargs):
        self._text = kwargs.pop('text')
        self._vm = kwargs.pop('vm')
        self._width = kwargs.pop('width', None)
        super().__init__(*args, **kwargs)

        self._button = ttk.Button(
            master=self,
            text=self._text,
            command=self.on_button,
            width=self._width
        )
        self._button.grid(row=0, column=0, padx=5, pady=5, sticky="NSEW")

    def on_button(self):
        print(f'{self._text} pressed')

    @property
    def text(self):
        return self._button['text']

    @text.setter
    def text(self, text):
        self._button['text'] = text
