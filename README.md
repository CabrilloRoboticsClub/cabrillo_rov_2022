## Cabrillo College's Robotics Club's ROV Repo for the MATE ROV competition

### Dubbed earle-s1 after Dr. Sylvia Earle

![frame__48cm Drawing](https://user-images.githubusercontent.com/27081199/120859450-14573780-c539-11eb-9be2-f1c2092adf8b.jpg)

## ROV
Start with this image onto the SD card
[https://cdimage.ubuntu.com/releases/20.04.3/release/ubuntu-20.04.3-preinstalled-server-arm64+raspi.img.xz](https://cdimage.ubuntu.com/releases/20.04.3/release/ubuntu-20.04.3-preinstalled-server-arm64+raspi.img.xz)

```
sudo apt update
sudo apt upgrade
sudo apt install net-tools
sudo hostnamectl set-hostname earle-s1
sudo echo "earle-s1" > /etc/hostname 

sudo apt install ipython3 curl 
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update
sudo apt install ros-noetic-desktop-full
sudo apt install ros-noetic-robot-pose-ekf ros-noetic-robot-localization ros-noetic-imu-filter-madgwick python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential ros-noetic-joy ros-noetic-joystick-drivers

crontab -l | { cat; echo "@reboot /home/ubuntu/cabrillo_rov/misc/controller.sh >/tmp/scriptLog"; } | crontab -

sudo apt install python3-pip
pip3 install pigpio

sudo rosdep init
rosdep update

ssh-keygen
cat /home/ubuntu/.ssh/id_rsa.pub # please put into the repo
git clone git@github.com:Carter90/cabrillo_rov.git

cd cabrillo_rov/
git pull
```
