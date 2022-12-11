from machine import Pin
from utime import sleep
led1=Pin(16,Pin.OUT)
led2=Pin(17,Pin.OUT)
led3=Pin(18,Pin.OUT)
led4=Pin(19,Pin.OUT)
led5=Pin(20,Pin.OUT)
led6=Pin(21,Pin.OUT)

while True:

    led1.value(1)
    sleep(.3)
    led1.value(0)
    led2.value(1)
    sleep(.3)
    led2.value(0)
    led3.value(1)
    sleep(.3)
    led3.value(0)
    led4.value(1)
    sleep(.3)
    led4.value(0)
    led5.value(1)
    sleep(.3)
    led5.value(0)
    led6.value(1)
    sleep(.3)
    led6.value(0)
    
    
    
    led6.value(0)
    sleep(0.2)