import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

pca = PCA9685(busio.I2C(SCL, SDA))

pca.frequency = 60

thrust1 = servo.Servo(pca.channels[0], min_pulse=100, max_pulse=2000)
thrust2 = servo.Servo(pca.channels[1], min_pulse=100, max_pulse=2000)
thrust3 = servo.Servo(pca.channels[2], min_pulse=100, max_pulse=2000)
thrust4 = servo.Servo(pca.channels[3], min_pulse=100, max_pulse=2000)

claw1 = servo.Servo(pca.channels[4])
claw2 = servo.Servo(pca.channels[5])
claw3 = servo.Servo(pca.channels[6])
claw4 = servo.Servo(pca.channels[7])

# set all the thrusters to zero to init

thrust1.angle = 180
thrust1.fraction = 0

thrust2.angle = 180
thrust2.fraction = 0

thrust3.angle = 180
thrust3.fraction = 0

thrust4.angle = 180
thrust4.fraction = 0

# this should start them moving
'''thrust1.angle = 90
#thrust1.fraction = 1

thrust2.angle = 90
#thrust2.fraction = 1

thrust3.angle = 90
#thrust3.fraction = 1

thrust4.angle = 90
#thrust4.fraction = 1
'''

thrust1.angle = input()