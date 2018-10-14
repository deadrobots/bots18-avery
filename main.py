#!/usr/bin/python
import os, sys
from wallaby import *
import Constants as c

def drivetimed(lspeed, rspeed, sleep):
    motor(c.mmright, rspeed)
    motor(c.mmleft, lspeed)
    msleep(sleep)

def waitforbutton():
    print "press button"
    while not right_button():
        pass

def main():    #this function linefollows and will stop at a soda can and pick it up
    print "Hi averyperez"
    start = seconds()
    while analog(c.ET) > **************************
        if analog(c.tophat) > 2000:  #tophat=0
            drivetimed(100,0,10)
        else:
            drivetimed(0,100, 10)


def drivesquare():    #drives in a square
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

    for i in range(1, 5):
        while analog(0) > 2000:
            drivetimed(100,0,500)
        while analog(0) < 2000:
            drivetimed(0,100, 500)



#finish challenge on board(picture on phone), test wait for button, and use drivetimed




if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();