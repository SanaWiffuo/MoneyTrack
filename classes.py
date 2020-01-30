class Product:
    def __init__(self, name, price, ratings, url , pic):
        self.name = name
        self.price = price
        self.ratings = ratings
        self.url = url
        self.pic = pic


class Lazada(Product):
    def __init__(self, name, price, ratings, url, pic):
        super().__init__(name, price, ratings, url, pic)
        self.platform = "Lazada"


class Shopee(Product):
    def __init__(self, name, price, ratings, url, pic):
        super().__init__(name, price, ratings, url, pic)
        self.platform = "Shopee"
        
class Track:
    def __init__(self, name, initial_price, scrape_price, url, last_updated, platform):
        self.name = name
        self.initial_price = initial_price
        self.scrape_price = scrape_price
        self.url = url
        self.last_updated = last_updated
        self.platform = platform
    

