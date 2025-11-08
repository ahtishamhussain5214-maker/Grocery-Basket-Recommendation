import pandas as pd

#in this code ill remove these columns who have more 50% unfill data.....
data = pd.read_csv("market_basket_transactions.csv")
data = data.drop(["Product3", "Product4", "Product5"], axis=1)
print(data.isnull().sum())
