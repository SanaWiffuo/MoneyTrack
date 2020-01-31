import requests 
from bs4 import BeautifulSoup as soup
import json
import pandas as pd
from fake_useragent import UserAgent
from firebase.firebase import FirebaseApplication
import time
from datetime import datetime
from pytz import timezone

def shopee(url):
    itemidlst = []
    shopidlst = []
    check = 0
    for i in url[::-1]:
        if i == ".":
            check += 1
        if check == 0:
            if i.isdigit():
                itemidlst.append(i)
        elif check == 1:
            if i.isdigit():
                shopidlst.append(i)
    itemidlst.reverse()
    itemid = "".join(itemidlst)
    shopidlst.reverse()
    shopid = "".join(shopidlst)
  
    ua = UserAgent()
    userAgent = ua.random
    headers = {
        'User-Agent': userAgent,
    }
    url = "https://shopee.sg/api/v2/item/get?itemid={}&shopid={}".format(itemid,shopid)
    r = requests.get(url, headers=headers).json()
    
    price = "$" + str(r['item']['price']/100000)
        
    return price

def lazada(url):
    ua = UserAgent()
    userAgent = ua.random
    headers = {
        'User-Agent': userAgent,
        'Referer': "https://www.lazada.sg"
        }

    ret = requests.get(url,headers=headers)
    page_soup = soup(ret.text, 'lxml')
    try:
        data = page_soup.select("[type='application/ld+json']")[0]
    except IndexError:
        return
    price = json.loads(data.text)["offers"]["price"]
    
    return price



url = "https://productify-3f2ab.firebaseio.com/"  

firebase = FirebaseApplication(url, None)
fmt = "%Y-%m-%d %H:%M:%S"
if __name__ == "__main__":
    while True:
        result = firebase.get("/", None)
        for name in result:
            if name == "users":
                continue
            for i in result[name]:
                if result[name][i]['platform'] == "Lazada":
                    url = result[name][i]['product url']
                    print(url)
                    price = lazada(url)
                    now_utc = datetime.now(timezone('UTC'))
                    now_pacific = now_utc.astimezone(timezone('Singapore'))
                    t = now_pacific.strftime(fmt)
                    firebase.patch("/{}/{}".format(name,i),{"scrape-price":price,"Last-updated":t})
                elif result[name][i]['platform'] == "Shopee":
                    url = result[name][i]['product url']
                    print(url)
                    price = shopee(url)
                    now_utc = datetime.now(timezone('UTC'))
                    now_pacific = now_utc.astimezone(timezone('Singapore'))
                    t = now_pacific.strftime(fmt)
                    firebase.patch("/{}/{}".format(name,i),{"scrape-price":price,"Last-updated":t})
                # time.sleep(120)
        print("Finished updating")
        time.sleep(1800)
        
            
