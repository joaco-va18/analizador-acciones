import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
precios = yf.download(["MSFT", "VOO", "BTC-USD", "ACAD", "GLD"], period="10y")["Close"]
pesos = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
precios_alineados = precios.dropna() # .dropna, elimina columnas/filas con NaN
retornos_log = np.log(precios_alineados / precios_alineados.shift(1))
covarianza = retornos_log.cov() * 252
print(covarianza)
volatilidad_d = retornos_log.std()
volatilidad_a = volatilidad_d * np.sqrt(252)
print(volatilidad_a)
pesos_ponderado = pesos @ volatilidad_a
riesgo_max = pesos_ponderado
print(riesgo_max)
# lo comrpobe a mano el riesgo max
var_port = pesos @ covarianza @ pesos
vol_port = np.sqrt(var_port)
print(vol_port)
rendimientos_esperados_a = retornos_log.mean() * 252
print(rendimientos_esperados_a)
rendimiento_equal = pesos @ rendimientos_esperados_a
lista_vol = []
lista_rendimiento = []
lista_pesos = []
lista_sharpe_p = []
rf = 0.04
np.random.seed(42)
for _ in range(5000):
    pesos_random = np.random.random(5)
    w = pesos_random / np.sum(pesos_random)
    retorno_p = w @ rendimientos_esperados_a
    vol_p = np.sqrt(w @ covarianza @ w)
    lista_vol.append(vol_p)
    lista_rendimiento.append(retorno_p)
    lista_pesos.append(w)
    sharpe = (retorno_p - rf) / vol_p
    lista_sharpe_p.append(sharpe)
print("---Minima varianza---")
posicion_min = np.argmin(lista_vol)
print(lista_pesos[posicion_min])
vol_min = (lista_vol[posicion_min])
print("La vol minima es:", vol_min)
retorno_min = (lista_rendimiento[posicion_min])
print("El retorno min es:", retorno_min)
sharpe_min = lista_sharpe_p[posicion_min]
print("El sharpe es:", sharpe_min)
print("---Sharpe portfolio---")
posicion_sharpe = np.argmax(lista_sharpe_p)
vol_s = (lista_vol[posicion_sharpe])
print("La vol del sharpe portfolio es:", vol_s)
retorno_s = (lista_rendimiento[posicion_sharpe])
print("El rendimiento del sharpe portfolio es:", retorno_s)
max_sharpe = (lista_sharpe_p[posicion_sharpe])
print("El mejor sharpe es:", max_sharpe)
print("Los pesos del sharpe portfolio son:", (lista_pesos[posicion_sharpe]))
plt.scatter(lista_vol, lista_rendimiento, s=5, alpha=0.3)
plt.scatter(vol_port, rendimiento_equal, color="red", s=100)
plt.scatter(vol_min, retorno_min, color="green", s=100)
plt.scatter(lista_vol[posicion_sharpe], lista_rendimiento[posicion_sharpe], color="orange", s=100)
plt.ylabel("Rendimiento esperado")
plt.xlabel("Volatilidad anual")
plt.title("Markowitz")
plt.savefig("Frontera.png")
plt.show()