import pandas as pd
import yfinance as yf
import numpy as np
datos = yf.download("AAPL", period="10y")
precios = datos["Close"]["AAPL"]
print(datos.tail())
retorno_log = np.log(precios / precios.shift(1))
return_group = retorno_log.groupby(retorno_log.index.year).mean()
print(return_group)
return_std = retorno_log.groupby(retorno_log.index.year).std()
print(return_std)
precios_rango = precios.loc["2025-01-01" : "2025-02-01"]
print(precios_rango)