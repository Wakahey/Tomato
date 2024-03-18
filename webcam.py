import cv2
from tkinter import Label
from PIL import Image, ImageTk


class Box:
    """Box"""

    def __init__(self, window, width=450, height=450):
        self.window = window
        self.width = width
        self.height = height
        self.cap = None
        self.label = None
        self.showing_frames = False
        self.flag_paused = False

    def get_box_info(self):
        """Gets Box Information """
        print(f"Window: {self.window}")
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")

    def show_frames(self):
        """Show Frames"""
        if self.showing_frames and not self.flag_paused:
            ret, frame = self.cap.read()
            if ret:  # Check if frame was successfully obtained
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image)

                imgtk = ImageTk.PhotoImage(image=img)  # Convert image to PhotoImage

                if self.label:
                    self.label.imgtk = imgtk
                    self.label.configure(image=imgtk)
                else:
                    self.label = Label(self.window, width=self.width, height=self.height, image=imgtk)
                    self.label.pack()

            # Repeat after an interval to capture continuously
            self.label.after(20, self.show_frames)

    def start(self):
        """Старт видео потока"""
        self.flag_paused = False
        self.cap = cv2.VideoCapture(0)
        self.label = Label(self.window, width=self.width, height=self.height)
        self.label.pack()
        self.showing_frames = True
        self.show_frames()

    def set_paused(self):
        """Пауза видео потока"""
        self.flag_paused = True

    def stop(self):
        """Стоп видео потока"""
        self.showing_frames = False
        if self.cap:
            self.cap.release()  # Release the camera
        if self.label:
            self.label.destroy()
