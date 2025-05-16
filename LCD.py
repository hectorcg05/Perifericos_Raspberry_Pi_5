'''Formato para Python
Nombre del archivo: LCD.py
Descripción: Mensajes a desplegar en lcd 16x2
Autor: Héctor Castillo Guerra 
Versión: 1.0'''
from RPLCD.i2c import CharLCD
from time import sleep

#creamos el objeto lcd
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2,
                          charmap='A00', auto_linebreaks=True)

lcd.clear()
lcd.write_string("Para un tutorial")
sleep(1)
lcd.clear()
lcd.write_string("Like y Suscribete")