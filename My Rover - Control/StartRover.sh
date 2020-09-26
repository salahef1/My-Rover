#!/bin/bash
echo "Executing StartRover shell script"
sudo pigpiod
echo "Started pigpio"
sudo motion
echo "Started motion"
echo "Starting Server..."
python3 Pi_server.py
