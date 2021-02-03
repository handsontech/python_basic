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

left= Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 55.5, 104)

ultra = UltrasonicSensor(Port.S2)

robot.drive(150,0)
#20 cm 이상 -> 계속 직진한다.
while ultra.distance() > 200:
    pass

#20 cm 이하 -> 다음 프로그램 실행
#10 cm 후진
robot.straight(-100)
#모터를 멈춘다. 
robot.stop()

