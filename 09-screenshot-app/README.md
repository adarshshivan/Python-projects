# Screenshot App

## Overview
The Screenshot App is a simple Python GUI tool that allows you to take screenshots easily.  
It provides two options — capturing the **entire screen** or **selecting a specific region**.  
Screenshots are automatically saved with timestamps for easy organization.  

This project uses **Tkinter** for the graphical interface, **PyAutoGUI** for screen capturing, and **Pillow** for image processing.

---

## Features
- 📷 **Full Screen Capture** — Captures the entire display with one click.
- ✂️ **Region Capture** — Lets you select a specific part of the screen to capture.
- 💾 **Auto Save** — Saves every screenshot with a unique timestamp in the `screenshots/` folder.
- 🪟 **User-Friendly GUI** — Clean and simple Tkinter interface.

---

## How to Run

```bash
cd 09-screenshot-app
python screenshot_app.py
```

Once the app window opens, choose one of the following options:

📷 Capture Full Screen
→ Takes a screenshot of your entire screen and saves it in the screenshots/ folder.

✂️ Capture Selected Region
→ Allows you to drag and select a specific area of your screen to capture.

Requirements

Make sure you have the following installed:

Python 3.x

Pillow

PyAutoGUI

Tkinter (comes preinstalled with Python)

Learning Highlights

Building simple GUIs with Tkinter.

Using PyAutoGUI to capture screens and automate tasks.

Working with Pillow (PIL) for image saving and manipulation.

Handling file saving and timestamps in Python.