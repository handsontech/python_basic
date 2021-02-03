#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

x = 20
y = 30

print(x > y)          #x 가 y 보다 크다.
print (x < y)         #x 가 y 보다 작다.
print (x == y)        #x 와 y 는 같다.
print (x != y)        #x 와 y 는 다르다.
print (x >= y)        #x 는 y 보다 크거나 같다.
print (x <= y)        #x 는 y 보다 작거나 같다.


