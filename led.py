'''Formato para Python
Nombre del archivo: led.py
Descripción: encender un led en modo blink
Autor: Héctor Castillo Guerra 
Versión: 1.0'''
from gpiozero import LED
from time import sleep

led= LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    