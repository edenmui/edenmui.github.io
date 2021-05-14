# %%
doc = '/Users/emporius/Downloads/airports.csv'
import pandas as pd
df = pd.read_csv(doc)
df
# %%
df = df[df['type'] != 'closed']
# %%
df
# %%
df.to_json?
# %%
df.to_json('iata.json', orient='index')
# %%
