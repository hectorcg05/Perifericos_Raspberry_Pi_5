'''Formato para Python
Nombre del archivo: sensor_agua.py
Descripción: detección de agua con sensor
Autor: Héctor Castillo Guerra 
Versión: 1.0'''
from gpiozero import Button
from signal import pause

sensor_agua = Button(24)

sensor_agua.when_pressed = lambda: print("Agua detectada")

print("Coloca agua en el sensor para probar el sensor")
pause()