#!/bin/bash

sudo apt update

sudo apt upgrade -y

sudo apt autoremove -y

sudo apt install python3-pip sshpass

pip3 install ansible

ansible-playbook -i ansible_inventory.yml ansible_playbook.yml