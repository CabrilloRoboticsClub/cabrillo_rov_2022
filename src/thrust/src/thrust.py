#!/usr/bin/env python3

import rospkg
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from dynamic_reconfigure.server import Server  # allows us to change consts on the fly
import pigpio


class Thrust:
  def __init__(self):
    rospy.init_node('thrust')
    self.thruster_pins = [20, 19, 24, 27]
    self.base = 1500
    self.max_from_base = 400  # max_forward = 1900, max_backward = 1100
    self.last = [self.base] * 4
    self.thrust = None
    self.overridden = False
    self.scaler = self.max_from_base / 3.0  # @TODO dynamic reconfigure this

  # @sync #TODO: add blocking so if we get a joy/command msg we will ignore it
  def move(self, data):
    if not self.overridden:
      data.linear.x  # forward/back
      data.angular.x  # "yaw" rotate left/right
      data.linear.z  # up/down
      data.angular.z  # "roll" rotate side/side # should not do this much/at all
      self.thrust(self.thruster_pins[0], 1500 + (data.linear.x * self.scaler))
      self.thrust(self.thruster_pins[1], 1500 + (data.linear.x * self.scaler))
      self.thrust(self.thruster_pins[2], 1500 - (data.linear.z * self.scaler))
      self.thrust(self.thruster_pins[3], 1500 - (data.linear.z * self.scaler))

      """
      for thruster_num in range(len(self.thruster_pins)):
        if abs(self.last[thruster_num] - data[thruster_num]) > .01:
          self.thrust(self.thruster_pins[thruster_num], 1500 + (data.axes[0] * 130))
          self.last[thruster_num] = data.axes[0]
      """

  # @sync #TODO: add blocking so if we get a joy/command msg we will ignore it
  def override(self, data):
    self.overridden = data
    if data:
      self.thrust(self.thruster_pins[0], 1500)
      self.thrust(self.thruster_pins[1], 1500)
      self.thrust(self.thruster_pins[2], 1500)
      self.thrust(self.thruster_pins[3], 1500)

  # Initializes everything
  def run(self):
    pi = pigpio.pi()
    pi.set_servo_pulsewidth(self.thruster_pins[0], 1500)
    pi.set_servo_pulsewidth(self.thruster_pins[1], 1500)
    pi.set_servo_pulsewidth(self.thruster_pins[2], 1500)
    pi.set_servo_pulsewidth(self.thruster_pins[3], 1500)
    self.thrust = pi.set_servo_pulsewidth
    rospy.Subscriber("cmd_vel", Twist, self.move)
    rospy.Subscriber("override", Bool, self.override)
    rospy.spin()


if __name__ == '__main__':
  t = Thrust()
  t.run()
