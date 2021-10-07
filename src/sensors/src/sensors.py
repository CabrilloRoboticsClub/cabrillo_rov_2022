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

if __name__ == '__main__':
    rospy.init_node('sensors')
    i2c = board.I2C()  # uses board.SCL and board.SDA
    sensor = adafruit_lis3mdl.LIS3MDL(i2c)
    mpu = adafruit_mpu6050.MPU6050(i2c)
    imu_publisher = rospy.Publisher('/imu/raw', Imu, queue_size=10)
    mag_publisher = rospy.Publisher('/mag/raw', MagneticField, queue_size=10)
    temp_publisher = rospy.Publisher('/temp/raw', Temperature, queue_size=10)
    pressure_publisher = rospy.Publisher('/pressure/raw', FluidPressure, queue_size=10)
    while not rospy.is_shutdown():
        pass # convert gyro to quaternions?
        imu_publisher.publish(orientation=Quaternion(*mpu.gyro,0),linear_acceleration=Vector3(*mpu.acceleration))
        mag_publisher.publish( MagneticField(magnetic_field=Vector3(*sensor.magnetic)))
        temp_publisher.publish(Temperature(temperature=mpu.temperature))
        pressure_publisher.publish(FluidPressure(fluid_pressure=0))
        time.sleep(0.1)

