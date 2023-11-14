
from machine import Pin,Timer
import time

led = Pin(15, Pin.OUT)
timer = Timer()


def rovid(darab):
    for i in range(darab):
        for i in range(500):
            led.toggle()
            time.sleep(0.001)
        led.off()
        time.sleep(0.1)
    led.off
    time.sleep(0.5)
        
def hosszu(darab):
    for i in range(darab):
        for i in range(1000):
            led.toggle()
            time.sleep(0.001)
        led.off()
        time.sleep(0.1)
    led.off
    time.sleep(0.5)
    
rovid(3)
hosszu(3)
rovid(3)