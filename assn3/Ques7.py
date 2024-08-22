import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'.\sales.csv')

products_to_compare = ['facecream', 'facewash', 'toothpaste']

df.plot(x='month_number', y=products_to_compare, kind='bar', figsize=(10, 5))
plt.title('Comparison of Monthly Sales for Facecream, Facewash, and Toothpaste')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.show()
