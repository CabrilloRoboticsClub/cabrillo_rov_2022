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
  /*
   * we open the top of the bouyancy engine and flip the switch
   * the bouyancy engine powers on and goes to water out position to evacuate the air from the syringe
   */

   // evacuate the air from the surface
  WaterOut();

  /*
   * wait 2 minutes to give time to get the bouyancy engine into position with the robot
   */
  delay(3*60*1000UL); //delay 3 minutes

/*
 * now starts the vertical profiling
 */
  
  // first descend (1/3)
  WaterIn();
  delay(1*60*1000UL); // delay 1 minute

// first ascend (1/3)
  WaterOut();
  delay(1*60*1000UL); // delay 1 minute

  // second descend (2/3)
  WaterIn();
  delay(1*60*1000UL); // delay 1 minute

  // second ascend (2/3)
  WaterOut();
  delay(1*60*1000UL); // delay 1 minute

  // third descend (3/3)
  WaterIn();
  delay(1*60*1000UL); // delay 1 minute

  // third ascend (3/3)
  WaterOut();

  
  delay(5*60*1000UL); // delay 5 minute
  // pull air in at end to reset
  WaterIn();
  
  /*
   * drop into a forever loop when finished
   */
  while(true){;}

} //end loop

void WaterIn() {
  spin(80);
}

void WaterOut(){
  spin(-80);
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
