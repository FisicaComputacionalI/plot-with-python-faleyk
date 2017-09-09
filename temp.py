import matplotlib.pyplot as plt
X = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
Y = [4,4,5,5,6,6,6,7,8,8,8,9,10,10,10,10,11,12,12,12,13,13,13]
plt.plot(X, Y, linewidth=1.0, c='blue', marker='*')
plt.xlim(0,22)
plt.ylim(0,15)
plt.title('Numero de primos y hermanos por anio de vida')
plt.ylabel('Numero de primos y hermanos por anio')
plt.xlabel('Numero de anios')
plt.savefig('temp.png')
plt.show()

