#include <Servo.h>

// https://www.arduino.cc/reference/en/libraries/servo/

#define ENG_PIN 3
#define PWM_MIN 500
#define PWM_MAX 2500

Servo engine;

void setup() {
  // put your setup code here, to run once:
  engine.attach(ENG_PIN, PWM_MIN, PWM_MAX);
  engine.write(90);
  delay(45000);
}

void loop() {
  // put your main code here, to run repeatedly:
  
}
