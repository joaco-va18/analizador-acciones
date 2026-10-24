import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from capstone_v2 import calcular_retorno_log
from capstone_v2 import descargar_precios_multi
from capstone_v2 import calcular_vol
tickers = ["MSFT", "SPY", "QQQ"]
periodo = "10y"
precios = descargar_precios_multi(tickers, periodo)
retornos_log = calcular_retorno_log(precios)
vol_d = calcular_vol(retornos_log, 1)
vol_a = calcular_vol(retornos_log, 252)
print(retornos_log)
print(vol_a)
cov_matriz = retornos_log.cov()
cov = cov_matriz.loc["MSFT", "SPY"] # seleciona la cov de los activos(de toda la tabla se queda con un numero unico)
var = vol_d["SPY"] ** 2
beta = cov / var
print("La beta de MSFT es de:", beta)
retornos_limpios = calcular_retorno_log(precios).dropna()
y = retornos_limpios["MSFT"]
unos = np.ones(len(y))   # los unos son para permitir que la recta cruce el eje vertical en un punto distinto de cero(estima el alpha). Sin esta la recta pasa por el punto (0,0) basicamente alpha = 0. La columna de unos es el alpha
x = np.column_stack([unos, retornos_limpios["SPY"], retornos_limpios["QQQ"]]) # sirve para unir arreglos (arrays) de forma vertical, conviertiendolas en columnas
print(x.shape)
coef = np.linalg.inv(x.T @ x) @ x.T @ y
print("El alpha y el beta es:", coef) # son los dos números que definen la forma y la inclinación de la línea recta en el gráfico(alpha y beta)
y_pred = x @ coef
print("La prediccion de MSFT:", y_pred)
residuos = y - y_pred
print(residuos.shape)
rss = (residuos ** 2).sum()
sigma2 = rss / (len(y) - 3) # 
print(sigma2)
residuo_a = np.sqrt(sigma2) * np.sqrt(252)
print("El error de predicion anual es de:", residuo_a)
correlacion = retornos_limpios.corr()
print("La corr es:", correlacion)
xtx_inv = np.linalg.inv(x.T @ x) # muestra la precisión de esos coeficientes
matriz = (xtx_inv * sigma2)
print(np.diag(matriz))
errores = np.sqrt(np.diag(matriz))
se_spy = errores[1]
se_qqq = errores[2]
extremo_inf_interv = coef[1] - 1.96 * se_spy
extremo_superior = coef[1] + 1.96 * se_spy
extremo_inf_interv_q = coef[2] - 1.96 * se_qqq
extremo_superior_q = coef[2] + 1.96 * se_qqq
t_spy = (coef[1] - 1) / se_spy
print("El extremo inferior del intervalo es:", extremo_inf_interv)
print("El extremo superior del intervalo es:", extremo_superior)
print("t:", t_spy)
print("El extremo inferior del intervalo qqq es:", extremo_inf_interv_q)
print("El extremo superior del intervalo qqq es:", extremo_superior_q)
t_qqq = (coef[2] - 1) / se_qqq
print("t_qqq:", t_qqq)
x_recta = np.array([retornos_limpios["SPY"].min(), retornos_limpios["SPY"].max()])
alpha_simple = retornos_limpios["MSFT"].mean() - beta * retornos_limpios["SPY"].mean()
y_recta = alpha_simple + beta * x_recta
plt.plot(x_recta, y_recta, color="red")
plt.scatter(retornos_log["SPY"], retornos_log["MSFT"], alpha=0.3)
plt.title("Rendimiento Acción vs. Mercado")
plt.xlabel("Mercado (Rm)")
plt.ylabel("Acción (Ri)")
plt.grid(True)
plt.show()
modelo = sm.OLS(y, x).fit()
print(modelo.summary())