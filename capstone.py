import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
datos = yf.download("MSFT", period="10y")
precios = datos["Close"]["MSFT"]
print("El type es:", type(precios))
print(datos.tail())
retornos_log = np.log(precios / precios.shift(1))
print("El retorno logaritmico diario es:", retornos_log.tail())
print("El retorno logaritmico de los 10 años es:", retornos_log.sum())
rendimiento = np.exp(retornos_log.sum()) - 1
print("El retnorno porcentual es de:", rendimiento * 100)
volatilidad_diaria = retornos_log.std()
vol_mens = volatilidad_diaria * np.sqrt(21)
vol_anual = volatilidad_diaria * np.sqrt(252)
print("La volatilidad anual es de", round(vol_anual, 4))
running_max = np.maximum.accumulate(precios)
drawdown = (precios - running_max) / running_max
max_dd = drawdown.min()
print("El mayor caida fue de:", max_dd)
spy_precios = yf.download("SPY", period="10y")["Close"]["SPY"]
print(spy_precios.tail())
spy_log_r = np.log(spy_precios / spy_precios.shift(1))
correlacion = retornos_log.corr(spy_log_r)
print("La correlacion(SYP, MSFT) es:", correlacion)
normal = np.random.normal(retornos_log.mean(), retornos_log.std(), 100000)
plt.hist(retornos_log.dropna(), bins=100, density=True)
plt.hist(normal, bins=100, density=True, alpha=0.5)
with open("informe.txt", "w") as f:
    f.write(f"Análisis de MSFT - período: 10 años\n")
    f.write(f"Volatilidad anual {round(vol_anual * 100, 4)}%\n")
    f.write(f"Retorno total: {rendimiento * 100}%\n")
    f.write(f"Maximo DrawDown: {max_dd}\n")
    f.write(f"La correlacion con el SPY: {round(correlacion, 4)}\n")
plt.savefig("histogram.png")
plt.show()
