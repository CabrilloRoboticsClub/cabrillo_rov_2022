#!/bin/python3
#
# code for manual testing sensor functionality outside of ros
#
# Organization: 
# - Cabrillo Robotics Club
# - Cabrillo College Student Senate Inter Club Council
# Authors:
# - Ciaran Farley
# - Carter Frost

from adafruit_lsm6ds.lsm6ds33 import LSM6DS33
from adafruit_lis3mdl import LIS3MDL
import board
i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = LSM6DS33(i2c) #toggle 1
mag = LIS3MDL(i2c) #toggle 2

print(mpu.gyro) #toggle 1
print(mag.magnetic) #toggle 2