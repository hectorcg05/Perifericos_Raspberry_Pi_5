'''Formato para Python
Nombre del archivo: keypad.py
Descripción: teclado matricial para detectar tecla o caracter presionado
Autor: Héctor Castillo Guerra 
Versión: 1.0'''
#!/usr/bin/env python3
from gpiozero import DigitalOutputDevice, Button
from time import sleep

class Keypad:
    def _init_(self, rows_pins, cols_pins, keys):
        """
        Initialize the Keypad with specified row and column pins and keypad layout.
        :param rows_pins: List of GPIO pins for the rows.
        :param cols_pins: List of GPIO pins for the columns.
        :param keys: List of keys in the keypad layout.
        """
        self.rows = [DigitalOutputDevice(pin) for pin in rows_pins]
        self.cols = [Button(pin, pull_up=False) for pin in cols_pins]
        self.keys = keys

    def read(self):
        """
        Read the currently pressed keys on the keypad.
        :return: A list of pressed keys.
        """
        pressed_keys = []
        for i, row in enumerate(self.rows):
            row.on()
            for j, col in enumerate(self.cols):
                if col.is_pressed:
                    index = i * len(self.cols) + j
                    pressed_keys.append(self.keys[index])
            row.off()
        return pressed_keys

try:
    rows_pins = [5, 6, 13, 19]
    cols_pins = [4, 17, 27, 22]
    keys = ["1", "2", "3", "A",
            "4", "5", "6", "B",
            "7", "8", "9", "C",
            "*", "0", "#", "D"]

    keypad = Keypad(rows_pins, cols_pins, keys)
    last_key_pressed = []

    while True:
        pressed_keys = keypad.read()
        if pressed_keys and pressed_keys != last_key_pressed:
            print(pressed_keys)
            last_key_pressed = pressed_keys
        sleep(0.1)

except KeyboardInterrupt:
    pass