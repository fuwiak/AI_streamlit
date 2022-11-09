import pandas as pd


path ='../data/Kazachstan_dataset.csv'

df = pd.read_csv(path, sep=',')

#extract float values from the column Latitude
df['lat'] = df['Latitude'].str.extract('(\d+\.\d+)', expand=False).astype(float)

df['lot'] = df['Longitude'].str.extract('(\d+\.\d+)', expand=False).astype(float)
df["Number of Protesters"].fillna(0, inplace = True)
df["Number of Protesters"] = df["Number of Protesters"].replace("Unknown", 0)
df["Number of Protesters"] = df["Number of Protesters"].astype(int)

df.to_csv('../data/df.csv', index=False)
