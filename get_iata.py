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

iata['Airport'] = iata['iata_code'] + ' - ' + iata['name']
 # %%
iata['Airport'].to_json('iata.json', orient='index')
# %%
