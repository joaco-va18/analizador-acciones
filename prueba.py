import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
datos = yf.download("MSFT", period="10y")
precios = datos["Close"]["MSFT"]
print("El type es:", type(precios))
print(datos.tail())