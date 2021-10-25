#1 - Imports

import pytest
import csv



def ler_dados_do_csv():
    testar_calcular_fosforos_csv = []
    nome_arquivo = 'fosforos.csv'
    try:
        with open(nome_arquivo, newline='') as csvfile:
            dados = csv.reader(csvfile, delimiter=',')
            next(dados)
            for linha in dados:
                testar_calcular_fosforos_csv.append(linha)
        return testar_calcular_fosforos_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'falha imprevista: {fail}')

def calcular_fosforos_csv(nun1, nun2):
    return nun1 * nun2


@pytest.mark.parametrize('nun1,nun2,resul',ler_dados_do_csv())
def testar_calcular_fosforos_csv(nun1, nun2, resul):
    resul = nun1*nun2
    resultado_atual = calcular_fosforos_csv(nun1,nun2)
    assert resultado_atual == resul

