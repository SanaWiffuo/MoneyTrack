from lazada import scrap_lazada
from shopee import scrap_shopee
import pandas as pd

product_lst = []

search_item = input("Please enter the product name:")
total_of_result = int(input("Please enter the number of result:"))

temp1= scrap_lazada(search_item,total_of_result)
for i in temp1:
    product_lst.append(i)

temp1 = scrap_shopee(search_item,total_of_result)
for i in temp1:
    product_lst.append(i)

    
df = pd.DataFrame([t.__dict__ for t in product_lst])
print(df)