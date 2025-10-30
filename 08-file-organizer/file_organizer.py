import os
import shutil
from tkinter import Tk, filedialog, messagebox

# ---------------- Function to organize files ----------------
def organize_folder(folder_path):
    # Define categories and extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"],
        "Others": []
    }

    # Go through files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        moved = False

        # Match file type
        for category, extensions in file_types.items():
            if ext.lower() in extensions:
                target_folder = os.path.join(folder_path, category)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                moved = True
                break

        # If no match, move to "Others"
        if not moved:
            target_folder = os.path.join(folder_path, "Others")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))

    messagebox.showinfo("Done", "✅ Files organized successfully!")

# ---------------- Tkinter UI ----------------
def select_folder():
    folder_path = filedialog.askdirectory(title="Select a folder to organize")
    if folder_path:
        organize_folder(folder_path)

# Main window
root = Tk()
root.withdraw()  # hide the main window
messagebox.showinfo("File Organizer", "Select the folder you want to organize")
select_folder()
