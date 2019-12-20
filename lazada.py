from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import pandas as pd

opts = Options()
ua = UserAgent()
userAgent = ua.random
opts.add_argument(f'user-agenta={userAgent}')

webdriver_path= "/usr/local/bin/chromedriver"
Lazada_url = "https://www.lazada.sg"
search_item = input("Please enter the product name:")
total_of_result = int(input("Please enter the number of result:"))

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


titles_list = []
prices_list = []

if len(item_titles)==0:
    print("Fail")
    
for i in range(total_of_result):
    titles_list.append(item_titles[i].text)
    prices_list.append(item_prices[i].text)


dfL = pd.DataFrame(zip(titles_list, prices_list), columns=['ItemName', 'Price'])
print(dfL)

browser.quit()