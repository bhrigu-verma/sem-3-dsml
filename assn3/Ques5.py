import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'.\sales.csv')

products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']

total_units_per_product = df[products].sum()

plt.figure(figsize=(7, 7))
plt.pie(total_units_per_product, labels=products, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Total Sales by Product')
plt.show()
