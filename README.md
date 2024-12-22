[Work in Progress]
# HMI: PyQT + Arduino
This project connects an Arduino device with a simple HC-05 Bluetooth module connected. This creates a socket which is used by a Python program which sends a BT command each time an element of the interface is modified. This UI uses PyQT to create a Human-Machine-Interface (HMI) to control this Arduino device
## Requirements
- Arduino Uno
- Any computer that runs Python3x
## Installation
- pip3 install pyqt5
## Files
- _main.py_: Python code containing all functions to be exectued when the HMI widgets, which send a Bluetooth command to the Arduino device through its socket
- _tutorialHMI.py_: Automatically created Python code interface using PyQT
- _tutorial_pyqt_hc05.ino_: Arduino code to connect HC-05 Bluetooth module through SoftwareSerial and command processing to set ON/OFF the internal LED
- _tutorialHMI.ui_: XML code that contains HMI interface for PyQT

