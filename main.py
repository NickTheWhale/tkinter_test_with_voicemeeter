import serial
from serial import SerialException

from voicemeeter import *
import voicemeeter
from voicemeeter.errors import VMRDriverError

from app import App

# constants
KIND = 'potato'


def main():
    # login to voicemeeter
    global vmr
    vmr = voicemeeter.remote(KIND)
    try:
        vmr.login()
    except VMRDriverError:
        voicemeeter.launch(KIND)

    # serial loop
    global arduino
    try:
        arduino = serial.Serial(port="COM38", baudrate=115200, timeout=0)
        connected = True
    except SerialException as e:
        connected = False
        print(e)

    # create global application object
    global app
    app = App("VMR Utility")
    app.initialize_widgets()
    if connected:
        app.after(10, print_serial)

    # add some ports to the combobox
    ports = ["COM38", "COM1", "COM17"]
    app.add_port(ports)

    # gui loop
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()


def print_serial():
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').rstrip()
        data = data.strip('<').strip('>').split(',')
        print("data:", data)
    app.after(10, print_serial)


if __name__ == "__main__":
    main()
