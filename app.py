import tkinter as tk
from tkinter import messagebox
import pygame

# Inicializa pygame para reproducir sonidos
pygame.mixer.init()

# Función para reproducir un sonido
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)  # Reproducir en bucle

# Función para detener el sonido
def stop_sound():
    pygame.mixer.music.stop()

# Crear la ventana principal
root = tk.Tk()
root.title("Ambiente Relajante")

# Configuración de la interfaz minimalista
root.geometry("1000x375")
root.configure(bg="white")

# Crear un frame para los botones
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

# Botones para reproducir diferentes sonidos
button1 = tk.Button(button_frame, text="Sonido de Lluvia", command=lambda: play_sound("rain_sound.mp3"))
button1.pack(side=tk.LEFT, padx=10)

button2 = tk.Button(button_frame, text="Sonido de Bosque", command=lambda: play_sound("forest_sound.mp3"))
button2.pack(side=tk.LEFT, padx=10)

button3 = tk.Button(button_frame, text="Sonido de Mar", command=lambda: play_sound("ocean_sound.mp3"))
button3.pack(side=tk.LEFT, padx=10)

button4 = tk.Button(button_frame, text="Detener Sonido", command=stop_sound)
button4.pack(side=tk.LEFT, padx=10)

# Ejecutar la aplicación
root.mainloop()