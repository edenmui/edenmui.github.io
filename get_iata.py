# %%
doc = '/Users/emporius/Downloads/airports.csv'
import pandas as pd
df = pd.read_csv(doc)
df
# %%
df = df[df['type'] != 'closed']

# %%
df.to_json('iata.json', orient='index')
# %%
iata = df[['iata_code', 'name']].dropna()
# %%
iata.columns = ['IATA', 'Name']
iata['ID'] = range(0,iata.shape[0])
iata.set_index('ID', drop=True, inplace=True)
# %%
iata.to_json('iata.json', orient='index')
# %%
# %%
