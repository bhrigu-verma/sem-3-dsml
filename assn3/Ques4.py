import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'.\sales.csv')

products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']

df.plot(x='month_number', y=products, kind='bar', stacked=True, figsize=(10, 5))
plt.title('Stacked Bar Chart of Monthly Sales Figures')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.show()
