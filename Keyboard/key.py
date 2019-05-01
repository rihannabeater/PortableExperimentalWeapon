import RPi.GPIO as GPIO
import time
import os
import pygame
import pigpio
import PiMotor

pygame.init()
pygame.display.set_mode((1, 1))

#Config Gun
bullet_pusher = PiMotor.Stepper("STEPPER2")

#GPIO Pins
tilt = 20
pan = 5
flywheel = 4

#Configure pigpio
pi = pigpio.pi()
pi.set_servo_pulsewidth(tilt, 1500)
pi.set_servo_pulsewidth(pan, 1500)

#start at 90 deg.
current_tilt = 1500
current_pan = 1500

#constraints
#min = 1000
#max = 2000
min=500
max=2500
step = 20

#Config Tank
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
                if keys[pygame.K_w]:
                    if(current_tilt<1600):
                        current_tilt=current_tilt+step
                        pi.set_servo_pulsewidth(tilt, current_tilt)
                        time.sleep(.01)
                if keys[pygame.K_s]:
                    if(current_tilt>min):
                        current_tilt=current_tilt-step
                        pi.set_servo_pulsewidth(tilt, current_tilt)
                        time.sleep(.01)
                if keys[pygame.K_d]:
                    if(current_pan<max):
                        current_pan=current_pan+step
                        pi.set_servo_pulsewidth(pan, current_pan)
                        time.sleep(.01)
                if keys[pygame.K_a]:
                    if(current_pan>min):
                        current_pan=current_pan-step
                        pi.set_servo_pulsewidth(pan, current_pan)
                        time.sleep(.01)
                if keys[pygame.K_SPACE]:
                        bullet_pusher.forward(0.005, 30)
                        bullet_pusher.backward(0.005, 30)
                if keys[pygame.K_g]:
                        print("Shooting")
                        GPIO.setmode(GPIO.BCM)
                        GPIO.setup(flywheel, GPIO.OUT)
                        GPIO.output(flywheel, GPIO.HIGH)
                if keys[pygame.K_h]:
                        print("Stopping Gun")
                        # pi.set_servo_pulsewidth(flywheel, 0)
                        # GPIO.output(flywheel,GPIO.HIGH)
                        GPIO.setmode(GPIO.BCM)
                        GPIO.setup(flywheel, GPIO.OUT)
                        GPIO.output(flywheel, GPIO.LOW)
                        GPIO.cleanup()
                if not keys[pygame.K_UP] and not keys[pygame.K_DOWN] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    left.stop()
                    right.stop()
                    both.stop()
                if keys[pygame.K_UP]:
                    #-----------Forward--------------------------# 
                    print("Move Forward")
                    forward_light.on()
                    #both.forward(75)
                    right.forward(55)
                    left.forward(75)
                    time.sleep(.01)
                if keys[pygame.K_DOWN]:
                    #-----------Reverse--------------------------# 
                    print("Move Reverse")
                    back_light.on()
                    both.reverse(75)
                    time.sleep(.01)
                if keys[pygame.K_RIGHT]:
                    #-----------Turn Right-----------------------# 
                    print("Turn Right")
                    right_light.on()
                    left.forward(75)
                    right.reverse(75)
                    time.sleep(.01)
                if keys[pygame.K_LEFT]:
                    #-----------Turn Left-----------------------# 
                    print("Turn Left")
                    left_light.on()
                    right.forward(75)
                    left.reverse(75)
                    time.sleep(.01)
                if keys[pygame.K_e]:
                    pi.set_servo_pulsewidth(pan, 1500)
                    pi.set_servo_pulsewidth(tilt, 1200)
                    pi.stop()
                    left.stop()
                    right.stop()
                    both.stop()
                    os.system("sudo killall pigpiod")
                pygame.event.pump()

except KeyboardInterrupt:
    pi.set_servo_pulsewidth(pan, 1500)
    pi.set_servo_pulsewidth(tilt, 1200)
    pi.stop()
    left.stop()
    right.stop()
    both.stop()
    os.system("sudo killall pigpiod")
    #GPIO.cleanup()

