# %%
doc = 'Assets/swift.csv'
import pandas as pd

df = pd.read_csv(doc)
df.columns = ['ID', 'ISO Country Code', 'Country Name', 'Bank Name', 'City', 'Branch', 'SWIFT' ]

df.fillna('Head Office', inplace=True)
import numpy as np

df['Type'] = df['Branch'].apply(lambda x: 'H' if x == '-' else 'B')

#df.set_index('SWIFT', inplace=True, drop=False)

target_countries = ['CN',
 'HK',
 'TR',
 'IN',
 'RS',
 'VG',
 'LU',
 'FR',
 'GB',
 'MA',
 'BD',
 'TW',
 'PK',
 'ID',
 'ES',
 'CA',
 'CZ',
 'SG',
 'GR',
 'VN',
 'EG',
 'KH',
 'US',
 'KR',
 'NL',
 'LK',
 'AE',
 'IL',
 'TH',
 'TN',
 'PL',
 'DK',
 'IT']

df = df[df['ISO Country Code'].isin(target_countries)]
df.to_csv('swift.csv')

df['SWIFT + NAME'] = df['SWIFT'] + ' - ' + df['Bank Name']
# %%
df = df.apply(lambda x: x.apply(lambda y: str(y).title()))
import json

banned = '''AD AI AG AW BS BH BZ BM BW VG KY CK CY DM ET GH GI GD GG IR IM JE LR LI MT MH MC MS NR BQ NU PA WS SM RS SC LC KN VC'''
banned = banned.split(' ')
df = df.query("`ISO Country Code` not in @banned")

lst = []
for id, swift_name in zip(df['ID'], df['SWIFT + NAME']):
    lst.append({"ID":f"{str(id).zfill(6)}", "BANK": swift_name.upper()})

content = json.dumps(lst, ensure_ascii=False)
with open('swift.json', 'w', encoding='utf-8') as js:
    js.write(content)
# %%
