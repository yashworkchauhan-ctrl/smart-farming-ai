import pickle
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

model = pickle.load(open("models/yield_model.pkl", "rb"))

class YieldInput(BaseModel):

    rainfall: float
    temperature: float
    fertilizer: float


@router.post("/predict_yield")

def predict_yield(data: YieldInput):

    features = [[
        data.rainfall,
        data.temperature,
        data.fertilizer
    ]]

    prediction = model.predict(features)

    return {"yield_prediction": float(prediction[0])}