import machine
import network
import time

wifi = network.WLAN(network.STA_IF)

wifi.active(True)

wifi_lista = wifi.scan()

for i in wifi_lista:
    print(i[0])
    
    
wifi.connect("ha","3.1415926")