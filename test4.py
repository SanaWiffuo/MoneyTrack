from threading import Thread
import queue 
import time

lst = [1,2,3,4,5]
queue = queue.Queue()
result = []
def func1(lst,queue):
    smtg = []
    if len(lst)%2==0:
        start = int(len(lst)/2)
    else:
        start = int(len(lst)//2)+1
        
    for i in range(start):
        time.sleep(2)
        print(i)
        smtg.append(i)
    queue.put(smtg)
    return smtg

def func2(lst,queue):
    smtg = []
    if len(lst)%2==0:
        start = int(len(lst)/2)
    else:
        start = int(len(lst)//2)+1
        
    for i in range(start,len(lst)):
        time.sleep(4)
        print(i)
        smtg.append(i)
    queue.put(smtg)
    return smtg
    
    
s = Thread(target=func1,args=(lst,queue))
s.start()
l = Thread(target=func2 ,args=(lst,queue))
l.start()

result = queue.get()
s.join()
l.join()
result += queue.get()

print(result)