# Brian Lesko 12/13/2023
# MicroPython listener, listens to its USB serial port and sends the resoponse back to the sender
# Put this file on the micropython board and make sure its running. Then run a python script on your computer to send a message to the pyboard.

import pyb 

greenLED = pyb.LED(2)
greenLED.on()

my_serial = pyb.USB_VCP()

while True:
    if my_serial.isconnected():
        if my_serial.any():
            my_data = my_serial.read()
            response = f'Arduino received: {my_data.decode("utf-8")}'
            my_serial.send(response)