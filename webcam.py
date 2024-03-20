import cv2
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

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
