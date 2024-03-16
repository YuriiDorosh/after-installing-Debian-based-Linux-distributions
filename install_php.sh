#!/bin/bash

sudo apt install software-properties-common ca-certificates lsb-release apt-transport-https 
LC_ALL=C.UTF-8 sudo add-apt-repository ppa:ondrej/php 
sudo apt update 
sudo apt install php8.2 

sudo apt-get update
sudo apt install php-intl php-cli php-common php-mysql php-json php-zip php-gd php-mbstring php-curl php-xml php-pear php-bcmath

sudo apt-get update
sudo apt-get install php-redis

sudo apt-get update
sudo apt install php-codesniffer