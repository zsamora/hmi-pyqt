[Work in Progress]
# HMI: PyQT + Arduino
This project connects an Arduino device with a simple HC-05 Bluetooth module connected. This creates a socket which is used by a Python program which sends a BT command each time an element of the interface is modified. This UI uses PyQT to create a Human-Machine-Interface (HMI) to control this Arduino device
## Requirements
- Arduino Uno
- Any computer that runs Python3x
## Installation
- pip3 install
- 
## Files
- main.py: Python code containing all functions to be exectued when the HMI widgets, which send a Bluetooth command to the Arduino device through its socket
- tutorialHMI.py: Automatically created Python code interface using PyQT

