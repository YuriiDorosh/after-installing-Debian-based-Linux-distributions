#!/bin/bash

# Check for arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: ./create_ssh_key.sh email@example.com"
    exit 1
fi

EMAIL=$1

ssh-keygen -t rsa -b 4096 -C "$EMAIL"
cat ~/.ssh/id_rsa.pub
