import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear una figura y un eje
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Crear un punto que será nuestro "círculo" en movimiento
circle, = plt.plot([], [], 'o', markersize=10)

# Función para inicializar el gráfico
def init():
    circle.set_data([], [])
    return circle,

# Función para actualizar la posición del círculo
def update(frame):
    x = frame  # El valor x se actualizará en cada frame
    y = 5  # Fija la posición y en 5
    circle.set_data(x, y)
    return circle,

# Crear la animación
ani = FuncAnimation(fig, update, frames=np.arange(0, 10, 0.1), init_func=init, blit=True)

# Mostrar la animación
plt.show()
