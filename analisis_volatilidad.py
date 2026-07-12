import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
datos = yf.download("UEC", period="5y")
print(datos.tail())
retornos = np.log(datos["Close"] / datos["Close"].shift(1))
volatilidad_diaria = retornos.std()
volatilidad_mensual = volatilidad_diaria * np.sqrt(21)
volatilidad_anual = volatilidad_diaria * np.sqrt(252)
print("La volatilidad mensual de UEC es de:", round(volatilidad_mensual, 4),
"La volatilidad anual de UEC es de:", round(volatilidad_anual, 4))
datos["Close"].plot()
plt.show()