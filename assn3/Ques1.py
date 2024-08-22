import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'.\sales.csv')

plt.figure(figsize=(10, 6))
plt.hist(df['total_profit'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Total Profit Across All Months')
plt.xlabel('Total Profit')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()