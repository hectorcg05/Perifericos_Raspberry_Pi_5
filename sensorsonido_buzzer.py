'''Formato para Python
Nombre del archivo: sensorsonido_buzzer.py
Descripción: cada detección de sonido activamos buzzer (sonido)
Autor: Héctor Castillo Guerra 
Versión: 1.0'''
from gpiozero import Button, Buzzer
from signal import pause
from time import sleep

sensor_sonido = Button(17)  # Pin del sensor de sonido
zumbador = Buzzer(18)       # Pin del buzzer

def detectar():
    print("Sonido detectado")
    zumbador.on()
    sleep(0.2)
    zumbador.off()

sensor_sonido.when_pressed = detectar

print("Esperando sonido...")

pause()
