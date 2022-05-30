#include <Servo.h>

// https://www.arduino.cc/reference/en/libraries/servo/
// 8 mm distance/rotation
// 0.5 rotations/sec

#define ENG_PIN 12
#define PWM_MIN 500
#define PWM_MAX 2500

Servo engine;

void setup() {
  // put your setup code here, to run once:
  engine.attach(ENG_PIN, PWM_MIN, PWM_MAX);
  /*
  engine.write(0);
  delay(2000);
  engine.write(90);
  */
}

void loop() {
  // put your main code here, to run repeatedly:
  
}

void spin(double mm) {
  if (mm >= 0){
    engine.write(180);
  }else{
    engine.write(0);
  }
  delay(abs((mm/8)*2000));
  engine.write(90);
}
