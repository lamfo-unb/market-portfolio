
#%%
import pandas as pd

dados = pd.read_csv('dados/black_friday.csv')
dados = pd.DataFrame(dados)
header = dados.head(50)

#%%
resumo = pd.DataFrame(
    {
        'colunas': dados.columns,
        'tipos': dados.dtypes,
        'nulos': dados.isna().sum()
    }
)

resumo.reset_index(drop=True, inplace=True)

# %%
product_category_3 = dados['Product_Category_3']
product_category_3 = pd.Series(product_category_3)
product_category_3.dropna(inplace=True)
product_category_3.mode()

# %%
