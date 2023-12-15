# Brian Lesko 12/13/2023
# MicroPython listener, listens to its USB serial port and sends the resoponse back to the sender
# Put this file on the micropython board and make sure its running. Then run a python script on your computer to send a message to the pyboard.

import pyb 

redLED = pyb.LED(1)
greenLED = pyb.LED(2)

my_serial = pyb.USB_VCP()

while True:
    if my_serial.isconnected():
        greenLED.on()
        if my_serial.any():
            redLED.on()
            my_data = my_serial.read()
            response = f'Arduino received: {my_data.decode("utf-8")}'
            my_serial.send(response)
            pyb.delay(400)
            redLED.off()
