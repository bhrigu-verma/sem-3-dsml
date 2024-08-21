import pandas as pd
def load_and_inspect():
    df = pd.read_csv(r"C:\Users\TANUSH\OneDrive\Desktop\sales.csv")
    print(df.head())
    print(df.info())
    print(df.describe())

load_and_inspect()