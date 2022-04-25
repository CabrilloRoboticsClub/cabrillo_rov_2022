#!/usr/bin/env python3
""" Display magnetometer data once per second """
"""
http://docs.ros.org/en/api/sensor_msgs/html/msg/Imu.html
http://docs.ros.org/en/api/sensor_msgs/html/msg/MagneticField.html
http://docs.ros.org/en/api/sensor_msgs/html/msg/Temperature.html

http://docs.ros.org/en/api/sensor_msgs/html/msg/FluidPressure.html

PlotJuggler
"""
import time
import board
import adafruit_lis3mdl
import adafruit_mpu6050
import rospy
from sensor_msgs.msg import Imu, MagneticField, Temperature, FluidPressure
from geometry_msgs.msg import Vector3, Quaternion
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33


class Sensors:
  def __init__(self):
    rospy.init_node('sensors')
    self.frame = "odom"
    i2c = board.I2C()  # uses board.SCL and board.SDA
    # self.mag_sensor = adafruit_lis3mdl.LIS3MDL(i2c)
    self.mpu = LSM6DS33(i2c)
    # self.mpu = adafruit_mpu6050.MPU6050(i2c)  # Other Sensor not currently installed
    self.imu_publisher = rospy.Publisher('/imu_data', Imu, queue_size=10)
    self.mag_publisher = rospy.Publisher('/mag/raw', MagneticField, queue_size=10)
    self.temp_publisher = rospy.Publisher('/temperature/raw', Temperature, queue_size=10)
    self.pressure_publisher = rospy.Publisher('/pressure/raw', FluidPressure, queue_size=10)

  def run(self):
    rospy.Timer(rospy.Duration(.1), self.read_imu)  # call function at 10hz
    rospy.Timer(rospy.Duration(.1), self.read_mag)
    rospy.Timer(rospy.Duration(1), self.read_temp)  # call function at 1hz
    rospy.Timer(rospy.Duration(.1), self.read_pressure)
    rospy.spin()

  def read_imu(self, _):  # for some reason a rospy.timer.TimerEvent object is being passed in, did not used to be
    imu = Imu(orientation=Quaternion(*self.mpu.gyro, 0), linear_acceleration=Vector3(*self.mpu.acceleration))
    imu.header.frame_id = self.frame
    imu.header.stamp = rospy.Time.now()
    self.imu_publisher.publish(imu)

  def read_mag(self, _):
    mag_f = MagneticField(magnetic_field=Vector3(*self.mpu.magnetic))
    mag_f.header.frame_id = self.frame
    mag_f.header.stamp = rospy.Time.now()
    self.mag_publisher.publish(mag_f)

  def read_temp(self, _):
    temp = Temperature(temperature=self.mpu.temperature)
    # very strange was getting -7.8125 at room temp if I held it could get it out of the negatives
    temp.header.frame_id = self.frame
    temp.header.stamp = rospy.Time.now()
    self.temp_publisher.publish(temp)

  def read_pressure(self, _):
    fluid_p = FluidPressure(fluid_pressure=0)  # @TODO read the sensor data
    fluid_p.header.frame_id = self.frame
    fluid_p.header.stamp = rospy.Time.now()
    self.pressure_publisher.publish(fluid_p)


if __name__ == '__main__':
  s = Sensors()
  s.run()
