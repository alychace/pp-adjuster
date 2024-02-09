#!/bin/bash
set -e

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

DIR="/usr/local/bin"

if [ ! -d "$DIR" ]; then
  echo "$DIRECTORY does not exist..."
  echo "Creating $DIR"
  mkdir -p $DIR
fi

# Copy files
cp $PWD/pp-adjuster.py /usr/local/bin/pp-adjuster

# Set permissions
chown root:root /usr/local/bin/pp-adjuster
chmod 655 /usr/local/bin/pp-adjuster
chmod +x /usr/local/bin/pp-adjuster