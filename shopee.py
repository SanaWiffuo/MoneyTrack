import requests
import pandas as pd
from fake_useragent import UserAgent
import time
import random


ua = UserAgent()
userAgent = ua.random
Shopee_url = 'https://shopee.sg'
keyword_search = input("Please enter the product name: ")
headers = {
'User-Agent': userAgent,
'Referer': '{}search?keyword={}'.format(Shopee_url, keyword_search)
}
url = 'https://shopee.sg/api/v2/search_items/?by=relevancy&keyword={}&limit=100&newest=0&oanrder=desc&page_type=search'.format(keyword_search)

r = requests.get(url, headers = headers).json()

titles_list = []
prices_list = []

for item in r['items']:
    titles_list.append(item['name'])
    prices_list.append("$"+str(item['price_min']/100000))

Shopee = pd.DataFrame(zip(titles_list, prices_list), columns=['ItemName', 'Price'])
print(Shopee)

