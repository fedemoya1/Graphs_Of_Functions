import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-8.0, 8.0, 1) 
y = np.where(x < 0, 0, np.power(-x, 3))
   
fig, ax = plt.subplots()

ax.stem(x,y)

ax.set(xlabel = 'Tiempo(s)', ylabel = 'Voltaje(V)', title='y = (-x)^3')

#Podemos que nos muestre una grilla en el gráfico
ax.grid(True)

#Guardamos la imagen creada
fig.savefig("Funcion con inversion en el tiempo discreto.png")

#Mostramos la imagen creada
plt.show()