# %%
doc = 'Assets/countries.csv'
from json import encoder
import pandas as pd
df = pd.read_csv(doc, )
filtered = df[['code', 'name', 'id']].copy()
filtered['Countries'] = filtered['code'] + ' - ' + filtered['name']
lst = []
for id, name in zip(range(0,filtered.shape[0]), filtered['Countries']):
    lst.append({"ID": f"C{str(id).zfill(6)}", "Countries": name})

import json
content = json.dumps(lst, ensure_ascii=False)
with open('iso3166.json', 'w', encoding='utf-8') as js:
    js.write(content)

# %%
