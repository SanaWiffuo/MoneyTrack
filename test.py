from threading import Thread

import time
def test():
    lst = []
    def run1(lst):
        for x in range(5):
            time.sleep(3)
            print("run1")
            lst.append(x)


    def run2(lst):
        for x in range(5):
            time.sleep(2)
            print("run2")
            lst.append(x)

    print("In main block")
    t1 = Thread(target=run1,args=(lst,))
    threads = [t1]
    t2 = Thread(target=run2,args=(lst,))
    threads += [t2]

    t1.start()
    t2.start()
    
    print("End of main block")
    return lst

lst = test()
print(lst)


# from threading import Thread
# import time
# def test():
#     lst = []
#     def run1():

#         for x in range(5):
            
#             time.sleep(3)
#             print("run1")
#             # lst.append(x)
        
#     def run2():
#         for x in range(5):
            
#             time.sleep(2)
#             print("run2")

#     print("In main block")
#     t1 = Thread(target=run1,args=lst)
#     threads = [t1]
#     t2 = Thread(target=run2,args=lst)
#     threads += [t2]

#     t1.start()
#     t2.start()

#     print("End of main block")
#     return lst
# print(test())

# from threading import Thread
# import time
# lst = []
# def run1(lst):

#     for x in range(5):
#         time.sleep(5)
#         print("run1")
#         lst.append(x)


# def run2(lst):

#     for x in range(5):
#         time.sleep(2)
#         print("run2")
#         lst.append(x)


# print("In main block")
# t1 = Thread(target=run1(lst))
# threads = [t1]
# t2 = Thread(target=run2(lst))
# threads += [t2]

# t1.start()
# t2.start()


# print("End of main block")
# print(lst)