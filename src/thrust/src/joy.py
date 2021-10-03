#!/usr/bin/env python

import rospkg
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import pigpio

def callback(data):
    global trust
    global thruster_pins
    global last
    #max_forward = 1900
    #max_backward = 1100
    if abs(last[0] - data.axes[0]) > .01:
        trust(thruster_pins[0], 1500 + (data.axes[0]*130))
        last[0] = data.axes[0]
    
    if abs(last[1] - data.axes[1]) > .01:
        trust(thruster_pins[1], 1500 + (data.axes[1]*130))
        last[1] = data.axes[1]
     
    if abs(last[2] - data.axes[4]) > .01:
        trust(thruster_pins[2], 1500 + (data.axes[4]*130))
        last[2] = data.axes[4]
    
    if abs(last[3] - data.axes[3]) > .01:
        trust(thruster_pins[3], 1500 + (data.axes[3]*130))
        last[3] = data.axes[3]

# Intializes everything
def start():
    global trust
    global thruster_pins
    global last
    thruster_pins = [24, 20, 27, 19]
    last = [1500, 1500, 1500, 1500]
    pi = pigpio.pi()
    pi.set_servo_pulsewidth(thruster_pins[0], 1500)
    pi.set_servo_pulsewidth(thruster_pins[1], 1500)
    pi.set_servo_pulsewidth(thruster_pins[2], 1500)
    pi.set_servo_pulsewidth(thruster_pins[3], 1500)
    trust = pi.set_servo_pulsewidth
    rospy.Subscriber("joy", Joy, callback)
    rospy.init_node('controller')
    rospy.spin()

if __name__ == '__main__':
    start()
