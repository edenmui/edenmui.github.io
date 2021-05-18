# %%
doc = 'Assets/countries.csv'
import pandas as pd
from pandas.core.indexes.base import ensure_index

df0 = pd.read_csv(doc)

df = df0[['code', 'name', 'id']].copy()
df['Countries'] = df['code'] + ' - ' + df['name']
df['Index'] = range(0,df.shape[0])
df['Index'] = df['Index'].apply(lambda x: str(x).zfill(4))
df.dropna(inplace=True)
lst = []

for id, name in zip(df['Index'], df['Countries']):
    lst.append(
        {"ID": id, "Country": name})

import json

content = json.dumps(lst,ensure_ascii=False)
with open('country_codes.json', 'w') as js:
    js.write(content)

# %%
