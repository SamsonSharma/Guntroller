import serial
import time as t
import numpy as np
arduino = serial.Serial('/dev/ttyUSB1', 9600)
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
mouse = Controller()



# use this for Xserv: xhost local:root
# run script as superuser


while True:
    string = str(arduino.readline()[:-2])
    stringarr = string.split("'")
    for strings in stringarr:    
        if strings == 'leftclick':
            mouse.press(Button.left)
            mouse.release(Button.left)
            print("click")
            
        elif strings == 'ADS':
            mouse.press(Button.right)
            print("rightclickdown")
        elif strings == 'STOPADS':
            mouse.release(Button.right)
            print("rightclickup")




  
# Collect all event until released
# with Listener(on_press = show) as listener:
#     listener.join()

