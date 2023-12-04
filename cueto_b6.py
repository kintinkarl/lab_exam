import pandas as pd
import random as r

df = pd.read_csv("Exam_Table.csv").dropna()
df.insert(0, "Location", [i for i in range(len(df.index))])
df.insert(0, "Site", [i for i in range(len(df.index))])
df.insert(0, "Replicate", [i for i in range(len(df.index))])

print(df)