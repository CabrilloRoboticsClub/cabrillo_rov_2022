import time
from adafruit_servokit import ServoKit

pwm_hat = ServoKit(channels=16)

# esc valid input raneg 1100 to 1900
# using 100 dif for testing
thrust1 = pwm_hat.continuous_servo[0]
thrust1.set_pulse_width_range(1400, 1600)
thrust1.throttle = 0

pwm_hat.continuous_servo[1].set_pulse_width_range(1400, 1600)
pwm_hat.continuous_servo[1].throttle = 0

pwm_hat.continuous_servo[2].set_pulse_width_range(1400, 1600)
pwm_hat.continuous_servo[2].throttle = 0

pwm_hat.continuous_servo[3].set_pulse_width_range(1400, 1600)
pwm_hat.continuous_servo[3].throttle = 0

time.sleep(5)

thrust1.throttle = 0.8

time.sleep(5)

thrust1.throttle = 0