import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("OPENWEATHER_API_KEY")

AQI_LABELS = {
    1: ("Good", "#28a745"),
    2: ("Fair", "#7cb342"),
    3: ("Moderate", "#ffb300"),
    4: ("Poor", "#f4511e"),
    5: ("Very Poor", "#b71c1c"),
}

# Weather condition wallpapers from Unsplash
WEATHER_BACKGROUNDS = {
    "Clear": "https://images.unsplash.com/photo-1601297183305-6df142704ea2?auto=format&fit=crop&w=1920&q=80",
    "Clouds": "https://images.unsplash.com/photo-1534088568595-a066f410bcda?auto=format&fit=crop&w=1920&q=80",
    "Rain": "https://images.unsplash.com/photo-1519692933481-e162a57d6721?auto=format&fit=crop&w=1920&q=80",
    "Drizzle": "https://images.unsplash.com/photo-1541919329513-35f7af297129?auto=format&fit=crop&w=1920&q=80",
    "Thunderstorm": "https://images.unsplash.com/photo-1605721911519-3dfeb3be25e7?auto=format&fit=crop&w=1920&q=80",
    "Snow": "https://images.unsplash.com/photo-1491002052546-bf38f186af56?auto=format&fit=crop&w=1920&q=80",
    "Mist": "https://images.unsplash.com/photo-1487621167305-5d248087c724?auto=format&fit=crop&w=1920&q=80",
    "Fog": "https://images.unsplash.com/photo-1487621167305-5d248087c724?auto=format&fit=crop&w=1920&q=80",
    "Haze": "https://images.unsplash.com/photo-1522163182402-834f871fd851?auto=format&fit=crop&w=1920&q=80",
}

DEFAULT_BG = "https://images.unsplash.com/photo-1477959858617-67f30bc75b82?auto=format&fit=crop&w=1920&q=80"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    aqi_data = None
    error_message = None
    bg_image_url = DEFAULT_BG

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        lat = request.form.get("lat", "").strip()
        lon = request.form.get("lon", "").strip()

        # Build weather request based on city input or GPS coordinates
        if lat and lon:
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        elif city:
            weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        else:
            error_message = "Please enter a city name or use your current location."
            return render_template("index.html", error=error_message, bg_image_url=bg_image_url)

        try:
            weather_res = requests.get(weather_url, timeout=10).json()

            if weather_res.get("cod") != 200:
                error_message = weather_res.get("message", "City not found. Please try again.").capitalize()
            else:
                resolved_lat = weather_res["coord"]["lat"]
                resolved_lon = weather_res["coord"]["lon"]
                main_condition = weather_res["weather"][0]["main"]
                bg_image_url = WEATHER_BACKGROUNDS.get(main_condition, DEFAULT_BG)

                weather_data = {
                    "city": weather_res["name"],
                    "country": weather_res["sys"]["country"],
                    "temp": round(weather_res["main"]["temp"], 1),
                    "feels_like": round(weather_res["main"]["feels_like"], 1),
                    "humidity": weather_res["main"]["humidity"],
                    "wind_speed": weather_res["wind"]["speed"],
                    "description": weather_res["weather"][0]["description"].title(),
                    "condition": main_condition,
                }

                # Fetch Air Quality Index using resolved latitude & longitude
                aqi_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={resolved_lat}&lon={resolved_lon}&appid={API_KEY}"
                aqi_res = requests.get(aqi_url, timeout=10).json()

                if "list" in aqi_res and len(aqi_res["list"]) > 0:
                    raw_aqi = aqi_res["list"][0]["main"]["aqi"]
                    components = aqi_res["list"][0]["components"]
                    label, color = AQI_LABELS.get(raw_aqi, ("Unknown", "#757575"))

                    aqi_data = {
                        "index": raw_aqi,
                        "label": label,
                        "color": color,
                        "pm2_5": components.get("pm2_5", "N/A"),
                        "pm10": components.get("pm10", "N/A"),
                    }

        except requests.exceptions.RequestException:
            error_message = "Failed to connect to weather service. Please check your network."

    return render_template(
        "index.html",
        weather=weather_data,
        aqi=aqi_data,
        error=error_message,
        bg_image_url=bg_image_url
    )

if __name__ == "__main__":
    app.run(debug=True)