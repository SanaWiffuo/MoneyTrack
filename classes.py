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

