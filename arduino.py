# Brian Lesko
# 11/22/23 
# Open serial communication with an arduino from a python script using the library pyserial using this class, or check out the example at the bottom of the file.

import serial # !pip install pyserial

class arduino:

    def __init__(self,port,baude_rate,timeout):
        self.port = port
        self.baude_rate = baude_rate
        self.timeout = timeout
        self.serial = serial.Serial(port=port, baudrate=baude_rate, timeout=timeout)

    def disconnect(self):
        self.serial.close()

    # Send a command and receive a response
    def send_and_receive(self,command):
        command = command + '\n' # setup for the readUntil function in the arduino code
        self.serial.write(command.encode('utf-8'))
        response = self.serial.readline().decode('utf-8').rstrip()
        return response
    
def example():
    # port = '/dev/ttyACM0' # on the raspberry pi, this is the port that the arduino is connected to
    # port = '/dev/tty.usbmodemF412FA9FD4E42' # on mac you must go to the terminal and type 'ls /dev/tty.*' to find the port
    port = 'COM4' # Windows port 
    my_arduino = arduino(port,9600,.1)

    command = "ON"
    response = my_arduino.send_and_receive(command)
    command = "OFF"
    response = my_arduino.send_and_receive(command)
    my_arduino.disconnect()

    # Hey It's Brian. remember you have to write a code on the ardino to listen for a serial communication