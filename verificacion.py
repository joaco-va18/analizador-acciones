import numpy as np
# retorno = np.array([0.02, -0.01, 0.03, -0.005])
# print("El retorno promedio es:", retorno.mean())
retornos = np.array([0.10, 0.04, -0.02])
pesos = np.array([0.3, 0.5, 0.2])
# np.dot(x, y) agarra dos array y lo multiplica componente por componente y los suma
print("El retorno del portfolio es de:", np.dot(pesos, retornos))
