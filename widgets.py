import tkinter as tk
from tkinter import ttk
from basewidgets import Dial, Progress, Slider, CheckButton, Button


class StripWidget(ttk.Labelframe):
    def __init__(self, *args, **kwargs):
        self._index = kwargs.pop('index')
        self._vm = kwargs.pop('vm')

        super().__init__(*args, **kwargs)

        label = self._vm.strip[self._index].label
        text = label if len(label) < 10 else f'{label[:10]}...'

        self.configure(text=text)

        self.dial_frame = ttk.Frame(self)
        self.dial_frame.grid(row=0, column=0)

        # dial
        self.dial = Dial(self.dial_frame, text='dial', vm=self._vm)
        self.dial.grid(row=0, column=0, sticky="NSEW")

        self.dial = Dial(self.dial_frame, text='dial', vm=self._vm)
        self.dial.grid(row=0, column=1, sticky="NSEW")

        self.slider_frame = ttk.Frame(self)
        self.slider_frame.grid(row=1, column=0)

        # progress
        self.progress = Progress(self.slider_frame)
        self.progress.grid(row=1, rowspan=5, column=0, padx=(20, 0), pady=(0, 17))

        # slider
        self.slider = Slider(self.slider_frame, vm=self._vm)
        self.slider.grid(row=1, rowspan=5, column=1, sticky="NSEW")

        # buttons
        self.button1 = CheckButton(self.slider_frame, text='button 1', vm=self._vm)
        self.button1.grid(row=1, column=2, sticky="NSEW")

        self.button2 = CheckButton(self.slider_frame, text='button 2', vm=self._vm)
        self.button2.grid(row=2, column=2, sticky="NSEW")

        self.button3 = CheckButton(self.slider_frame, text='button 3', vm=self._vm)
        self.button3.grid(row=3, column=2, sticky="NSEW")

        self.button4 = CheckButton(self.slider_frame, text='button 4', vm=self._vm)
        self.button4.grid(row=4, column=2, sticky="NSEW")

        self.button5 = CheckButton(self.slider_frame, text='button 5', vm=self._vm)
        self.button5.grid(row=5, column=2, sticky="NSEW")

    @property
    def gain(self):
        return self.slider.gain

    @gain.setter
    def gain(self, gain):
        self.slider.gain = gain

    @property
    def level(self):
        return self.progress.level

    @level.setter
    def level(self, level):
        self.progress.level = level

    def update(self):
        # level
        current_lvl = 80 + max(self._vm.strip[self._index].levels.postfader)
        step = 0.7
        if self.level < current_lvl:
            self.level = current_lvl
        else:
            self.level -= step

        # gain
        current_gain = self._vm.strip[self._index].gain
        if self.gain != current_gain:
            self.gain = current_gain

class BusWidget(ttk.Labelframe):
    def __init__(self, *args, **kwargs):
        self._index = kwargs.pop('index')
        self._vm = kwargs.pop('vm')

        super().__init__(*args, **kwargs)

        device = self._vm.bus[self._index].device
        text = device if len(device) < 27 else f'{device[:27]}...'

        self.configure(text=text)
        
        self.slider_frame = ttk.Frame(self)
        self.slider_frame.grid(row=1, column=0)

        self.progress = Progress(self.slider_frame)
        self.progress.grid(row=1, rowspan=5, column=0, padx=(20, 0), pady=(0, 17))

        self.slider = Slider(self.slider_frame, vm=self._vm)
        self.slider.grid(row=1, rowspan=5, column=1, sticky="NSEW")

        self.button = CheckButton(self.slider_frame, text='button', vm=self._vm)
        self.button.grid(row=5, column=2, pady=(8, 0))

    @property
    def gain(self):
        return self.slider.gain

    @gain.setter
    def gain(self, gain):
        self.slider.gain = gain

    @property
    def level(self):
        return self.progress.level

    @level.setter
    def level(self, level):
        self.progress.level = level

    def update(self):
        # level
        current_level = 80 + max(self._vm.bus[self._index].levels.all)
        level_step = 0.7
        if self.level < current_level:
            self.level = current_level
        else:
            self.level -= level_step

        # gain
        current_gain = self._vm.bus[self._index].gain
        if self.gain != current_gain:
            self.gain = current_gain

class ControlWidget(ttk.Labelframe):
    def __init__(self, *args, **kwargs):
        self._vm = kwargs.pop('vm')
        super().__init__(*args, **kwargs)

        self._buttons = []
        for i in range(5):
            self._buttons.append(Button(
                master=self,
                text=f'button {i}',
                vm=self._vm,
                width=8
            ))
            self._buttons[-1].grid(row=0, column=i)