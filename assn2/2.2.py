import pandas as pd 

data={
    "Names": ['Alice','Bob','Charlie','David','Eve'],
    "ages":[25,30,35,40,45],
    "cities":['New York','Los Angeles','Chicago','Houston','Phoenix'],
    "scores":[85.5, 90.3, 78.9, 88.5, 92.7]
}
c = pd.DataFrame(data)

print(c["Names"])
print(c["scores"])
d = c.query('ages>30')
print(d)
options =["Chicago","Houston"]
e=c[(c['cities'].isin(options))]
print(e)