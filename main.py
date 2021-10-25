import csv

import pytest

teste_dados_calculo = [
    (40, 5, 200),  # teste 1
    (40, 10, 400),  # teste 2
    (40, 12, 480),  # teste 3


]

def calcular_fosforos(nun1, nun2):
    return nun1 * nun2

@pytest.mark.parametrize('nun1,nun2,resul',teste_dados_calculo)
def testar_calcular_fosforos(nun1, nun2, resul):
    resul = nun1 * nun2
    resultado_atual = calcular_fosforos(nun1, nun2)
    assert resultado_atual == resul



