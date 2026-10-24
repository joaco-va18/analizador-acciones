import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
import pandas as pd
datos = yf.download(["MSFT", "SPY", "IWM", "IWD", "IWF", "^IRX"], period="10y")
precios = datos["Close"][["MSFT", "SPY", "IWM", "IWD", "IWF", "^IRX"]]
R_log = np.log(precios / precios.shift(1))
Rf_d = (precios["^IRX"] / 100 / 252)
datos_modelo = pd.DataFrame({
    "MSFT_exc": R_log["MSFT"] - Rf_d,
    "Rm":  R_log["SPY"]  - Rf_d,
    "SMB":      R_log["IWM"]  - R_log["SPY"],
    "HML":      R_log["IWD"]  - R_log["IWF"],
}).dropna()
print(datos_modelo.shape)
X = sm.add_constant(datos_modelo[["Rm", "SMB", "HML"]])
y = datos_modelo["MSFT_exc"]
modelo = sm.OLS(y, X).fit()
print(modelo.summary())
print("El Alpha y los Beta son:", modelo.params)