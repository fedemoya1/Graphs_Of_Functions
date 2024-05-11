import numpy as np
import matplotlib.pyplot as plt

#Rango para el eje X
x = np.arange(-8, 8, 1)

#Funciones a graficar
y1 = np.exp(x)
y2 = np.exp(-x)
y3 = np.cos(x)
y4 = np.exp(x)*np.cos(np.pi*x)
y5 = np.exp(-x)*np.cos(np.pi*x)

#Tamaño de la figura
plt.figure(figsize=(10, 6))

#Seteamos en qué índice se va a graficar cada función
plt.subplot(3, 2, 1)
plt.stem(x, y1)
plt.title('y = e^(kn); k > 0')
plt.grid(True)

plt.subplot(3, 2, 2)
plt.stem(x, y2)
plt.title('y = e^(kn); k < 0')
plt.grid(True)

plt.subplot(3, 2, 3)
plt.stem(x, y3)
plt.title('y = e^(jwn); Re[y] = cos(wn)')
plt.grid(True)

plt.subplot(3, 2, 4)
plt.stem(x, y4)
plt.title('y = e^(kn+jwn); Re[y] = e^(kn) * cos(wn) con k > 0')
plt.grid(True)

plt.subplot(3, 2, 5)
plt.stem(x, y5)
plt.title('y = e^(kn+jwn); Re[y] = e^(kn) * cos(wn) con k < 0')
plt.grid(True)

plt.tight_layout()
plt.savefig('Funciones Exponenciales en tiempo Discreto.png')
plt.show()