# Cabrillo College's Robotics Club's ROV Repo for the MATE ROV 2022 competition

## Dubbed hydrozoa

![frame__48cm Drawing](https://user-images.githubusercontent.com/27081199/120859450-14573780-c539-11eb-9be2-f1c2092adf8b.jpg)


#### SHORE Computer REQUIREMENTS:

* Ubuntu 20.04 LTS 64 Bit
* 32BG HDD or SSD

#### ROV Onbard Computer REQUIREMENTS:

* Raspberry Pi (3B+ or 4)
* 16GB or larger MicroSD Card


## setup instructions

1) open a terminal and navigate to your home directory
```bash 
cd ~ 
```

2) clone the code repo into your home folder 
```bash
git clone https://github.com/cabrillorobotics/cabrillo_rov.git 
```

3) install raspberry pi imager
```bash
sudo snap install rpi-imager 
```

4) connect MicroSD card

3) in raspberry pi imager: <br>
    * CHOOSE OS > <br>
    Other general-purpose OS > <br>
    Ubuntu > <br>
    Ubuntu Server 20.04 LTS 64 Bit
    * CHOOSE STORAGE<br>
    use the MicroSD card you just inserted
    * WRITE
    * Remove and re-insert MicroSD Card

4) copy the `user-data` file to the boot partition on the sd card (replace the file in the destination)

5) remove the card from the shore computer and insert it into the robot pi

6) connect the robot to power

while we wait for the pi to do its cloud init we can finish setting up the shore computer

7) install python and ansible
```bash
sudo apt install -y python3-pip sshpass 
sudo pip3 install ansible
```

8) run the ansible playbook to setup the shore and rov
```bash
ansible-playbook -i setup/ansible_inventory.yml setup/ansible_playbook.yml
```

## usage

the rov will automatically launch ros at boot

to start the shore interface run
```bash
~/cabrillo_rov/misc/shore_startup.sh
```
