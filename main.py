#!/usr/bin/python
import os, sys
from wallaby import *
import Constants as c

def drivetimed(speed, msleep):
    motor(c.mmright, speed)
    motor(c.mmleft, speed)
def waitforbutton():
    print "press button"
    while not right_button():
        pass

def main():
    print "Hi avery"
    enable_servos()
    grabcan()


def drivesquare():
    motor(c.mmright, 100)
    motor(c.mmleft , 100)
    msleep(2000)
    for i in range(1, 5):
        motor(c.mmleft, 100)
        motor(c.mmright, 100)
        msleep(3000)
        drivetimed(0, 1000)
        waitforbutton()
        motor(c.mmleft, 0)
        motor(c.mmright,100)
        msleep(1200)


def movearm():
    enable_servos()
    set_servo_position(0,100)
    msleep(1000)
    set_servo_position(0,2000)
    msleep(1000)
    enable_servos()
    set_servo_position(0,100)
    msleep(1000)
    set_servo_position(0,2000)
    msleep(1000)


def grabcan():
    ao()
    set_servo_position(c.clawarm, c.clawarmdown)#claw move down
    msleep(1000)
    set_servo_position(c.claw, c.clawopen) # claw arm opens
    msleep(1000)
    motor(c.mmleft, 100)
    motor(c.mmright, 100)
    msleep(2000)
    ao()
    set_servo_position(c.claw, c.clawclosed)#claw closes on can
    msleep(1000)
    ao()
    set_servo_position(c.clawarm, c.clawarmup)
    msleep(3000)


#finish challenge on board(picture on phone), test wait for button, and use drivetimed




if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();