import requests
import serial
import time


arduino_port = 'COM3'
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)
try:
    while True:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin").json()
        price = response["data"]["priceUsd"].split(".")[0]
        print(price)
        time.sleep(2)

        def send_message_to_lcd(message):
            ser.write(message.encode() + b'\n')

        send_message_to_lcd("BTC: "+price+"$")
        time.sleep(5)

except serial.SerialException as e:
    print(f"Error opening serial port: {e}")

finally:
    ser.close()
