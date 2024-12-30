import tkinter as tk
from tkinter import messagebox
import pygame
from PIL import Image, ImageTk

pygame.mixer.init()

def play_sound(sound_file):
    click_sound = "assets/sounds/click.mp3"
    pygame.mixer.music.load(click_sound)
    pygame.mixer.music.play()
    pygame.time.wait(300)
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)

def stop_sound():
    pygame.mixer.music.stop()

root = tk.Tk()
root.title("Ambient House")

root.geometry("1200x575")
root.configure(bg="white")

icon_image = tk.PhotoImage(file="assets/icon.png")
root.iconphoto(False, icon_image)

button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10, expand=True)

def resize_image(image_path, size=(100, 100)):
    image = Image.open(image_path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)

rain_image = tk.PhotoImage(file="assets/buttons/rain.png")
fire_image = tk.PhotoImage(file="assets/buttons/fire.png")
noise_image = tk.PhotoImage(file="assets/buttons/noise.png")
ocean_image = tk.PhotoImage(file="assets/buttons/ocean.png")
jazz_image = tk.PhotoImage(file="assets/buttons/jazz.png")

button1 = tk.Button(button_frame, image=rain_image, command=lambda: play_sound("assets/sounds/rain.mp3"), bg="white", borderwidth=0)
button1.pack(side=tk.LEFT, padx=10)

button2 = tk.Button(button_frame, image=fire_image, command=lambda: play_sound("assets/sounds/fireplace.mp3"), bg="white", borderwidth=0)
button2.pack(side=tk.LEFT, padx=10)

button3 = tk.Button(button_frame, image=noise_image, command=lambda: play_sound("assets/sounds/noise.mp3"), bg="white", borderwidth=0)
button3.pack(side=tk.LEFT, padx=10)

button4 = tk.Button(button_frame, image=ocean_image, command=lambda: play_sound("assets/sounds/ocean.mp3"), bg="white", borderwidth=0)
button4.pack(side=tk.LEFT, padx=10)

button5 = tk.Button(button_frame, image=jazz_image, command=lambda: play_sound("assets/sounds/jazz.mp3"), bg="white", borderwidth=0)
button5.pack(side=tk.LEFT, padx=10)

root.mainloop()