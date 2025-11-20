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
#   SIMULACIÓN LDR (LÓGICA)
# -----------------------------
def process_ldr_value(light_value: float):
    """
    Lógica simulada del sensor LDR.
    El ESP32 enviará valores entre 0 y 4095.
    """
    
    # Puedes cambiar este umbral según tu proyecto real
    UMBRAL_OSCURIDAD = 1500

    if light_value < UMBRAL_OSCURIDAD:
        led_state["led1"] = True   # Encender LED por oscuridad
    else:
        led_state["led1"] = False  # Apagar LED

    # devolvemos el valor para mantener consistencia
    return light_value


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

    # Guardamos distancia normal
    data["distance"] = body.distance

    # Procesamos luz con la lógica de LDR
    processed_light = process_ldr_value(body.light)
    data["light"] = processed_light

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
    print("GET /api/motor solicitado ->", motor_state)
    return motor_state

@router.post("/motor")
def set_motor(body: MotorModel):
    motor_state["motor"] = body.motor
    print("POST /api/motor recibido ->", motor_state)
    return {
        "message": "Motor actualizado",
        "status": motor_state
    }
