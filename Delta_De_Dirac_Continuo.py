import numpy as np
import matplotlib.pyplot as plt

#Datos a presentar:
#Estos son los pasos a dar en el eje X, de -4 a 4 dando pasos de 0.01
#Mientras más pequeños sea el tercer parámetro, nuestro gráfico tendrá mayor precisión
#Caso contrario, si dejamos pasos de a 1, por ejemplo, cuando el gráfico pase de 0 a 1 lo hará en línea recta con cierta pendiente
x = np.arange(-4.0, 4.0, 0.01) 

#y me define los puntos en el eje Y
y = [] 

#Acá agregamos los puntos necesarios en Y
for i in x:
    if i < 0.0 or i > 0.01:
        y.append(0)
    else:
        y.append(1)

#Creamos una figura y un set de subplots    
fig, ax = plt.subplots()

#Mapeamos los valores de x e y
ax.plot(x,y)

#Le damos nombres a los ejes y le ponemos un título al gráfico
ax.set(xlabel = 'Tiempo(s)', ylabel = 'Voltaje(V)', title='Función Delta de Dirac: d(t)')

#Podemos que nos muestre una grilla en el gráfico
ax.grid(True)

#Guardamos la imagen creada
fig.savefig("Delta de Dirac en tiempo continuo.png")

#Mostramos la imagen creada
plt.show()