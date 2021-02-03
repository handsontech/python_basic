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

like_pizza = True
like_tomato = False

print(like_pizza and like_tomato)    #피자와 토마토 둘 다 좋아하면 -> 참
print(like_pizza or like_tomato)     #피자, 토마토 둘 중 하나만 좋아해도 -> 참
print(not like_tomato)               #토마토를 좋아하지 않으면 -> 참