#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Made by HandsonTechnology 
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
ev3.speaker.beep()


#빨간색으로 켜짐 (빨간, 노랑, 초록, 오렌지)
ev3.light.on(Color.RED)

#브릭등 꺼짐
ev3.light.off()


#무한 반복으로 코드가 동작하므로
#사용자가 직접 취소 버튼을 이용하여 프로그램을 종료해야 한다. 
while True:
    ev3.light.on(Color.RED)
    wait(1000)
    ev3.light.on(Color.YELLOW)
    wait(1000)
    ev3.light.on(Color.GREEN)
    wait(1000) 
