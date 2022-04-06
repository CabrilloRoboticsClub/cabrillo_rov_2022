# setup

first time setup instructions for Cabrillo ROV


## SHORE Computer

REQUIREMENTS:
* Ubuntu 20.04 LTS 64 Bit
* 32BG HDD or SSD


## ROV Onbard Computer

REQUIREMENTS:
* Raspberry Pi (3B+ or 4)
* 16GB or larger MicroSD Card


Steps to setup raspberry pi rov onboard computer from scratch
1) install raspberry pi imager
2) connect MicroSD card
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
7) wait untill `ping hydrozoa` returns a reply
8) from inside the cabrillo_rov repo folder on the shore pc run the ansible playbook ``` ansible-playbook -i setup/ansible_inventory.yml setup/ansible_playbook_rov.yml```

