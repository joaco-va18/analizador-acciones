import numpy as np
import matplotlib.pyplot as plt
datos = np.random.normal(0.001, 0.02, 10000)
print("Los datos son:", datos)
print("El promedio es:", np.mean(datos))
print("El desvios es:", np.std(datos))
plt.hist(datos, bins=100)
# bin es el grosor de las barras a menor bins(ej. bins=10) barras mas gruesas, a mayor bins(bins=100) barras mas gruesas
plt.show()