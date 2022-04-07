#!/bin/bash
#
# execution of this is added to ubuntu user's crontab by running the ansible playbook "ansible_playbook_rov.yml"
#
sleep 1
source /opt/ros/noetic/setup.bash
roscore &
cd /home/ubuntu/cabrillo_rov/
git pull    # Comment out for quicker rov startup
catkin_make # Comment out for quicker rov startup
source ./devel/setup.bash
sleep 5
roslaunch ./launch/rov.launch &
