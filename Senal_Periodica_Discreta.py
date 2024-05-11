import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-25.0, 25.0, 1) 
y = np.cos(np.pi*x*1/21)
   
fig, ax = plt.subplots()

ax.stem(x,y)

ax.set(xlabel = 'Tiempo(s)', ylabel = 'Voltaje(V)', title='y = sin(x*pi/21)')

#Podemos que nos muestre una grilla en el gráfico
ax.grid(True)

#Guardamos la imagen creada
fig.savefig("Funcion periódica en tiempo discreto.png")

#Mostramos la imagen creada
plt.show()