import pandas as pd
import pytest
from capstone_v2 import calcular_vol, calcular_retorno_log
def test_vol_cero_si_no_hay_dispersion():
    retornos = pd.Series([0.01, 0.01, 0.01, 0.01])
    resultado = calcular_vol(retornos, 252)
    assert resultado == 0
def test_vol_escalado_anualizado():
    retornos = pd.Series([0.01, -0.01])
    resultado = calcular_vol(retornos, 252)
    assert resultado == pytest.approx(0.224499, abs=1e-5)
def test_retorno_log_precio_duplicado():
    precios = pd.Series([100, 200])
    resultado = calcular_retorno_log(precios)
    assert resultado.iloc[1] == pytest.approx(0.693147, abs=1e-5)
