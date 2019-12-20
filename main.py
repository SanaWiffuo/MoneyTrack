from lazada import scrap_lazada

from shopee import scrap_shopee


title_lst = []
price_lst = []

temp1,temp2 = scrap_lazada()
for i in range(len(temp1)):
    title_lst.append(temp1[i])
    price_lst.append(temp2[i])

temp1,temp2 = scrap_shopee()
for i in range(len(temp1)):
    title_lst.append(temp1[i])
    price_lst.append(temp2[i])

    
print(title_lst)
print(price_lst)