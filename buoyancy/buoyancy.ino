#include <Servo.h>

// https://www.arduino.cc/reference/en/libraries/servo/
// 8 mm distance/rotation
// 0.5 rotations/sec
//When Uploading to current Arduino Nano use the “ATmega380P (Old Bootloader)" option, for the new board defaults work 

#define ENG_PIN 2
#define PWM_MIN 500
#define PWM_MAX 2500

Servo engine;

void setup() {
  engine.attach(ENG_PIN, PWM_MIN, PWM_MAX);
} //end setup

// @TODO you might try moving all of the code besides the while loop into
// setup some arduinos have issues with that
void loop() {
  //Start at the surface of the pool
  spin(-80.0);     //Homing (start with syring in open position)
  delay(45000); // 45 sec get into position
  spin(80.0);  // Down
  delay(45000); // 45 sec sink
  spin(-80.0);   // Up
  delay(45000); // 45 sec ascend
  spin(80.0);  // Down
  delay(45000); // 45 sec sink
  spin(-80.0);   // Up
  // ascend up then drop into a forever while loop
  // until unit is power cycled
  while(true){;}
} //end loop

void spin(double mm) {
  if (mm >= 0){
    engine.write(180);
  }else{
    engine.write(0);
  }
  delay(abs((mm/8)*2000));
  engine.write(90);
}
