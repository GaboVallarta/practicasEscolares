import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation
# Crear una figura y un eje



figure,ax = plt.subplots()
ax.set_xlim(0,10)
ax.set_ylim(0,10)
#ay=plt.subplot()
rectangle=Rectangle([5,5],1,1,edgecolor='blue')
# Dibujar un gráfico de líneas
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.add_patch(rectangle)

def init():
    rectangle.set_data([], [])
    return rectangle,

def update(frame,rectangle):
    size=frame
    Rectangle.set_height(rectangle,size+1)

ani = FuncAnimation(figure, update, frames=np.arange(0, 10, 0.1), init_func=init, blit=True)

# Mostrar el gráfico
plt.show()