import numpy as np
M = np.array([[0, -1], [1, 0]])
# col_1 = np.array([0, 1])
# col_2 = np.array([-1, 0])
v = np.array ([3, 2])
resultado_A = M @ v
# lo que hace @ es la multiplicacion de las matrices, cumple la misma funcion de np.dot
# resultado_B = 3 * col_1 + 2 * col_2
print("La trasnfromacion del V es:", resultado_A)
# print("La trasnfromacion del V es:", resultado_B)
