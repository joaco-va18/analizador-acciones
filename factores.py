import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
datos = yf.download(["MSFT", "SPY", "QQQ"], period="10y")
precios = datos["Close"][["MSFT", "SPY", "QQQ"]]
R_log = np.log(precios / precios.shift(1))
Vol_D = R_log.std()
Vol_A = Vol_D * np.sqrt(252)
print("La vol diaria es:", Vol_D)
print("La vol anual es:", Vol_A)
R_limpios = R_log.dropna()
X = sm.add_constant(R_limpios[["SPY"]]) # sm.add_constant(...) — le pega adelante la columna de unos. Es el np.ones + np.column_stack en un solo paso.
modelo_aux = sm.OLS(R_limpios["QQQ"], X).fit() # sm.OLS(y, X) — arma el modelo. El orden importa: primero lo que querés explicar, después con qué. Acá y es QQQ (una sola columna, un corchete) y X es la tabla que armaste arriba. .fit() — resuelve. Acá adentro pasa toda la matemática que derivaste: $(X^\top X)^{-1}X^\top y$, los residuos, sigma2, los errores estándar. Todo.
print(modelo_aux.summary())
qqq_limpio = modelo_aux.resid
print("Los reiduos de QQQ son:", qqq_limpio)
X2 = R_limpios[["SPY"]]
X2["QQQ_limpio"] = qqq_limpio
X2 = sm.add_constant(X2)
modelo2 = sm.OLS(R_limpios["MSFT"], X2).fit()
print(modelo2.summary())