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
    self.gripper_pins = [4, 5, 14, 15]
    # 4 front vertical
    # 5 front horizontal
    # 14 rear horizontal
    # 15 rear vertical

    self.actuation_range = 180
    self.pwm_min = 1000
    self.pwm_max = 2000

    #self.base = 1500
    #self.angle = 90
    #self.grippers = None
    # 500-2500 if we want 180 deg, 1000-2000 for 90 deg
    self.max_from_base = 500  # max_forward = 2000, max_backward = 1000

  def move(self, data, which_gripper=0):
    servos.servo[self.gripper_pins[which_gripper]].angle = self.angle + (data * self.angle)
    

  # Initializes everything
  def run(self):
    # instanciate servokit for the 16 channel servo board
    kit = ServoKit(channels = 16)

    # front vertical
    kit.servo[self.gripper_pins[0]].actuation_range = self.actuation_range
    kit.servo[self.gripper_pins[0]].set_pulse_width_range(self.pwm_min, self.pwm_max)

    # front horizontal
    kit.servo[self.gripper_pins[1]].actuation_range = self.actuation_range
    kit.servo[self.gripper_pins[1]].set_pulse_width_range(self.pwm_min, self.pwm_max)

    # rear horizontal
    kit.servo[self.gripper_pins[2]].actuation_range = self.actuation_range
    kit.servo[self.gripper_pins[2]].set_pulse_width_range(self.pwm_min, self.pwm_max)

    # rear vertical
    kit.servo[self.gripper_pins[3]].actuation_range = self.actuation_range
    kit.servo[self.gripper_pins[3]].set_pulse_width_range(self.pwm_min, self.pwm_max)

    #servos.servo[self.gripper_pins[0]].set_pulse_width_range(self.base - self.max_from_base, self.base + self.max_from_base)
    #servos.servo[self.gripper_pins[1]].set_pulse_width_range(self.base - self.max_from_base, self.base + self.max_from_base)
    #servos.servo[0].angle = self.angle
    #servos.servo[1].angle = self.angle
    rospy.Subscriber("cmd_gripper1", Float32, self.move, 0)
    rospy.Subscriber("cmd_gripper2", Float32, self.move, 1)
    rospy.spin()


if __name__ == '__main__':
  g = Grip()
  g.run()
