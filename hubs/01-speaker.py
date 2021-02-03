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

#Write your program here.

#Hello 라고 말한다.
ev3.speaker.say('Hello')

#기본 비프음을 1번 재생한다.
ev3.speaker.beep()

#20 ms 기다린다. (쉼표의 개념)
wait(20)

#1500 Hz의 주파수를 1000 ms 동안 재생한다.
ev3.speaker.beep(1500,1000)

#EV3 에 내장된 파일을 재생한다.
ev3.speaker.play_file(SoundFile.EV3)



do = 523
re = 587
mi = 659

ev3.speaker.beep(mi, 500)
wait(20)
ev3.speaker.beep(re, 500)
wait(20)
ev3.speaker.beep(do, 500)
wait(20)
ev3.speaker.beep(re, 500)
wait(20)
ev3.speaker.beep(mi, 500)
wait(20)
ev3.speaker.beep(mi, 500)
wait(20)
ev3.speaker.beep(mi, 500)
wait(20)





brick.display.text('World') #World 제일 위에 표시
wait(1000)
brick.display.clear()  #디스플레이 지우기
brick.display.text('Hello',(60, 50)) #(60,50) 위치에 Hello 표시 
wait(1000)
brick.display.image(ImageFile.LEFT) #LEFT 이미지 표시
wait(1000)
