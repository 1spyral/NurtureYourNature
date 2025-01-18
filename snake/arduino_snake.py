import serial
import time

# Set up serial communication with Arduino
ser = serial.Serial(
    port='/dev/cu.usbserial-1130',  # Default Arduino port on Linux (may need to change for your system)
    baudrate=9600,        # Match this with Arduino's Serial.begin() rate
    timeout=1             # Read timeout in seconds
)

# Give the serial connection time to establish
time.sleep(1)

print("Arduino connected")

#pin a = 1, pin b = 2
def move_motor(pin, speed):
    command = f"{pin}{speed}\n"
    ser.write(command.encode())
    time.sleep(0.1)  # Small delay to ensure command is processed


    