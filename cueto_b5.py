

for i in range(0, len(df)):
if((df.iloc[i]['Scientific Name']!='Pomacentrus adelus')):
    print df.loc[df['Scientific Name'] == df.iloc[i]['Scientifc Name'], df.iloc[i]['Count']].mean()