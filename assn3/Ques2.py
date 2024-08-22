import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'.\sales.csv')

products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']

data = [df[product] for product in products]

plt.figure(figsize=(10, 5))
plt.boxplot(data, labels=products)
plt.title('Distribution of Monthly Sales for Each Product')
plt.xlabel('Product')
plt.ylabel('Total Units Sold')
plt.show()
