#!/usr/bin/env python3

import rospkg
import rospy
import board
import busio
import adafruit_pca9685
from std_msgs.msg import Float32
from dynamic_reconfigure.server import Server  # allows us to change consts on the fly
from adafruit_servokit import ServoKit


class Grip:
  def __init__(self):
    rospy.init_node('Grip')
    self.gripper_pins = [4, 5]
    self.base = 1500
    self.angle = 90
    self.grippers = None
    # 500-2500 if we want 180 deg, 1000-2000 for 90 deg
    self.max_from_base = 500  # max_forward = 2000, max_backward = 1000

  def move(self, data, which_gripper=0):
    servos.servo[self.gripper_pins[which_gripper]].angle = self.angle + (data * self.angle)
    

  # Initializes everything
  def run(self):
    servos = ServoKit(channels = 16)
    servos.servo[self.gripper_pins[0]].set_pulse_width_range(self.base - self.max_from_base, self.base + self.max_from_base)
    servos.servo[self.gripper_pins[1]].set_pulse_width_range(self.base - self.max_from_base, self.base + self.max_from_base)
    servos.servo[0].angle = self.angle
    servos.servo[1].angle = self.angle
    rospy.Subscriber("cmd_gripper1", Float32, self.move, 0)
    rospy.Subscriber("cmd_gripper2", Float32, self.move, 1)
    rospy.spin()


if __name__ == '__main__':
  g = Grip()
  g.run()
