from test2 import scrap_lazada
from shopee import scrap_shopee
import pandas as pd
from threading import Thread
from multiprocessing import Process
import queue 
queue = queue.Queue()
search_item = "monitor"#input("Please enter the product name:")
total_of_result = 2 #int(input("Please enter the number of result:"))

# product_lst = scrap_lazada(search_item, total_of_result)
# product_lst.extend(scrap_shopee(search_item, total_of_result))

s = Thread(target=scrap_shopee,args=(search_item, total_of_result,queue))
s.start()
l = Thread(target=scrap_lazada ,args=(search_item, total_of_result,queue))
l.start()

result = queue.get()
s.join()
l.join()
result += queue.get()
df = pd.DataFrame([t.__dict__ for t in result])
print(df)
