import pandas as pd
from itertools import combinations
from collections import Counter

data = pd.read_csv("market_basket_transactions.csv").fillna('')
transactions = data[['Product1','Product2','Product3','Product4','Product5']].values.tolist()

counter = Counter()
for t in transactions:
    items = [i for i in t if i]
    for r in [2, 3]:
        counter.update(combinations(sorted(items), r))

total = len(transactions)
product = input("Enter a product name: ")

related = [(combo, (count/total)*100) for combo, count in counter.items() if product in combo]
related = sorted(related, key=lambda x: x[1], reverse=True)[:5]

for combo, pct in related:
    print(f"{combo} --> {pct:.2f}%")
