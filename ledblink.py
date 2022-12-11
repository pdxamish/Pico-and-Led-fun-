from machine import Pin
from utime import sleep

led1 = Pin(16,Pin.OUT)
led2 = Pin(17,Pin.OUT)
led3 = Pin(18,Pin.OUT)
led4 = Pin(19,Pin.OUT)
led5 = Pin(20,Pin.OUT)
led6 = Pin(21,Pin.OUT)


while True:

    led2.value(0)
    led4.value(0)
    led6.value(0)
    led1.value(1)
    led3.value(1)
    led5.value(1)
    sleep(0.2)
    led1.value(0)
    led3.value(0)
    led5.value(0)
    led2.value(1)
    led4.value(1)
    led6.value(1)
    sleep(0.2)
    
