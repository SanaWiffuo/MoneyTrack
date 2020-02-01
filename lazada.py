import requests 
from classes import Lazada
from bs4 import BeautifulSoup as soup
import json
import pandas as pd
from fake_useragent import UserAgent

def scrape(search_item,total_of_result):
    my_url = "https://www.lazada.sg/catalog/?q={}".format(search_item)

    ua = UserAgent()
    userAgent = ua.random
    headers = {
        'User-Agent': userAgent,
        'Referer': "https://www.lazada.sg"
        }

    ret = requests.get(my_url,headers=headers)
    page_soup = soup(ret.text, 'lxml')
    data = page_soup.select("[type='application/ld+json']")[1]
    oJson = json.loads(data.text)["itemListElement"]
    results = []

    for product in oJson:
        results.append(Lazada(product['name'],product['offers']['price'],"Unavailable",product['url'], product['image']))
        if len(results)==total_of_result:
            break
    df = pd.DataFrame([t.__dict__ for t in results])
    print(df)
    return results

if __name__ == "__main__":
    lst = scrape("monitor",20)
    df = pd.DataFrame([t.__dict__ for t in lst])
    print(df)
