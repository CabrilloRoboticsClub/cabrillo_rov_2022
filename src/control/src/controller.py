#!/usr/bin/env python3

import rospkg
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32, Bool


class Controller:
  def __init__(self):
    rospy.init_node('controller')
    self.last = [0] * 6
    self.thruster_cmd = rospy.Publisher('cmd_vel', Twist, queue_size=4)
    self.gripper1_cmd = rospy.Publisher('cmd_gripper1', Float32, queue_size=4)
    self.gripper2_cmd = rospy.Publisher('cmd_gripper2', Float32, queue_size=4)
    self.light = rospy.Publisher('light', Bool, queue_size=2)
    self.light_on = False
    self.override_pub = rospy.Publisher('override', Bool, queue_size=2)
    self.overridden = False

    # @TODO create and add service call for taking/saving images

    self.last[2] = 0  # start grippers at open
    self.last[5] = 0  # start grippers at open

  # if the override topic changes somewhere else this will update Controllers knowledge
  def override(self, data):
    self.overridden = data.data

  def callback(self, data):
    t = Twist()
    significant_twist_delta = False
    gripper_scaler = .05  # if you want the top triggers to move more per a click then increase this number
    """ @NOTE
        axis_angular.z: 0  # left stick up/down
        axis_linear.x: 1   # left stick left/right
        axis_angular.x: 3  # right stick left/right
        axis_linear.z: 4   # right stick up/down
        
        @note value 1 means not pressed, -1 fully pressed
        gripper left close axis 5  # left trigger "LT" on controller
        gripper left open button 5 # left button "LB" on controller
        
        @note value 1 means not pressed, -1 fully pressed
        gripper right close axis 2 
        gripper right open button 4
        
        A button is buttons[0]           == buttons: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        B button is buttons[1]           == buttons: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        X button is buttons[2]           == buttons: [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        Y button is buttons[3]           == buttons: [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        Left Top Trigger is buttons[4]   == buttons: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        Right Top Trigger is buttons[5]  == buttons: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        Back button is buttons[6]        == buttons: [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        Start button is buttons[7]       == buttons: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        Center button is buttons[8]      == buttons: [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        Left Stick Click is buttons[9]   == buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        Right Stick Click is buttons[10] == buttons: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        """
    for axis in [0, 1, 3, 4]:
      # if abs(self.last[axis] - data.axes[axis]) > .01:  # this is to avoid over-updating but will cause issues with
      # very fine movements on one axes but not the other on the same stick, if this node is running a low cpu system
      # then reimplement
      if axis == 0:
        t.angular.z = data.axes[axis]
      elif axis == 1:
        t.linear.x = -data.axes[axis]
      elif axis == 3:
        t.angular.x = data.axes[axis]
      elif axis == 4:
        t.linear.z = -data.axes[axis]
      self.last[axis] = data.axes[axis]
      significant_twist_delta = True

    if significant_twist_delta:
      self.thruster_cmd.publish(t)

    # grippers, most of this code is the smooth the closing and opening of the claw over time
    for trigger, button in [(2, 4), (5, 5)]:
      move_gripper = False
      if data.buttons[button]:  # gripper right open button 4, left 5
        # ensure its 0/positive
        self.last[trigger] = self.last[trigger] + gripper_scaler if self.last[trigger] + gripper_scaler <= 1 else 1
        move_gripper = True
      elif data.axes[trigger] != 1:
        pressed = 1 - data.axes[trigger]  # 0 not pressed, 2 fully pressed
        self.last[trigger] = self.last[trigger] - gripper_scaler * pressed if self.last[trigger] - gripper_scaler * \
                                                                              pressed > 0 else 0  # ensure its 0->1
        move_gripper = True
      if move_gripper and trigger == 2:
        self.gripper2_cmd.publish(self.last[trigger])
      elif move_gripper:
        self.gripper1_cmd.publish(self.last[trigger])

    # Center button is buttons[8]
    if data.buttons[8]:
      self.overridden = not self.overridden  # toggle state True/False False/True
      self.override_pub.publish(Bool(self.overridden))

    # Y button is buttons[3] yellow for light
    if data.buttons[3]:
      self.light_on = not self.light_on
      self.light.publish(Bool(self.light_on))

  def run(self):
    rospy.Subscriber("joy", Joy, self.callback)
    rospy.Subscriber("override", Bool, self.override)
    rospy.spin()


if __name__ == '__main__':
  c = Controller()
  c.run()
