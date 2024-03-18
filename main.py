import tkinter as tk
from tkinter import ttk
from webcam import WebCamera

class ProductionGUI:
    """
    Основной класс для работы с интерфейсом.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Система технического зрения для выявления брака у продукции")

        # Создание объекта класса для работы с камерой.
        self.video = WebCamera(root, width=800, height=600)

        # Создание фрейма для кнопок.
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        # Создание стилей для кнопок (цвет, шрифт и т.д).
        self.style = ttk.Style()
        self.style.configure(
            'Start.TButton', foreground='black',
            background='green', font=('Arial', 12, 'bold')
        )
        self.style.configure(
            'Pause.TButton', foreground='white',
            background='orange', font=('Arial', 12, 'bold')
        )
        self.style.configure(
            'Stop.TButton', foreground='black',
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

        # Переменная для хранения состояния видео.
        self.is_playing = False

        # Задание размера окна
        self.root.geometry("1500x900")

    def start_video(self):
        # Начать воспроизведение видео.
        self.video.start()
        self.is_playing = True

    def pause_video(self):
        # Приостановить воспроизведение видео.
        self.video.set_paused()
        self.is_playing = False

    def stop_video(self):
        # Остановить воспроизведение видео.
        self.video.stop()
        self.is_playing = False


if __name__ == "__main__":
    root = tk.Tk()
    app = ProductionGUI(root)
    root.mainloop()
