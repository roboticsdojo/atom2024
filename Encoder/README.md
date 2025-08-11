# Testing your serial motor connection (Arduino - Raspberry Pi)

## 1. Install Required packages

Open a terminal and run:

```bash
sudo apt update
sudo apt install python3-pip
pip3 install pyserial

```
## 2. Find Your Arduino's Serial port
```bash
ls /dev/tty*
```
Look for:

* /dev/ttyACM0 (common for Arduino Uno/Mega)
* /dev/ttyUSB0 (common for CH340-based clones)

## 3. Set Proper Permissions
```bash
sudo chmod 666 /dev/ttyACM0  # Replace with your device
```

(Or add your user to the dialout group for permanent access:)
```bash
sudo usermod -a -G dialout $USER
```
Log out and back in for changes to apply.

## 4. Connect using miniterm
```bash
python3 -m serial.tools.miniterm /dev/ttyACM0 57600
```
(Replace /dev/ttyACM0 and 57600 with your actual port/baud rate.)

To move both wheels at full speed:
```bash
o 255 255
```
To move in the opposite direction:
```bash
0 -255 -255
```
To read encoder values:
```bash
e
```
#### More commands can be found in:
```bash
motor_control/src/commands.h
```

## 5. Exit Miniterm
Press Ctrl+] to quit.

# Troubleshooting
## If the port is not found:

1. Check connections:
```bash
dmesg | grep tty
```
(Look for "FTDI" or "CDC ACM" messages.)

2. Install drivers( for CH340 clones):
```bash
sudo apt install firmware-realtek
```
## If you get 'Permission denied':
```bash
sudo chmod a+rw /dev/ttyACM0
```
## If miniterm isn't found::
```bash
sudo apt install python3-serial
```
