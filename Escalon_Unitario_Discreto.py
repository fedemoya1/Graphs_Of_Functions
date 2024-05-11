import numpy as np
import matplotlib.pyplot as plt

#Creamos los valores en el eje X desde -2 a 10 dando pasos de a 1
x = np.arange(-4, 10) 

#Creamos los valores en el eje Y los cuales van a ser 0 para x menos a 0 y 1 para x mayor a 1
y = np.where(x < 0, 0, 1)

#Mapeamos los valores con la función stem
plt.stem(x, y) 

#Le damos nombre a los ejes
plt.xlabel('Tiempo discreto (s)')
plt.ylabel('Voltaje (V)')

#Le ponemos título al gráfico
plt.title('Escalon unitario en tiempo discreto u[n]')

#Guardamos la imagen creada
plt.savefig('Escalon unitario en tiempo discreto.png')

#Mostramos la imagen
plt.show()