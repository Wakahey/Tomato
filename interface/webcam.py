import cv2
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import torch
from ultralytics import YOLO
import sys


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
        self.neural_report = None
        self.label = None
        self.showing_frames = False
        self.flag_paused = False

        # Загрузка предварительно обученной модели Pytorch YOLO
        self.model = YOLO("weights/best.pt")
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
                result_data = results[0].probs.data
                print(result_data)
                spoiled_result = result_data[1].item()
                print(spoiled_result)
                normal_result = result_data[0].item()
                print(normal_result)
                self.neural_report.config(text="Брак!")
                # if spoiled_result > 0.85:
                #     self.neural_report.config(text="Брак!")
                # elif normal_result > 0.85:
                #     self.neural_report.config(text="Нормально")
                # else:
                #     self.neural_report.config(text="Не понятно")



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

            self.neural_report = tk.Label(self.window, text="отображение", font=("Helvetica", 16))
            self.neural_report.pack()

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
            self.neural_report.destroy()

    # def update_tomato_label(self, report_name):
    #     if report_name:
    #         # Получаем первый класс из списка (можно настроить логику выбора)
    #         tomato_class = report_name
    #         self.tomato_label.config(text=f"Tomato Class: {tomato_class}")
    #     else:
    #         self.tomato_label.config(text="No tomato detected")