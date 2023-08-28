# This repository was created for my needs, but I give access to anyone who wants to use it and adding something to it. Here you will not find 100% system setup, but only what I need when reinstalling the Ubuntu OS.

# Contents:
- [Update packages](#update-packages)
- [Bind to change the keyboard layout to alt+shift](#bind-to-change-the-keyboard-layout-to-altshift)
- [Installing and configuring git](#installing-and-configuring-git)
- [For Python](#for-python)
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

---

## Update packages:

```bash
sudo apt update
sudo apt upgrade
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


 ## Installing Spotify:
   ```bash 
   sudo apt install spotify-client 
   ```   
   
   ---

   ## Installing Discord:  
   
   ####  
   ```bash 
   sudo apt install ./discord.deb
   ```