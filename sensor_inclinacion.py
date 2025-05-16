from gpiozero import Button
from signal import pause

sensor_inclinacion = Button(22)

sensor_inclinacion.when_pressed = lambda: print("Inclinación detectada")

print("Coloca el sensor en posición vertical y después muevelo para probar")
pause()