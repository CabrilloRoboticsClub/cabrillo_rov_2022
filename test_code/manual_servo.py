import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

pca = PCA9685(busio.I2C(SCL, SDA))

pca.frequency = 60

# esc valid input raneg 1100 to 1900
# using 100 dif for testing
thrust1 = servo.Servo(pca.channels[0], min_pulse=1400, max_pulse=1600)
thrust2 = servo.Servo(pca.channels[1], min_pulse=1400, max_pulse=1600)
thrust3 = servo.Servo(pca.channels[2], min_pulse=1400, max_pulse=1600)
thrust4 = servo.Servo(pca.channels[3], min_pulse=1400, max_pulse=1600)

claw1 = servo.Servo(pca.channels[4])
claw2 = servo.Servo(pca.channels[5])
claw3 = servo.Servo(pca.channels[6])
claw4 = servo.Servo(pca.channels[7])

# print("thrust fraction = 0, angle = 180")

# thrust1.fraction = 0
# thrust1.angle = 180
# thrust2.fraction = 0
# thrust2.angle = 180
# thrust3.fraction = 0
# thrust3.angle = 180
# thrust4.fraction = 0
# thrust4.angle = 180


# # that section above works and I get the 2 init beeps
# print("sleep 5")
# time.sleep(5)
# print("fraction 1")
# thrust1.fraction = 1
# thrust2.fraction = 1
# thrust3.fraction = 1
# thrust4.fraction = 1

# print("angle 150")
# thrust1.angle = 150
# thrust2.angle = 150
# thrust3.angle = 150
# thrust4.angle = 150

# time.sleep(30)

claw1.angle = 90
claw2.angle = 90
claw3.angle = 90
claw4.angle = 90