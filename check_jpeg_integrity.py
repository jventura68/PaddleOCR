import os
from PIL import Image
import argparse

def check_jpeg_integrity(image_path):
    try:
        with Image.open(image_path) as im:
            im.verify()  # Verificamos si la imagen es válida.
        return True
    except:
        return False

def find_corrupt_images(directory):
    corrupt_images = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.jpeg') or file.lower().endswith('.jpg'):
                file_path = os.path.join(root, file)
                if not check_jpeg_integrity(file_path):
                    corrupt_images.append(file_path)

    return corrupt_images

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Buscar imágenes JPEG corruptas en un directorio.")
    parser.add_argument("directory", help="Directorio donde buscar las imágenes corruptas.")
    args = parser.parse_args()

    corrupt_images = find_corrupt_images(args.directory)
    
    if corrupt_images:
        print("Se encontraron las siguientes imágenes corruptas:")
        for path in corrupt_images:
            print(path)
    else:
        print("No se encontraron imágenes corruptas en el directorio especificado.")

