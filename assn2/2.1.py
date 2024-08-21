import pandas as pd 
#a) Create a DataFrame with the above data.

data={
    "Names": ['Alice','Bob','Charlie','David','Eve'],
    "ages":[25,30,35,40,45],
    "cities":['New York','Los Angeles','Chicago','Houston','Phoenix'],
    "scores":[85.5, 90.3, 78.9, 88.5, 92.7]
}

#b) Display the first 3 rows of the DataFrame.
c = pd.DataFrame(data)
print(c.loc[[0,1]])

#c) Display the summary statistics of the DataFrame.
print(c.describe())
#d) Display the data types of each column.
print(c.info())