#!/usr/bin/env python3
import time
from ev3dev2.sound import Sound
spkr = Sound()
print("Starting program...")
time.sleep(1.5)
print("Initializing...")
time.sleep(1)
print("Initializing Constants...")
time.sleep(.5)
print("Constants good!")
time.sleep(.1)
print("Connecting to controller")
time.sleep(.75)
print("Connected!")
time.sleep(2)
spkr.play_file('Package/bark.wav')