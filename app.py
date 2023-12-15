# Brian Lesko 12/14/23
import customize_gui # streamlit GUI modifications
import streamlit as st
import arduino as ard
gui = customize_gui.gui()

def main():
    gui.clean_format()
    gui.about(text = "This app sends your text input to an arduino over a usb cord - using serial communication ")
    st.title("Arduino Serial Communication")

    with st.chat_message("assistant"):
        try: 
            st.write("Connecting to: /dev/tty.usbmodem3685375E31302...")
            port = '/dev/tty.usbmodem3685375E31302' # on mac in terminal: 'ls /dev/tty.*' to find the port
            my_arduino = ard.arduino(port,9600,.1)
            st.write("Connection successful")

        except Exception as e:
            st.write("Could not connect to arduino")

    user_input = st.chat_input("What do you want to send to the arduino?")
    if user_input:
        st.chat_message("user").write(user_input)
        my_arduino.send(user_input)
        response = my_arduino.read()
        with st.chat_message("assistant"):
            st.write(response)
            
main()