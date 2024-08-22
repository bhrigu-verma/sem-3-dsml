import pandas as pd

file_path = 'C:/Users/piyus/OneDrive/Desktop/Piyush/DSML/DSMLAss4/DSMLdataprepo.csv'
df = pd.read_csv(file_path)

print("Data type before conversion :-",df['hits'].dtype)

df['hits'] = pd.to_numeric(df['hits'], errors='coerce')

print("\nData type after conversion :-",df['hits'].dtype)

print("\nFirst few rows after conversion :-",df[['hits']].head())