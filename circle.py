import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation


# Crear la figura y el eje
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Crear un círculo (centro en (0, 5), radio=0.5)
circle = Circle((0, 5), 0.5, edgecolor='blue', facecolor='none')
ax.add_patch(circle)

# Función de inicialización
def init():
    circle.set_center((0, 5))  # Establece la posición inicial del círculo
    return circle,

# Función para actualizar la posición del círculo
def update(frame):
    x = frame  # El valor de x se actualiza en cada frame
    y = 5  # Mantener la posición y fija
    circle.set_center((x, y))  # Actualizar la posición del círculo
    return circle,

# Crear la animación
ani = FuncAnimation(fig, update, frames=np.arange(0, 10, 0.1), init_func=init, blit=True)

# Mostrar la animación
plt.show()

# anda
# a