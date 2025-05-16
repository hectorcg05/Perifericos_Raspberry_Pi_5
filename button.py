'''Formato para Python
Nombre del archivo: button.py
Descripción: presionar boton simple
Autor: Héctor Castillo Guerra 
Versión: 1.0'''
import RPi.GPIO as GPIO
import time

ButtonPin = 16  # Pin conectado al botón

GPIO.setmode(GPIO.BCM)
GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(ButtonPin) == GPIO.LOW:  # Botón presionado (activo en bajo)
            print("Button Pressed")
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
