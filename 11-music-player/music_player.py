import tkinter as tk
from tkinter import filedialog, messagebox, Listbox
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Create main window
root = tk.Tk()
root.title("🎵 Music Player App")
root.geometry("500x400")
root.resizable(False, False)

# Global variables
playlist = []
current_song = ""
paused = False

# Functions
def load_songs():
    global playlist
    files = filedialog.askopenfilenames(
        title="Select Songs", 
        filetypes=(("MP3 Files", "*.mp3"), ("All Files", "*.*"))
    )
    if files:
        for file in files:
            playlist.append(file)
            song_list.insert(tk.END, os.path.basename(file))

def play_song():
    global current_song, paused
    try:
        selected = song_list.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a song to play.")
            return
        song_index = selected[0]
        current_song = playlist[song_index]
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
        paused = False
        now_playing_label.config(text=f"Now Playing: {os.path.basename(current_song)} 🎶")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def pause_song():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True
    else:
        pygame.mixer.music.unpause()
        paused = False

def stop_song():
    pygame.mixer.music.stop()
    now_playing_label.config(text="Stopped")

def clear_playlist():
    global playlist
    playlist = []
    song_list.delete(0, tk.END)
    pygame.mixer.music.stop()
    now_playing_label.config(text="Playlist Cleared")

# UI Setup
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=10)

song_list = Listbox(frame, bg="white", width=60, height=10, selectbackground="lightgreen")
song_list.pack()

now_playing_label = tk.Label(root, text="No song playing", font=("Arial", 12))
now_playing_label.pack(pady=10)

# Control buttons
controls_frame = tk.Frame(root)
controls_frame.pack(pady=10)

btn_load = tk.Button(controls_frame, text="Load Songs", command=load_songs, width=12)
btn_play = tk.Button(controls_frame, text="Play", command=play_song, width=12)
btn_pause = tk.Button(controls_frame, text="Pause/Resume", command=pause_song, width=12)
btn_stop = tk.Button(controls_frame, text="Stop", command=stop_song, width=12)
btn_clear = tk.Button(controls_frame, text="Clear Playlist", command=clear_playlist, width=12)

btn_load.grid(row=0, column=0, padx=5)
btn_play.grid(row=0, column=1, padx=5)
btn_pause.grid(row=0, column=2, padx=5)
btn_stop.grid(row=1, column=0, padx=5, pady=5)
btn_clear.grid(row=1, column=1, padx=5, pady=5)

# Run the GUI
root.mainloop()
