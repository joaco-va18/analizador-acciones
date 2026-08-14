import numpy as np
C0 = 100000
flujos = [10000, 13000, 20000, 20000, 23500]
i = 0.115
van = -C0
for t, flujo in enumerate(flujos, start=1):
    van += flujo /(1+ i) ** t
print("El VAN es:", van)