#!/usr/bin/env python3

__author__ = "Connor S"
## also thanks for help to https://gist.github.com/Quantum357 aswell as Sebastiaans adaptations after a Artur Poznanski program.##

## Import libraries ##
import evdev
import ev3dev.auto as ev3
import threading
import time

## PS4 Button Maps (For event.code)

# Button X or Cross = 304
# Button Circle = 305
# Button Triangle = 307
# Button Square = 308

# Button Left Shoulder or L1 = 310
# Button Right Shoulder or R1 = 311
# Button Left2 = 312
# Button Right2 = 313
# Button LeftT = 317
# Button RightT = 318

# Button Share = 314
# Button Options = 315
# Button PS = 316

# Axis left Joystick X = 0
# Axis Left Joystick Y = 1
# Axis Right Joystick X = 3
# Axis Right Joystick Y = 4

# Axis Left Trigger or L2 = 2
# Axis Right Trigger or R2 = 5

# Axis D-pad X = 16
# Axis D-pad Y = 17

## Event.type ##

# Button Press = 1
# Joystick Move = 3


## Some helpers ##
def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)


def scale(val, src, dst):
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]


def scale_stick(value):
    return scale(value, (0, 255), (-500, 500))


def dc_clamp(value):
    return clamp(value, -500, 500)


## Initializing ##
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
ps4dev = devices[0].fn
gamepad = evdev.InputDevice(ps4dev)

invert = 2
forward_speed = 0
forward_speed1 = 0
grab_speed1 = 0
grab_speed = 0
start = """



***********************************************
*                                             *
*           %%%%%%%%%%       %%%%%%%%%%%%%    *
*         %%%%     %%%%     %%%%     %%%%     *
*        %%%%              %%%%     %%%%      *
*       %%%%              %%%%     %%%%       *
*      %%%%    %%%%%%    %%%%     %%%%        *
*     %%%%     %%%%     %%%%     %%%%         *
*     %%%%%%%%%%%      %%%%%%%%%%%%%          *
*                                             *                  
*********************************************** 
    #Press right or left d-pad buttons to change drive base to-
    clockwise and counter-clockwise                           
"""

running = True
## The Motors ##
class MotorThread(threading.Thread):
    def __init__(self):
        print("Initializing Motors...")
        time.sleep(.5)
        print("Motors connected!")
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.claw_motor = ev3.MediumMotor(ev3.OUTPUT_A | ev3.OUTPUT_D)
        print("Motors connected!")
        time.sleep(.1)
        threading.Thread.__init__(self)

    def run(self):
        print("Progam started!")
        time.sleep(.5)
        print(start)
        while running:
            self.right_motor.run_forever(speed_sp=dc_clamp(forward_speed))
            self.left_motor.run_forever(speed_sp=dc_clamp(forward_speed1))
            self.claw_motor.run_forever(speed_sp=dc_clamp(grab_speed + grab_speed1))
        self.right_motor.stop()
        self.left_motor.stop()
        self.claw_motor.stop()


motor_thread = MotorThread()
motor_thread.setDaemon(True)
motor_thread.start()

## The PS4 Controller Mapping ##

for event in gamepad.read_loop():  # this loops infinitely
    # Mapping X/Cross button to inversee controls on click (.75 seconds delay)
    if event.type == 1:
        if event.code == 304:
            if invert == 2:
                invert -= 1
                time.sleep(0.75)
            if invert == 1:
                invert += 1
                time.sleep(0.75)
            else:
                invert = 2
    # Mapping joysticks to drive base in tank drive
    if invert % 2 == 0:
        if event.type == 3:  # left stick is moved
            if event.code == 4:  # Y axis on right stick
                forward_speed = -scale_stick(event.value)
            if forward_speed < 100 and forward_speed > -100:
                forward_speed = 0
            if event.code == 1:  # Y axis on left stick
                forward_speed1 = -scale_stick(event.value)
            if forward_speed1 < 100 and forward_speed1 > -100:
                forward_speed1 = 0
    # Mapping both triggers the Medium motor
            if event.code == 2:
                grab_speed = scale_stick(event.value)
            if grab_speed < 100 and -grab_speed > -100:
                grab_speed = 0
            if event.code == 5:
                grab_speed1 = -scale_stick(event.value)
            if grab_speed < 100 and grab_speed1 > -100:
                grab_speed1 = 0
    # Inverted controls for drive base only
    else:
        if event.type == 3:  # left stick is moved
            if event.code == 4:  # Y axis on right stick
                forward_speed = scale_stick(event.value)
            if forward_speed < 100 and forward_speed > -100:
                forward_speed = 0
            if event.code == 1:  # Y axis on left stick
                forward_speed1 = scale_stick(event.value)
            if forward_speed1 < 100 and forward_speed1 > -100:
                forward_speed1 = 0
    # Mapping both triggers the Medium motor
            if event.code == 2:
                grab_speed = scale_stick(event.value)
            if grab_speed < 100 and -grab_speed > -100:
                grab_speed = 0
            if event.code == 5:
                grab_speed1 = -scale_stick(event.value)
            if grab_speed < 100 and grab_speed1 > -100:
                grab_speed1 = 0
    # if you press button O then the program will cancel