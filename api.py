from flask import Flask, render_template, request, redirect, url_for
from shopee import *
from lazada import *


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        item = request.form['item']
        num = request.form['num']
        return redirect('/search/{}/{}'.format(item, num))
    return render_template("index.html")


@app.route('/search/<string:item>/<int:num>', methods=['GET'])
def search(item, num):
    try:
        product = scrap_shopee(item, num)
        product += scrap_lazada(item, num)
        return render_template("results.html", products=product)
    except Exception:
        return render_template("error.html")


app.run()
