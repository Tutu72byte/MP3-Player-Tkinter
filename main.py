import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MP3Player:
    def __init__(self, root):
        self.root = root
        self.root.title("Python MP3 Player Tutuianu Ionescu")
        self.root.geometry("450x300")
        self.root.configure(bg="#f8f9fa")

        pygame.mixer.init()

        #Titlu 
        self.track_name = tk.StringVar(value="Nicio piesă selectata")
        tk.Label(root, textvariable=self.track_name, font=("Comic Sans MS", 11, "italic"), bg="#f8f9fa").pack(pady = 30)

        # Butoane
        btn_frame = tk.Frame(root, bg="#f8f9fa")
        btn_frame.pack()

        tk.Button(btn_frame, text="Load MP3", command=self.load_music, width=8).grid(row=0, column=0, pady=10)
        tk.Button(btn_frame, text="Play", command=self.play_music, width=8).grid(row=0, column=1, pady=10)
        tk.Button(btn_frame, text="Pause", command=self.pause_music, width=8).grid(row=0, column=2, pady=10)
        tk.Button(btn_frame, text="Stop", command=self.stop_music, width=8).grid(row=0, column=3, pady=10)

        # Slider Volum
        vol_frame = tk.Frame(root, bg="#f8f9fa")
        vol_frame.pack(pady=30)
        tk.Label(vol_frame, text="Volum:", bg="#f8f9fa").pack(side=tk.LEFT, padx=5)
        
        self.volume_slider = tk.Scale(vol_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume, bg="#f8f9fa", length=200)
        self.volume_slider.set(70) # Volum inițial la 70%
        pygame.mixer.music.set_volume(0.7)
        self.volume_slider.pack(side=tk.LEFT)

    def load_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fisiere MP3", "*.mp3")])
        if file_path:
            pygame.mixer.music.load(file_path)
            self.track_name.set(os.path.basename(file_path))

    def play_music(self):
        pygame.mixer.music.play()

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def set_volume(self, val):
        volume = float(val) / 100
        pygame.mixer.music.set_volume(volume)

# Rulare program
root = tk.Tk()
aplicatie_final = MP3Player(root)
root.mainloop()