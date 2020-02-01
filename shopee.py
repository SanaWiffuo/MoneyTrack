import requests
import pandas as pd
from fake_useragent import UserAgent
import json
from classes import Shopee


def product_search(keyword_search,total_of_result):
    ua = UserAgent()
    userAgent = ua.random
    Shopee_url = 'https://shopee.sg'
    headers = {
        'User-Agent': userAgent,
        'Referer': '{}search?keyword={}'.format(Shopee_url, keyword_search)
    }
    url = 'https://shopee.sg/api/v2/search_items/?by=relevancy&keyword={}&limit={}&newest=0&order=desc&page_type=search&version=2'.format(
        keyword_search,total_of_result)
    r = requests.get(url, headers=headers)
    
    return r.json()

def product_detail(itemid,shopid):
    ua = UserAgent()
    userAgent = ua.random
    headers = {
        'User-Agent': userAgent,
    }
    url = "https://shopee.sg/api/v2/item/get?itemid={}&shopid={}".format(itemid,shopid)
    r = requests.get(url, headers=headers)
    
    return r.json()
    
def scrap_shopee(keyword_search, total_of_result):
    product_lst = []
    products = product_search(keyword_search,total_of_result)
    for i in range(len(products['items'])):  
        itemid = products['items'][i]['itemid']
        shopid = products['items'][i]['shopid']
        item = product_detail(itemid, shopid)
        image = "https://cf.shopee.sg/file/{}".format(item['item']['images'][0])
        name = item['item']['name']
        ratings = str(round(item['item']['item_rating'].get("rating_star"), 2))+"("+str(
            int(sum(item['item']['item_rating'].get("rating_count"))/2))+")"
        price = item['item']['price']/100000
        url = "https://shopee.sg/"
        for i in name:
            if i.isalpha() == True:
                url += i
            elif i.isdigit() == True:
                url += i
            else:
                if url[-1] == "-":
                    continue
                url += "-"
        url = url+"-i.{}.{}".format(shopid,itemid)
        product_lst.append(Shopee(name,price,ratings, url, image))
    
    return product_lst

if __name__ == "__main__":
    while True:
        product_lst = scrap_shopee("monitor",20)
        df = pd.DataFrame([t.__dict__ for t in product_lst])
        print(df)


        