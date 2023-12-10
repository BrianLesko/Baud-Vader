# Arduino + Python

This code implements serial communication with an arduino. It is based on pyserial. Ive been calling it a wrapper around the pyserial library and have created it to match another wrapper for the socket library - used for ethernet communication.

&nbsp;

<div align="center"><img src="docs/preview.gif" width="800"></div>

&nbsp;

## Dependencies

This code uses the following libraries:
- `pyserial`: For handling system resources, ports, etc

&nbsp;

## Usage

In your Python script: 
```
import arduino as ard 
port = 'your_port'
baude_rate = 9600
my_arduino = ard.arduino(port,baude_rate,.1)
response = my_arduino.send_and_receive('Message')
```

&nbsp;

## How it Works

The app as follows:
1. The class is initialized with the port your arduino is plugged into, the bauderate, and a timeout
2. send_and_receive encodes and send your message using utf-8 byte encoding 
3. the response is decoded automatically

&nbsp;

## Repository Structure
```
repository/
├── arduino.py # the class is in this python file
├── requirements.txt # the python packages needed to run locally
├── .gitignore # includes the local virtual environment named my_env
└── docs/
    └── preview.png # preview photo for Github
```

&nbsp;

## Topics 
```
Python | Arduino | Serial Communication
External device | decode bytes | communication | custom classes
Self taught coding | Mechanical engineer | Robotics engineer 
Brian Lesko | Brian Joseph Lesko
```
&nbsp;

<hr>

&nbsp;

<div align="center">



╭━━╮╭━━━┳━━┳━━━┳━╮╱╭╮        ╭╮╱╱╭━━━┳━━━┳╮╭━┳━━━╮
┃╭╮┃┃╭━╮┣┫┣┫╭━╮┃┃╰╮┃┃        ┃┃╱╱┃╭━━┫╭━╮┃┃┃╭┫╭━╮┃
┃╰╯╰┫╰━╯┃┃┃┃┃╱┃┃╭╮╰╯┃        ┃┃╱╱┃╰━━┫╰━━┫╰╯╯┃┃╱┃┃
┃╭━╮┃╭╮╭╯┃┃┃╰━╯┃┃╰╮┃┃        ┃┃╱╭┫╭━━┻━━╮┃╭╮┃┃┃╱┃┃
┃╰━╯┃┃┃╰┳┫┣┫╭━╮┃┃╱┃┃┃        ┃╰━╯┃╰━━┫╰━╯┃┃┃╰┫╰━╯┃
╰━━━┻╯╰━┻━━┻╯╱╰┻╯╱╰━╯        ╰━━━┻━━━┻━━━┻╯╰━┻━━━╯
  


&nbsp;


<a href="https://twitter.com/BrianJosephLeko"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-white/x-logo-white.svg" width="30" alt="X Logo"></a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="https://github.com/BrianLesko"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-white/github-mark-white.svg" width="30" alt="GitHub"></a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="https://www.linkedin.com/in/brianlesko/"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-white/linkedin-icon-white.svg" width="30" alt="LinkedIn"></a>

follow all of these or i will kick you

</div>


&nbsp;


