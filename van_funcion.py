import numpy as np
def van(C0, flujos, i):
    van = -C0
    for t, flujo in enumerate(flujos, start=1):
        van += flujo / (1 + i) ** t
    return van
print("Proyecto 1:", van(100000, [30000, 40000, 50000, 30000], 0.01))
print("Proyecto 2:", van(100000, [30000, 40000, 50000, 30000], 0.06))
print("Proyecto 3:", van(100000, [30000, 40000, 50000, 30000], 0.1))
print("Proyecto 4:", van(100000, [30000, 40000, 50000, 30000], 0.115))
print("Proyecto 5:", van(100000, [30000, 40000, 50000, 30000], 0.14))
print("Proyecto 6:", van(100000, [30000, 40000, 50000, 30000], 0.181))
print("Proyecto 7:", van(100000, [30000, 40000, 50000, 30000], 0.5))
# es para cambiar el salto o incremento entre los números.
C0 = 100000
flujos = [30000, 40000, 50000, 30000]
for tasa in np.arange(0.01, 0.50, 0.001):
    if van(C0, flujos, tasa) < 0:
        print( "TIR =", round(tasa, 4))
        break
nominal = 1000
cupon = 50
tasa_mercado = 0.04
n = 5
flujos_cupon = [cupon] * (n - 1) + [cupon + nominal]
precio = van(0, flujos_cupon, tasa_mercado)
print("El precio del bono es:", round(precio, 4))