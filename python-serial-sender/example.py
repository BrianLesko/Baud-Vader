# Brian Lesko 12/13/2023
# Python listener, listens to a serial port and prints the response

import arduino as ard

try: 
    port = '/dev/tty.usbmodem3685375E31302' # on mac in terminal: 'ls /dev/tty.*' to find the port
    my_arduino = ard.arduino(port,9600,.1)
except Exception as e:
    print("Could not connect to arduino")
    exit()
    
# send a command and receive a response
print("Laptop Sending... ")
command = "Hello from the laptop!"
my_arduino.send(command)
response = my_arduino.read()
print(response)
