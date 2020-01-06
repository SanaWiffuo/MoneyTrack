import requests 
from classes import Product,Lazada
from bs4 import BeautifulSoup as soup
import json
import pandas as pd
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options


def scrap_lazada(search_item,total_of_result):
    my_url = "https://www.lazada.sg/catalog/?spm=a2o42.home.search.1.654346b5pMzA3m&q={}&_keyori=ss&from=search_history&sugg=monitor_0_1".format(search_item)

    ua = UserAgent()
    userAgent = ua.random
    headers = {'User-Agent': userAgent}


    ret = requests.get(my_url,headers=headers)
    page_soup = soup(ret.text, 'lxml')

    data = page_soup.select("[type='application/ld+json']")[1]
    oJson = json.loads(data.text)["itemListElement"]
    results = []

    for product in oJson:
        results.append(Lazada(product['name'], product['offers']['price'],"",product['url'], product['image']))
        if len(results)==total_of_result:
            break
        
    return results
    
#for ratings   it is damn slow!!!
# webdriver_path= "/usr/local/bin/chromedriver"
# options = webdriver.ChromeOptions()
# options.add_argument('--headless') 
# options.add_argument('start-maximized') 
# options.add_argument('disable-infobars')
# options.add_argument('--disable-extensions')

# browser = webdriver.Chrome(webdriver_path,options=options)

# for i in range(len(results)):
#     browser.get("{}".format(results[i].url))
#     ratings = browser.find_elements_by_class_name('score-average')
#     ratings_count = browser.find_elements_by_class_name('count')
#     num_of_ratings = [i for i in ratings_count[0].text if i.isdigit()==True]
#     results[i].ratings = ratings[0].text+"("+"".join(num_of_ratings)+")"
# browser.quit()
if __name__ == "__main__":
    df = pd.DataFrame([t.__dict__ for t in scrap_lazada("monitor",5)])
    print(df)