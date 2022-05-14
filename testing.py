import serial

arduino = serial.Serial(port="COM38", baudrate=115200, timeout=0)


def get_arduino_data():
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').rstrip()
        data = data.strip('<').strip('>').split(',')
    else:
        data = ''
    return data


while True:
    data = get_arduino_data()
    if data != '':
        print(data)
