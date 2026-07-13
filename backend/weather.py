import requests

API_KEY = "285415dfa6b7b052790891a23cfa86fb"

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if "main" not in data:
        return {"error": "City not found"}

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    if temperature > 35:
        advice = "High temperature. Irrigate crops properly."
    elif humidity > 80:
        advice = "High humidity. Risk of fungal diseases."
    else:
        advice = "Weather looks good for farming."

    return {
        "temperature": temperature,
        "humidity": humidity,
        "advice": advice
    }