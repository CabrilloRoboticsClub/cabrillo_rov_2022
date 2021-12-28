#!/usr/bin/env python3

import rospkg
import rospy
from std_msgs.msg import Float32
from dynamic_reconfigure.server import Server  # allows us to change consts on the fly
import pigpio


class Grip:
  def __init__(self):
    rospy.init_node('Grip')
    self.gripper_pins = [1, 7]
    self.base = 1500
    self.grippers = None
    # 500-2500 if we want 180 deg, 1000-2000 for 90 deg
    self.max_from_base = 500  # max_forward = 2000, max_backward = 1000

  def move(self, data, which_gripper=0):
    self.grippers(self.gripper_pins[which_gripper], 1500 + (data * self.max_from_base))

  # Initializes everything
  def run(self):
    pi = pigpio.pi()
    pi.set_servo_pulsewidth(self.gripper_pins[0], 1500)
    pi.set_servo_pulsewidth(self.gripper_pins[1], 1500)
    self.grippers = pi.set_servo_pulsewidth
    rospy.Subscriber("cmd_gripper1", Float32, self.move, 0)
    rospy.Subscriber("cmd_gripper2", Float32, self.move, 1)
    rospy.spin()


if __name__ == '__main__':
  g = Grip()
  g.run()
