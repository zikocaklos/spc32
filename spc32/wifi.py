import network
import time

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    print("Conectando a WiFi...")
    while not wlan.isconnected():
        time.sleep(1)
        print("...")

    print("Conectado:", wlan.ifconfig())
    return wlan
