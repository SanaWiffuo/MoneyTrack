import requests 
from bs4 import BeautifulSoup as soup
import json
import pandas as pd
from fake_useragent import UserAgent

my_url = 'https://www.lazada.sg/catalog/?spm=a2o42.home.search.1.64e646b5uVoSRh&q=monitor&_keyori=ss&from=search_history&sugg=monitor_0_1'  

ua = UserAgent()
userAgent = ua.random
headers = {'User-Agent': userAgent}


ret = requests.get(my_url,headers=headers)


page_soup = soup(ret.text, 'lxml')

data = page_soup.select("[type='application/ld+json']")[1]
oJson = json.loads(data.text)["itemListElement"]
numProducts = len(oJson)
results = []

for product in oJson:
    results.append([product['name'], product['offers']['price'], product['image'],product['url']])  # etc......

df =  pd.DataFrame(results)
print(df)