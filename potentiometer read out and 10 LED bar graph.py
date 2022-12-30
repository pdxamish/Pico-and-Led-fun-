# Bargraph LED display - 10 segment, multi color, Common cathode
# Turn on and off each segment

#ALSO REQUIRED!!!
#220 ohm resistor for each Segment - connect to ground
#Wire according to information provided on associated video on YouTube

#Find pin #1 - usually the corner that has a chamfer
#pin 1 to pin 21/GP16
#Continue down this side connecting the pins as such
#pin 2 to pin 22/GP17
#pin 3 to pin 24/GP18
#pin 4 to pin 25/GP19
#pin 5 to pin 26/GP20
#pin 6 to pin 27/GP21
#pin 7 to pin 29/GP22
#pin 8 to pin 31/GP26
#pin 9 to pin 32/GP27
#pin 10 to pin 34/G28
#Connect all the pins on the opposite side to ground through a 220 Ohm resistor

#load libraries
import machine
from machine import ADC
from utime import sleep

potentiometer = ADC(28)



A_LED = machine.Pin(16,machine.Pin.OUT)  #Create an output pin for each segment
B_LED = machine.Pin(17,machine.Pin.OUT)  
C_LED = machine.Pin(18,machine.Pin.OUT)  
D_LED = machine.Pin(19,machine.Pin.OUT)  
E_LED = machine.Pin(20,machine.Pin.OUT)  
F_LED = machine.Pin(21,machine.Pin.OUT)  
G_LED = machine.Pin(22,machine.Pin.OUT)  
H_LED = machine.Pin(26,machine.Pin.OUT)  
I_LED = machine.Pin(27,machine.Pin.OUT)  
J_LED = machine.Pin(0,machine.Pin.OUT)  

def off():
    print("off")
    A_LED.value(0)       #Turn ON LED Bars in sequence
    B_LED.value(0)       
    C_LED.value(0)       
    D_LED.value(0)       
    E_LED.value(0)        
    F_LED.value(0)        
    G_LED.value(0)       
    H_LED.value(0)       
    I_LED.value(0)       
    J_LED.value(0)
    

def one():
    print("10%")
    A_LED.value(1)       #Turn ON LED Bars in sequence
    B_LED.value(0)       
    C_LED.value(0)       
    D_LED.value(0)       
    E_LED.value(0)        
    F_LED.value(0)        
    G_LED.value(0)       
    H_LED.value(0)       
    I_LED.value(0)       
    J_LED.value(0)

def two():
    print("20%")
    A_LED.value(1)       #Turn ON LED Bars in sequence
    B_LED.value(1)       
    C_LED.value(0)       
    D_LED.value(0)       
    E_LED.value(0)        
    F_LED.value(0)        
    G_LED.value(0)       
    H_LED.value(0)       
    I_LED.value(0)       
    J_LED.value(0)
    

def three():
    print("30%")
    A_LED.value(1)       #Turn ON LED Bars in sequence
    B_LED.value(1)       
    C_LED.value(1)       
    D_LED.value(0)       
    E_LED.value(0)        
    F_LED.value(0)        
    G_LED.value(0)       
    H_LED.value(0)       
    I_LED.value(0)       
    J_LED.value(0)
    
    
def four():
    print("40%")
    A_LED.value(1)       #Turn ON LED Bars in sequence
    B_LED.value(1)       
    C_LED.value(1)       
    D_LED.value(1)       
    E_LED.value(0)        
    F_LED.value(0)        
    G_LED.value(0)       
    H_LED.value(0)       
    I_LED.value(0)       
    J_LED.value(0)


def five():
    print("50%")
    A_LED.value(1)       #Turn ON LED Bars in sequence
    B_LED.value(1)       
    C_LED.value(1)       
    D_LED.value(1)       
    E_LED.value(1)        
    F_LED.value(0)        
    G_LED.value(0)       
    H_LED.value(0)       
    I_LED.value(0)       
    J_LED.value(0)



def six():
    ####print("60%)
    A_LED.value(1)       #Turn ON LED Bars in sequence
    B_LED.value(1)       
    C_LED.value(1)       
    D_LED.value(1)       
    E_LED.value(1)        
    F_LED.value(1)        
    G_LED.value(0)       
    H_LED.value(0)       
    I_LED.value(0)       
    J_LED.value(0)
    
    
def seven():
    print("70%")
    A_LED.value(1)       #Turn ON LED Bars in sequence
    B_LED.value(1)       
    C_LED.value(1)       
    D_LED.value(1)       
    E_LED.value(1)        
    F_LED.value(1)        
    G_LED.value(1)       
    H_LED.value(0)       
    I_LED.value(0)       
    J_LED.value(0)
    
    

def eight():
    print("80%")
    A_LED.value(1)       #Turn ON LED Bars in sequence
    B_LED.value(1)       
    C_LED.value(1)       
    D_LED.value(1)       
    E_LED.value(1)        
    F_LED.value(1)        
    G_LED.value(1)       
    H_LED.value(1)       
    I_LED.value(0)       
    J_LED.value(0)



def nine():
    print("90%")
    A_LED.value(1)       #Turn ON LED Bars in sequence
    B_LED.value(1)       
    C_LED.value(1)       
    D_LED.value(1)       
    E_LED.value(1)        
    F_LED.value(1)        
    G_LED.value(1)       
    H_LED.value(1)       
    I_LED.value(1)       
    J_LED.value(0)
    
    
def ten():
    print("fully Open")
    A_LED.value(1)       #Turn ON LED Bars in sequence
    B_LED.value(1)       
    C_LED.value(1)       
    D_LED.value(1)       
    E_LED.value(1)        
    F_LED.value(1)        
    G_LED.value(1)       
    H_LED.value(1)       
    I_LED.value(1)       
    J_LED.value(1)    
    
while True:
    potentiometer_value = potentiometer.read_u16()   #reading analog pin
    print(potentiometer_value)
    if potentiometer_value <1000:
        zero()
    elif potentiometer_value <6000:
        one()
    elif potentiometer_value <13000:
        two()
    elif potentiometer_value <20000:
        three()
    elif potentiometer_value <27000:
        four()
    elif potentiometer_value <34000:
        five()
    elif potentiometer_value <41000:
        six()
    elif potentiometer_value <46000:
        seven()
    elif potentiometer_value <52000:
        eight()
    elif potentiometer_value <57000:
        nine()
    elif potentiometer_value >63000:
        ten()
         
            
    
    
        
    