import pandas as pd
import random


num_transactions = 2500

products = [
    "Bread", "Milk", "Eggs", "Butter", "Cheese", "Apples", "Bananas", "Oranges",
    "Chicken", "Rice", "Pasta", "Cereal", "Juice", "Tea", "Coffee", "Sugar",
    "Salt", "Soap", "Shampoo", "Toothpaste", "Chips", "Biscuits", "Coke",
    "Pepsi", "Water Bottle", "Cake", "Donut", "Pizza", "Burger", "Ice Cream"
]


transactions = []
for t in range(1, num_transactions + 1):
    num_items = random.randint(2, 5)
    selected_items = random.sample(products, num_items)
    row = [t] + selected_items + [None] * (5 - num_items)
    transactions.append(row)


columns = ["TransactionID", "Product1", "Product2", "Product3", "Product4", "Product5"]
df = pd.DataFrame(transactions, columns=columns)


df.to_csv("market_basket_transactions.csv", index=False)

print("✅ market_basket_transactions.csv created successfully!")
