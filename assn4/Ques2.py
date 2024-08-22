import pandas as pd

file_path = 'C:/Users/piyus/OneDrive/Desktop/Piyush/DSML/DSMLAss4/DSMLdataprepo.csv'
df = pd.read_csv(file_path)

missing_values = df.isnull().sum()
columns_with_missing = missing_values[missing_values > 0]
print("Columns with missing values:\n")
print(columns_with_missing)

columns_to_drop = columns_with_missing[columns_with_missing >= 3].index
df.drop(columns=columns_to_drop, inplace=True)
print(f"\nDropped columns with 3 or more missing values: {list(columns_to_drop)}")

for column in columns_with_missing.index:
    if column not in columns_to_drop:
        if df[column].dtype in ['float64', 'int64']:
            median_value = df[column].median()
            df[column].fillna(median_value, inplace=True)
            print(f"Filled missing values in '{column}' with median: {median_value}")
        else:
            most_frequent_value = df[column].mode()[0]
            df[column].fillna(most_frequent_value, inplace=True)
            print(f"Filled missing values in '{column}' with most frequent value: {most_frequent_value}")