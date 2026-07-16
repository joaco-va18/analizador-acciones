import numpy as np
# este es el numero de variables(tiradas en este caso)
n = 10000
# 1 cara ; 0 cruz
# 0 representa el valor minimo que puede salir(low)
# 2 representa el maximo, NO se incluye en los resultados
# np.random.randint() es una funcion de numpy que genera enteros de forma aleatoria dentro de un rango determinado
tiradas = np.random.randint(0, 2, size=n)
print("Las tiradas son:", tiradas)
cantidad_caras = (tiradas == 1).sum()
cantidad_cruz = (tiradas == 0).sum()
print("La cantidad de caras es:", cantidad_caras,
"La cantidad de cruzes son:", cantidad_cruz)
prob_empirica = cantidad_caras / n
print("La probabilidad empirica de caras es:", prob_empirica)
espacio_muestral = [0, 1]
total = 2
favorables = [1]
prob_teoricas = len(favorables) / total
print("La probabilidad teorica es de:", prob_teoricas)