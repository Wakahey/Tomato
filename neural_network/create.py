import multiprocessing

from ultralytics import YOLO


def main():
    # Загружаем модель
    model = YOLO('yolov8s-cls.pt')

    # Запускаем тренировку
    results = model.train(data='dataset', epochs=20, imgsz=640)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()