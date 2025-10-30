import os

# Folder where test files will be created
test_folder = r"C:\Users\adars\OneDrive\Desktop\Python projects\08-file-organizer\TestFolder"

# Make sure the folder exists
os.makedirs(test_folder, exist_ok=True)

# File names by type
test_files = {
    "Images": ["photo1.jpg", "logo.png", "pic.gif"],
    "Documents": ["notes.txt", "resume.pdf", "report.docx", "sheet.xlsx"],
    "Videos": ["movie.mp4", "clip.mkv"],
    "Audio": ["song.mp3", "voice.wav"],
    "Archives": ["backup.zip", "project.rar"],
    "Code": ["main.py", "index.html", "style.css", "script.js"],
    "Others": ["randomfile.xyz", "datafile.unknown"]
}

# Create dummy files
for category, files in test_files.items():
    for filename in files:
        file_path = os.path.join(test_folder, filename)
        with open(file_path, "w") as f:
            f.write(f"This is a dummy {category} file named {filename}.\n")

print("✅ Test files created successfully in:", test_folder)
