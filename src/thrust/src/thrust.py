#!/usr/bin/env python3

import math
import rospkg
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from dynamic_reconfigure.server import Server  # allows us to change consts on the fly
import pigpio


class Thrust:
  def __init__(self, pi):
    self.pi = pi
    rospy.init_node('thrust')
    self.thruster_pins = [20, 19, 24, 27]
    self.base = 1500
    self.max_from_base = 400  # max_forward = 1900, max_backward = 1100
    self.last = [self.base] * 4
    self.thrust = None
    self.overridden = False
    self.scaler = self.max_from_base / 2.0  # @TODO dynamic reconfigure this
    self.angular_scaler = 1.0 / 2.0                # @TODO dynamic reconfigure this

  # @sync #TODO: add blocking so if we get a joy/command msg we will ignore it
  def move(self, data):
    if not self.overridden:
      # data.linear.x  # forward/back
      # data.angular.x  # "roll" rotate side/side & Sideways & roll (angular.x & linear.y) (roll & sway)
      # data.linear.z  # up/down
      # data.angular.z  # "yaw" rotate left/right

      # @NOTE: data.angular.x is already from -1 -> 1 so can just use it as such
      self.thrust(self.thruster_pins[0], self.base + ((data.linear.x - (self.angular_scaler * data.angular.z)) * self.scaler))
      self.thrust(self.thruster_pins[1], self.base + ((data.linear.x + (self.angular_scaler * data.angular.z)) * self.scaler))
      self.thrust(self.thruster_pins[2], self.base + ((data.linear.z - (self.angular_scaler * data.angular.x)) * self.scaler))
      self.thrust(self.thruster_pins[3], self.base + ((data.linear.z + (self.angular_scaler * data.angular.x)) * self.scaler))

  # @sync #TODO: add blocking so if we get a joy/command msg we will ignore it
  def override(self, data):
    self.overridden = data.data
    if data.data:
      self.thrust(self.thruster_pins[0], self.base)
      self.thrust(self.thruster_pins[1], self.base)
      self.thrust(self.thruster_pins[2], self.base)
      self.thrust(self.thruster_pins[3], self.base)

  # Initializes everything
  def run(self):
    self.pi.set_servo_pulsewidth(self.thruster_pins[0], self.base)
    self.pi.set_servo_pulsewidth(self.thruster_pins[1], self.base)
    self.pi.set_servo_pulsewidth(self.thruster_pins[2], self.base)
    self.pi.set_servo_pulsewidth(self.thruster_pins[3], self.base)
    self.thrust = self.pi.set_servo_pulsewidth
    rospy.Subscriber("cmd_vel", Twist, self.move)
    rospy.Subscriber("override", Bool, self.override)
    rospy.spin()


class Light:
  def __init__(self, pi):
    self.pi = pi
    self.light_pin = None

  def light_message(self, data):
    self.pi.write(self.light_pin, int(data.data))  # 0(False/Off) / 1(True/On)

  def run(self):
    rospy.Subscriber("light", Bool, self.light_message)


if __name__ == '__main__':
  pi = pigpio.pi()
  t = Thrust(pi)
  l = Light(pi)

  # after you figure out which pin you want to use and put it in light_pin then comment this back in
  # l.run()
  t.run()