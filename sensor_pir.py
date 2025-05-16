'''Formato para Python
Nombre del archivo: sensor_pir.py
Descripción: detección de movimiento de acuerdo a medición de pir
Autor: Héctor Castillo Guerra 
Versión: 1.0'''
from gpiozero import Button
from signal import pause

sensor_pir = Button(23)

sensor_pir.when_pressed = lambda: print("Movimiento detectada")

print("Muevete frente al sensor para probarlo.")
pause()