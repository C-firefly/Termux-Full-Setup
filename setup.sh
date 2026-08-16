#!/data/data/com.termux/files/usr/bin/bash

clear

termux-setup-storage
clear

pkg update -y
pkg upgrade -y

pkg install python -y
clear

python termux_full_setup.py

exit