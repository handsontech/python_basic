#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from threading import Thread

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

#2회 반복
for i in range(2):
    #2초 동안 직진
    robot.drive(100, 0) 
    wait(2000)
    #1초 동안 회전 (모터마다 회전 시간은 조금씩 다를 수 있음)
    #robot.turn(90) 사용가능
    robot.drive(100, 110)
    wait(1000)

#2초 동안 직진
robot.drive(100, 0)
wait(2000)
        
robot.stop()
