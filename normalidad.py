import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from capstone_v2 import calcular_retorno_log
from scipy import stats
precios = yf.download(["MSFT", "VOO", "BTC-USD", "ACAD", "GLD"], period="10y")["Close"]
print("---DIARIOS---")
retornos = calcular_retorno_log(precios)
for ticker in retornos.columns:
    serie = retornos[ticker].dropna()
    asimetria = stats.skew(serie)
    curtosis = stats.kurtosis(serie)
    jb_stat, p_valor = stats.jarque_bera(serie)
    print(f"{ticker}: skew={round(asimetria, 4)}  curtosis={round(curtosis, 4)}  p={p_valor}")
print("---MENSUALES---")
retornos_m = retornos.resample("ME").sum()
for ticker in retornos_m.columns:
    serie = retornos_m[ticker].dropna()
    asimetria = stats.skew(serie)
    curtosis = stats.kurtosis(serie)
    jb_stat, p_valor = stats.jarque_bera(serie)
    print(f"{ticker}: skew={round(asimetria, 4)}  curtosis={round(curtosis, 4)}  p={p_valor}")
acad = retornos["ACAD"].dropna()
print("con todo:", stats.kurtosis(acad))
print("sin el peor día:", stats.kurtosis(acad.drop(acad.idxmin())))
plt.figure()
stats.probplot(retornos["VOO"].dropna(), dist="norm", plot=plt)
plt.title("QQ-plot: VOO vs Normal")
plt.savefig("qq_voo.png")
plt.figure()
stats.probplot(retornos["ACAD"].dropna(), dist="norm", plot=plt)
plt.title("QQ-plot: ACAD vs Normal")
plt.savefig("qq_acad.png")
plt.figure()
stats.probplot(retornos_m["VOO"].dropna(), dist="norm", plot=plt)
plt.title("QQ-plot_mensual: VOO vs Normal")
plt.savefig("qq_voo_mensual.png")
plt.figure()
stats.probplot(retornos_m["ACAD"].dropna(), dist="norm", plot=plt)
plt.title("QQ-plot_mensual: ACAD vs Normal")
plt.savefig("qq_acad_mensual.png")
plt.show()
