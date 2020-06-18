# import pandas as pd
from typing import Generator


def gerar_linhas(path) -> Generator:
    return (line for line in open(path))


class CamposHistoricoB3:

    def __init__(self):
        self.posicao_inicial = 0
        self.tamanho_campos = [2, 8, 2, 12, 3, 12, 10, 3, 4, 13, 13, 13,
                               13, 13, 13, 13, 5, 18, 18, 13, 1, 8, 7, 13, 12, 3]
        self.nomes_campos = ['tipreg', 'data_pregao', 'codbdi', 'codneg', 'tpmerc', 'nomres', 'especi', 'prazot',
                             'modref', 'preabe', 'premin', 'premed', 'preult', 'preofc', 'preofc', 'preofv', 'totneg',
                             'quatot', 'voltot', 'preexe', 'indopc', 'datven', 'fatcot', 'ptoexe', 'codisi', 'dismes']

    def split(self, linha: str, tamanho_campo: int) -> str:
        posicao_inicial = self.posicao_inicial
        posicao_final = posicao_inicial + tamanho_campo
        campo = linha[posicao_inicial:posicao_final]
        self.posicao_inicial = posicao_final
        return campo

    def get_campos(self, linha: str) -> dict:
        campos = [self.split(linha=linha, tamanho_campo=tamanho)
                  for tamanho in self.tamanho_campos]
        self.posicao_inicial = 0
        return dict(zip(self.nomes_campos, campos))


if __name__ == '__main__':
    path_in = 'dados/COTAHIST_A2020/COTAHIST_A2020.TXT'
    lines = gerar_linhas(path_in)
    next(lines)
    line01 = next(lines)
    line02 = next(lines)
    campos = CamposHistoricoB3()

    line_first = campos.get_campos(line01)
    line_second = campos.get_campos(line02)
    print(line_second)
