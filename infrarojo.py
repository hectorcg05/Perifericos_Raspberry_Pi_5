'''Formato para Python
Nombre del archivo: infrarojo.py
Descripción: obstaculos detectados por medicion de sensor infrarojo
Autor: Héctor Castillo Guerra 
Versión: 1.0'''

#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

ObstaclePin = 18  # Pin conectado al sensor infrarrojo

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if GPIO.input(ObstaclePin) == 0:  # LOW = obstáculo detectado
            print("¡Obstáculo detectado!")
        else:
            print("No hay obstáculo.")
        time.sleep(0.5)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
