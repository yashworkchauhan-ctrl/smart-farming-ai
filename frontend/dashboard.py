import streamlit as st
import pandas as pd

def dashboard():

    st.title("🌾 Farmer Dashboard")

    col1,col2,col3 = st.columns(3)

    col1.metric("Crop Predictions","120")
    col2.metric("Disease Scans","85")
    col3.metric("Weather Requests","64")

    data = pd.DataFrame({
        "Crop":["Rice","Wheat","Maize"],
        "Yield":[4.5,3.2,2.8]
    })

    st.bar_chart(data.set_index("Crop"))