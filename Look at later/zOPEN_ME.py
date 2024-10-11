#!/usr/bin/env python3

__author__ = 'Connor S.'
import time
from timer import timer, get_timer
from pygame import mixer  # Load the popular external library

mixer.init()
# mixer.music.load(r"C:\Users\Control 3\Documents\EV3 Drive Bases\Music Package\beep1.wav")
# mixer.music.play()
# time.sleep(.1)
# mixer.music.stop()
def thumbs_up():
    return print("______________________________________________"),print("______________________________________________"),print("________________________________████__________"),print("________________________________████__________"),print("________________________________██__██________"),print("______________________________▓▓____██________"),print("______________________________▓▓____██________"),print("____________________________██____██__________"),print("____________________________██____██__________"),print("__________________________██______██__________"),print("__________________________██____██____________"),print("__██████████____________██______██____________"),print("██░░▒▒▒▒░░▒▒██____██████________██████████████"),print("██░░░░░░░░▒▒██__██__________________________██"),print("██▒▒▒▒▒▒░░▒▒██__██__________________________██"),print("██▓▓▓▓▓▓▓▓▓▓██__██________________██████████__"),print("██▓▓▓▓▒▒▓▓▓▓██__██________________________██__"),print("██▓▓▓▓▒▒▒▒▒▒██__▓▓________________░░░░____██__"),print("██▓▓▓▓▓▓▓▓▓▓██__██________________████████____"),print("██▓▓▓▓▓▓▓▓▓▓██__██______________________██____"),print("██▓▓▓▓▓▓▓▓▓▓██__██______________________██____"),print("██▓▓▓▓▓▓▓▓▓▓██__██________________██████______"),print("██▓▓▓▓▓▓__▓▓██__██____________________██______"),print("██▓▓▓▓▓▓▓▓▓▓██____████████████████████________"),print("__██████████__________________________________"),print("______________________________________________")
print("After exiting please selcet your wanted drive base")
print("These drive bases are:")
print(" ev3_ps4_v01.pv")
print("     Left joystick does forwards backwards and turning, right joystick up and down moves medium motor")
print(" ev3_ps4_v02.pv")
print("     Inverse of ev3-ps4_v01.pv  in case of reversed motors")
print(" TankDrive_Trigger_Bot_v01")
print("     Left joystick up and down moves left drive motor, right joystick up and down moves right drive motor, and triggers move medium motor")
print(" TankDrive_Trigger_Bot_v02")
print("     Inverse of TankDrive_Trigger_Bot_v01 in case of reversed motors")
print("If program is not working, try these in order:")
print(" 1. Making sure driving motors on on ports B and C and the medium motor is on port A")
print(" 2. Make sure your controler is paired, you can do this by checking if the controller light is solid blue")
print(" 3. Try getting new motor cables")
print(" 4. Ask a mentor first than a teacher for help")
print("To go back to robot file browser press the (esc) button on your EV3")
print(" ")
print(" ")
print(" ")
# thumbs_up()