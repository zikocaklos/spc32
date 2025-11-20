import urequests
import time
from wifi import connect_wifi
from hcsr04 import HCSR04
from tsl2561 import read_light
from servo import Servo

SSID = "TU_WIFI"
PASSWORD = "CONTRASEÑA"
API = "https://TU_BACK_RENDER.onrender.com/api"

connect_wifi(SSID, PASSWORD)

distance_sensor = HCSR04(trigger_pin=5, echo_pin=18)
servo = Servo(15)

while True:
    try:
        distance = distance_sensor.distance_cm()
        light = read_light()

        urequests.post(f"{API}/update",
            json={"distance": distance, "light": light})

        led_response = urequests.get(f"{API}/data").json()
        leds = led_response["leds"]

        if leds["red"] == 1:
            servo.move(0)
        elif leds["yellow"] == 1:
            servo.move(90)
        elif leds["green"] == 1:
            servo.move(180)

        print("Distancia:", distance, "Luz:", light)
    except Exception as e:
        print("Error:", e)

    time.sleep(2)
