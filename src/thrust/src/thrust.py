#!/usr/bin/env python3

import math
import rospkg
import rospy
import board
import busio
import adafruit_pca9685
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from dynamic_reconfigure.server import Server  # allows us to change consts on the fly
from adafruit_servokit import ServoKit


class Thrust:
  def __init__(self):
    rospy.init_node('thrust')
    self.thruster_pins = [0, 1, 2, 3]
    self.base = 1500
    self.max_from_base = 400  # max_forward = 1900, max_backward = 1100
    self.last = [self.base] * 4
    self.thrust = None
    self.overridden = False
    self.scaler = 1.0 / 3.0 # @TODO dynamic reconfigure this

  # @sync #TODO: add blocking so if we get a joy/command msg we will ignore it
  def move(self, data):
    if not self.overridden:
      data.linear.x  # forward/back
      data.angular.x  # "roll" rotate side/side # should not do this much/at all, currently ignored
      data.linear.z  # up/down
      data.angular.z  # "yaw" rotate left/right

      # math.cos() 
      # @NOTE: data.angular.x is already from -1 -> 1 so can just use it as such
      
      servos.continuous_servo[self.thruster_pins[0]].throttle = (data.linear.x - data.angular.z) * self.scaler
      servos.continuous_servo[self.thruster_pins[1]].throttle = (data.linear.x + data.angular.z) * self.scaler
      servos.continuous_servo[self.thruster_pins[2]].throttle = data.linear.z * self.scaler
      servos.continuous_servo[self.thruster_pins[3]].throttle = data.linear.z * self.scaler

  # @sync #TODO: add blocking so if we get a joy/command msg we will ignore it
  def override(self, data):
    self.overridden = data.data
    if data.data:
      servos.continuous_servo[self.thruster_pins[0]].throttle = 0
      servos.continuous_servo[self.thruster_pins[1]].throttle = 0
      servos.continuous_servo[self.thruster_pins[2]].throttle = 0
      servos.continuous_servo[self.thruster_pins[3]].throttle = 0

  # Initializes everything
  def run(self):
    servos = ServoKit(channels = 16)
    servos.servo[self.thruster_pins[0]].set_pulse_width_range(self.base - self.max_from_base, self.base + self.max_from_base)
    servos.servo[self.thruster_pins[1]].set_pulse_width_range(self.base - self.max_from_base, self.base + self.max_from_base)
    servos.servo[self.thruster_pins[2]].set_pulse_width_range(self.base - self.max_from_base, self.base + self.max_from_base)
    servos.servo[self.thruster_pins[3]].set_pulse_width_range(self.base - self.max_from_base, self.base + self.max_from_base)
    servos.continuous_servo[self.thruster_pins[0]].throttle = 0
    servos.continuous_servo[self.thruster_pins[1]].throttle = 0
    servos.continuous_servo[self.thruster_pins[2]].throttle = 0
    servos.continuous_servo[self.thruster_pins[3]].throttle = 0
    rospy.Subscriber("cmd_vel", Twist, self.move)
    rospy.Subscriber("override", Bool, self.override)
    rospy.spin()


if __name__ == '__main__':
  t = Thrust()
  t.run()
