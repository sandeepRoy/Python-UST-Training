import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.HIGH)
print("LED ON")

#from machine import Pin, Timer
#led = Pin(25, Pin.OUT)
#timer = Timer()

#def blink(timer):
#    led.toggle()

#timer.init(freq=4.5, mode=Timer.PERIODIC, callback=blink)