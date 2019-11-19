import requests
import json
import re
# getting date from firebase (json)
r = requests.get('https://stan-izone.firebaseio.com/users.json')

print(r.json())

# webscraping
url = 'https://www.lazada.sg/products/acer-eb321hqu-d-315-inch-wqhd-ips-new-monitor-i444318328-s1181378318.html?spm=a2o42.searchlist.list.1.4f5a5c5bfVd3HS&search=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

html = requests.get(url, headers=headers)
print(html)
