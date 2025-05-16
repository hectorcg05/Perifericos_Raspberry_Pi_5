from gpiozero import Button
from signal import pause

LOGFILE = "mensajes.txt"   # <- aquí pones tu nombre de fichero

def log(msg: str):
    print(msg)
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

sensor_inclinacion = Button(22)
sensor_pir        = Button(23)
sensor_agua       = Button(24)

sensor_inclinacion.when_pressed = lambda: log("Inclinación detectada")
sensor_pir.when_pressed         = lambda: log("Movimiento detectada")
sensor_agua.when_pressed        = lambda: log("Agua detectada")

log("Sensores listos para detectar")
pause()