from flask import Flask, render_template, request, redirect, url_for
from shopee import scrap_shopee
from lazada import scrap_lazada
from threading import Thread
import queue

app = Flask(__name__)
app.config["DEBUG"] = True
l_queue = queue.Queue()
s_queue = queue.Queue()
over = queue.Queue()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        item = request.form['item']
        return redirect('/search/{}'.format(item))
    try:
        return render_template("index.html")
    except Exception:
        return render_template("error.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pass']
        return redirect('/')
    try:
        return render_template("login.html")
    except Exception:
        return render_template("error.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pass']
        return redirect('/')
    try:
        return render_template("signup.html")
    except Exception:
        return render_template("error.html")


@app.route('/search/<string:item>', methods=['GET'])
def search(item):
    try:
        l = Thread(target=scrap_lazada, args=(item, 20, l_queue, over))
        l.start()
        s = Thread(target=scrap_shopee, args=(item, 20, s_queue, over))
        s.start()

        result = over.get()
        s.join()
        l.join()
        result += over.get()

        return render_template("results.html", products=result)
    except Exception:
        return render_template("error.html")


# @app.route('/track', methods=['GET', 'POST'])
# def track():
#     if request.method == "POST":


app.run()
