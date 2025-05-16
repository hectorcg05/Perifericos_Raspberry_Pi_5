'''Formato para Python
Nombre del archivo: ultrasonico.py
Descripción: medición de distancia con ultrasonico
Autor: Héctor Castillo Guerra 
Versión: 1.0'''
from gpiozero import DistanceSensor
from time import sleep

sensor= DistanceSensor(echo=24, trigger=23, max_distance=1.0)
try:
    while True:
        distancia= sensor.distance *100
        print(f"distancia: {distancia:.3f} cm")
        sleep(1)
except KeyboardInterrupt:
    print("\n El usuario interrumpio")