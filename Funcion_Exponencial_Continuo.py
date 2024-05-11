import numpy as np
import matplotlib.pyplot as plt

#Rango para el eje X
x = np.arange(-2, 6, 0.01)

#Funciones a graficar
y1 = np.exp(x)
y2 = np.exp(-x)
y3 = np.cos(x)
y4 = np.exp(x)*np.cos(2*np.pi*x)
y5 = np.exp(-x)*np.cos(2*np.pi*x)

#Tamaño de la figura
plt.figure(figsize=(10, 6))

#Seteamos en qué índice se va a graficar cada función
plt.subplot(3, 2, 1)
plt.plot(x, y1)
plt.title('y = e^(kt); k > 0')
plt.grid(True)

plt.subplot(3, 2, 2)
plt.plot(x, y2)
plt.title('y = e^(kt); k < 0')
plt.grid(True)

plt.subplot(3, 2, 3)
plt.plot(x, y3)
plt.title('y = e^(jwt); Re[y] = cos(wt)')
plt.grid(True)

plt.subplot(3, 2, 4)
plt.plot(x, y4)
plt.title('y = e^(kt+jwt); Re[y] = e^(kt) * cos(wt) con k > 0')
plt.grid(True)

plt.subplot(3, 2, 5)
plt.plot(x, y5)
plt.title('y = e^(kt+jwt); Re[y] = e^(kt) * cos(wt) con k < 0')
plt.grid(True)

plt.tight_layout()
plt.savefig('Funciones Exponenciales en tiempo Continuo.png')
plt.show()