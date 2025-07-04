# 🌦️ Weather App (Python GUI Project)

This is my **final project** required to complete the course:

🎓 **[Practical Projects using Python + ChatGPT](https://almdrasa.com/tracks/programming-foundations/courses/python-projects/)** offered by [Almdrasa](https://almdrasa.com)

By completing this project, I have successfully finished the full course with **7 useful and educational Python projects**. This specific project helped me apply what I learned in the **API lessons** and **GUI lessons** using `tkinter`.

---

## 🧠 Project Overview

This app allows users to enter any city name and view the current weather details using **real-time API data** from [OpenWeatherMap](https://openweathermap.org). It fetches:

* Temperature
* Humidity
* Wind Speed
* Pressure
* Precipitation percentage
* Condition description
* Weather icon and last updated time

The app includes both a **simple version** and an **enhanced version** with dynamic features and a dark/light theme switcher.

---

## 📂 Files in the Repository

| File                       | Description                                     |
| -------------------------- | ----------------------------------------------- |
| `weather app.py`           | Basic version with main weather logic           |
| `weather app_chatgpt.py`   | Enhanced version with icon, theme, and forecast |
| `weather app planning.jpg` | Visual planning of the app (interface layout)   |

---

## 🚀 Features Comparison

### 🔹 Basic Version – `weather app.py`

* Enter a city and get:

  * Temperature
  * Humidity
  * Wind speed
  * Pressure
  * Estimated precipitation
* Simple and clean interface using `tkinter`

---

### ⚡ Enhanced Version – `weather app_chatgpt.py`

Includes all basic features, plus:

* ✅ **Real precipitation %** using 5-day forecast API
* ✅ **Weather icon** fetched and displayed dynamically
* ✅ **Current time and date display**
* ✅ **Dark / Light mode toggle**
* ✅ **Better UI layout and design**
* ✅ **Error handling and empty states**

---

## 🎯 What I Learned

* How to consume real-world APIs and handle JSON data
* GUI layout building using `tkinter`
* How to apply conditions, calculations, and formatting
* Switching themes dynamically
* Fetching & displaying images from URLs
* Organizing projects into scalable files

---

## 🧰 Tech Stack

* `Python 3.13`
* `tkinter` for GUI
* `requests` for API calls
* `Pillow` (`PIL`) for weather icon display
* OpenWeatherMap APIs

---

## 📸 Preview

Planning board & layout idea:
`weather app planning.jpg`

---

## ✅ Run the Project

Make sure you have Python and required libraries installed, then run:

```bash
python "weather app.py"
# or
python "weather app_chatgpt.py"
```

