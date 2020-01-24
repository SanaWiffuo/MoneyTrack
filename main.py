from lazada import scrap_lazada
from shopee import scrap_shopee
import pandas as pd
from threading import Thread
import queue 

l_queue = queue.Queue()
s_queue = queue.Queue()
over = queue.Queue()
search_item = "ps4" #input("Please enter the product name:")
total_of_result = 10 #int(input("Please enter the number of result:"))

l = Thread(target=scrap_lazada ,args=(search_item, total_of_result,l_queue,over))
l.start()
s = Thread(target=scrap_shopee,args=(search_item, total_of_result,s_queue,over))
s.start()

result = over.get()
s.join()
l.join()
result += over.get()

if __name__ == "__main__":
    df = pd.DataFrame([t.__dict__ for t in result])
    print(df)
    
