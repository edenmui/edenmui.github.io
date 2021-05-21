# %%
doc = 'Assets/airports.csv'
import pandas as pd
df = pd.read_csv(doc)
df = df[df['type'] != 'closed']
iata = df[['iata_code', 'name', 'iso_country']].dropna()
iata.columns = ['IATA', 'Name', 'Country']
iata['ID'] = range(0,iata.shape[0])
iata.set_index('ID', drop=False, inplace=True)
iata['Name'] = iata['Country'] + ' - ' + iata['IATA'] + ' - ' + iata['Name']
lst = []
for name, id in zip(iata['Name'], iata['ID']):
    lst.append(dict({"ID":f"i{str(id).zfill(6)}",  "Name":name}))
import json
with open('iata.json', 'w') as js:
    content = json.dumps(lst)
    js.write(content)
# %%

iata
# %%
fil = iata[(iata['Country'].isin(['CN', 'LK', 'FR', 'IN', 'BD'])) & (iata['Name'].str.contains('International'))]
fil.to_excel('fil.xlsx')
# %%
