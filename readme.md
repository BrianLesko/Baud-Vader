# Baud Vader
This code implements wired serial communication between two devices - Just make sure they have the same baud rate. 

To recreate what ive done here you'll need a laptop, an arduino, and a usb C cable.

&nbsp;

## Local Computer Dependencies

This code uses the following libraries:
- `pyserial`: For handling system resources, ports, etc
- `streamlit`: For creating the user interface

## Run this demo yourself

To run this demo yourself, you must have an arduino. 

You can choose to run one of the following codes on the arduino:
 - `MicroPython`: from micropython-serial-listener upload main.py to the board
 - `Arduino C++`: from arduino-serial-listener upload the sketch using the arduino IDE

Once the arduino is running one of the above programs, is plugged into your computer, and the port is correct, you can send messages to your arduino in multiple ways:
 - `streamlit app`: in the terminal: streamlit run app.py
 - `python-serial-sender`: your feedback will be in the terminal 
 - `Arduino IDE`
 - `Arduino Lab for Micropython`
 - `VS Code arduino extension`

&nbsp;

## How it Works

The app as follows:
1. The python script app.py is run by Streamlit in a loop, updating when you interact with the HTML page
2. The arduino waits for a message
2. Your message is sent to the arduino over USB C serial communication 
3. The arduino receives your message and responds

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


