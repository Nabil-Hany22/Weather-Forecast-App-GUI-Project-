import tkinter as tk
from tkinter import PhotoImage
import requests
from datetime import datetime
from io import BytesIO
from PIL import Image, ImageTk

API_KEY = "fe92e330ca0cfc872187847318fac7fb"

# الوضع الحالي
is_dark = True

# ثيمات
THEMES = {
    "dark": {
        "bg": "#1e1e1e",
        "fg": "#ffffff",
        "btn_bg": "#3c3f41",
        "btn_fg": "#ffffff",
    },
    "light": {
        "bg": "#ffffff",
        "fg": "#000000",
        "btn_bg": "#dddddd",
        "btn_fg": "#000000",
    }
}

FONT = ("Segoe UI", 12)

def get_theme():
    return THEMES["dark"] if is_dark else THEMES["light"]

def apply_theme():
    theme = get_theme()
    window.configure(bg=theme["bg"])
    top_frame.configure(bg=theme["bg"])
    result_frame.configure(bg=theme["bg"])
    mode_button.configure(bg=theme["btn_bg"], fg=theme["btn_fg"])

    # تحديث كل الليبلز
    for label in all_labels:
        label.configure(bg=theme["bg"], fg=theme["fg"])

def toggle_mode():
    global is_dark
    is_dark = not is_dark
    apply_theme()
    mode_button.config(text="Switch to Dark Mode" if not is_dark else "Switch to Light Mode")

def get_weather():
    city_name = city_entry.get().strip()
    current_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric"

    try:
        current_response = requests.get(current_url)
        forecast_response = requests.get(forecast_url)

        current_data = current_response.json()
        forecast_data = forecast_response.json()

        if current_data["cod"] == 200 and forecast_data["cod"] == "200":
            temp = current_data["main"]["temp"]
            humidity = current_data["main"]["humidity"]
            wind = current_data["wind"]["speed"]
            pressure = current_data["main"]["pressure"]
            description = current_data["weather"][0]["description"]
            icon_code = current_data["weather"][0]["icon"]

            # تحميل أيقونة الطقس
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            icon_response = requests.get(icon_url)
            img_data = Image.open(BytesIO(icon_response.content))
            img_resized = img_data.resize((70, 70))
            icon_image = ImageTk.PhotoImage(img_resized)
            weather_icon.config(image=icon_image)
            weather_icon.image = icon_image

            # نسبة سقوط المطر
            pop = forecast_data["list"][0].get("pop", 0)
            precipitation_percent = int(pop * 100)

            now = datetime.now().strftime("%Y-%m-%d  %I:%M %p")
            time_label.config(text=f"Updated: {now}")
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
    time_label.config(text="")
    weather_icon.config(image="")

# 🪟 النافذة
window = tk.Tk()
window.title("Weather Forecast")
window.geometry("600x520")

# 🔼 زر التبديل بين الوضعين
mode_button = tk.Button(window, text="Switch to Light Mode", font=FONT, command=toggle_mode)
mode_button.pack(pady=5)

# 🔍 شريط البحث
top_frame = tk.Frame(window)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Location:", font=FONT).pack(side="left", padx=5)
city_entry = tk.Entry(top_frame, font=FONT, width=25)
city_entry.pack(side="left", padx=5)

search_button = tk.Button(top_frame, text="Search", font=FONT, command=get_weather)
search_button.pack(side="left", padx=5)

# 🧾 عرض البيانات
result_frame = tk.Frame(window)
result_frame.pack(pady=10, anchor="w", padx=30)

time_label = tk.Label(result_frame, text="Updated: --", font=FONT)
temperature_label = tk.Label(result_frame, text="Temperature: --°C", font=FONT)
humidity_label = tk.Label(result_frame, text="Humidity: --%", font=FONT)
wind_label = tk.Label(result_frame, text="Wind Speed: -- km/h", font=FONT)
pressure_label = tk.Label(result_frame, text="Pressure: -- hPa", font=FONT)
condition_label = tk.Label(result_frame, text="Condition: --", font=FONT)
precipitation_label = tk.Label(result_frame, text="Precipitation: --%", font=FONT)

# ترتيب الليبلز
all_labels = [
    time_label, temperature_label, humidity_label, wind_label,
    pressure_label, condition_label, precipitation_label
]

for label in all_labels:
    label.pack(anchor="w", pady=4)

# 🌤️ أيقونة الطقس
weather_icon = tk.Label(window)
weather_icon.pack(pady=10)

# تطبيق الثيم الحالي
apply_theme()

window.mainloop()
