import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'.\sales.csv')

campaign_data = {
    'Product': ['Facecream', 'Facewash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer'],
    'Start Month': [1, 2, 3, 4, 5, 6],
    'End Month': [3, 4, 5, 6, 7, 8]
}

gantt_df = pd.DataFrame(campaign_data)

plt.figure(figsize=(10, 5))
plt.barh(gantt_df['Product'], gantt_df['End Month'] - gantt_df['Start Month'], left=gantt_df['Start Month'])
plt.title('Gantt Chart for Sales Campaigns')
plt.xlabel('Month')
plt.ylabel('Product')
plt.show()
