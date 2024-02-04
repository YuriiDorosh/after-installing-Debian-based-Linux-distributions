#!/bin/bash
sudo apt update
sudo apt install nodejs
sudo apt install npm
cd ~
curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nodejs_18.19.0-1nodesource1_amd64.deb
sudo apt install nodejs