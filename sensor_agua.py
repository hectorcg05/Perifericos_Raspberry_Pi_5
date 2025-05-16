from gpiozero import Button
from signal import pause

sensor_agua = Button(24)

sensor_agua.when_pressed = lambda: print("Agua detectada")

print("Coloca agua en el sensor para probar el sensor")
pause()