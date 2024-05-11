import numpy as np
import matplotlib.pyplot as plt

tau = np.pi/2
x = np.arange(-20.0, 11.0, 0.01) 
y = np.exp(tau*x) - np.power(tau*x, 5)*np.cos(tau*x)
   
fig, ax = plt.subplots()

ax.plot(x,y)

ax.set(xlabel = 'Tiempo(s)', ylabel = 'Voltaje(V)', title='y = e^(pi*x/2) - cos(pi*x/2)*[(pi*x/2)^5]')

#Podemos que nos muestre una grilla en el gráfico
ax.grid(True)

#Guardamos la imagen creada
fig.savefig("Funcion con escalamiento en el tiempo continuo.png")

#Mostramos la imagen creada
plt.show()