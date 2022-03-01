## Cabrillo College's Robotics Club's ROV Repo for the MATE ROV competition

### Dubbed earle-s1 after Dr. Sylvia Earle

![frame__48cm Drawing](https://user-images.githubusercontent.com/27081199/120859450-14573780-c539-11eb-9be2-f1c2092adf8b.jpg)

## ROV
Start with this image onto the SD card
[https://cdimage.ubuntu.com/releases/20.04.3/release/ubuntu-20.04.4-preinstalled-server-armhf+raspi.img.xz](https://cdimage.ubuntu.com/releases/20.04.3/release/ubuntu-20.04.4-preinstalled-server-armhf+raspi.img.xz)
or
[https://cdimage.ubuntu.com/releases/20.04.3/release/ubuntu-20.04.4-preinstalled-server-arm64+raspi.img.xz](
https://cdimage.ubuntu.com/releases/20.04.3/release/ubuntu-20.04.4-preinstalled-server-arm64+raspi.img.xz)


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

crontab -l | { cat; echo "@reboot /home/ubuntu/cabrillo_rov/misc/rov_startup.sh >/tmp/scriptLog"; } | crontab -

sudo apt install python3-pip
pip3 install pigpio

sudo rosdep init
rosdep update

ssh-keygen
cat /home/ubuntu/.ssh/id_rsa.pub # please put into the repo
git clone git@github.com:cabrillorobotics/cabrillo_rov.git

cd cabrillo_rov/
git pull
```
##Other Notes
`sudo apt-get install raspi-config rpi-update`

(https://cdimage.ubuntu.com/releases/20.04.3/release/ubuntu-20.04.3-preinstalled-server-arm64+raspi.img.xz)[https://cdimage.ubuntu.com/releases/20.04.3/release/ubuntu-20.04.3-preinstalled-server-arm64+raspi.img.xz]

`sudo nano /etc/udev/rules.d/99-com.rules `
Then paste
`SUBSYSTEM=="ic2-dev", GROUP="i2c", MODE="0660"`

```
sudo chown :i2c /dev/i2c-1
sudo chmod g+rw /dev/i2c-1
```

`@reboot pigpiod;chown :i2c /dev/i2c-1;chmod g+rw /dev/i2c-1`

```
sudo apt install ros-noetic-robot-localization ros-noetic-usb-cam
pip3 install adafruit-circuitpython-lsm6ds
```

`sudo nano /lib/systemd/system/pigpiod.service`
Then paste
```
[Unit]
Description=Daemon required to control GPIO pins via pigpio
[Service]
ExecStart=/usr/local/bin/pigpiod
ExecStop=/bin/systemctl kill -s SIGKILL pigpiod
Type=forking
[Install]
WantedBy=multi-user.target
```

## Shore
```
#ros desktop install and stuff like the rqt and joy
```

`export ROS_MASTER_URI=http://$(getent hosts earle-s1.local | cut -d " " -f1):11311`

### Uncomplicated Firewall may cause issues
Something to note the Ubuntu Uncomplicated Firewall might cause issues its been fine until tonight if you do a `ros topic echo /cmd_vel` on both the laptop(shore) and the rov(sshed in) and don't see it on the rover its probably a firewall issue.
11311
`sudo ufw disable`

`sudo ufw enable`

