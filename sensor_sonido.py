'''Formato para Python
Nombre del archivo: sensor_sonido.py
Descripción: detección de cualquier sonido por sensor
Autor: Héctor Castillo Guerra 
Versión: 1.0'''

from gpiozero import Button
from signal import pause

sensor_sonido = Button(17)

def detectar():
    print("sonido detectado")

sensor_sonido.when_pressed = detectar

print("esperando....")

pause()

