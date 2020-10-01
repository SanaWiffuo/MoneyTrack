from flask import Flask, render_template, request, redirect, url_for
from shopee import *
from test2 import *
from threading import Thread
import queue
from firebase.firebase import FirebaseApplication
import requests

url = ""
firebase = FirebaseApplication(url, None)
app = Flask(__name__, template_folder="templates")
app.config["DEBUG"] = True
queue = queue.Queue()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        item = request.form['item']
        num = request.form['num']
        return redirect('/search/{}/{}'.format(item, num))
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['item']
        password = request.form['num']
        users = firebase.get('/users')
    return render_template("login.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form['item']
        password = request.form['num']
        firebase.patch("/User/{}".format(username),
                       {"password": password})
    return render_template("signup.html")


@app.route('/search/<string:item>/<int:num>', methods=['GET'])
def search(item, num):
    try:
        s = Thread(target=scrap_shopee, args=(item, num, queue))
        s.start()
        l = Thread(target=scrap_lazada, args=(item, num, queue))
        l.start()

        result = queue.get()
        s.join()
        l.join()
        result += queue.get()

        return render_template("results.html", products=result)
    except Exception:
        return render_template("error.html")


app.run()
