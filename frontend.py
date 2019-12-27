from tkinter import *
from classes import Product, Lazada
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import pandas as pd
import sys
import requests
from lazada import scrap_lazada
from shopee import scrap_shopee

window = Tk()
# window.geometry('1400x900')
window.title("Productify")
window.resizable(0, 0)
window.attributes("-fullscreen", True) 
def result():
    l = scrap_shopee("food", 10)
    for i in l:
        label = Label(window, text= str(i.name))
        label.pack()
        label = Label(window, text= str(i.url))
        label.pack()
# def printSomething():
#     # if you want the button to disappear:
#     # button.destroy() or button.pack_forget()
#     label = Label(window, text= "")
#     #this creates a new label to the GUI
#     label.pack() 
Label(window, text="Welcome to Productify",
              width=50).pack()
Label(window, text="Search for the cheapest product", width=50).pack()

button = Button(window, text="Print Me", command=result) 
button.pack()







# tkinter.Entry(window, width=10, relief=tkinter.RIDGE).pack()
# # tkinter.Button(
# #     window, text="Search", fg='black', relief=tkinter.SU NKEN, width=5).pack()

# button = tkinter.Button(window, text="Search", command=result)
# button.pack()

window.mainloop()
