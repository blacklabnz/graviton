#!/bin/bash
#                         _ _              
#    __ _ _ __ __ ___   _(_) |_ ___  _ __  
#   / _` | '__/ _` \ \ / / | __/ _ \| '_ \ 
#  | (_| | | | (_| |\ V /| | || (_) | | | |
#   \__, |_|  \__,_| \_/ |_|\__\___/|_| |_|
#   |___/                                  
#
echo "Graviton Start"
cd /mnt/graviton
pip install -r requirements.txt 
#python graviton.py
gnuicorn graviton:app
