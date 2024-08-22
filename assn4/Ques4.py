import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/piyus/OneDrive/Desktop/Piyush/DSML/DSMLAss4/DSMLdataprepo.csv'
df = pd.read_csv(file_path)

class_distribution = df['category_desc'].value_counts()

print("Class distribution:\n")
print(class_distribution)

plt.figure(figsize=(10, 6))
class_distribution.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Class Distribution in category_desc')
plt.xlabel('Classes')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.show()