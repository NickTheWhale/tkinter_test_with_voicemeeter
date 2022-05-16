import serial
from serial import SerialException

from voicemeeter import *
import voicemeeter
from voicemeeter.errors import VMRDriverError

from app import App

# constants
KIND = 'potato'
arduino_is_connected = False


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
    # try:
    arduino = serial.Serial(port="COM38", baudrate=115200, timeout=0)
    arduino_is_connected = True
    # except SerialException:
    #     print("failed to connect to serial port")
    # finally:
    #     print("failed to connect to serial port")
    #     arduino_is_connected = False

    # create global application object
    global app
    app = App("VMR Utility")
    app.initialize_widgets()

    if arduino_is_connected:
        app.after(10, print_serial)

    # gui loop
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()


def task():
    print("hey is this thing loopin'?", time.time())
    app.after(1000, task)


def print_serial():
    if arduino_is_connected:
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').rstrip()
            data = data.strip('<').strip('>').split(',')
            print("data:", data)
    app.after(10, print_serial)


def any_click(name, ent):
    print(f'name: {name} ent: {ent}')


if __name__ == "__main__":
    main()
