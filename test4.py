from firebase.firebase import FirebaseApplication
from classes import Track
import pandas as pd
url = "https://productify-3f2ab.firebaseio.com/"
firebase = FirebaseApplication(url, None)
result = firebase.get("/{}".format("f"), None)
products = []
for key in result:
    p = result[key]
    last_updated = p['Last-updated']
    initial_price = p['initial-price']
    name = p['name']
    platform = p['platform']
    url = p['product url']
    scrape_price = p['scrape-price']
    products.append(Track(name,initial_price,scrape_price,url,last_updated,platform))
    
df = pd.DataFrame([t.__dict__ for t in products])
print(df)