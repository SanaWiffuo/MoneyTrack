import tkinter
from classes import Product, Lazada
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import pandas as pd
import sys
import requests
from lazada import scrap_lazada


def result():
    l = scrap_lazada("monitor", 10)
    T = tkinter.Text(window, height=3, width=30)
    for i in l:
        T.insert(window, i)


window = tkinter.Tk()
window.geometry('500x500')
window.title("Productify")
window.resizable(0, 0)


tkinter.Label(window, text="Welcome to Productify",
              width=50).pack()
tkinter.Label(window, text="Search for the cheapest product", width=50).pack()


tkinter.Entry(window, width=10, relief=tkinter.RIDGE).pack()
tkinter.Button(
    window, text="Search", fg='black', relief=tkinter.SUNKEN, width=5).pack()

tkinter.Button(window, text="Search", command=result).pack()

window.mainloop()
