import pandas as pd

file_path = '/DSMLdataprepo.csv'
df = pd.read_csv(file_path)

print("Data types of columns before correction :- \n")
print(df.dtypes)

for column in df.columns:
    if df[column].dtype == 'object':
        try:
            df[column] = pd.to_numeric(df[column])
        except ValueError:
            pass

print("\nData types of columns after correction :- \n")
print(df.dtypes)