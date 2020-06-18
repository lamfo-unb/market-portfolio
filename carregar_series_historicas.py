import pandas as pd
from typing import Callable


def f(line: str) -> bool:
    """Indica se a linha possui o layout desejado"""

    if line[0:2] == '01':
        return True
    return False


def rows_to_skip(path: str, layout_indicator: Callable) -> list:
    """Retorna a linhas que não correspondem ao layout desejado"""

    with open(path) as file:
        lines = (line for line in file)
        index = 0
        rows = []
        for line in lines:
            layout_desejado = layout_indicator(line)
            if not layout_desejado:
                rows.append(index)
            index += 1
    return rows


if __name__ == "__main__":
    path = 'dados/COTAHIST_A2020/COTAHIST_A2020.TXT'
    pular_linhas = rows_to_skip(path, f)

    largura_colunas = [2, 8, 2, 12, 3, 12, 10, 3, 4, 13, 13, 13, 13, 13, 13, 13, 5, 18, 18, 13, 1, 8, 7, 13, 12, 3]
    colunas = ['tipreg', 'data_pregao', 'codbdi', 'codneg', 'tpmerc', 'nomres', 'especi', 'prazot', 'modref', 'preabe',
               'premin', 'premed', 'preult', 'preofc', 'preofc', 'preofv', 'totneg', 'quatot', 'voltot', 'preexe',
               'indopc', 'datven', 'fatcot', 'ptoexe', 'codisi', 'dismes']

    columns_espc = tuple(zip(colunas, largura_colunas))
    dados = pd.read_fwf(path, skiprows=pular_linhas, widths=largura_colunas, header=None, dtype=str)
    dados.columns = colunas
    header = dados.head(100)
