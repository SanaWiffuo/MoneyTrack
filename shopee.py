import requests
import pandas as pd
from fake_useragent import UserAgent
import sys
from classes import Product, Shopee
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def scrap_shopee(keyword_search, total_of_result):

    ua = UserAgent()
    userAgent = ua.random
    Shopee_url = 'https://shopee.sg'

    headers = {
        'User-Agent': userAgent,
        'Referer': '{}search?keyword={}'.format(Shopee_url, keyword_search)
    }
    url = 'https://shopee.sg/api/v2/search_items/?by=relevancy&keyword={}&limit=100&newest=0&oanrder=desc&page_type=search'.format(
        keyword_search)
    print(url)
    r = requests.get(url, headers=headers).json()

    product_lst = []
    num = 0
    for item in r['items']:
        if total_of_result == num:
            break

        url = "https://shopee.sg/"
        for i in item['name']:

            if i.isalpha() == True:
                url += i

            elif i.isdigit() == True:
                url += i

            else:
                if url[-1] == "-":
                    continue
                url += "-"
        num += 1

        product_lst.append(Shopee(item['name'], "$"+str(item['price_min']/100000), str(round(item['item_rating'].get("rating_star"), 2))+"("+str(
            int(sum(item['item_rating'].get("rating_count"))/2))+")", url+"-i.{}.{}".format(item['shopid'], item['itemid']),""))
        # i wrote these based on the structure of the url by combining the name + shopid + itemid
        
        
       
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') 
    options.add_argument('start-maximized') 
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    browserdriver = webdriver.Chrome(options = options)
    
    for i in range(len(product_lst)):
        browserdriver.get(product_lst[i].url)
        time.sleep(2)
        products = [item for item in WebDriverWait(browserdriver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[type="application/ld+json"]')))]
        products_json = [product.get_attribute('innerHTML') for product in products[1:]]
        
        for product in products_json:
            try:
                product_lst[i].pic = json.loads(product)['image']
                print(product_lst[i].pic)
            except KeyError:
                pass
            
    browserdriver.quit()
        
    if len(product_lst) == 0:
        print("Fail")
        sys.exit()

    return product_lst


if __name__ == "__main__":
    df = pd.DataFrame([t.__dict__ for t in scrap_shopee("monitor", 5)])
    print(df)
