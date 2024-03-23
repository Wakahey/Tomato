import os
from PIL import Image

def convert_webp_to_png_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.webp'):
                webp_file_path = os.path.join(root, file_name)
                png_file_path = os.path.join(root, file_name.rsplit('.', 1)[0] + '.png')
                convert_webp_to_png(webp_file_path, png_file_path)
                os.remove(webp_file_path)  # Удаление файла WebP

def convert_webp_to_png(webp_file, png_file):
    im = Image.open(webp_file)
    im.save(png_file, 'PNG')

# Указываем путь к папке
folder_path = r'/neural_network/dataset/test/normal'

# Пример использования
convert_webp_to_png_in_folder(folder_path)


