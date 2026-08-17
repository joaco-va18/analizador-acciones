import pandas as pd
from capstone_v2 import calcular_vol
def test_vol_cero_si_no_hay_dispersion():
    retornos = pd.Series([0.01, 0.01, 0.01, 0.01])
    resultado = calcular_vol(retornos, 252)
    assert resultado == 0