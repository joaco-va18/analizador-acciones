import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
def evaluar_portfolio(pesos, mu, cov, rf):
    retorno = pesos @ mu
    vol_p = np.sqrt(pesos @ cov @ pesos)
    sharpe = (retorno - rf) / vol_p
    return retorno, vol_p, sharpe
precios = yf.download(["MSFT", "META", "AMPX", "ACAD", "UEC"], period="10y")["Close"]
precios_alineados = precios.dropna()
retornos_log = np.log(precios_alineados / precios_alineados.shift(1))
mitad = len(retornos_log) // 2
retornos_is = retornos_log.iloc[:mitad]    # primera mitad
mu_is = retornos_is.mean() * 252
cov_is = retornos_is.cov() * 252
retornos_oss = retornos_log.iloc[mitad:]   # segunda mitad.      # print(len(retornos_is), len(retornos_oss), len(retornos_log))
mu_oss = retornos_oss.mean() * 252
cov_oss = retornos_oss.cov() * 252
lista_vol = []
lista_rendimiento = []
lista_pesos = []
lista_sharpe_p = []
rf = 0.04
np.random.seed(46)
for _ in range(5000):
    pesos_random = np.random.random(5)
    w = pesos_random / np.sum(pesos_random)
    retorno_p = w @ mu_is
    vol_p = np.sqrt(w @ cov_is @ w)
    lista_vol.append(vol_p)
    lista_rendimiento.append(retorno_p)
    lista_pesos.append(w)
    sharpe = (retorno_p - rf) / vol_p
    lista_sharpe_p.append(sharpe)
print("-----Minima var-----")
pos_min = np.argmin(lista_vol)
print("La volatilidad es:",lista_vol[pos_min])
pesos_minvar = lista_pesos[pos_min]
print("Los pesos son:", lista_pesos[pos_min])
print("El retorno es:", lista_rendimiento[pos_min])
print("-----Max Sharpe-----")
pos_max = np.argmax(lista_sharpe_p)
print("La volatilidad es:", lista_vol[pos_max])
pesos_sharpe = lista_pesos[pos_max]
print("Los pesos son:", lista_pesos[pos_max])
print("El retorno es:", lista_rendimiento[pos_max])
pesos_equal = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
print("-----------------------------------------------------")
print("----- Máximo Sharpe -----")
ret, vol, sh = evaluar_portfolio(pesos_sharpe, mu_is, cov_is, rf)
print("IS :", round(ret,4), round(vol,4), round(sh,4))
ret, vol, sh = evaluar_portfolio(pesos_sharpe, mu_oss, cov_oss, rf)
print("OOS:", round(ret,4), round(vol,4), round(sh,4))
print("----- Mínima varianza -----")
ret, vol, sh = evaluar_portfolio(pesos_minvar, mu_is, cov_is, rf)
print("IS :", round(ret,4), round(vol,4), round(sh,4))
ret, vol, sh = evaluar_portfolio(pesos_minvar, mu_oss, cov_oss, rf)
print("OOS:", round(ret,4), round(vol,4), round(sh,4))
print("----- Equiponderado (1/N) -----")
ret, vol, sh = evaluar_portfolio(pesos_equal, mu_is, cov_is, rf)
print("IS :", round(ret,4), round(vol,4), round(sh,4))
ret, vol, sh = evaluar_portfolio(pesos_equal, mu_oss, cov_oss, rf)
print("OOS:", round(ret,4), round(vol,4), round(sh,4))