'''Formato para Python
Nombre del archivo: encoder.py
Descripción: encoder rotatorio mediciones por posición
Autor: Héctor Castillo Guerra 
Versión: 1.0'''

from gpiozero import RotaryEncoder
from signal import pause

encoder = RotaryEncoder(a=5, b=6, max_steps=100)

def posicion():
    print(f"Posición actual: {encoder.steps}")

encoder.when_rotated = posicion

print("gira la perilla")
pause()