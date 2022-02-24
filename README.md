# My Rover

**My Rover** allows users to control a robot powered by Raspberry Pi 3b+ using an Android App via Wifi.

## What you will need

**Hardware :**
  - Raspberry Pi 3b+
  - L298N Drive Controller Board Dual H-Bridge DC Module
  - HC-SR04 ultrasonic sensor
  - 1kΩ Resistor + 2kΩ Resistor
  - A camera (I used the 170° night vision module)
  - 2 Axis Pan Tilt brackets + 2*MG90S motors
  - A Robot chassis + 2*Motors
  - PowerBank (To power the Raspberry Pi)
  - Batteries + batteries holder (To Power the motors)
  
**Software :**
   - Android Studio
   - Motion (on your Raspberry Pi)
```sh
$ sudo apt-get update
$ sudo apt-get install motion
```
  - pigpio (on your Raspberry Pi)
```sh
$ sudo apt-get update
$ sudo apt-get install pigpio python-pigpio python3-pigpio
```

## Setup

**Hardware :**
  - Assemble your robot chassis and motors by following the instructions that came with your chassis.
  - Wire up the motors to the L298N Drive and to the Raspberry Pi, following the first part of this tutorial 
  - Wire up the HC-SR04 sensor to the Rasberry Pi (don't forget to add the resistors to your circuit) following the first part of this tutorial
  - Assemble your pan tilt brackets following the instructiins
  - Wire the motors to the Raspberry Pi
  - Plug your camera to the Raspberry Pi's camera port
  
**Software :**
  - Open the project in `My-Rover/My Rover - Android App/` inside Android Studio and run the App
  - Copy the files inside  `My-Rover/My Rover - Control/` over to your Raspberry Pi
  - Run the script `StartRover.sh` (it will start a python server)
```sh
$ sudo ./StartRover.sh
```
  - Enter the Raspberry Pi's IP Adress inside the Android App
  
  ***ET VOILÀ***
