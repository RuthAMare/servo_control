# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50) # 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (at pulse off)
servo.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)

#Rotating the servo
print ("Rotating 180 degrees in 10 steps")

# Defining the variable duty
duty = 2

# Loop for duty values from 2 to 12 (0 to 180 degrees)
while duty <= 12:
    servo.ChangeDutyCycle(duty)
    time.sleep(0.4)
    servo.ChangeDutyCycle(0)
    time.sleep(0.6)
    duty = duty + 1

# Wait a couple of seconds
time.sleep(2)

# Turn back to 90 degrees
print ("Turning back to 90 degrees for 2 seconds")
servo.ChangeDutyCycle(7)
time.sleep(1)
servo.ChangeDutyCycle(0)
time.sleep(1)

#turning back to 0 degrees
print ("Turning back to 0 degrees")
servo.ChangeDutyCycle(2)
time.sleep(1)
servo.ChangeDutyCycle(0)

#Clean things up at the end
servo.stop()
GPIO.cleanup()
print ("Environment cleaned")


