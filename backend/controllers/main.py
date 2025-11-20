from fastapi import APIRouter

router = APIRouter(prefix="/api")

# Variables simuladas (Render no puede leer directamente hardware)
data = {
    "distance": 0,
    "light": 0
}

led_state = {
    "led1": False,
    "led2": False
}

@router.get("/sensors")
def get_sensors():
    return {
        "distance": data["distance"],
        "light": data["light"]
    }


@router.post("/update")
def update_sensor_values(distance: float, light: float):
    data["distance"] = distance
    data["light"] = light
    return {"message": "Datos actualizados"}


@router.post("/leds")
def set_leds(led1: bool, led2: bool):
    led_state["led1"] = led1
    led_state["led2"] = led2
    return {"message": "LEDs actualizados", "status": led_state}


@router.get("/leds")
def get_leds():
    return led_state
