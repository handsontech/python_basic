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

while True:
    if Button.LEFT in ev3.buttons.pressed():
        ev3.screen.load_image(ImageFile.LEFT)
    elif Button.RIGHT in ev3.buttons.pressed():
        ev3.screen.load_image(ImageFile.RIGHT)
    elif Button.UP in ev3.buttons.pressed():
        ev3.screen.load_image(ImageFile.FORWARD)
    elif Button.DOWN in ev3.buttons.pressed():
        ev3.screen.load_image(ImageFile.BACKWARD)

