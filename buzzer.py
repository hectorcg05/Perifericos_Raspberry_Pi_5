from gpiozero import Buzzer
from time import sleep

zumbador = Buzzer(18)

try:
    while True:
        zumbador.on()
        sleep(0.2)
        zumbador.off()
        sleep(0.2)
except KeyboardInterrupt:
    zumbador.off()