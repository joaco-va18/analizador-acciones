import numpy as np
import pandas as pd
import yfinance as yf
datos = yf.download(["MSFT", "ACAD", "UEC"], period="10y")
precios = datos["Close"]
print(precios)
retorno_log = np.log(precios / precios.shift(1))
print(retorno_log.tail())
volatilidad_d = retorno_log.std()
vol_m = volatilidad_d * np.sqrt(21)
vol_a = volatilidad_d * np.sqrt(252)
print(vol_a)
corr = retorno_log.corr()
print(corr)