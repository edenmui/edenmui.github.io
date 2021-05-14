# %%
doc = '/Users/emporius/Downloads/ISO3166-2_2020 - Sheet1.csv'
import pandas as pd
df = pd.read_csv(doc)
df = df.iloc[:,1:]
# %%
country = df[df['class'] == 'Country']

filtered = country[['Country', 'NameL']]
# %%
filtered['NameL'] = filtered['NameL'].apply(str.title).apply(lambda x: x.replace('.',''))
# %%

filtered['NameL'] = filtered['Country'] + ' - ' + filtered['NameL']
filtered['ID'] = range(0,filtered.shape[0])
lst = []
for id, name in zip(filtered['ID'], filtered['NameL']):
    lst.append({"ID": id, "Country": name})
# %%
import json
content = json.dumps(lst)
with open('iso3166.json', 'w') as js:
    js.write(content)
# %%
