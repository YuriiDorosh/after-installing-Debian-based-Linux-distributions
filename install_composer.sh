#!/bin/bash

sudo apt-get update

sudo apt-get install curl

sudo apt-get install php php-curl

curl -sS https://getcomposer.org/installer -o composer-setup.php
sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer

sudo composer self-update