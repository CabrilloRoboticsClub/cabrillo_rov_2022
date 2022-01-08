#!/bin/bash
#make a on boot cronjob with `chrontab -e`
# then paste at the bottom `@reboot /home/ubuntu/cabrillo_rov/misc/rov_startup.sh`
#sudo pigpiod # put this line in a cronjob under root on boot or create a service
sleep 1
source /opt/ros/noetic/setup.bash
roscore &
cd cabrillo_rov/
git pull    # Comment out for quicker rov startup
catkin_make # Comment out for quicker rov startup
source ./devel/setup.bash
sleep 5
roslaunch ./launch/rov.launch &
