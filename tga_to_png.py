from PIL import Image #pip install Pillow
import os

# Directorul în care se găsesc fișierele TGA
input_dir = "tga_folder"

# Obținerea tuturor fișierelor .tga din director
tga_files = [f for f in os.listdir(input_dir) if f.endswith('.tga')]

# Parcurgerea tuturor fișierelor TGA și convertirea lor în PNG
for tga_file in tga_files:
    # Deschiderea fișierului .tga folosind Pillow
    with Image.open(os.path.join(input_dir, tga_file)) as img:
        # Salvarea imaginii în format .png
        img.save(os.path.join(input_dir, tga_file.replace('.tga', '.png')))
