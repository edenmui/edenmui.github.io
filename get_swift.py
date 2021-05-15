# %%
doc = 'Assets/swift.csv'
import pandas as pd
from pandas.core.frame import DataFrame

df = pd.read_csv(doc)
df.columns = ['ID', 'ISO Country Code', 'Country Name', 'Bank Name', 'City', 'Branch', 'SWIFT' ]

df.fillna('Head Office', inplace=True)
import numpy as np

df['Type'] = df['Branch'].apply(lambda x: 'H' if x == '-' else 'B')

df.set_index('SWIFT', inplace=True, drop=False)

df['SWIFT + NAME'] = df['SWIFT'] + ' - ' + df['Bank Name'] + ' (' + df['Branch'] + '), ' + df['City'] + ', ' + df['Country Name']

import json

lst = []
for swift, swift_name in zip(df['SWIFT'], df['SWIFT + NAME']):
    lst.append({"SWIFT":swift, "BANK": swift_name})

content = json.dumps(lst, ensure_ascii=False)
with open('swift.json', 'w', encoding='utf-8') as js:
    js.write(content)

