import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\TANUSH\OneDrive\Desktop\sales.csv")
(df.plot(x="month_number",y=["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"]))
plt.show()

plt.bar(df['month_number'], df['total_units'], color='skyblue')
plt.show()
products=["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"]

total_sales_by_product = df[products].sum()
plt.pie(total_sales_by_product, labels=total_sales_by_product.index)
plt.show()