#Python usa librerias como matplotlib con objetos predeterminados como pyplot que tienen propiedades que permiten enviar las instrucciones a la maquina de una forma resumida. Matplotlib es una libreria para crear graficas en 2 dimensiones. 
import matplotlib.pyplot as plt
X = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
Y = [4,4,5,5,6,6,6,7,8,8,8,9,10,10,10,10,11,12,12,12,13,13,13]
plt.scatter(X, Y, s=60, c='blue', marker='^')
plt.xlim(0,25)
plt.ylim(0,25)
plt.title('Numero de primos y hermanos por anio de vida')
plt.ylabel('Numero de primos y hermanos por anio')
plt.xlabel('Numero de anios')
#Con esta isntruccion guardamos la imagen con el formato que queramos.
plt.savefig('temp.png')
#Con esta instruccion mostramos la figura. 
plt.show()

