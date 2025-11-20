from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.main import router as esp32_router

app = FastAPI()

# CORS para permitir llamadas desde Flutter
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas del ESP32
app.include_router(esp32_router)

@app.get("/")
def home():
    return {"message": "Backend ESP32 funcionando correctamente 🚀"}
