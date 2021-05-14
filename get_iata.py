# %%
doc = '/Users/emporius/Downloads/airports.csv'
import pandas as pd
df = pd.read_csv(doc)
df
# %%
df = df[df['type'] != 'closed']

# %%
iata = df[['iata_code', 'name']].dropna()
# %%
iata.columns = ['IATA', 'Name']
iata['ID'] = range(0,iata.shape[0])
iata.set_index('ID', drop=False, inplace=True)
# %%
iata.to_json('iata.json', orient='index')

# %%
iata
# %%
lst = []
for iata, name, id in zip(iata['IATA'], iata['Name'], iata['ID']):
    lst.append(dict({"ID":id, "IATA":iata, "Name":name}))
# %%
import json
with open('iata.json', 'w') as js:
    content = json.dumps(lst)
    js.write(content)
# %%

# %%
