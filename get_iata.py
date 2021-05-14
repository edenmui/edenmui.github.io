# %%
doc = '/Users/emporius/Downloads/airports.csv'
import pandas as pd
df = pd.read_csv(doc)
df
# %%
df = df[df['type'] != 'closed']
df
# %%
iata = df[['iata_code', 'name', 'iso_country']].dropna()
# %%
iata.columns = ['IATA', 'Name', 'Country']
iata['ID'] = range(0,iata.shape[0])
iata.set_index('ID', drop=False, inplace=True)
# %%
# %%
iata['Name'] = iata['Country'] + ' - ' + iata['IATA'] + ' - ' + iata['Name']

# %%
lst = []
for name, id in zip(iata['Name'], iata['ID']):
    lst.append(dict({"ID":id,  "Name":name}))
# %%
import json
with open('iata.json', 'w') as js:
    content = json.dumps(lst)
    js.write(content)
# %%

# %%
