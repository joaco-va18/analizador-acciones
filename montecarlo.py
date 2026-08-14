import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
datos = yf.download("META", period="10y")
precios = datos["Close"]["META"]
log_ret = np.log(precios / precios.shift(1))
# .iloc[-1] es para tener la ultima fila de algo. 0 = la primer fila de la hisotira. 1 = la segunda..... -1 = hoy. -2 = ayer.....
P0 = precios.iloc[-1]
mu = log_ret.mean()
sigma = log_ret.std()
n_dias = 252
precios_finales = []
# es para generar retornos al azar
for _ in range(1000):
    retornos_simulator = np.random.normal(mu, sigma, n_dias)
    # np.cumsum acumula
    log_acu = np.cumsum(retornos_simulator)
    precios_d = P0 * np.exp(log_acu)
    precios_finales.append(precios_d[-1])
    plt.plot(precios_d)
mediana = np.percentile(precios_finales, 50)
p5 = np.percentile(precios_finales, 5)
p95 = np.percentile(precios_finales, 95)
prob_perder = (np.array(precios_finales) < P0).mean()
print("La media de META es:", round(mediana, 4))
print("El 5% de los precios terminan por debajo de:", round(p5, 4))
print("El 5% de los precios termina por encima de:", round(p95, 4))
print("La probabilidad de perder es de:", round(prob_perder * 100, 4), "%")
plt.show()
