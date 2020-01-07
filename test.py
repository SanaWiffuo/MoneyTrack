import requests 
from classes import Product,Lazada
from bs4 import BeautifulSoup as soup
import json
import pandas as pd
from fake_useragent import UserAgent



my_url = "https://shopee.sg/search?keyword=monitor"
ua = UserAgent()
userAgent = ua.random
headers = {'User-Agent': userAgent}


ret = requests.get(my_url,headers=headers)
page_soup = soup(ret.text, 'html.parser')
print(page_soup)

data = page_soup.select("[type='application/ld+json']")[2]
print(data)
oJson = json.loads(data.text)
print(oJson)
results = []

for product in oJson:
    results.append(Lazada(product['name'],"$"+product['offers']['price'],"",product['url'], product['image']))
   
print(results)
    
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

# if __name__ == "__main__":
#     df = pd.DataFrame([t.__dict__ for t in scrap_lazada("monitor",5)])
#     print(df)