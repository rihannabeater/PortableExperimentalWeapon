#!/usr/bin/python

import PiMotor
import time
import pygame

pygame.init()
pygame.display.set_mode((1, 1))

#Name of Individual MOTORS 
left = PiMotor.Motor("MOTOR1",1)
right = PiMotor.Motor("MOTOR2",1)
both = PiMotor.LinkedMotors(left,right)

#Names for Individual Arrows
back_light = PiMotor.Arrow(1)
left_light = PiMotor.Arrow(2)
forward_light = PiMotor.Arrow(3) 
right_light = PiMotor.Arrow(4)

try:
    while True:
                keys = pygame.key.get_pressed()
                if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
                    left.stop()
                    right.stop()
                    both.stop()
                if keys[pygame.K_w]:
                    #-----------Forward--------------------------# 
                    print("Move Forward")
                    forward_light.on()
                    #both.forward(75)
                    right.forward(55)
                    left.forward(75)
                    time.sleep(.01)
                if keys[pygame.K_s]:
                    #-----------Reverse--------------------------# 
                    print("Move Reverse")
                    back_light.on()
                    both.reverse(75)
                    time.sleep(.01)
                if keys[pygame.K_d]:
                    #-----------Turn Right-----------------------# 
                    print("Turn Right")
                    right_light.on()
                    left.forward(75)
                    right.reverse(75)
                    time.sleep(.01)
                if keys[pygame.K_a]:
                    #-----------Turn Left-----------------------# 
                    print("Turn Left")
                    left_light.on()
                    right.forward(75)
                    left.reverse(75)
                    time.sleep(.01)
                pygame.event.pump()

except KeyboardInterrupt:
    right.stop()
    left.stop()
    both.stop()

    

