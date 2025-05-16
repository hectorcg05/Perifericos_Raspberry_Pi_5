'''Formato para Python
Nombre del archivo: sensor_inclinación.py
Descripción: inclinación detectada por sensor pequeño
Autor: Héctor Castillo Guerra 
Versión: 1.0'''
from gpiozero import Button
from signal import pause

sensor_inclinacion = Button(22)

sensor_inclinacion.when_pressed = lambda: print("Inclinación detectada")

print("Coloca el sensor en posición vertical y después muevelo para probar")
pause()