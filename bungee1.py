import pandas as pd
groc_item= pd.read_csv("main.csv")
groc_item.head()
groc_item.groupby('product_description')['price'].mean()
groc_item["price_new"] = groc_item['price'].fillna(groc_item.groupby('product_description')['price'].transform("mean"))
groc_item[grocery["price"].isna()].head()




