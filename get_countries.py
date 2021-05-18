# %%
doc = 'Assets/countries.csv'
import pandas as pd
from pandas.core.indexes.base import ensure_index
df0 = pd.read_csv(doc)

df = df0[['code', 'name', 'id']].copy()
df['Countries'] = df['code'] + ' - ' + df['name']

lst = []
for id, name in zip(df['code'], df['Countries']):
    lst.append({"ID": f"{str(id).zfill(6)}", "Code - Country": name})

import json
content = json.dumps(lst,ensure_ascii=False)
with open('country_codes.json', 'w', encoding='utf-8') as js:
    js.write(content)

# %%