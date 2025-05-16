from gpiozero import LEDBarGraph, RotaryEncoder
from signal import pause

encoder = RotaryEncoder(a=5, b=6, max_steps=10)
bar = LEDBarGraph(12,13,14,15,16,17,18,19,20,21)

#hacemos una función
def actualizar():
    valor=encoder.steps
    if valor < 0:
        encoder.steps = 0
        valor = 0
    elif valor > 10:
        encoder.steps = 10
        valor = 10

    bar.value = valor / 10
encoder.when_rotated = actualizar
print('Gira perilla para controlar la barra de leds')
pause()