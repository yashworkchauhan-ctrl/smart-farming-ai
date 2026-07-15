# 🌱 Smart Farming AI Platform

An AI-powered Smart Farming Platform developed as a Final Year Project to help farmers make better decisions using Machine Learning, Artificial Intelligence, Weather Analysis, and Crop Prediction.

---

## 📌 Project Overview

Smart Farming AI Platform is an intelligent agriculture application that provides AI-based recommendations for farmers. The system predicts the best crop, recommends fertilizer, detects plant diseases from images, predicts crop yield, provides weather information, and allows users to interact with an AI assistant.

The main objective of this project is to improve farming decisions using Artificial Intelligence and Machine Learning.

---

# 🎯 Objectives

- Help farmers choose the best crop.
- Recommend suitable fertilizers.
- Detect plant diseases using AI.
- Predict crop yield.
- Provide weather information.
- Store prediction history.
- Offer AI-based farming assistance.

---

# ✨ Features

## 🔐 User Authentication
- User Login
- User Signup
- Secure Authentication

---

## 🌾 Crop Recommendation
Predicts the most suitable crop based on:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- pH Value
- Rainfall

---

## 🌱 Fertilizer Recommendation

Suggests the best fertilizer using:

- Soil Nutrients
- Soil Type
- Temperature
- Moisture
- Crop Type

---

## 🍃 Plant Disease Detection

Detects diseases from uploaded plant leaf images using Deep Learning.

Supported Plants:

- Tomato
- Potato
- Pepper Bell

---

## 🌦 Weather Information

Displays:

- Temperature
- Humidity
- Weather Condition

Provides weather details useful for farming decisions.

---

## 📈 Crop Yield Prediction

Predicts expected crop production using Machine Learning.

Inputs include:

- Rainfall
- Temperature
- Fertilizer

---

## 🤖 AI Farming Assistant

Users can ask agriculture-related questions using Google's Gemini AI.

Examples:

- Best fertilizer for wheat
- Tomato disease treatment
- Organic farming
- Irrigation suggestions

---

## 📊 Dashboard

Displays:

- Total Predictions
- Crop Predictions
- Fertilizer Recommendations
- AI Chats
- Prediction History

---

## 💾 Database

SQLite Database is used to store:

- User Information
- Login Details
- Prediction History
- AI Chat History

---

# 🧠 Machine Learning Models

The project uses multiple Machine Learning models.

| Module | Model |
|---------|-------|
| Crop Recommendation | Random Forest |
| Fertilizer Recommendation | Random Forest |
| Yield Prediction | Regression Model |
| Disease Detection | TensorFlow CNN |

---

# 🛠 Technologies Used

## Programming Language

- Python

---

## Frontend

- Streamlit

---

## Backend

- FastAPI

---

## Machine Learning

- Scikit-Learn
- TensorFlow
- NumPy
- Pandas

---

## Database

- SQLite

---

## AI

- Google Gemini API

---

## Image Processing

- Pillow (PIL)

---

## APIs

- Weather API
- Gemini API

---

# 📂 Project Structure

```
Smart-Farming-AI
│
├── backend
│   ├── app.py
│   ├── weather.py
│   ├── disease_api.py
│   ├── yield_api.py
│
├── frontend
│   ├── app.py
│   ├── dashboard.py
│   ├── yield_ui.py
│
├── models
│   ├── crop_model.pkl
│   ├── fertilizer_model.pkl
│   ├── yield_model.pkl
│   └── plant_disease_model.h5
│
├── dataset
│
├── requirements.txt
│
└── README.md
```

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/yashworkchauhan-ctrl/smart-farming-ai.git
```

Go to project

```bash
cd smart-farming-ai
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Install Requirements

```bash
pip install -r requirements.txt
```

Run Backend

```bash
uvicorn backend.app:app --reload
```

Run Frontend

```bash
streamlit run frontend/app.py
```

---

# 📸 Screenshots

### Login Page

(Add Screenshot)
<img width="1917" height="867" alt="Screenshot 2026-07-15 153122" src="https://github.com/user-attachments/assets/0441d8e1-ec30-453d-83b4-a97eef5556fb" />

---

### Dashboard
<img width="1917" height="857" alt="image" src="https://github.com/user-attachments/assets/1d09ea04-8202-4195-a4c5-376fa5d77814" />

(Add Screenshot)

---

### Crop Recommendation

(Add Screenshot)

---<img width="1917" height="877" alt="image" src="https://github.com/user-attachments/assets/8f998795-98d7-4dc3-a4e6-a5ead7c9940b" />


### Fertilizer Recommendation

(Add Screenshot)
<img width="1916" height="875" alt="image" src="https://github.com/user-attachments/assets/948f3b8b-5915-48fc-85cc-49d65d271b75" />

---

### Disease Detection

(Add Screenshot)

---<img width="1917" height="855" alt="image" src="https://github.com/user-attachments/assets/54726551-fce0-40f1-859c-fd24406bcc1d" />


### Weather Module

(Add Screenshot)
<img width="1917" height="871" alt="image" src="https://github.com/user-attachments/assets/16b8c643-91d9-4421-8c01-e9c724e67496" />

---

### Yield Prediction

(Add Screenshot)
<img width="1917" height="871" alt="image" src="https://github.com/user-attachments/assets/9d3795f3-a27d-41a7-8e40-e39a02442afa" />

---

# 🚀 Future Scope

- Live Satellite Monitoring
- IoT Sensor Integration
- Drone Monitoring
- Voice Assistant
- Multi-language Support
- Mobile Application
- Cloud Deployment
- SMS Alerts
- Real-time Weather API
- Advanced Deep Learning Models

---

# 📈 Advantages

- Easy to Use
- AI-Based Recommendations
- Fast Prediction
- User Friendly Interface
- Secure Login System
- Stores Prediction History
- Helps Farmers Make Better Decisions

---

# 👨‍💻 Author

**Yash Chauhan**

B.Tech Final Year

Smart Farming AI Platform

---

# ⭐ GitHub

If you like this project, please give it a ⭐ on GitHub.
