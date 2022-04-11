import time
from adafruit_servokit import ServoKit

pwm_hat = ServoKit(channels=16)

# esc valid input raneg 1100 to 1900
# using 100 dif for testing
thrust1 = pwm_hat.continuous_servo[0]
thrust1.set_pulse_width_range(min_pulse=1400, max_pulse=1600)
thrust1.throttle = 0

thrust2 = pwm_hat.continuous_servo[1]
thrust2.set_pulse_width_range(min_pulse=1400, max_pulse=1600)
thrust2.throttle = 0

thrust3 = pwm_hat.continuous_servo[2]
thrust3.set_pulse_width_range(min_pulse=1400, max_pulse=1600)
thrust3.throttle = 0

thrust4 = pwm_hat.continuous_servo[3]
thrust4.set_pulse_width_range(min_pulse=1400, max_pulse=1600)
thrust4.throttle = 0

time.sleep(5)

thrust1.throttle = 0.8

time.sleep(5)

thrust1.throttle = 0