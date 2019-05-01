import time
import pygame
import pigpio

pygame.init()
pygame.display.set_mode((1, 1))

#GPIO Pins
tilt = 8
pan = 5

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
step = 10

try:
    while True:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    if(current_tilt<max):
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
                pygame.event.pump()

except KeyboardInterrupt:
    pi.set_servo_pulsewidth(pan, 1500)
    pi.set_servo_pulsewidth(tilt, 1500)
    pi.stop()
