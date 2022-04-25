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

    # create class member variabe for the kit instance
    self.kit = None

    self.gripper_pins = [4, 5, 14, 15]
    # 4 front vertical
    # 5 front horizontal
    # 14 rear horizontal
    # 15 rear vertical

    # pwm value at claw fully closed
    self.pwm_min = 500
    # pwm value at claw fullly open
    self.pwm_max = 1500
    # pwm value to start at
    self.pwm_base = 1500

    # angle value for claw closed
    self.angle_min = 0
    # angle value for claw open
    self.angle_max = 100
    # angle value at claw halfway open
    self.angle_base = 50


  def move(self, data, which_gripper=0):
    self.kit.servo[self.gripper_pins[which_gripper]].angle = self.angle_base + (data * (self.angle_max / 2))
    

  # Initializes everything
  def run(self):
    # instanciate servokit for the 16 channel servo board
    self.kit = ServoKit(channels = 16)

    # run through the gripper pins and set them up
    for pin in self.gripper_pins:
      # set the actuation range for the servokit library
      self.kit.servo[pin].actuation_range = self.angle_max - self.angle_min
      # set the pwm range the servos respond to
      self.kit.servo[pin].set_pulse_width_range(self.pwm_min, self.pwm_max)
      # initialise the claw servos half open
      self.kit.servo[pin].angle = self.angle_base

    rospy.Subscriber("cmd_gripper1", Float32, self.move, 0)
    rospy.Subscriber("cmd_gripper2", Float32, self.move, 1)
    rospy.spin()


if __name__ == '__main__':
  g = Grip()
  g.run()

kit.servo[14].set_pulse_width_range(500, 1500)
kit.servo[14].actuation_range = 100