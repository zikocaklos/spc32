from fastapi import APIRouter

router = APIRouter(prefix="/api")

# Variables simuladas (Render no puede leer hardware)
data = {
    "distance": 0,
    "light": 0
}

led_state = {
    "led1": False,
    "led2": False
}

motor_state = {
    "motor": False
}

# -----------------------------
#        SENSORES
# -----------------------------
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
    return {"message": "Datos actualizados correctamente"}


# -----------------------------
#           LEDS
# -----------------------------
@router.get("/leds")
def get_leds():
    return led_state


@router.post("/leds")
def set_leds(led1: bool, led2: bool):
    led_state["led1"] = led1
    led_state["led2"] = led2
    return {
        "message": "LEDs actualizados",
        "status": led_state
    }


# -----------------------------
#           MOTOR
# -----------------------------
@router.get("/motor")
def get_motor():
    return motor_state


@router.post("/motor")
def set_motor(motor: bool):
    motor_state["motor"] = motor
    return {
        "message": "Motor actualizado",
        "status": motor_state
    }
