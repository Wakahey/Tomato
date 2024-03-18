import tkinter as tk
from tkinter import ttk
from webcam import Box
import cv2
import imutils

class ProductionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Система технического зрения для выявления ")

        # Создание фрейма для кнопок
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        # Создание кнопок
        self.start_button = ttk.Button(self.button_frame, text="Старт", command=self.start_video)
        self.start_button.pack(side='left', padx=10, pady=5)

        self.pause_button = ttk.Button(self.button_frame, text="Пауза", command=self.pause_video)
        self.pause_button.pack(side='left', padx=10, pady=5)

        self.stop_button = ttk.Button(self.button_frame, text="Стоп", command=self.stop_video)
        self.stop_button.pack(side='left', padx=10, pady=5)

        # Создание видеоэлемента
        self.video = Box(root, width=800, height=600)

        # Переменная для хранения состояния видео
        self.is_playing = False

        # Задание размера окна
        self.root.geometry("1500x900")

    def start_video(self):
        # Начать воспроизведение видео
        self.video.start()
        self.is_playing = True

    def pause_video(self):
        # Приостановить воспроизведение видео
        self.video.set_paused()
        self.is_playing = False

    def stop_video(self):
        # Остановить воспроизведение видео
        self.video.stop()
        self.is_playing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductionGUI(root)
    root.mainloop()
