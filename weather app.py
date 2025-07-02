import tkinter as tk
import requests

API_KEY = "fe92e330ca0cfc872187847318fac7fb"

def get_weather():
    city_name = city_entry.get().strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            pressure = data["main"]["pressure"]
            description = data["weather"][0]["description"]

            # استخراج كمية المطر لو موجودة
            rain_volume = data.get("rain", {}).get("1h", 0)

            # تحويلها لنسبة تقريبية (افتراضية)
            if rain_volume == 0:
                precipitation_percent = 0
            elif rain_volume < 1:
                precipitation_percent = 20
            elif rain_volume < 2:
                precipitation_percent = 40
            elif rain_volume < 3:
                precipitation_percent = 60
            else:
                precipitation_percent = 80

            # عرض البيانات
            temperature_label.config(text=f"Temperature: {temp}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_label.config(text=f"Wind Speed: {wind} km/h")
            pressure_label.config(text=f"Pressure: {pressure} hPa")
            precipitation_label.config(text=f"Precipitation: {precipitation_percent}%")

        else:
            temperature_label.config(text="City not found.")
            humidity_label.config(text="")
            wind_label.config(text="")
            pressure_label.config(text="")
            precipitation_label.config(text="")
    
    except Exception as e:
        temperature_label.config(text="Error fetching data.")
        print(e)

window = tk.Tk()
window.title("Weather Forecast")
window.geometry("500x400")  

FONT = ("Arial", 14)

tk.Label(window, text="Location:", font=FONT).grid(row=0, column=0, padx=10, pady=20, sticky="e")
city_entry = tk.Entry(window, font=FONT, width=25)
city_entry.grid(row=0, column=1, padx=10, pady=20)

search_button = tk.Button(window, text="Search", font=FONT, command=get_weather)
search_button.grid(row=0, column=2, padx=10, pady=20)

temperature_label = tk.Label(window, text="Temperature: --°C", font=FONT)
temperature_label.grid(row=1, column=0, columnspan=3, sticky="w", padx=20, pady=10)

humidity_label = tk.Label(window, text="Humidity: --%", font=FONT)
humidity_label.grid(row=2, column=0, columnspan=3, sticky="w", padx=20, pady=10)

wind_label = tk.Label(window, text="Wind Speed: --km/h", font=FONT)
wind_label.grid(row=3, column=0, columnspan=3, sticky="w", padx=20, pady=10)

pressure_label = tk.Label(window, text="Pressure: --hPa", font=FONT)
pressure_label.grid(row=4, column=0, columnspan=3, sticky="w", padx=20, pady=10)

precipitation_label = tk.Label(window, text="Precipitation: --%", font=FONT)
precipitation_label.grid(row=5, column=0, columnspan=3, sticky="w", padx=20, pady=10)

window.mainloop()
