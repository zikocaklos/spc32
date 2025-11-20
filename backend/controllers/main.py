from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api")

# -----------------------------
#   MODELOS PARA RECIBIR JSON
# -----------------------------
class LEDModel(BaseModel):
    led1: bool
    led2: bool

class MotorModel(BaseModel):
    motor: bool

class SensorUpdate(BaseModel):
    distance: float
    light: float


# -----------------------------
#   VARIABLES SIMULADAS
# -----------------------------
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
def update_sensor_values(body: SensorUpdate):
    data["distance"] = body.distance
    data["light"] = body.light
    return {"message": "Datos actualizados correctamente"}


# -----------------------------
#           LEDS
# -----------------------------
@router.get("/leds")
def get_leds():
    return led_state


@router.post("/leds")
def set_leds(body: LEDModel):
    led_state["led1"] = body.led1
    led_state["led2"] = body.led2
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
def set_motor(body: MotorModel):
    motor_state["motor"] = body.motor
    return {
        "message": "Motor actualizado",
        "status": motor_state
    }
