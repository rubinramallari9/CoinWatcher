# CoinWatcher

:

🪙 Coin Watcher
Coin Watcher is a simple project that fetches the current price of Bitcoin (BTC) using Python and displays it on an LCD connected to an Arduino. This project is perfect for those interested in combining Python programming with Arduino to create a real-time Bitcoin price tracker.

✨ Features
Fetches real-time Bitcoin price using Python.
Displays the price on an LCD connected to an Arduino.
Easy to set up and customize.
🛠️ Hardware Requirements
Arduino board (e.g., Uno, Nano)
LCD display (e.g., 16x2)
Potentiometer (for contrast control)
Jumper wires
Breadboard (optional)
🔌 Wiring Diagram
Connect the LCD to the Arduino as follows:

LCD Pin 1 (VSS) to Arduino GND
LCD Pin 2 (VDD) to Arduino 5V
LCD Pin 3 (V0) to the middle pin of a 10k potentiometer (other two pins to 5V and GND)
LCD Pin 4 (RS) to Arduino digital pin 12
LCD Pin 5 (RW) to Arduino GND
LCD Pin 6 (E) to Arduino digital pin 11
LCD Pins 11-14 (D4-D7) to Arduino digital pins 5, 4, 3, 2 respectively
LCD Pin 15 (A) to Arduino 5V (through a 220-ohm resistor)
LCD Pin 16 (K) to Arduino GND

![image](https://github.com/user-attachments/assets/503d2f0f-26ef-41df-9293-94c25f5d156f)
