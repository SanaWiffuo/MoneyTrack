class Product:
    def __init__(self,name,price,ratings,url):
        self.name = name
        self.price = price
        self.ratings = ratings
        self.url = url
        
class Lazada:
    def __init__(self,name,price,ratings,url):
        super().__init__(name,price,ratings,url)
        self.platform = "Lazada"
        
class Shopee:
     def __init__(self,name,price,ratings,url):
        super().__init__(name,price,ratings,url)
        self.platform = "Shopee"
        
    
    