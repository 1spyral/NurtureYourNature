import serial
import time
import pygame

pygame.mixer.init()

# Set up serial communication with Arduino
ser = serial.Serial(
    port='COM5',  # Default Arduino port on Linux (may need to change for your system)
    baudrate=9600,        # Match this with Arduino's Serial.begin() rate
    timeout=1             # Read timeout in seconds
)

# Give the serial connection time to establish
time.sleep(2)

print("Arduino connected")

#pin a = 1, pin b = 2
def move_motor(pin, speed):
    command = f"{pin}{speed}\n"
    ser.write(command.encode())
    time.sleep(0.1)  # Small delay to ensure command is processed


def sad():
    move_motor(3, 180)
    time.sleep(0.5)
    
def happy():
    pygame.mixer.music.load('happy.mp3')
    pygame.mixer.music.play()
    move_motor(3, 0)
    move_motor(3, 30)
    move_motor(3, 0)
    move_motor(3, 30)
    move_motor(3, 0)
    time.sleep(3)
    
def pour():
    sad()
    # Play sound while motor moves
    pygame.mixer.music.load('notgood.mp3')
    pygame.mixer.music.play()
    move_motor(1, 180)
    time.sleep(0.5)
    move_motor(1, 0)
    time.sleep(1.5)
    move_motor(1, 180)
    
def throw():
    # Dramatic throw sequence
    sad()
    pygame.mixer.music.load('mlg.mp3')
    pygame.mixer.music.play()
    # Wind up even further back for dramatic effect
    move_motor(2, 150)
    time.sleep(0.3)
    
    # Explosive forward throw motion
    move_motor(2, 0)
    time.sleep(0.2)
    
    # Small bounce back
    move_motor(2, 30)
    time.sleep(0.2)
    
    # Return to starting position
    move_motor(2, 180)
    
    time.sleep(1)
    move_motor(2, 0)
    
    time.sleep(1)
    move_motor(2, 180)
    
    time.sleep(1)
    move_motor(2, 0)
    
    time.sleep(1)
    move_motor(2, 180)
    
    time.sleep(1)
    move_motor(2, 0)
    
    time.sleep(1)
    move_motor(2, 180)

happy()

# while True:
    # print("Enter command: pin")
    # pin = input()
    # print("Enter command: speed")
    # speed = input()
    # move_motor(pin, speed)

    
