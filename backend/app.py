import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import numpy as np
from PIL import Image
import tensorflow as tf
import pickle
import io
import requests
import sqlite3

app = FastAPI()

# ---------------- DATABASE ----------------

def connect_db():
    return sqlite3.connect("smart_farming.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        result TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_log(log_type, result):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO logs(type,result) VALUES (?,?)", (log_type, result))
    conn.commit()
    conn.close()

create_tables()

# ---------------- LOAD MODELS ----------------
crop_model = pickle.load(open("models/crop_model.pkl", "rb"))
fert_model = pickle.load(open("models/fertilizer_model.pkl", "rb"))
yield_model = pickle.load(open("models/yield_model.pkl", "rb"))
disease_model = tf.keras.models.load_model("models/plant_disease_model.h5")

# ---------------- INPUT ----------------

class CropInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

class FertilizerInput(BaseModel):
    temperature: float
    humidity: float
    moisture: float
    soil_type: int
    crop_type: int
    nitrogen: float
    potassium: float
    phosphorous: float

class WeatherInput(BaseModel):
    city: str

class YieldInput(BaseModel):
    rainfall: float
    temperature: float
    fertilizer: float

# ---------------- CROP ----------------

@app.post("/predict_crop")
def predict_crop(data: CropInput):
    features = [[data.N, data.P, data.K, data.temperature, data.humidity, data.ph, data.rainfall]]
    result = str(crop_model.predict(features)[0])
    insert_log("crop", result)
    return {"recommended_crop": result}

# ---------------- FERTILIZER ----------------

@app.post("/predict_fertilizer")
def predict_fertilizer(data: FertilizerInput):
    features = [[data.temperature, data.humidity, data.moisture, data.soil_type,
                 data.crop_type, data.nitrogen, data.potassium, data.phosphorous]]
    result = str(fertilizer_model.predict(features)[0])
    insert_log("fertilizer", result)
    return {"fertilizer": result}

# ---------------- DISEASE ----------------

@app.post("/detect_disease")
async def detect_disease(file: UploadFile = File(...)):
    contents = await file.read()

    image = Image.open(io.BytesIO(contents)).convert("RGB")
    image = image.resize((128, 128))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = disease_model.predict(image)

    classes = ["Apple Scab", "Apple Black Rot", "Corn Rust", "Corn Leaf Blight", "Healthy"]
    disease = classes[np.argmax(prediction)]

    insert_log("disease", disease)

    return {"disease": disease}

# ---------------- WEATHER ----------------

API_KEY = "285415dfa6b7b052790891a23cfa86fb"

@app.post("/weather")
def weather(data: WeatherInput):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={data.city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    result = {
        "temperature": response["main"]["temp"],
        "humidity": response["main"]["humidity"],
        "description": response["weather"][0]["description"]
    }

    insert_log("weather", str(result))

    return result

# ---------------- YIELD ----------------

@app.post("/predict_yield")
def predict_yield(data: YieldInput):
    features = [[data.rainfall, data.temperature, data.fertilizer]]
    prediction = yield_model.predict(features)
    return {"yield_prediction": float(prediction[0])}

# ---------------- HISTORY ----------------

@app.get("/history")
def history():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY id DESC")
    data = cursor.fetchall()
    conn.close()
    return {"data": data}