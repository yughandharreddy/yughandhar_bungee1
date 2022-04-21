import pandas as pd
groc_item= pd.read_csv("main.csv")
groc_item["sales_amount"]=groc_item["sale_quantity"].where( groc_item["unit"]!="pcs"),groc_item["product_description"].str.split("-",expand=True)[1].astype("float"),groc_item["sale_quantity"])