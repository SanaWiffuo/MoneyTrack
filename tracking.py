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
                if result[name][i]['platform'] == "lazada":
                    url = result[name][i]['product url']
                    price = lazada(url)
                    firebase.patch("/{}/{}".format(name,i),{"scrape-price":price})
                elif result[name][i]['platform'] == "shopee":
                    url = result[name][i]['product url']
                    price = shopee(url)
                    firebase.patch("/{}/{}".format(name,i),{"scrape-price":price})
            time.sleep(60)
        time.sleep(1800)
            

# result = firebase.post("/zachary",{"name":"Ansmite 24' 75Hz IPS Curved FHD LED Monitor Hdmi HDR Super Slim and Sleek Design","platform":"shopee","product url":
#     "https://shopee.sg/Anmite-24-75Hz-IPS-Curved-FHD-LED-Monitor-Hdmi-HDR-Super-Slim-and-Sleek-Design-i.152295628.2285979907","initial-price":300,"scrape-price":0})
# result = firebase.post("/hwen",{"name":"AMD Ryzen 7 3700X R7 3700X 3.6 GHz Eight-Core Sinteen-Thread CPU Processor 7NM L3=32M 100-000000071 Socket AM4 new and with fan","platform":"lazada","product url":
#     "https://www.lazada.sg/products/amd-ryzen-7-3700x-r7-3700x-36-ghz-eight-core-sinteen-thread-cpu-processor-7nm-l332m-100-000000071-socket-am4-new-and-with-fan-i556430870-s1579876774.html?spm=a2o42.searchlist.list.1.6e178e5dnIln3D&search=1"
#     ,"initial-price":351,"scrape-price":0})