
from pandas_datareader import data
import numpy as np

class DownloadData:
    
    def __init__(self, symbols, date_start, date_end, fonte_data = 'yahoo'):
        self.symbols = symbols
        self.date_start = date_start
        self.date_end = date_end
        self.fonte_data = fonte_data
        self._precos = None
    
    @property
    def precos(self):
        return self._precos

    
    def download_precos(self):
        
        self._precos = data.DataReader(
                name = self.symbols,
                data_source = self.fonte_data,
                start = self.date_start, end = self.date_end)['Close']
        
        return None


def main():
    SYMBOLS = ['PETR4.SA', 'LAME4.SA', 'ITSA4.SA']
    START = '2016-01-01'
    END = '2019-12-30'
    
    ativos = DownloadData(SYMBOLS, START, END)
    ativos.download_precos()
    
    return ativos

if __name__ == "__main__":
    data_ = main()
    print(data_.precos.head())
    