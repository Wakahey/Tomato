import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from webcam import WebCamera
from PIL import ImageTk, Image
import logging
import torch
from ultralytics import YOLO
class SettingsGUI:
    def __init__(self, parent):
        self.parent = parent
        self.root = tk.Toplevel(parent)
        self.root.title("Настройки")

        # Создание элементов интерфейса для выбора овощей
        self.vegetable_label = ttk.Label(self.root, text="Выберите овощи для отбраковки:")
        self.vegetable_label.pack()

        self.tomato_checkbox = ttk.Checkbutton(self.root, text="Помидоры")
        self.tomato_checkbox.pack()

        self.cucumber_checkbox = ttk.Checkbutton(self.root, text="Огурцы")
        self.cucumber_checkbox.pack()

        self.potato_checkbox = ttk.Checkbutton(self.root, text="Картошка")
        self.potato_checkbox.pack()

        self.onion_checkbox = ttk.Checkbutton(self.root, text="Лук")
        self.onion_checkbox.pack()

        self.garlic_checkbox = ttk.Checkbutton(self.root, text="Чеснок")
        self.garlic_checkbox.pack()

        self.ok_button = ttk.Button(self.root, text="Применить", command=self.apply_settings)
        self.ok_button.pack()

    def apply_settings(self):
        # Здесь можно добавить логику обработки выбранных настроек
        self.root.destroy()

class ProductionGUI:
    """
    Основной класс для работы с интерфейсом.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Система технического зрения для выявления брака у продукции")

        # # Установка изображения в качестве фона
        # self.background_image = Image.open("static/background.jpg")
        # self.background_image = self.background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()),
        #                                                      Image.LANCZOS)
        # self.background_photo = ImageTk.PhotoImage(self.background_image)
        # self.background_label = tk.Label(self.root, image=self.background_photo)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Загрузка предварительно обученной модели Pytorch YOLO


        # Создание объекта класса для работы с камерой.
        self.video = WebCamera(root, width=800, height=600,)

        # Настройка логгирования
        self.log_text = ScrolledText(self.root, width=30, height=10)
        self.log_text.pack(expand=True, fill="both")
        self.log_text.place(x=0, y=0)

        self.log_text_neural_network = ScrolledText(self.root, width=30, height=5)
        self.log_text_neural_network.pack()
        self.log_text_neural_network.place(y=350)

        # Создание фрейма для кнопок.
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        # Создание стилей для кнопок (цвет, шрифт и т.д).
        self.style = ttk.Style()
        self.style.configure(
            'Start.TButton', foreground='white',
            background='green', font=('Arial', 12, 'bold')
        )
        self.style.configure(
            'Pause.TButton', foreground='white',
            background='orange', font=('Arial', 12, 'bold')
        )
        self.style.configure(
            'Stop.TButton', foreground='white',
            background='red', font=('Arial', 12, 'bold')
        )

        # Создание кнопок
        self.start_button = ttk.Button(
            self.button_frame, text="Старт",
            command=self.start_video, style="Start.TButton"
        )
        self.start_button.pack(side='left', padx=10, pady=5)

        self.pause_button = ttk.Button(
            self.button_frame, text="Пауза",
            command=self.pause_video, style="Pause.TButton"
        )
        self.pause_button.pack(side='left', padx=10, pady=5)

        self.stop_button = ttk.Button(
            self.button_frame, text="Стоп",
            command=self.stop_video, style="Stop.TButton"
        )
        self.stop_button.pack(side='left', padx=10, pady=5)

        self.settings_frame = tk.Frame(self.root)
        self.settings_frame.pack(anchor="ne")  # Размещение фрейма в правом верхнем углу

        # Создание кнопки настроек
        self.settings_button = ttk.Button(
            self.settings_frame, text="Настройки",
            command=self.open_settings
        )
        self.settings_button.pack(side="right", padx=20,)

        # Переменная для хранения состояния видео.
        self.is_playing = False

        # Задание размера окна
        self.root.geometry("1300x900")

    def start_video(self):
        # Начать воспроизведение видео.
        self.video.start()
        self.is_playing = True
        self.log_text.insert(tk.END, "Видео начало воспроизведение\n")
        self.log_text.see(tk.END)

    def pause_video(self):
        # Приостановить воспроизведение видео.
        self.video.set_paused()
        self.is_playing = False
        self.log_text.insert(tk.END, "Видео приостановлено\n")
        self.log_text.see(tk.END)

    def stop_video(self):
        # Остановить воспроизведение видео.
        self.video.stop()
        self.is_playing = False
        self.log_text.insert(tk.END, "Видео остановлено\n")
        self.log_text.see(tk.END)

    def open_settings(self):
        # Открыть окно настроек
        settings_gui = SettingsGUI(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProductionGUI(root)
    root.mainloop()
