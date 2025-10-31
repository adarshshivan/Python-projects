import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab
import pyautogui
import os
import datetime

# Create screenshots folder if not exists
save_path = "screenshots"
os.makedirs(save_path, exist_ok=True)

# Capture full screen
def capture_full_screen():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    image = pyautogui.screenshot()
    image.save(f"{save_path}/screenshot_full_{timestamp}.png")
    messagebox.showinfo("Success", f"Full screen captured!\nSaved as screenshot_full_{timestamp}.png")

# Capture selected region
def capture_region():
    messagebox.showinfo("Info", "After clicking OK, drag to select a region of the screen.")
    root.withdraw()  # Hide the main window while selecting
    screenshot = pyautogui.screenshot(region=pyautogui.mouseInfo())
    messagebox.showinfo("Done", "Region screenshot captured!")  # Placeholder
    root.deiconify()

# Safer region capture using ImageGrab
def capture_region_advanced():
    messagebox.showinfo("Info", "After clicking OK, drag to select a region of the screen.")
    root.withdraw()

    # Use pyautogui's built-in region select tool
    region = pyautogui.screenshot(region=pyautogui.locateOnScreen(pyautogui.screenshot()))
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    image_path = f"{save_path}/screenshot_region_{timestamp}.png"
    region.save(image_path)

    messagebox.showinfo("Success", f"Region captured!\nSaved as screenshot_region_{timestamp}.png")
    root.deiconify()

# Create GUI window
root = tk.Tk()
root.title("📸 Screenshot App")
root.geometry("400x250")
root.config(bg="#f0f0f0")

label = tk.Label(root, text="Choose Screenshot Type", font=("Arial", 16, "bold"), bg="#f0f0f0")
label.pack(pady=20)

btn_full = tk.Button(root, text="📷 Capture Full Screen", font=("Arial", 12), bg="#4CAF50", fg="white", command=capture_full_screen)
btn_full.pack(pady=10, ipadx=10, ipady=5)

btn_region = tk.Button(root, text="✂️ Capture Selected Region", font=("Arial", 12), bg="#2196F3", fg="white", command=capture_region_advanced)
btn_region.pack(pady=10, ipadx=10, ipady=5)

root.mainloop()
