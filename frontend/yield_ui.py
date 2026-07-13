import streamlit as st
import requests

def yield_prediction():

    st.title("🌾 Crop Yield Prediction")

    rainfall = st.number_input("Rainfall")
    temperature = st.number_input("Temperature")
    fertilizer = st.number_input("Fertilizer Amount")

    if st.button("Predict Yield"):

        data = {
            "rainfall": rainfall,
            "temperature": temperature,
            "fertilizer": fertilizer
        }

        res = requests.post(
            "http://127.0.0.1:8000/predict_yield",
            json=data
        )

        st.success(res.json())