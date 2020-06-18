

from pandas_datareader import data
import pandas as pd

SYMBOLS = ['PETR4.SA', 'LAME4.SA', 'ITSA4.SA']
START = '2016-01-01'
END = '2019-12-30'

data = data.DataReader(
    name=SYMBOLS,
    data_source='yahoo',
    start=START,
    end=END
)['Close']

resume = pd.DataFrame(
    {
        'colunms': data.columns,
        'types': data.dtypes,
        'nulls': data.isna().sum()
    }
)
resume.reset_index(inplace=True, drop=True)

