import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
datos = yf.download("TSLA", period="10y")
precios = datos["Close"]["TSLA"]
retornos_log = np.log(precios / precios.shift(1))
vol_roll_d = retornos_log.rolling(window=20,).std()
vol_anual = vol_roll_d * np.sqrt(252)
plt.plot(vol_anual * 100)
plt.ylabel("Volatilidad anual (%)")
plt.show()