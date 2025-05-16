'''Formato para Python
Nombre del archivo: buzzer.py
Descripción: activar sonido en buzzer
Autor: Héctor Castillo Guerra 
Versión: 1.0'''
from gpiozero import Buzzer
from time import sleep

zumbador = Buzzer(18)

try:
    while True:
        zumbador.on()
        sleep(0.2)
        zumbador.off()
        sleep(0.2)
except KeyboardInterrupt:
    zumbador.off()