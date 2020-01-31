import requests 
from bs4 import BeautifulSoup as soup
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from firebase.firebase import FirebaseApplication
import time
from datetime import datetime

def shopee(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') 
    options.add_argument('start-maximized') 
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    browserdriver = webdriver.Chrome(options = options)

    browserdriver.get(url)
    time.sleep(2)
    products = [item for item in WebDriverWait(browserdriver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[type="application/ld+json"]')))]
    products_json = [product.get_attribute('innerHTML') for product in products[1:]]
    
    for product in products_json:
        try:
            price = json.loads(product)['offers']['price']
        except KeyError:
            pass
    
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

    data = page_soup.select("[type='application/ld+json']")[0]
    price = json.loads(data.text)["offers"]["price"]
    return price



url = "https://productify-3f2ab.firebaseio.com/"  

firebase = FirebaseApplication(url, None)

if __name__ == "__main__":
    while True:
        result = firebase.get("/", None)
        for name in result:
            for i in result[name]:
                if result[name][i]['platform'] == "Lazada":
                    url = result[name][i]['product url']
                    print(url)
                    price = lazada(url)
                    ts = time.time()
                    st = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    firebase.patch("/{}/{}".format(name,i),{"scrape-price":price,"Last-updated":st})
                elif result[name][i]['platform'] == "Shopee":
                    url = result[name][i]['product url']
                    print(url)
                    price = shopee(url)
                    ts = time.time()
                    st = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    firebase.patch("/{}/{}".format(name,i),{"scrape-price":price,"Last-updated":st})
                time.sleep(120)
        time.sleep(1800)
            
