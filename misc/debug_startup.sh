#!/bin/bash
#
# run this on a second computer to watch stuff
#

source /opt/ros/noetic/setup.bash
cd ~/cabrillo_rov/
git pull
catkin_make
source ./devel/setup.bash
export ROS_MASTER_URI='http://hydrozoa.local:11311'
export ROS_HOSTNAME=$HOSTNAME.local
sleep 1

rqt --perspective-file misc/debug.perspective