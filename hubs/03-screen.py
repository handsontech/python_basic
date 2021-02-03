#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

from pybricks.media.ev3dev import SoundFile, ImageFile, Font


# Made by HandsonTechnology 
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.beep()


ev3.screen.print('World') #World 화면에 출력
wait(1000)

ev3.screen.clear() #화면 지우기

ev3.screen.draw_text(60, 50, 'Hello') # x=60, y=50 Hello 출력
wait(1000)

ev3.screen.load_image(ImageFile.LEFT) #EV3 내장된 이미지를 표시
wait(1000)


#글자 크기 변경
#글자 크기 정의 
font = Font(size=100)

#폰트 설정
ev3.screen.set_font(font) 
#화면 지우기
ev3.screen.clear()
#글자 크기 확인
ev3.screen.print('Big Font')
wait(5000)


