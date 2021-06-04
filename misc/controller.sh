#!/bin/bash
#in a on boot cronjob /home/ubuntu/bin/controller
#sudo pigpiod # put this line in a cronjob under root on boot
sleep 1
roscore &
sleep 5
rosrun joy joy_node &
sleep 5
/home/ubuntu/mate/src/thrust/src/joy.py
