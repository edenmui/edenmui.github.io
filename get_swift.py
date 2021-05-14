# %%
doc = 'Assets/BIC.csv'
import pandas as pd

df = pd.read_csv(doc)
df['SWIFT_BIC11'] = df['SWIFT_BIC8'] + df['BRANCH']
# %%
df
# %%
