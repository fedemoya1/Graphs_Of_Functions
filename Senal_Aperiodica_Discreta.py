import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 20, 1) 
y = np.log(x)
   
fig, ax = plt.subplots()

ax.stem(x,y)

ax.set(xlabel = 'Tiempo(s)', ylabel = 'Voltaje(V)', title='y = log(n)')

#Podemos que nos muestre una grilla en el gráfico
ax.grid(True)

#Guardamos la imagen creada
fig.savefig("Funcion aperiódica en tiempo discreto.png")

#Mostramos la imagen creada
plt.show()