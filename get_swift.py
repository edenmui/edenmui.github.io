# %%
doc = 'Assets/BIC.csv'
import pandas as pd
from pandas.core.frame import DataFrame

df = pd.read_csv(doc)
df.columns = ['ID', 'ISO Country Code', 'Country Name', 'Bank Name', 'City', 'Branch', 'SWIFT' ]
# %%
df.fillna('-', inplace=True)
import numpy as np
df['Type'] = df['Branch'].apply(lambda x: 'H' if x == '-' else 'B')
df
# %%
# %%
