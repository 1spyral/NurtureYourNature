#include <Servo.h>

// Create servo objects
Servo servo1;
Servo servo2;
Servo servo3;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Attach servos to pins
  servo1.attach(2);
  servo2.attach(3);
  servo3.attach(4);
  
  // Initialize servos to center position
  servo1.write(90);
  servo2.write(90);
  servo3.write(90);
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming command
    int pin = Serial.read() - '0';  // Convert char to int
    int angle = Serial.parseInt();
    
    // Control servo based on pin and input angle
    if (angle >= 0 && angle <= 180) {
      switch(pin) {
        case 1:
          servo1.write(angle);
          break;
        case 2:
          servo2.write(angle);
          break;
        case 3:
          servo3.write(angle);
          break;
      }
    }
    
    // Clear any remaining characters
    while(Serial.available() > 0) {
      Serial.read();
    }
  }
}
