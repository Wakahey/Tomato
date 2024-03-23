import os
import shutil
import random

# Путь к корневой директории
root_dir = "/caltech101"

# Путь к директориям train и test
train_dir = os.path.join(root_dir, "train")
test_dir = os.path.join(root_dir, "test")

# Создание директорий train и test, если они не существуют
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Получаем список классов (имен поддиректорий)
classes = os.listdir(root_dir)

# Для каждого класса
for class_name in classes:
    # Получаем путь к директории класса
    class_dir = os.path.join(root_dir, class_name)

    # Получаем список файлов в директории класса
    files = os.listdir(class_dir)

    # Перемешиваем файлы для случайного разделения
    random.shuffle(files)

    # Вычисляем индекс, с которого начинается разделение на train и test (80/20)
    split_index = int(0.8 * len(files))

    # Разделяем файлы на train и test
    train_files = files[:split_index]
    test_files = files[split_index:]

    # Создаем поддиректории для класса в train и test, если они не существуют
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

    # Копируем файлы в директории train
    for file in train_files:
        src = os.path.join(class_dir, file)
        dst = os.path.join(train_dir, class_name, file)
        shutil.copy(src, dst)

    # Копируем файлы в директории test
    for file in test_files:
        src = os.path.join(class_dir, file)
        dst = os.path.join(test_dir, class_name, file)
        shutil.copy(src, dst)