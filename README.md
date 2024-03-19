# This repository was created for my needs, but I give access to anyone who wants to use it and adding something to it. Here you will not find 100% system setup, but only what I need when reinstalling the Ubuntu OS.

# Contents:
- [Update packages](#update-packages)
- [Add keyboard layout](#add-keyboard-layout)
- [Monitors Config](#monitors-config)
- [Bind to change the keyboard layout to alt+shift](#bind-to-change-the-keyboard-layout-to-altshift)
- [Installing and configuring git](#installing-and-configuring-git)
- [For Python](#for-python)
- [For PHP](#for-php)
- [Creating ssh key](#creating-ssh-key)
- [Google Chrome](#google-chrome)
- [PyCharm](#pycharm)
- [Visual Studio Code](#visual-studio-code)
- [Vim](#vim)
- [Installing Docker](#installing-docker)
- [Installing Docker Compose](#installing-docker-compose)
- [Installing PostgreSQL](#installing-postgresql)
- [Installing GCC](#installing-gcc)
- [Installing OBS](#installing-obs-open-broadcaster-software)
- [Installing Nvidia Drivers](#installing-nvidia-drivers)
- [Installing Spotify](#installing-spotify)
- [Installing Discord](#installing-discord)
- [Installing Node.Js](#installing-nodejs)
- [Installing Postman](#installing-postman)
- [Installing Composer](#installing-composer)
- [Installing TypeScript](#installing-typescript)
- [Installing Redis](#installing-redis)
- [Installing Telegram Desktop](#installing-telegram-desktop)
- [Installing PHP Code Sniffer](#installing-php-code-sniffer)
- [Installing L2TP](#installing-l2tp)

---

## Update packages:

```bash
sudo apt update
sudo apt upgrade
```

---

## Add keyboard layout: 


Open Settings.

Click Keyboard in the sidebar to open the panel.

Click the + button in the Input Sources section, select the language which is associated with the layout, then select a layout and press Add.

---

## Monitors Config: 

### xrandr (example)
```bash
$ xrandr
```

```bash
DVI-D-1 connected primary 1920x1080+1920+0 (normal left inverted right x axis y axis) 527mm x 296mm

HDMI-1 connected 1920x1080+0+0 (normal left inverted right x axis y axis) 527mm x 296mm
```

```bash
xrandr --output DVI-D-1 --right-of HDMI-1
```

---

## Bind to change the keyboard layout to alt+shift:
```bash
gsettings set org.gnome.desktop.input-sources xkb-options "['grp:alt_shift_toggle']"
```

---

## Installing and configuring git:
```bash
sudo apt install git
git config --global user.name "Your_Name"
git config --global user.email "your_email@example.com"
```

---

## For Python:
```bash
sudo apt install pip
sudo apt install python3.10-venv
```

---

## For PHP:

### PHP
```bash
sudo apt install software-properties-common ca-certificates lsb-release apt-transport-https 
LC_ALL=C.UTF-8 sudo add-apt-repository ppa:ondrej/php 
sudo apt update 
sudo apt install php8.2  
```
### base extensions
```bash
sudo apt-get update
sudo apt install php-intl php-cli php-common php-mysql php-json php-zip php-gd php-mbstring php-curl php-xml php-pear php-bcmath

```

### PHP-Redis
```bash
sudo apt-get update
sudo apt-get install php-redis
```

---

## Creating ssh key:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
cat ~/.ssh/id_rsa.pub
```
---

## Google Chrome:
```bash
wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt update
sudo apt --only-upgrade install google-chrome-stable
```

---

## PyCharm:
```bash
sudo apt update
sudo apt install snapd
sudo snap install pycharm-community --classic
```

---

## Visual Studio Code:
```bash
sudo apt update
sudo apt install snapd
sudo snap install code --classic
```

---

## Vim:
```bash
sudo apt update
sudo apt install vim
```

---

## Installing Docker:

#### Updating APT packages:
```bash
sudo apt update
```

#### Installing packages to allow APT to work with HTTPS:
```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

#### Adding the official Docker GPG key to your system:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

#### Adding the Docker repository:
```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

#### Update the APT packages again:
```bash
sudo apt update
```

#### Installing Docker:
```bash
sudo apt install docker-ce
```

#### Check that Docker is installed correctly:
```bash
sudo systemctl status docker
```

---

## Installing Docker Compose:

#### Updating APT packages:
```bash
sudo apt update
```

#### Downloading the latest version of Docker Compose:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

#### Giving the file executable rights:
```bash
sudo chmod +x /usr/local/bin/docker-compose
```

#### Check your Docker Compose installation:
```bash
docker-compose --version
```

---

## Installing PostgreSQL:

#### Updating APT packages:
```bash
sudo apt update
```

#### Installing PostgreSQL and additional components:
```bash
sudo apt install postgresql postgresql-contrib
```

#### Switch to the postgres user:
```bash
sudo -i -u postgres
```
#### Login to the PostgreSQL command line:
```bash
psql
```

#### For exit:
```bash
\q
```

#### Additional steps:

If you need to set a password for the postgres user:
```bash
sudo -i -u postgres
psql
```

Set a password:
```bash
\password postgres
```

---

## Installing GCC:
```bash
sudo apt update
sudo apt install build-essential
```

---

## Installing OBS (Open Broadcaster Software):
```bash
sudo add-apt-repository ppa:obsproject/obs-studio
sudo apt update
sudo apt install obs-studio
```

---

## Installing NVIDIA drivers:

#### Ubuntu
```bash
sudo ubuntu-drivers autoinstall
```

#### Debian 
```bash
sudo apt install nvidia-driver
```

---


##  Installing Spotify:
  ```bash 
sudo snap install spotify  
```   
  
---

## Installing Discord:  

```bash 
sudo snap install discord
```

---

## Installing Node.Js:
```bash 
sudo apt install nodejs 
sudo apt install npm
cd ~
curl -sL https://deb.nodesource.com/setup_18.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs
```   

if error:
```bash
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nodejs_18.19.0-1nodesource1_amd64.deb
sudo apt install nodejs
node -v
```

---

## Installing Postman:
```bash
  sudo snap install postman
```

---

## Installing Composer:
```bash
  sudo apt-get update
  sudo apt-get install curl
  sudo apt-get install php php-curl
  curl -sS https://getcomposer.org/installer -o composer-setup.php
  sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
  sudo composer self-update
```

---

## Installing TypeScript:
```bash
  sudo apt install node-typescript
```

---

## Installing Redis:
```bash
  sudo apt-get install redis-server
```

---

## Installing Telegram Desktop:
```bash
  sudo snap install telegram-desktop
```

---

## Installing PHP Code Sniffer:
```bash
  sudo apt-get update
  sudo apt-get install php-xml
  sudo apt install php-codesniffer
```

---

## Installing L2TP:
```bash
  sudo apt update
  sudo apt install network-manager-l2tp network-manager-l2tp-gnome strongswan libstrongswan-extra-plugins
```

---