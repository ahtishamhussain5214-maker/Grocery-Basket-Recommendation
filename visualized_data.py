import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv("market_basket_transactions.csv")

all_items = pd.concat([
    df['Product1'], df['Product2'], df['Product3'], df['Product4'], df['Product5']
])

top_items = all_items.value_counts().head(50)

sns.barplot(x=top_items.values, y=top_items.index)
plt.title("Top Selling Items")
plt.xlabel("Number of Occurrences")
plt.ylabel("Product Name")
plt.show()
