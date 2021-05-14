# %%
doc = 'Assets/countries.csv'
from json import encoder
import pandas as pd

df = pd.read_csv(doc, )

# %%

filtered = df[['code', 'name', 'id']]
# %%
filtered['name'] = filtered['name'].apply(str.title).apply(lambda x: x.replace('.',''))
# %%

filtered['name'] = filtered['code'] + ' - ' + filtered['name']
lst = []
for id, name in zip(filtered['id'], filtered['name']):
    lst.append({"ID": id, "code": name})
# %%
import json

content = json.dumps(lst, ensure_ascii=False)
with open('iso3166.json', 'w', encoding='utf-8') as js:
    js.write(content)
# %%
