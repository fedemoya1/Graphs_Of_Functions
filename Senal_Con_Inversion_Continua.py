import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-8.0, 8.0, 0.01) 
y = np.where(x < 0, 0, -x)
   
fig, ax = plt.subplots()

ax.plot(x,y)

ax.set(xlabel = 'Tiempo(s)', ylabel = 'Voltaje(V)', title='y = r(-t)')

#Podemos que nos muestre una grilla en el gráfico
ax.grid(True)

#Guardamos la imagen creada
fig.savefig("Funcion con inversion en el tiempo continuo.png")

#Mostramos la imagen creada
plt.show()