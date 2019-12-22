class Product:
    def __init__(self,name,price,ratings,url):
        self.name = name
        self.price = price
        self.ratings = ratings
        self.url = url
        
class Lazada(Product):
    def __init__(self,name,price,ratings,url):
        super().__init__(name,price,ratings,url)
        self.platform = "Lazada"
        
class Shopee(Product):
     def __init__(self,name,price,ratings,url):
        super().__init__(name,price,ratings,url)
        self.platform = "Shopee"
        
    
    