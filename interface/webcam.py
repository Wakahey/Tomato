import cv2
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import torch
class WebCamera:
    """Класс для работы с камерой"""

    def __init__(self, window, width=450, height=450):
        """
        Инициализация переменных в объект класса для работы с камерой.

        :param window: объект окна
        :param width: ширина окна
        :param height: длина окна
        """
        self.window = window
        self.width = width
        self.height = height
        self.cap = None
        self.label = None
        self.showing_frames = False
        self.flag_paused = False

        # Загрузка предварительно обученной модели Pytorch YOLO
        self.model = torch.hub.load('weights/best.pt', 'yolov5n', pretrained=True)

    def get_box_info(self):
        """Получение информации по окну"""
        print(f"Window: {self.window}")
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")

    def show_frames(self):
        """Метод класса показывающий изображение с камеры"""
        if self.showing_frames and not self.flag_paused:
            ret, frame = self.cap.read()
            if ret:

                tensor = torch.from_numpy(frame).permute(2, 0, 1).float().div(255.0).unsqueeze(0)

                results = self.model(tensor)

                for box in results.xyxy[0]:
                    x1, y1, x2, y2, conf, cls = box
                    # Отрисовка рамки вокруг объектов
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
                    # Добавление метки класса и уверенности
                    cv2.putText(frame, f'{int(cls)}: {conf:.2f}', (int(x1), int(y1) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image)

                imgtk = ImageTk.PhotoImage(image=img)

                if self.label:
                    self.label.imgtk = imgtk
                    self.label.configure(image=imgtk)
                else:
                    self.label = Label(self.window, width=self.width, height=self.height, image=imgtk)
                    self.label.pack()

            self.label.after(20, self.show_frames)

    def start(self):
        """Метод класса запускающий поток камеры"""
        self.flag_paused = False
        try:
            try:
                self.cap = cv2.VideoCapture(0)
            except Exception as exc:
                self.window.insert(tk.END, "")

            self.label = Label(self.window, width=self.width, height=self.height)
            self.label.pack()
            self.showing_frames = True
            self.show_frames()
        except Exception as exc:
            self.window.insert(tk.END, "")


    def set_paused(self):
        """Метод класса останавливающий поток камеры"""
        self.flag_paused = True

    def stop(self):
        """Метод класса закрывающий поток камеры"""
        self.showing_frames = False
        if self.cap:
            self.cap.release()
        if self.label:
            self.label.destroy()
