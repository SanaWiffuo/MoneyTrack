import requests
import pandas as pd

Shopee_url = 'https://shopee.sg'
keyword_search = 'Monitor'
headers = {
 'User-Agent': 'Chrome',
 'Referer': '{}search?keyword={}'.format(Shopee_url, keyword_search)
}
url = 'https://shopee.sg/api/v2/search_items/?by=relevancy&keyword={}&limit=100&newest=0&oanrder=desc&page_type=search'.format(keyword_search)

r = requests.get(url, headers = headers).json()

titles_list = []
prices_list = []

for item in r['items']:
    titles_list.append(item['name'])
    prices_list.append(item['price_min'])

Shopee = pd.DataFrame(zip(titles_list, prices_list), columns=['ItemName', 'Price'])
print(Shopee)