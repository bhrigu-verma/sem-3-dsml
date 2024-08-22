import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'.\sales.csv')

products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']

df.plot(x='month_number', y=products, kind='bar', figsize=(10, 5))
plt.title('Monthly Sales Figures of All Products')
plt.xlabel('Month')
plt.ylabel('Units sold')
plt.show()
