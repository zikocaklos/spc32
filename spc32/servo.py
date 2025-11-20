from machine import Pin, PWM

class Servo:
    def __init__(self, pin):
        self.pwm = PWM(Pin(pin), freq=50)

    def move(self, angle):
        duty = int(((angle / 180) * 102) + 26)
        self.pwm.duty(duty)
