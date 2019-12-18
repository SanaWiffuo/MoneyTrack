# Web Scraping
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")

webdriver_path= "/usr/local/bin/chromedriver"
Lazada_url = "https://www.lazada.sg"
search_item = input("Please enter the product name:")
total_of_result = int(input("Please enter the number of result:"))

options = webdriver.ChromeOptions()
options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

browser = webdriver.Chrome(webdriver_path,options=options,chrome_options=opts)
browser.get(Lazada_url)

search_bar = browser.find_element_by_id("q")
search_bar.send_keys(search_item)
search_bar.submit()

item_titles = browser.find_elements_by_class_name('c16H9d')
item_prices = browser.find_elements_by_class_name('c13VH6')


titles_list = []
prices_list = []


for i in range(total_of_result):
    titles_list.append(item_titles[i].text)
    prices_list.append(item_prices[i].text)
# for title in item_titles:
#     titles_list.append(title.text)
# for price in item_prices:
#     prices_list.append(price.text)
print(titles_list)
print(prices_list)

