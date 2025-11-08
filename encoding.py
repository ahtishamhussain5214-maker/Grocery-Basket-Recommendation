import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

data = pd.read_csv("market_basket_transactions.csv")
data = data.fillna('')

transactions = data[['Product1', 'Product2', 'Product3', 'Product4', 'Product5']].values.tolist()

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)

basket = pd.DataFrame(te_ary, columns=te.columns_).astype(int)

print(basket.head(20))
