import tkinter as tk
import requests

API_KEY = "fe92e330ca0cfc872187847318fac7fb"

# الألوان والخط
BG_COLOR = "#e0f7fa"
TEXT_COLOR = "#004d40"
BTN_COLOR = "#00796b"
BTN_TEXT = "#ffffff"
FONT = ("Segoe UI", 12)

def get_weather():
    city_name = city_entry.get().strip()
    
    # طلب حالة الطقس الحالية
    current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric"

    try:
        current_response = requests.get(current_url)
        forecast_response = requests.get(forecast_url)

        current_data = current_response.json()
        forecast_data = forecast_response.json()

        if current_data["cod"] == 200 and forecast_data["cod"] == "200":
            # current weather
            temp = current_data["main"]["temp"]
            humidity = current_data["main"]["humidity"]
            wind = current_data["wind"]["speed"]
            pressure = current_data["main"]["pressure"]
            description = current_data["weather"][0]["description"]

            # precipitation probability from forecast
            pop = forecast_data["list"][0].get("pop", 0)  # probability of precipitation
            precipitation_percent = int(pop * 100)

            # تحديث الواجهة
            temperature_label.config(text=f"Temperature: {temp}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_label.config(text=f"Wind Speed: {wind} km/h")
            pressure_label.config(text=f"Pressure: {pressure} hPa")
            condition_label.config(text=f"Condition: {description.capitalize()}")
            precipitation_label.config(text=f"Precipitation: {precipitation_percent}%")
        else:
            show_error("City not found.")
    except Exception as e:
        show_error("Error fetching data.")
        print(e)

def show_error(message):
    temperature_label.config(text=message)
    humidity_label.config(text="")
    wind_label.config(text="")
    pressure_label.config(text="")
    condition_label.config(text="")
    precipitation_label.config(text="")

# النافذة
window = tk.Tk()
window.title("Weather Forecast")
window.geometry("550x430")
window.configure(bg=BG_COLOR)

# إدخال المدينة
top_frame = tk.Frame(window, bg=BG_COLOR)
top_frame.pack(pady=20)

tk.Label(top_frame, text="Location:", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR).pack(side="left", padx=5)
city_entry = tk.Entry(top_frame, font=FONT, width=25)
city_entry.pack(side="left", padx=5)

search_button = tk.Button(top_frame, text="Search", font=FONT, bg=BTN_COLOR, fg=BTN_TEXT, command=get_weather)
search_button.pack(side="left", padx=5)

# عرض البيانات
result_frame = tk.Frame(window, bg=BG_COLOR)
result_frame.pack(pady=10, anchor="w", padx=30)

temperature_label = tk.Label(result_frame, text="Temperature: --°C", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR)
temperature_label.pack(anchor="w", pady=5)

humidity_label = tk.Label(result_frame, text="Humidity: --%", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR)
humidity_label.pack(anchor="w", pady=5)

wind_label = tk.Label(result_frame, text="Wind Speed: -- km/h", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR)
wind_label.pack(anchor="w", pady=5)

pressure_label = tk.Label(result_frame, text="Pressure: -- hPa", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR)
pressure_label.pack(anchor="w", pady=5)

condition_label = tk.Label(result_frame, text="Condition: --", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR)
condition_label.pack(anchor="w", pady=5)

precipitation_label = tk.Label(result_frame, text="Precipitation: --%", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR)
precipitation_label.pack(anchor="w", pady=5)

window.mainloop()
