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
    l = scrap_shopee("noodles", 10)
    for i in range(len(l)):
        name = Label(window, text=str(i.name))
        name.grid(column=0, row=i+1)
        price = Label(window, text=str(i.price))
        price.grid(column=1, row=i+1)
        ratings = Label(window, text=str(i.ratings))
        ratings.grid(column=2, row=i+1)
        url = Label(window, text=str(i.url))
        url.grid(column=3, row=i+1)

# Label(window, text="Welcome to Productify",
#               width=50).pack()
# Label(window, text="Search for the cheapest product", width=50).pack()


button = Button(window, text="Print Me", command=result)
button.grid(column=0, row=1)


# tkinter.Entry(window, width=10, relief=tkinter.RIDGE).pack()
# # tkinter.Button(
# #     window, text="Search", fg='black', relief=tkinter.SU NKEN, width=5).pack()

# button = tkinter.Button(window, text="Search", command=result)
# button.pack()

window.mainloop()
