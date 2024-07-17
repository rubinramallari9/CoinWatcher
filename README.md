# 🪙 Coin Watcher

Coin Watcher is a simple project that fetches the current price of Bitcoin (BTC) using Python and displays it on an LCD connected to an Arduino. This project is perfect for those interested in combining Python programming with Arduino to create a real-time Bitcoin price tracker.

# ✨ Features

1. Fetches real-time Bitcoin price using Python.
2. Displays the price on an LCD connected to an Arduino.
3. Easy to set up and customize.


# 🛠️ Hardware Requirements

1. Arduino board (e.g., Uno, Nano)
2. LCD display (e.g., 16x2)
3. Potentiometer (for contrast control)
4. Jumper wires
5. Breadboard (optional)


# 🔌 Wiring Diagram

Connect the LCD to the Arduino as follows:

1. LCD Pin 1 (VSS) to Arduino GND
2. LCD Pin 2 (VDD) to Arduino 5V
3. LCD Pin 3 (V0) to the middle pin of a 10k potentiometer (other two pins to 5V and GND)
4. LCD Pin 4 (RS) to Arduino digital pin 12
5. LCD Pin 5 (RW) to Arduino GND
6. LCD Pin 6 (E) to Arduino digital pin 11
7. LCD Pins 11-14 (D4-D7) to Arduino digital pins 5, 4, 3, 2 respectively
8. LCD Pin 15 (A) to Arduino 5V (through a 220-ohm resistor)
9. LCD Pin 16 (K) to Arduino GND

![image](https://github.com/user-attachments/assets/503d2f0f-26ef-41df-9293-94c25f5d156f)


# 🖥️ Arduino Code

Upload the following code to your Arduino using the Arduino IDE:


#include <LiquidCrystal.h>

// Initialize the library by associating any needed LCD interface pin
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  lcd.begin(16, 2);  // Set up the LCD's number of columns and rows
  Serial.begin(9600); // Start the serial communication
}

void loop() {
  if (Serial.available()) {
    String message = Serial.readStringUntil('\n'); // Read incoming string
    lcd.clear();  // Clear the display
    lcd.print(message); // Print the message to the LCD
    Serial.println(message); // Print the message to the Serial Monitor for debugging
  }
}
