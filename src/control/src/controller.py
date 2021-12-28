#!/usr/bin/env python3

import rospkg
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32


class Controller:
  def __init__(self):
    rospy.init_node('controller')
    self.last = [0] * 6
    self.thruster_cmd = rospy.Publisher('cmd_vel', Twist, queue_size=4)
    self.gripper1_cmd = rospy.Publisher('cmd_gripper1', Float32, queue_size=4)
    self.gripper2_cmd = rospy.Publisher('cmd_gripper2', Float32, queue_size=4)
    self.last[2] = 0  # start grippers at open
    self.last[5] = 0  # start grippers at open

  def callback(self, data):
    t = Twist()
    significant_twist_delta = False
    gripper_scaler = .05
    """ @NOTE
        axis_angular.x: 0  # left up/down
        axis_linear.x: 1   # left left/right
        axis_angular.z: 3  # right left/right
        axis_linear.z: 4   # right up/down
        
        @note value 1 means not pressed, -1 fully pressed
        gripper left close axis 5  # left trigger "LT" on controller
        gripper left open button 5 # left button "LB" on controller
        
        @note value 1 means not pressed, -1 fully pressed
        gripper right close axis 2 
        gripper right open button 4
        """
    for axis in [0, 1, 3, 4]:
      # if abs(self.last[axis] - data.axes[axis]) > .01:  # this is to avoid over-updating but will cause issues with
      # very fine movements on one axes but not the other on the same stick, if this node is running a low cpu system
      # then reimplement
      if axis == 0:
        t.angular.x = data.axes[axis]
      elif axis == 1:
        t.linear.x = data.axes[axis]
      elif axis == 3:
        t.angular.z = data.axes[axis]
      elif axis == 4:
        t.linear.z = data.axes[axis]
      self.last[axis] = data.axes[axis]
      significant_twist_delta = True

    if significant_twist_delta:
      self.thruster_cmd.publish(t)

    # grippers, most of this code is the smooth the closing and opening of the claw over time
    for trigger, button in [(2, 4), (5, 5)]:
      move_gripper = False
      if data.buttons[button]:  # gripper right open button 4, left 5
        # ensure its 0/positive
        self.last[trigger] = self.last[trigger] - gripper_scaler if self.last[trigger] - gripper_scaler > 0 else 0
        move_gripper = True
      elif data.axes[trigger] != 1:
        pressed = 1 - data.axes[trigger]  # 0 not pressed, 2 fully pressed
        self.last[trigger] = self.last[trigger] + gripper_scaler * pressed if self.last[trigger] + gripper_scaler * \
                                                                              pressed <= 1 else 1  # ensure its 0->1
        move_gripper = True
      if move_gripper and trigger == 2:
        self.gripper2_cmd.publish(self.last[trigger])
      elif move_gripper:
        self.gripper1_cmd.publish(self.last[trigger])

  def run(self):
    rospy.Subscriber("joy", Joy, self.callback)
    rospy.spin()


if __name__ == '__main__':
  c = Controller()
  c.run()
