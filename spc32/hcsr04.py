from machine import Pin, time_pulse_us
import time

class HCSR04:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)

    def distance_cm(self):
        self.trigger.off()
        time.sleep_us(2)
        self.trigger.on()
        time.sleep_us(10)
        self.trigger.off()

        duration = time_pulse_us(self.echo, 1, 30000)
        distance = duration / 58.0
        return distance
