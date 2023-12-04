import pandas as pd

df1 = df[['Scientific Name', 'Size Est (cm)']].drop_duplicates()

print(df1)