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

#컬러센서를 초기화
cs = ColorSensor(Port.S3)

#색상을 읽는다. Color.RED, Color.BLUE ..
color = cs.color()
#반사광값을 읽는다. 0 ~ 100%
reflection = cs.reflection()
#주변광값을 읽는다. 0 ~ 100%
ambient = cs.ambient()

print(color)
print(reflection)
print(ambient)
