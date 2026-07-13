import streamlit as st
import sqlite3
import random
import google.generativeai as genai
import os

# ================== API KEY ==================
GOOGLE_API_KEY = "AIzaSyDsCAsjMPuIvhVTYyB-riXlVRGN3Fk24C0"

genai.configure(api_key=GOOGLE_API_KEY)

# 🔥 FIXED MODEL
model = genai.GenerativeModel("gemini-pro")

# ================= DB =================
conn = sqlite3.connect("app.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    type TEXT,
    input TEXT,
    result TEXT
)
""")

conn.commit()

# ================= FUNCTIONS =================
def save_history(user, type_, inp, result):
    c.execute("INSERT INTO history (username,type,input,result) VALUES (?,?,?,?)",
              (user, type_, str(inp), str(result)))
    conn.commit()

def get_history(user):
    c.execute("SELECT * FROM history WHERE username=?", (user,))
    return c.fetchall()

def get_counts(user):
    c.execute("SELECT COUNT(*) FROM history WHERE username=?", (user,))
    total = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM history WHERE username=? AND type='crop'", (user,))
    crop = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM history WHERE username=? AND type='fertilizer'", (user,))
    fert = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM history WHERE username=? AND type='chatbot'", (user,))
    chat = c.fetchone()[0]

    return total, crop, fert, chat

# ================= UI =================
st.set_page_config(page_title="Smart Farming AI", layout="wide")

if "user" not in st.session_state:
    st.session_state.user = None

# ================= AUTH =================
if st.session_state.user is None:

    st.title("🔐 Login / Signup")

    option = st.selectbox("Choose", ["Login", "Signup"])

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if option == "Signup":
        if st.button("Create Account"):
            try:
                c.execute("INSERT INTO users (username,password) VALUES (?,?)", (user,pwd))
                conn.commit()
                st.success("Account Created!")
            except:
                st.error("User already exists")

    if option == "Login":
        if st.button("Login"):
            c.execute("SELECT * FROM users WHERE username=? AND password=?", (user,pwd))
            if c.fetchone():
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Invalid credentials")

# ================= MAIN =================
else:
    st.sidebar.success(f"👤 {st.session_state.user}")

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()

    feature = st.sidebar.selectbox("Select Feature", [
        "Dashboard",
        "Crop Recommendation",
        "Fertilizer Recommendation",
        "Disease Detection",
        "Weather",
        "Yield Prediction",
        "AI Chatbot",
        "History"
    ])

    st.title("🌾 Smart Farming AI Platform")

    # ===== DASHBOARD =====
    if feature == "Dashboard":
        total, crop, fert, chat = get_counts(st.session_state.user)

        col1,col2,col3,col4 = st.columns(4)
        col1.metric("Total", total)
        col2.metric("Crop", crop)
        col3.metric("Fertilizer", fert)
        col4.metric("AI Chats", chat)

    # ===== CROP =====
    elif feature == "Crop Recommendation":
        st.header("🌱 Crop Recommendation")

        N = st.number_input("Nitrogen")
        P = st.number_input("Phosphorus")
        K = st.number_input("Potassium")

        if st.button("Predict Crop"):
            result = random.choice(["Rice","Wheat","Maize","Cotton"])
            st.success(result)
            save_history(st.session_state.user,"crop",[N,P,K],result)

    # ===== FERTILIZER =====
    elif feature == "Fertilizer Recommendation":
        st.header("🧪 Fertilizer")

        N = st.number_input("N ")
        P = st.number_input("P ")
        K = st.number_input("K ")

        if st.button("Recommend"):
            result = random.choice(["Urea","DAP","Potash"])
            st.success(result)
            save_history(st.session_state.user,"fertilizer",[N,P,K],result)

    # ===== DISEASE =====
    elif feature == "Disease Detection":
        st.header("🍃 Disease Detection")

        file = st.file_uploader("Upload leaf image")

        if file:
            result = random.choice(["Healthy","Rust","Blight"])
            st.success(result)
            save_history(st.session_state.user,"disease","image",result)

    # ===== WEATHER =====
    elif feature == "Weather":
        st.header("🌦 Weather")

        city = st.text_input("City")

        if st.button("Get Weather"):
            result = f"{random.randint(20,40)}°C, Humidity {random.randint(40,90)}%"
            st.success(result)
            save_history(st.session_state.user,"weather",city,result)

    # ===== YIELD =====
    elif feature == "Yield Prediction":
        st.header("📈 Yield Prediction")

        rain = st.number_input("Rainfall")
        temp = st.number_input("Temperature")
        fert = st.number_input("Fertilizer")

        if st.button("Predict Yield"):
            result = round(rain*0.02 + temp*0.03 + fert*0.05,2)
            st.success(f"{result} tons/hectare")
            save_history(st.session_state.user,"yield",[rain,temp,fert],result)

    # ===== CHATBOT (GEMINI) =====
    elif feature == "AI Chatbot":
         st.header("🤖 Gemini AI Chatbot")

         q = st.text_input("Ask about farming")

    if st.button("Ask AI"):
        try:
            model = genai.GenerativeModel("gemini-pro")  # ✅ FIXED

            response = model.generate_content(q)

            if response and response.text:
                st.success(response.text)
                save_history(st.session_state.user, "chatbot", q, response.text)
            else:
                st.warning("No response")

        except Exception as e:
            st.error(f"Error: {e}")

    # ===== HISTORY =====
    elif feature == "History":
        st.header("📜 History")

        data = get_history(st.session_state.user)

        if len(data)==0:
            st.warning("No history yet")
        else:
            for d in data[::-1]:
                st.write(f"Type: {d[2]}")
                st.write(f"Input: {d[3]}")
                st.write(f"Result: {d[4]}")
                st.markdown("---")