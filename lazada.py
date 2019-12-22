from classes import Product,Lazada
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import pandas as pd
import sys
import requests

def scrap_lazada(search_item,total_of_result):
    opts = Options()
    ua = UserAgent()
    userAgent = ua.random
    opts.add_argument(f'user-agenta={userAgent}')

    webdriver_path= "/usr/local/bin/chromedriver"
    Lazada_url = "https://www.lazada.sg"
    

    options = webdriver.ChromeOptions()
    options.add_argument('--headless') 
    options.add_argument('start-maximized') 
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')

    browser = webdriver.Chrome(webdriver_path,options=options)
    browser.get(Lazada_url)

    search_bar = browser.find_element_by_id("q")
    search_bar.send_keys(search_item)
    search_bar.submit()

    item_titles = browser.find_elements_by_class_name('c16H9d')
    item_prices = browser.find_elements_by_class_name('c13VH6')
    links = browser.find_elements_by_xpath("//div[@class='cRjKsc']/a")
    
    # titles_list = []
    # prices_list = []
    # url_list = []
    # ratings_list =[]
    
    product_lst = []
    
    if len(item_titles)==0:
        print("Fail")
        sys.exit()

    
    for i in range(total_of_result):
        # titles_list.append(item_titles[i].text)
        # prices_list.append(item_prices[i].text)
        # url_list.append(links[i].get_attribute("href"))
        product_lst.append(Lazada(item_titles[i].text,item_prices[i].text,"",links[i].get_attribute("href")))
        
    
    for i in range(len(product_lst)):
        browser.get("{}".format(product_lst[i].url))
        ratings = browser.find_elements_by_class_name('score-average')
        # ratings_list.append(ratings[0].text)
        product_lst[i].ratings = ratings[0].text
        

 
    # dfL = pd.DataFrame(zip(titles_list, prices_list,ratings_list,url_list), columns=['ItemName', 'Price','Ratings','Url'])
    # dfL['Platform'] = 'Lazada'
    # print(dfL)
    
    for i in product_lst:
        print(i.name,i.price,i.ratings,i.url,i.platform)

    browser.quit()
    
    return product_lst
scrap_lazada("demon slayer",10)