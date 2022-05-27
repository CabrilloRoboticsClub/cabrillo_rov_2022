#!/bin/bash
#make a on boot cronjob with `chrontab -e`
# then paste at the bottom `@reboot /home/ubuntu/cabrillo_rov/misc/shore.sh`
source /opt/ros/noetic/setup.bash
cd ~/cabrillo_rov/
git pull    # Comment out for quicker rov startup
catkin_make # Comment out for quicker rov startup
source ./devel/setup.bash
export ROS_MASTER_URI=http://$(getent hosts hydrozoa | cut -d " " -f1):11311
#export ROS_MASTER_URI='http://earle-s1.local:11311'
export ROS_HOSTNAME=$HOSTNAME.local
sleep 1
roslaunch ./launch/shore.launch
