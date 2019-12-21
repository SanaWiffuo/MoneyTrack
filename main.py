from lazada import scrap_lazada
from shopee import scrap_shopee
import pandas as pd


title_lst = []
price_lst = []

search_item = input("Please enter the product name:")
total_of_result = int(input("Please enter the number of result:"))

temp1,temp2 = scrap_lazada(search_item,total_of_result)
for i in range(len(temp1)):
    title_lst.append(temp1[i])
    price_lst.append(temp2[i])

temp1,temp2 = scrap_shopee(search_item,total_of_result)
for i in range(len(temp1)):
    title_lst.append(temp1[i])
    price_lst.append(temp2[i])

    
result = pd.DataFrame(zip(title_lst, price_lst), columns=['ItemName', 'Price'])
print(result)