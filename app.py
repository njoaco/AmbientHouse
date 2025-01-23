import tkinter as tk
from tkinter import messagebox
import pygame
from PIL import Image, ImageTk, ImageSequence

pygame.mixer.init()

# Diccionario para mantener el estado de reproducción de cada sonido
playing_sounds = {}

def play_sound(sound_file):
    if sound_file in playing_sounds and playing_sounds[sound_file]:
        stop_sound()
        playing_sounds[sound_file] = False
    else:
        click_sound = "assets/sounds/click.mp3"
        pygame.mixer.music.load(click_sound)
        pygame.mixer.music.play()
        pygame.time.wait(300)
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play(-1)
        playing_sounds[sound_file] = True

def stop_sound():
    click_sound = "assets/sounds/click.mp3"
    pygame.mixer.music.load(click_sound)
    pygame.mixer.music.stop()

root = tk.Tk()
root.title("Ambient House")

root.geometry("1200x575")
root.configure(bg="white")

icon_image = tk.PhotoImage(file="assets/icon.png")
root.iconphoto(False, icon_image)

button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10, expand=True)

def resize_image(image_path, size=(150, 150)):
    image = Image.open(image_path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)

rain_image = resize_image("assets/buttons/rain.png")
fire_image = resize_image("assets/buttons/fire.png")
noise_image = resize_image("assets/buttons/noise.png")
ocean_image = resize_image("assets/buttons/ocean.png")
jazz_image = resize_image("assets/buttons/jazz.png")

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