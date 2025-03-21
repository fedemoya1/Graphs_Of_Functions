import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2.0, 15.0, 1) 
y = np.where(x - np.pi/2 < 0, 0, np.sin(x - np.pi/2))
   
fig, ax = plt.subplots()

ax.stem(x,y)

ax.set(xlabel = 'Tiempo(s)', ylabel = 'Voltaje(V)', title='y = sin(x - pi/2)')

#Podemos que nos muestre una grilla en el gráfico
ax.grid(True)

#Guardamos la imagen creada
fig.savefig("Funcion con desplazamiento en el tiempo discreto.png")

#Mostramos la imagen creada
plt.show()