'''Formato para Python
Nombre del archivo: servo_con_infrarojo.py
Descripción: activación de motor servo en caso de no detectar obstaculo
Autor: Héctor Castillo Guerra 
Versión: 1.0'''
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

ObstaclePin = 18     # Pin del sensor IR
ServoPin = 17        # Pin del servo motor

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ServoPin, GPIO.OUT)
    global pwm
    pwm = GPIO.PWM(ServoPin, 50)  # Frecuencia del servo a 50Hz
    pwm.start(0)

def set_angle(angle):
    duty = 2 + (angle / 18)
    GPIO.output(ServoPin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.3)
    GPIO.output(ServoPin, False)
    pwm.ChangeDutyCycle(0)

def loop():
    while True:
        if GPIO.input(ObstaclePin) == 0:  # LOW = obstáculo detectado
            print("Detected Barrier!")
            set_angle(90)  # Detener en 90°
        else:
            print("No obstacle")
            # Movimiento constante entre 0 y 120°
            set_angle(0)
            time.sleep(0.5)
            set_angle(120)
            time.sleep(0.5)

def destroy():
    pwm.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()