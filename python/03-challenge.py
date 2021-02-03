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

# 1번 문제 정답

white = 67.2321
black = 20.121
avg = (black+white)/2
print(avg)      #43.67655



# 2번 문제 정답

day = 13
print('오늘은 '+str(day)+ '일 입니다.') # 오늘은 13일 입니다.
day = day +7
print('다음주는 '+str(day)+ '일 입니다.') #다음주는 20일 입니다.
