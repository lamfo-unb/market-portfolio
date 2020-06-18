import pandas as pd
import re

path_in = 'dados/TradeIntraday_20200617_1/TradeIntraday_20200617_1.txt'
dados = pd.read_csv(path_in, sep=';', decimal=',')
header = dados.head(100)
simbolos = dados['TckrSymb'].nunique()
simbolos = pd.Series(simbolos)

dados['TckrSymb'].value_counts()

lame = dados.query("TckrSymb == 'LAME4'")
lame.reset_index(drop=True, inplace=True)
lame.loc[:, 'NtryTm'] = lame['NtryTm'].apply(lambda x: str(x))
lame['NtryTm'].str.extract(r"^[0-9]{4}")
valor = lame['NtryTm'][0]

# Obtendo horário de negociação do papel
padrao = re.compile(r'^[0-9]{4}')
padrao.findall()


def extract_pattern(pattern: re.Pattern, string: str) -> str:
    busca = pattern.findall(string=string)
    try:
        res = busca[0]
    except IndexError:
        res = ''
    return res


lame['horario'] = lame['NtryTm'].apply(lambda x: extract_pattern(padrao, x))
