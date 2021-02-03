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



# 왼쪽 모터 B 포트 모터 초기화
left_motor = Motor(Port.B)
# 오른쪽 모터 C 포트 모터 초기화
right_motor = Motor(Port.C)

# 드라이브베이스 초기화
robot = DriveBase(left_motor, right_motor, 55.5, 104)


#10 cm 전진
robot.straight(100)
ev3.speaker.beep()

#10 cm 후진
robot.straight(-100)
ev3.speaker.beep()



