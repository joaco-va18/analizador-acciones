import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
def calcular_vol(retornos, periodos):
    vol_d = retornos.std()
    vol_x = vol_d * np.sqrt(periodos)
    return vol_x
def calcular_vol_roll(retornos, ventana, periodos):
    vol_r_d = retornos.rolling(window=ventana).std()
    vol_r_x = vol_r_d * np.sqrt(periodos)
    return vol_r_x
def calcular_retorno_log(precios):
    retorno_log = np.log(precios / precios.shift(1))
    return retorno_log
def calcular_drawdown(precios):
    running_max = np.maximum.accumulate(precios)
    dd = (precios - running_max) / running_max
    return dd
def descargar_precios(ticker, periodo):
    datos = yf.download(ticker, period=periodo)
    precios = datos["Close"][ticker]
    return precios
def informe(vol_a, vol_r_a, rendimiento, max_dd, correlacion, ticker, periodo):
    with open("informe.txt", "w") as f:
        f.write(f"El ticker es: {ticker}\n")
        f.write(f"El periodo a evaluar es: {periodo}\n")
        f.write(f"Volatilidad anual {round(vol_a * 100, 4)}%\n")
        f.write(f"Volatilidad rolling actual (20 días): {round(vol_r_a.iloc[-1] * 100, 4)}%\n")
        f.write(f"Retorno total: {round(rendimiento * 100, 4)}%\n")
        f.write(f"Maximo DrawDown: {round(max_dd * 100, 4)}%\n")
        f.write(f"La correlacion con el SPY: {round(correlacion, 4)}\n")
if __name__ == "__main__":
    precios = descargar_precios("MSFT", "10y")
    retornos_log = calcular_retorno_log(precios)
    print("El retorno logaritmico diario es:", retornos_log.tail())
    print("El retorno logaritmico de los 10 años es:", retornos_log.sum())
    rendimiento = np.exp(retornos_log.sum()) - 1
    print("El retnorno porcentual es de:", rendimiento * 100)
    vol_a = calcular_vol(retornos_log, 252)
    vol_r_a = calcular_vol_roll(retornos_log, 20, 252)
    dd = calcular_drawdown(precios)
    max_dd = dd.min()
    drawdown_g = dd * 100
    print("El mayor caida fue de:", max_dd)
    precios_spy = descargar_precios("SPY", "10y")
    spy_log_r = calcular_retorno_log(precios_spy)
    correlacion = retornos_log.corr(spy_log_r)
    print("La correlacion(SYP, MSFT) es:", correlacion)
    normal = np.random.normal(retornos_log.mean(), retornos_log.std(), 100000)
    plt.hist(retornos_log.dropna(), bins=100, density=True)
    plt.hist(normal, bins=100, density=True, alpha=0.5)
    informe(vol_a, vol_r_a, rendimiento, max_dd, correlacion, "MSFT", "10y")
    plt.savefig("histogram.png")
    plt.figure()
    plt.plot(vol_r_a * 100)
    plt.ylabel("Volatilidad anual (%)")
    plt.savefig("volatilidad_rolling.png")
    plt.figure()
    plt.plot(drawdown_g)
    plt.ylabel("Drawdown (%)")
    plt.savefig("drawdown_diario.png")
    plt.show()