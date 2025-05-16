'''Formato para Python
Nombre del archivo: DHT11.py
Descripción: Sensor de temperatura y humedad, meciones
Autor: Héctor Castillo Guerra 
Versión: 1.0'''

import time
import adafruit_dht
import board

dht_device = adafruit_dht.DHT11(board.D4)

try:
    while True:
        temperatura = dht_device.temperature
        humedad = dht_device.humidity
        print(f"temperatura: {temperatura}°c  Humedad: {humedad}%")
        time.sleep(2)
except KeyboardInterrupt:
    print("lectura detenida")
except RuntimeError as error:
    print(f"error de lectura: {error}")
