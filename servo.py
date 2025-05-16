'''Formato para Python
Nombre del archivo: servo.py
Descripción: activar motor servo de manera simple
Autor: Héctor Castillo Guerra 
Versión: 1.0'''
import RPi.GPIO as GPIO
import time

# Configuración
servo_pin = 17  # GPIO17 = pin físico 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Crear señal PWM a 50Hz (frecuencia estándar para servos)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def set_angle(angle):
    duty = 2 + (angle / 18)  # Conversión de ángulo a ciclo de trabajo
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        set_angle(0)
        time.sleep(1)
        set_angle(90)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
