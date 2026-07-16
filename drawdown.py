import numpy as np
precios = np.array([100, 150, 90, 120])
running_max = np.maximum.accumulate(precios)
drawdown_en_cada_punto = (precios - running_max) / running_max
print("El drawdown en cada punto es:", drawdown_en_cada_punto)
print("El Max DrawDown es:", drawdown_en_cada_punto.min())