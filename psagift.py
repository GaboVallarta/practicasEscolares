from PIL import Image
import os

# Directorio donde están los archivos .ps
ps_directory = 'C:\\Users\\Gabri\\Desktop\\practicasEscolares\\'  # Reemplaza con tu directorio

# Lista para guardar los frames
frames = []

# Leer todos los archivos .ps del directorio
for file_name in sorted(os.listdir(ps_directory)):
    if file_name.endswith('.ps'):
        file_path = os.path.join(ps_directory, file_name)
        # Abrir el archivo .ps y convertirlo a una imagen
        img = Image.open(file_path)
        frames.append(img)
    else:
        print("no")

# Guardar los frames como un GIF
frames[0].save('animation.gif', save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)
