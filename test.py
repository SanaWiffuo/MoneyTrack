from shopee import *
from classes import Shopee
def product_search(keyword_search,total_of_result):
    ua = UserAgent()
    userAgent = ua.random
    Shopee_url = 'https://shopee.sg'
    headers = {
        'User-Agent': userAgent,
        'Referer': '{}search?keyword={}'.format(Shopee_url, keyword_search)
    }
    url = 'https://shopee.sg/api/v2/search_items/?by=relevancy&keyword={}&limit={}&newest=0&order=desc&page_type=search&version=2'.format(
        keyword_search,total_of_result)
    print(url)
    r = requests.get(url, headers=headers)
    print(r.status_code)
    return r.json()

def product_detail(itemid,shopid):
    ua = UserAgent()
    userAgent = ua.random
    headers = {
        'User-Agent': userAgent,
    }
    url = "https://shopee.sg/api/v2/item/get?itemid={}&shopid={}".format(itemid,shopid)
    r = requests.get(url, headers=headers)
    print(r.request.headers)
    print(r.status_code)
    
    return r.json()
    

if __name__ == "__main__":
    product_lst = []
    products = product_search("monitor",50)
    # print(products)
    for i in range(len(products['items'])):  
        itemid = products['items'][i]['itemid']
        shopid = products['items'][i]['shopid']
        item = product_detail(itemid, shopid)
        image = "https://cf.shopee.sg/file/{}".format(item['item']['images'][0])
        name = item['item']['name']
        ratings = str(round(item['item']['item_rating'].get("rating_star"), 2))+"("+str(
            int(sum(item['item']['item_rating'].get("rating_count"))/2))+")"
        price = "$" + str(item['item']['price']/100000)
        url = "https://shopee.sg"+"-i.{}.{}".format(shopid,itemid)
        product_lst.append(Shopee(name,price,ratings, url, image))
    df = pd.DataFrame([t.__dict__ for t in product_lst])
    print(df)

        