from gpiozero import Button
from signal import pause

sensor_pir = Button(23)

sensor_pir.when_pressed = lambda: print("Movimiento detectada")

print("Muevete frente al sensor para probarlo.")
pause()