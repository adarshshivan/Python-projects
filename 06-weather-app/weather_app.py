import requests
import tkinter as tk
from tkinter import messagebox

# -------- Replace this with your API key --------
API_KEY = "47a8487d0a09d119d3391b19e82b9fa7"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name!")
        return

    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        result_label.config(
            text=f"🌡 Temperature: {temp}°C\n☁️ Condition: {weather}\n💧 Humidity: {humidity}%"
        )
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch data. Check your connection.")

# ------------------ UI ------------------
root = tk.Tk()
root.title("🌦 Weather App")
root.geometry("350x350")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text="Weather App", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

city_entry = tk.Entry(root, width=25, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0", justify="center")
result_label.pack(pady=20)

root.mainloop()
