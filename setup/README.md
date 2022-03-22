# setup

first time setup instructions for Cabrillo ROV


## SHORE Computer

REQUIREMENTS:
* Ubuntu 20.04 LTS 64 Bit
* 32BG HDD


## ROV Onbard Computer

REQUIREMENTS:
* Raspberry Pi (3B+ or 4)
* 32GB or larger MicroSD Card


Steps to setup raspberry pi rov onboard computer from scratch
1) install raspberry pi imager
2) connect micro sd card
3) in raspberry pi imager: <br>
    * CHOOSE OS > <br>
    Other general-purpose OS > <br>
    Ubuntu > <br>
    Ubuntu Server 20.04 LTS 64 Bit
    * CHOOSE STORAGE<br>
    use the sd card you just inserted
    * WRITE
    * DO NOT REMOVE SD CARD
4) copy the `user-data` file to the boot partition on the sd card
5) remove the card from the shore computer and insert it into the robot pi
6) connect the robot to power
