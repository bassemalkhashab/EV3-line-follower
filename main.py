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
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S4)
left_motor = Motor(Port.A,Direction.CLOCKWISE)
right_motor = Motor(Port.D,Direction.CLOCKWISE)
moveSteering = DriveBase(left_motor, right_motor, 56, 120)
while(1):
    
    right_motor.run(300)
    left_motor.run(300)
    # left_val = left_sensor.reflection()
    # right_val = right_sensor.reflection()
    # eerrorrroro = left_val-right_val
    # moveSteering.drive(401,0)