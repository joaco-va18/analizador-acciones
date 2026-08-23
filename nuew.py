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
rendimiento_1 = np.exp(retornos_log.sum()) - 1
rendimiento = np.exp(retornos_log.sum())
print(rendimiento)
print("El retnorno porcentual es de:", rendimiento_1 * 100)