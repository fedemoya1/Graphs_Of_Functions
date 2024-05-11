import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-8.0, 8.0, 1) 
y = x 
   
fig, ax = plt.subplots()

ax.stem(x,y)

ax.set(xlabel = 'Tiempo(s)', ylabel = 'Voltaje(V)', title='y = x')

#Podemos que nos muestre una grilla en el gráfico
ax.grid(True)

#Guardamos la imagen creada
fig.savefig("Funcion discreta en el tiempo.png")

#Mostramos la imagen creada
plt.show()