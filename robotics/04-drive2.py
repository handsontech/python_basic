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

#속도 100mm/s, 회전 속도: 110 deg/s
robot.drive(100,110)

#1초 동안 모터 동작
wait(1000)

#모터를 멈춘다. 
robot.stop()



