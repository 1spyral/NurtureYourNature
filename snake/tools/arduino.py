import serial

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1) 

def write(x):
    arduino.write(bytes(x, "utf-8"))

def read():
    return arduino.readline()